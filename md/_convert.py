#!/usr/bin/env python3
"""Conversor fiel PDF -> Markdown para el Reto 3.

Caracteristicas:
- Extrae el texto en orden de lectura con PyMuPDF (sort=True).
- Marca cada pagina con [p. N].
- Detecta bloques de imagen y los describe con su posicion.
- Detecta tablas con pdfplumber y las emite como tablas Markdown.
- OCR (tesseract, spa+eng) de paginas sin capa de texto (<100 chars visibles).
- Cabecera de trazabilidad por archivo.
NO resume: vuelca todo el texto.
"""
import sys, os, io, subprocess, tempfile
import fitz  # PyMuPDF
import pdfplumber

def ocr_page(page, lang="spa+eng"):
    pix = page.get_pixmap(dpi=300)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
        img = tf.name
    pix.save(img)
    try:
        out = subprocess.run(["tesseract", img, "stdout", "-l", lang],
                             capture_output=True, text=True)
        return out.stdout
    finally:
        os.unlink(img)


def extract_text_blocks(pg, font_fix=None):
    """Order-aware extraction: split into columns by x-position, drop narrow
    vertical watermark strips and de-duplicate repeated running heads."""
    w = pg.rect.width
    blocks = [b for b in pg.get_text("blocks") if b[6] == 0]
    blocks = [b for b in blocks if (b[2] - b[0]) >= 15]  # drop vertical watermarks
    blocks.sort(key=lambda b: (0 if b[0] < 0.45 * w else 1, round(b[1])))
    txt = "\n".join(b[4].strip() for b in blocks if b[4].strip())
    # global ligature normalization (Hindawi/older PDFs embed ligature glyphs)
    for a, b in [("\ufb00", "ff"), ("\ufb01", "fi"), ("\ufb02", "fl"),
                 ("\ufb03", "ffi"), ("\ufb04", "ffl"), ("\ufb05", "ft"),
                 ("\ufb06", "st")]:
        txt = txt.replace(a, b)
    if font_fix == "th":
        # In this source the 'Th' glyph pair is mis-mapped to '.' at word start.
        # Only replace a '.' that is NOT preceded by an alphanumeric char.
        import re
        txt = re.sub(r"(?<![A-Za-z0-9])\.(?=[a-z])", "Th", txt)
    return txt


def tables_md(pl_page):
    """Return list of markdown tables detected on a pdfplumber page."""
    out = []
    try:
        for t in (pl_page.extract_tables() or []):
            rows = [[("" if c is None else str(c).replace("\n", " ").strip())
                     for c in r] for r in t if any(r)]
            if len(rows) < 2:
                continue
            ncol = max(len(r) for r in rows)
            rows = [r + [""] * (ncol - len(r)) for r in rows]
            md = ["| " + " | ".join(rows[0]) + " |",
                  "| " + " | ".join(["---"] * ncol) + " |"]
            for r in rows[1:]:
                md.append("| " + " | ".join(r) + " |")
            out.append("\n".join(md))
    except Exception as e:
        out.append(f"[!] Error de deteccion de tabla: {e}")
    return out

def convert(pdf_path, out_md, title_note="", font_fix=None):
    doc = fitz.open(pdf_path)
    n = doc.page_count
    # detect image-only pages
    imgonly = []
    for i, pg in enumerate(doc):
        if len(pg.get_text().strip().replace(" ", "").replace("\n", "")) < 100 and pg.get_images():
            imgonly.append(i + 1)
    warnings = []
    if imgonly:
        warnings.append(f"Paginas sin capa de texto util (requirieron OCR): {imgonly}")

    parts = []
    parts.append(f"<!-- Archivo original: {os.path.basename(pdf_path)} -->")
    parts.append(f"<!-- Paginas: {n} -->")
    parts.append("<!-- Metodo de extraccion: PyMuPDF (texto ordenado) + pdfplumber (tablas) "
                 + ("+ OCR tesseract spa+eng (paginas imagen)" if imgonly else "")
                 + " -->")
    if warnings:
        parts.append("<!-- ADVERTENCIAS DE CALIDAD: " + " | ".join(warnings) + " -->")
    if title_note:
        parts.append(f"<!-- {title_note} -->")
    parts.append("")

    # frequency of each xref to spot recurring header/footer images
    from collections import Counter
    xfreq = Counter()
    for pg in doc:
        for im in pg.get_images(full=True):
            xfreq[im[0]] += 1
    n_imgonly = max(1, n)

    pl_doc = pdfplumber.open(pdf_path)
    try:
        for i, pg in enumerate(doc):
            parts.append(f"\n---\n\n### [p. {i+1}]\n")
            raw = pg.get_text().strip().replace(" ", "").replace("\n", "")
            if len(raw) < 100 and pg.get_images():
                txt = ocr_page(pg).strip()
                parts.append("> _Pagina sin capa de texto: contenido transcrito por OCR._\n")
                parts.append(txt if txt else "[Sin texto reconocible]")
            else:
                txt = extract_text_blocks(pg, font_fix).strip()
                parts.append(txt if txt else "[Pagina en blanco o sin texto extraible]")

            # image blocks description
            imgs = pg.get_images(full=True)
            if imgs:
                info = []
                for im in imgs:
                    xref = im[0]
                    w, h = im[2], im[3]
                    tag = " [recurrente: posible encabezado/pie/logo]" if xfreq[xref] > n / 2 else ""
                    info.append(f"xref{xref} {w}x{h}px{tag}")
                parts.append(f"\n> [Imagen(es) en la pagina: {len(imgs)} | " + "; ".join(info) + "]")

            for t in tables_md(pl_doc.pages[i]):
                parts.append("\n**Tabla detectada (formato Markdown):**\n\n" + t)
    finally:
        pl_doc.close()

    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts) + "\n")
    print(f"OK -> {out_md} ({n} pag, OCR pages={imgonly})")

if __name__ == "__main__":
    # map: source pdf -> output md, note
    JOBS = [
        ("EBSCO-FullText-10_19_2026.pdf",
         "md/referencias/EBSCO-FullText-10_19_2026.md",
         "Benavides-Astudillo et al. (2020) - Un experimento ... Ingenieria Social - Rev. Ciencia UNEMI 13(32) 27-40",
         None),
        ("EBSCO-FullText-10_19_2026 (1).pdf",
         "md/referencias/EBSCO-FullText-10_19_2026 (1).md",
         "Benavides et al. (2020) - Caracterizacion de los ataques de phishing ... - Cienc Tecn UTEQ 13(1) 97-104",
         None),
        ("Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.pdf",
         "md/referencias/Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.md",
         "Lu & Yu (2021) - Research on WiFi Penetration Testing with Kali Linux - Complexity 2021. Fuente con mapeo de fuente corrupto (ligadura 'Th'->'.'); normalizado y documentado.",
         "th"),
        ("carla,+ODIGOS+V2-NUM3-2021-47-76.pdf",
         "md/referencias/carla,+ODIGOS+V2-NUM3-2021-47-76.md",
         "Prado Diaz (2021) - Ingenieria social, un ejemplo practico - Revista ODIGOS 2(3) 47-76",
         None),
        ("indecs2023-pp168-173.pdf",
         "md/referencias/indecs2023-pp168-173.md",
         "Budavari, Albini & Mester (2023) - The Role of Social Engineering in the Energy Balance of Systems - INDECS 21(2) 168-173",
         None),
        ("mquinde,+articulo10.pdf",
         "md/referencias/mquinde,+articulo10.md",
         "Crespo-Martinez (2021) - Analisis de vulnerabilidades con SQLMAP ... - Ingenius (25) 104-113",
         None),
        ("Octubre_2024.pdf",
         "md/referencias/Octubre_2024.md",
         "Zambrano Hernandez et al. (2024) - Una mirada a metodologias para pruebas de penetracion en ciberseguridad - UNAD/CSIRT",
         None),
        ("Guía de aprendizaje - Reto 3 -  Diseño de estrategias de detección, defensa y fortalecimiento de la postura de ciberseguridad.pdf",
         "md/actividad/Guía de aprendizaje - Reto 3.md",
         "ACTIVIDAD - Guia de aprendizaje Reto 3",
         None),
        ("Rúbrica de evaluación - Reto 3 - Diseño de estrategias de detección, defensa y fortalecimiento.pdf",
         "md/rubrica/Rúbrica de evaluación - Reto 3.md",
         "RUBRICA - Reto 3",
         None),
    ]
    for src, dst, note, ffix in JOBS:
        try:
            convert(src, dst, note, font_fix=ffix)
        except Exception as e:
            print(f"FAIL {src}: {e}")
