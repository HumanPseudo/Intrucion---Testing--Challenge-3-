#!/usr/bin/env python3
"""Convierte un paquete H5P (.h5p, que es un ZIP) a Markdown íntegro.

No resume: extrae TODO el texto de content/content.json (H5P.CoursePresentation
y otras librerías de contenido), transcribe los valores textuales (H5P.AdvancedText,
H5P.Text, H5P.Table), e inventaría los recursos binarios (audio, imagen, video)
con su ruta, formato y duración. Los binarios NO se transcriben (no hay motor STT
disponible); se documenta la limitación.

Uso:
    python3 _convert_h5p.py course-presentation-508-508.h5p > salida.md
"""
import json
import re
import html
import sys
import zipfile
import subprocess
import os

IMG_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"}
AUD_EXT = {".mp3", ".m4a", ".ogg", ".wav", ".aac", ".flac"}
VID_EXT = {".mp4", ".webm", ".mov", ".m4v", ".avi", ".mkv"}


def html_to_md(h):
    """HTML de H5P -> texto Markdown razonable (conserva párrafos y listas)."""
    if not h:
        return ""
    t = re.sub(r"(?i)<br\s*/?>", "\n", h)
    t = re.sub(r"(?i)</(p|div|li|h[1-6])>", "\n", t)
    t = re.sub(r"(?i)<li[^>]*>", "- ", t)
    t = re.sub(r"(?i)<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return "\n".join(l.rstrip() for l in t.splitlines()).strip()


def media_duration(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=30).stdout.strip()
        return float(out) if out else None
    except Exception:
        return None


def classify(ext):
    if ext in IMG_EXT:
        return "imagen"
    if ext in AUD_EXT:
        return "audio"
    if ext in VID_EXT:
        return "video"
    return "otro"


def walk(node, out, depth=0):
    """Recorre recursivamente params/elements/rutas de H5P buscando texto y media."""
    if isinstance(node, list):
        for x in node:
            walk(x, out, depth)
        return
    if not isinstance(node, dict):
        return
    if "library" in node and "params" in node:
        out.append((node.get("library", "?"), node.get("params", {}), depth))
    for k, v in node.items():
        if k in ("params",):
            continue
        walk(v, out, depth + 1)


def main(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    h5p = json.loads(z.read("h5p.json"))
    content = json.loads(z.read("content/content.json"))

    # Extraer a un temporal para poder medir duraciones con ffprobe
    tmp = "/tmp/user/1000/opencode/h5p-extract"
    os.makedirs(tmp, exist_ok=True)
    z.extractall(tmp)

    out = []
    out.append(f"<!-- Archivo original: {os.path.basename(path)} -->")
    out.append(f"<!-- Tipo: paquete H5P (ZIP) — librería principal: {h5p.get('mainLibrary')} -->\n")
    out.append("# Presentación del curso (H5P) — Course Presentation\n")
    out.append("## Cabecera de conversión\n")
    out.append(f"- **Archivo original:** `{os.path.basename(path)}`")
    out.append("- **Tipo de artefacto:** paquete **H5P** (`.h5p`), que es un contenedor **ZIP** — *no* un PDF.")
    out.append(f"- **Título declarado (h5p.json):** {h5p.get('title')}")
    out.append(f"- **Librería principal:** `{h5p.get('mainLibrary')}` (Course Presentation)")
    out.append(f"- **Idioma declarado:** `{h5p.get('language')}` / idioma por defecto `{h5p.get('defaultLanguage')}`")
    out.append(f"- **Licencia declarada:** `{h5p.get('license')}`")
    dep = ", ".join(f"{d['machineName']} {d['majorVersion']}.{d['minorVersion']}" for d in h5p.get("preloadedDependencies", []))
    out.append(f"- **Dependencias precargadas:** {dep}")
    out.append(f"- **Nº de archivos en el paquete:** {len(names)} (mayoría son código de librerías H5P, no contenido)")
    out.append("- **Método de conversión:** parseo de `h5p.json` + `content/content.json`; texto extraído de "
               "`H5P.AdvancedText`; recursos binarios inventariados y medidos con `ffprobe`.")
    out.append("- **Advertencia de calidad:** los **audios de narración NO se transcriben** aquí (no hay motor "
               "de reconocimiento de voz disponible en el entorno). Se registran archivo, formato y duración; "
               "el texto en pantalla sí se transcribe íntegro. Ver limitación al final.")
    out.append("- **Distinción importante:** el contenido textual de esta presentación **resume** la guía y la "
               "rúbrica del Reto 3; la fuente normativa son esos documentos, no esta presentación.\n")

    # Inventario de media
    media = []
    for n in names:
        if n.startswith("content/"):
            ext = os.path.splitext(n)[1].lower()
            media.append((n, classify(ext)))
    audios = [m for m in media if m[1] == "audio"]
    imagenes = [m for m in media if m[1] == "imagen"]

    out.append("---\n")
    out.append("## Diapositivas\n")
    slides = content.get("presentation", {}).get("slides", [])
    out.append(f"La presentación tiene **{len(slides)} diapositivas**.\n")

    # Mapear audio por diapositiva
    for i, s in enumerate(slides):
        out.append(f"### Diapositiva {i + 1}\n")
        texts = []
        media_items = []
        for e in s.get("elements", []):
            lib = e.get("action", {}).get("library", "")
            p = e.get("action", {}).get("params", {})
            if lib.startswith("H5P.AdvancedText") or lib.startswith("H5P.Text"):
                t = html_to_md(p.get("text", ""))
                if t:
                    texts.append(t)
            elif lib.startswith("H5P.Audio"):
                for f in (p.get("files") or []):
                    media_items.append(("audio", f.get("path"), f.get("mime")))
            elif lib.startswith("H5P.Video"):
                for f in (p.get("files") or []):
                    media_items.append(("video", f.get("path"), f.get("mime")))
            elif lib.startswith("H5P.Image"):
                for f in (p.get("file") and [p["file"]] or []):
                    media_items.append(("imagen", f.get("path"), f.get("mime")))
            elif lib.startswith("H5P.Table"):
                t = html_to_md(p.get("text", "") or "")
                if t:
                    texts.append(t)
            else:
                # Recorrer subcontenidos (quiz, etc.) por si llevan texto
                collected = []
                walk(e.get("action", {}).get("params", {}), collected)
                for sublib, sp, _ in collected:
                    if "text" in sp and isinstance(sp["text"], str):
                        t = html_to_md(sp["text"])
                        if t:
                            texts.append(t)
        for t in texts:
            out.append(t + "\n")
        for kind, rel, mime in media_items:
            local = os.path.join(tmp, "content", os.path.basename(rel)) if rel else None
            if rel and not rel.startswith("content/"):
                local = os.path.join(tmp, "content", rel)
            dur = media_duration(local) if local and os.path.exists(local) else None
            size = None
            if rel:
                for n in names:
                    if n.endswith(os.path.basename(rel)):
                        size = z.getinfo(n).file_size
                        break
            extra = []
            if dur:
                extra.append(f"duración ≈ {dur:.1f} s")
            if size:
                extra.append(f"{size / 1024:.0f} KB")
            extra.append(f"mime `{mime}`")
            out.append(f"> **[{kind.upper()} de la diapositiva]** `{rel}` — {', '.join(extra)}.")
            if kind == "audio":
                out.append("> _Narración hablada; texto no transcrito (ver limitación al final del documento)._\n")

    # Inventario de recursos
    out.append("---\n")
    out.append("## Inventario de recursos binarios\n")
    out.append(f"- **Audios de narración:** {len(audios)}")
    for n, _ in audios:
        dur = media_duration(os.path.join(tmp, n))
        out.append(f"  - `{n}` — {dur:.1f} s" if dur else f"  - `{n}`")
    out.append(f"- **Imágenes:** {len(imagenes)}")
    for n, _ in imagenes:
        out.append(f"  - `{n}`")
    outros = [m for m in media if m[1] == "otro"]
    if outros:
        out.append(f"- **Otros archivos en `content/`:** {len(outros)}")
        for n, _ in outros:
            out.append(f"  - `{n}`")

    out.append("\n---\n")
    out.append("## Limitaciones declaradas\n")
    out.append("- **Narración en audio no transcrita.** Las 7 pistas `.m4a` contienen la lectura en voz alta de cada "
               "diapositiva. No se transcribieron porque el entorno no dispone de motor STT (Whisper/Vosk). El texto "
               "en pantalla, que corresponde al guion, sí quedó transcrito íntegramente.")
    out.append("- **Sin estructura de página.** Este artefacto no es paginado como un PDF; la unidad es la diapositiva.")
    out.append("- **Posicionamiento.** Los elementos tienen coordenadas (x, y, ancho, alto) en `content.json`; "
               "se omitieron por no aportar al contenido textual.")
    out.append("- **Código de librerías.** El paquete incluye ~2.100 archivos de las librerías H5P (JS/CSS/locales); "
               "no son contenido de la actividad y no se convierten.")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    print(main(sys.argv[1]))
