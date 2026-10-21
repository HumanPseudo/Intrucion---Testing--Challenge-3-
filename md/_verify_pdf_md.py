#!/usr/bin/env python3
"""Verifica fidelidad PDF -> MD comparando el vocabulario (tokens) de ambos.

Para cada PDF y su .md: extrae el texto del PDF (PyMuPDF), normaliza (minúsculas,
sin acentos, ligaduras, sin puntuación), tokeniza en palabras y calcula:
  - cuántos tipos/palabras del PDF aparecen en el MD (cobertura)
  - palabras del PDF ausentes en el MD (candidatas a pérdida)
  - palabras del MD ausentes en el PDF (añadidos/OCR/artefactos)

No reescribe nada; solo reporta.
"""
import os
import re
import sys
import unicodedata

import fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PDF -> MD (rutas relativas a la raíz del proyecto)
MAP = {
    "Guía de aprendizaje - Reto 3 -  Diseño de estrategias de detección, defensa y fortalecimiento de la postura de ciberseguridad.pdf":
        "md/actividad/Guía de aprendizaje - Reto 3.md",
    "Rúbrica de evaluación - Reto 3 - Diseño de estrategias de detección, defensa y fortalecimiento.pdf":
        "md/rubrica/Rúbrica de evaluación - Reto 3.md",
    "EBSCO-FullText-10_19_2026.pdf": "md/referencias/EBSCO-FullText-10_19_2026.md",
    "EBSCO-FullText-10_19_2026 (1).pdf": "md/referencias/EBSCO-FullText-10_19_2026 (1).md",
    "Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.pdf":
        "md/referencias/Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.md",
    "carla,+ODIGOS+V2-NUM3-2021-47-76.pdf": "md/referencias/carla,+ODIGOS+V2-NUM3-2021-47-76.md",
    "indecs2023-pp168-173.pdf": "md/referencias/indecs2023-pp168-173.md",
    "mquinde,+articulo10.pdf": "md/referencias/mquinde,+articulo10.md",
    "Octubre_2024.pdf": "md/referencias/Octubre_2024.md",
}

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi",
       "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st"}


def norm(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    # tokens: letras y dígitos (separa por cualquier otra cosa)
    return re.findall(r"[a-z0-9]+", s)


def pdf_text(path):
    doc = fitz.open(path)
    return "\n".join(p.get_text() for p in doc)


def md_text(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def main():
    print("=" * 96)
    print("VERIFICACIÓN DE FIDELIDAD PDF -> MD (comparación de vocabulario por tokens)")
    print("=" * 96)
    overall = []
    for pdf, md in MAP.items():
        pp = os.path.join(ROOT, pdf)
        mp = os.path.join(ROOT, md)
        if not os.path.exists(pp):
            print(f"[FALTA PDF] {pdf}")
            continue
        if not os.path.exists(mp):
            print(f"[FALTA MD ] {md}")
            continue
        ptoks = norm(pdf_text(pp))
        mtoks = norm(md_text(mp))
        pset, mset = set(ptoks), set(mtoks)
        missing = pset - mset
        extra = mset - pset
        cov_tokens = 100.0 * (len(ptoks) - sum(1 for t in ptoks if t in missing)) / max(1, len(ptoks))
        cov_types = 100.0 * (len(pset) - len(missing)) / max(1, len(pset))
        print(f"\n### {pdf}")
        print(f"    MD: {md}")
        print(f"    tokens PDF={len(ptoks):>7}  tokens MD={len(mtoks):>7}")
        print(f"    cobertura por ocurrencias: {cov_tokens:6.2f}%   por tipos(vocabulario): {cov_types:6.2f}%")
        print(f"    palabras del PDF AUSENTES en MD: {len(missing)}   |   palabras solo en MD: {len(extra)}")
        if missing:
            # ordenar por frecuencia en el PDF
            freq = {}
            for t in ptoks:
                if t in missing:
                    freq[t] = freq.get(t, 0) + 1
            top = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:25]
            print("    Ausentes (top por frecuencia):")
            for w, c in top:
                print(f"       {w:<24} x{c}")
        overall.append((pdf, cov_tokens, cov_types, len(missing), len(extra)))

    print("\n" + "=" * 96)
    print("RESUMEN")
    print("=" * 96)
    print(f"{'PDF':<70}{'cob.occ':>9}{'cob.tip':>9}{'faltan':>8}{'extra':>7}")
    for pdf, a, b, m, e in overall:
        print(f"{pdf[:69]:<70}{a:8.2f}%{b:8.2f}%{m:8d}{e:7d}")


if __name__ == "__main__":
    main()
