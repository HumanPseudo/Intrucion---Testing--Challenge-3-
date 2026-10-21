# INDEX de conversión a Markdown — Reto 3 (Intrusión y Testing, 203028113)

Generado para el Reto 3 «Diseño de estrategias de detección, defensa y fortalecimiento de la postura de ciberseguridad».

Cubre **todos** los artefactos de la carpeta `resources/` convertibles a texto: los **9 PDF** y el paquete **H5P** (`.h5p`).

> **Añadido — insumos del Reto 2.** Se incorporó el material del Reto 2 (que vive en el vault `Obsidian/Brain/Test 2`) bajo **`md/reto2/`**, porque el Reto 3 se construye a partir de él. El documento maestro es el **Anexo 1** (48 págs), que trae la sección del Reto 3 (pp. 32-35) y sus 5 instrumentos. Ver **`md/reto2/CONTEXTO-RETO3.md`** (contexto consolidado) y la sección *Inventario del paquete Reto 2* más abajo.

## Metodología de conversión

### PDF → Markdown (`md/_convert.py`)

- **Texto:** PyMuPDF (`get_text("blocks")`) en orden de lectura, con separación de columnas por posición X y descarte de marcas de agua verticales estrechas (marca de agua Wiley).
- **Tablas:** detección con `pdfplumber` y volcado como tablas Markdown.
- **Figuras/imágenes:** se enumeran los bloques de imagen por página (con xref y tamaño). Las imágenes recurrentes (logotipos/encabezados/pies) se señalan.
- **Páginas sin capa de texto (<100 caracteres):** OCR con Tesseract (`spa+eng`, 300 dpi); se marca explícitamente en el `.md`.
- **Ligaduras:** se normalizan ligaduras Unicode (`ﬁ`, `ﬂ`, `ﬀ`, etc.) a ASCII.
- **Casos especiales:** el PDF de *Complexity* trae un mapeo de fuente corrupto (ligadura "Th" → "."). Se normalizó y se documentó en la cabecera del `.md`; queda un residuo menor («e School» por «The School»).
- **No se resume ni reinterpreta:** se vuelca todo el texto, con marcas de página `[p. N]`.

### H5P → Markdown (`md/_convert_h5p.py`)

- **Qué es:** un `.h5p` **es un ZIP** que contiene una presentación interactiva (librería `H5P.CoursePresentation`), no un PDF.
- **Contenido:** se parsea `h5p.json` (metadatos) y `content/content.json` (diapositivas, textos y referencias a media); el texto se extrae de los elementos `H5P.AdvancedText`.
- **Media:** los audios/imágenes se inventarían con ruta, formato y **duración** (`ffprobe`).
- **Narración:** los 7 audios `.m4a` **no se transcriben** (no hay motor STT en el entorno); se declara la limitación.
- **No se convierte el código de librerías** H5P (~2.100 archivos JS/CSS/locales), que no es contenido de la actividad.

## Inventario de PDFs (9 PDF, todos en `resources/`)

| # | PDF original | `.md` generado | Págs | Estado | Observaciones de calidad |
|---|--------------|----------------|:----:|--------|--------------------------|
| 1 | `Guía de aprendizaje - Reto 3 -  Diseño de estrategias de detección, defensa y fortalecimiento de la postura de ciberseguridad.pdf` | `md/actividad/Guía de aprendizaje - Reto 3.md` | 9 | OK (con OCR en p. 9) | p. 9 es una contraportada de imagen → OCR (logotipo; texto reconocible mínimo). «Tabla 1. Tabla de descripción» también como texto; la reconstrucción de tabla Markdown tiene columnas duplicadas por el diseño del original (el contenido textual está íntegro). |
| 2 | `Rúbrica de evaluación - Reto 3 - Diseño de estrategias de detección, defensa y fortalecimiento.pdf` | `md/rubrica/Rúbrica de evaluación - Reto 3.md` | 9 | OK | Tabla 1 (rúbrica completa con los 3 criterios y sus 4 niveles) extraída y volcada como tabla Markdown + texto. Sin pérdidas detectadas. |
| 3 | `EBSCO-FullText-10_19_2026.pdf` | `md/referencias/EBSCO-FullText-10_19_2026.md` | 15 | OK | Artículo UNEMI 13(32) 27-40 (14 págs) + 1 pág. de aviso de copyright EBSCO. Lista de referencias íntegra. |
| 4 | `EBSCO-FullText-10_19_2026 (1).pdf` | `md/referencias/EBSCO-FullText-10_19_2026 (1).md` | 9 | OK | Artículo Ciencia y Tecnología 13(1) 97-104 (8 págs) + 1 pág. de aviso de copyright EBSCO. |
| 5 | `Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.pdf` | `md/referencias/Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.md` | 8 | OK (con advertencia) | Fuente con mapeo corrupto: "Th" aparece como ".". Normalizado (documentado). Liga 2 columnas correctamente separadas. Residuo menor: «e School» en lugar de «The School». Marca de agua «Downloaded from…» eliminada. |
| 6 | `carla,+ODIGOS+V2-NUM3-2021-47-76.pdf` | `md/referencias/carla,+ODIGOS+V2-NUM3-2021-47-76.md` | 30 | OK | Páginas 47-76. Buen texto (2 columnas). |
| 7 | `indecs2023-pp168-173.pdf` | `md/referencias/indecs2023-pp168-173.md` | 6 | OK | Ecuaciones (1)-(3) conservadas como texto. Lista de 26 referencias íntegra. Figuras con pie. |
| 8 | `mquinde,+articulo10.pdf` | `md/referencias/mquinde,+articulo10.md` | 10 | OK | Ingenius N.º 25, pp. 104-113. Incluye DOI y cita sugerida por el propio autor. |
| 9 | `Octubre_2024.pdf` | `md/referencias/Octubre_2024.md` | 14 | OK (con OCR en p. 1) | p. 1 es portada gráfica → OCR (parcialmente ruidoso; el título se reconoce bien). Resto con capa de texto. |

## Inventario de artefactos NO-PDF (también convertidos)

| # | Artefacto original | `.md` generado | Unidad | Estado | Observaciones |
|---|--------------------|----------------|:------:|--------|---------------|
| 10 | `course-presentation-508-508.h5p` | `md/actividad/course-presentation-508-508.md` | 7 diapositivas | OK (con advertencia) | Paquete **H5P** (ZIP de 23 MB, 2.191 archivos), librería `H5P.CoursePresentation`. Se convirtieron **todas** las diapositivas con su texto íntegro y el inventario de los 7 audios `.m4a` (con duración) y 3 imágenes. **Advertencia:** la narración en audio **no se transcribió** (sin motor STT); el texto en pantalla sí está completo. Es material **resumen** de la guía/rúbrica, no fuente normativa. |

## Archivos de la carpeta sin conversión (no textuales)

- `references.md`: ya es Markdown; es la lista de referencias de origen (no requiere conversión).

## Mapa referencia ↔ PDF de respaldo

| Referencia (`references.md`) | PDF en la carpeta | ¿Coincide? |
|---|---|---|
| Crespo-Martínez (2021), Ingenius, 104-113 | `mquinde,+articulo10.pdf` | ✅ |
| Lu & Yu (2021), Complexity, 1-8 | `Complexity - 2021 - Lu - …pdf` | ✅ |
| Benavides-Astudillo, Fuertes-Díaz & Sánchez-Gordon (2020), Ciencia UNEMI 13(32) 27-40 | `EBSCO-FullText-10_19_2026.pdf` | ✅ |
| Benavides-Astudillo, Fuertes-Díaz & Sánchez-Gordon (2020), Ciencia y Tecnología 13(1) 97-104 | `EBSCO-FullText-10_19_2026 (1).pdf` | ✅ |
| Budavári, Albini & Mester (2023), INDECS 21(2) 168-173 | `indecs2023-pp168-173.pdf` | ✅ |
| Prado Díaz (2021), ODIGOS 2(3) 47-76 | `carla,+ODIGOS+V2-NUM3-2021-47-76.pdf` | ✅ |
| Zambrano Hernández et al. (2024), Boletín CSIRT UNAD (Octubre 2024) | `Octubre_2024.pdf` | ✅ |

**Sin PDF huérfanos:** los 9 PDF corresponden a 7 referencias + 2 materiales del curso (guía y rúbrica).
**Citas sin PDF de respaldo:** las 2 OVI/OVA de 2026 citadas en la guía (`repository.unad.edu.co/handle/10596/83223` y `/83229`) no tienen PDF en la carpeta y sus enlaces devuelven **404**.

## Incertidumbres

- El DOI de Wiley (`10.1155/2021/5570001`) devuelve **403** a peticiones automatizadas (bloqueo anti-bot); la resolución y los metadatos se confirmaron vía Crossref.
- Los enlaces EBSCO de `references.md` resuelven a la pantalla de login de la biblioteca UNAD (**200**) pero requieren autenticación institucional; no es posible confirmar el contenido exacto sin sesión.
- Los dos *handles* de repositorio UNAD citados en la guía devuelven 404: no fue posible verificar su existencia.

---

## Inventario del paquete Reto 2 (`md/reto2/`)

Material del Reto 2 incorporado para dar contexto al Reto 3. Origen: vault `Obsidian/Brain/Test 2` (enlace `Test 2/Vault Obsidian - Test 2`).

### Punto de entrada

| Archivo | Qué es |
|---------|--------|
| **`md/reto2/CONTEXTO-RETO3.md`** | ⭐ **Contexto consolidado**: requisitos del Reto 3, caso, insumos ofensivos del Reto 2 (activos, vectores, CVE, CKC, MITRE, ruta, riesgo) y trazabilidad sugerida vector→control |

### Fuentes (`md/reto2/fuentes/`)

| Archivo | Origen | Unidad | Estado |
|---------|--------|:------:|--------|
| `Anexo 1 - Caso AgroSmart del Sumapaz.md` | `05 - Fuentes/Anexo 1 Caso AgroSmart del Sumapaz.pdf` | 48 págs | OK (OCR en pp. 31, 36). **Documento maestro**; Reto 3 en pp. 32-35. Tablas con celdas fragmentadas (diseño 2 columnas), texto íntegro. |
| `Guía de aprendizaje - Reto 2.md` | `05 - Fuentes/Guía de aprendizaje - Reto 2 …pdf` | 6 págs | OK |
| `Guion del video.md` | Nota Obsidian (entregable Reto 2) | — | Copia literal |
| `Referencias y lectura.md` | Nota Obsidian (referentes APA 7) | — | Copia literal |

### Instrumentos y contexto (`md/reto2/instrumentos/`, `md/reto2/contexto/`)

14 instrumentos (1.1, 1.B, 1.C, 2.1-2.9, 3.13, Declaración IA) + 8 notas de contexto (arquitectura, marco legal/ROE, rúbrica, glosario…). Copias literales de las notas del vault (ya en Markdown de calidad). Detalle en `md/reto2/CONTEXTO-RETO3.md` sección 5.

### No incluido

- Video MP4 y `.pptx` del Reto 2 (binarios).
- Anexo A — blueprint del Cyber Range (material del Reto 5).
