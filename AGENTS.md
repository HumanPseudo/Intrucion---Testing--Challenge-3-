# AGENTS.md — Challenge 3 (Intrusión y Testing · UNAD)

Academic repo for the **Challenge 3 defensive-design report** (individual, midterm, 125 points).
The report designs detection, defense, hardening, monitoring, containment and response for the
case **AgroSmart del Sumapaz S.A.S.**, traceable to the Challenge 2 offensive analysis. Keep
changes minimal: never alter the substance of source/reference files, and never rename or move
them. Cosmetic normalization (e.g. replacing the section symbol) is allowed but must not change
what the material says.

## Core paths

- `md/` — converted course material and Challenge 2 inputs (**read-only reference**).
  - `md/actividad/` — Challenge 3 learning guide (15 steps) and the H5P presentation conversion.
  - `md/rubrica/` — Challenge 3 evaluation rubric (authoritative on numeric thresholds).
  - `md/reto2/` — Challenge 2 package: `CONTEXTO-RETO3.md` (consolidated context),
    `contexto/` (architecture, legal/ROE, glossary), `instrumentos/` (1.x/2.x + AI declaration),
    `fuentes/` (Annex 1 master case, Challenge 2 guide, video script, references).
  - `md/referencias/` — converted course articles (copyrighted; local only).
- `resources/` — original course PDFs/H5P, `references.md` and `REVISION_RETO3.md` (the audit with
  errata already fixed and ambiguities A1–A8). **Read-only.**
- `report/` — the deliverable sources (tracked): `doc.md` (content), `Makefile` (render),
  `header.tex` (LaTeX extras), `README.md` (how-to). Renders `doc.md` → `report.pdf` / `.docx`.
- `plan.md` — operational checklist (6 phases over the 15 guide steps, rubric checklist, schedule).
- `README.md` — task summary and structure.

## Rules of the challenge (do not violate)

- **Traceability first.** Every control, hardening action and detection rule must name the
  Challenge 2 vector/asset/cause it addresses. No generic good-practice lists.
- **No tests, no exploitation.** This challenge is design only; validation is deferred to the
  Cyber Range (Challenge 4). The report must say so explicitly.
- **Editable matrices.** Tables must be integrated as editable content in the document; never
  screenshots, images of tables or external-repository links.
- **APA + AI log.** ≥8 sources (≥3 course + ≥3 technical frameworks); mandatory AI-usage
  declaration/log with prompts, purpose, verification and own adjustments.
- **Never invent case data.** Assets (A-01…A-08), vectors (10), CVEs/CWEs and MITRE techniques come
  only from `md/reto2/` and Annex 1.
- Word count of the body, **excluding references**, must stay between **6,000 and 8,000**.

## Citation errata (already fixed — do not reintroduce old forms)

Taken from `resources/REVISION_RETO3.md`:

- UNAD Bulletin authorship = **Palomo Luna, Zambrano Hernández, Moreno Molano & Peña Hidalgo**
  (Boletín N.º 28, 2024) — not "Zambrano Hernández, Peña Hidalgo, Cárdenas Corral".
- UNEMI article year = **2020** (the guide said 2019).
- INDECS author = **Albininé Budavári, E.** (the guide said "Budavári, E. A.").
- Use **direct DOIs**: UNEMI `10.29076/issn.2528-7737vol13iss32.2020pp27-40p`; phishing
  `10.18779/cyt.v13i1.357`; INDECS `10.7906/indecs.21.2.5` (not EBSCO proxy links).
- The two **OVI/OVA** UNAD handles (`10596/83223`, `10596/83229`) return **404 → "to be verified"**;
  cite only with that caveat or omit.

## Deliverable pipeline

```bash
cd report
make          # report.pdf
make docx     # main editable report.docx
make wordcount  # body word count + per-section breakdown (6,000–8,000 gauge)
make check      # full verification pass (word count, sections, tables, sources)
make clean
```

Requires **Pandoc** and a Unicode-capable LaTeX engine (`xelatex`) with the DejaVu fonts — **not**
`pdflatex` (the matrices use `≥`, `→`, `↔`). See `report/README.md`.

## Verification checklist before finishing

Automated: `cd report && make check` (script: `tools/check_report.py`; exits non-zero on failure).

- `report/doc.md` has the **10 sections** with visible headings and references to every table.
- Section titles and **Table 1–13** numbers stay identical across `report/doc.md`, `plan.md` Section 3 and
  `report/README.md` (one object, three views — do not merge the files).
- Each table is titled, numbered and referenced in the text; all are editable.
- Every control maps to a Challenge 2 vector/asset; no orphan controls.
- No-test declaration and AI log present.
- References: ≥8, in APA, with bidirectional citation↔reference correspondence.
- Body word count between 6,000 and 8,000 (references excluded) — `make wordcount`.
- No leftover `[..]` placeholders or `> **[to complete …]**` blocks.
- `resources/*.pdf`, `resources/*.h5p` and `md/referencias/` are not committed (copyright).

## Gotchas

- `md/` and `resources/` filenames are **Spanish with spaces/accents** — quote paths in the shell.
- The `md/reto2/fuentes/Anexo 1` conversion has Annex tables split into 2-column PDF cells; the
  textual content is complete but read it carefully.
- Do not rename or move files in `md/` or `resources/`: `plan.md` and this file cite their exact
  paths.
