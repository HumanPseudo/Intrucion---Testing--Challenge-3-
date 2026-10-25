# Deliverable — Challenge 3 (Intrusión y Testing)

How to turn `doc.md` into the submitted document. Everything here is content-only:
edit `doc.md`, run one command, get `report.pdf` (or `report.docx`).

- Write **all** content in `doc.md` (front matter holds title, author, date, `lang`).
- The mandatory matrices are already scaffolded as editable Markdown tables inside `doc.md`
  (Tables 1–13). Replace the `[..]` cells and the `> **[to complete …]**` blocks with your own
  analysis; do **not** paste images of tables or link to external repositories (rubric forbids it).
- `report.pdf`, `report.docx` and LaTeX temp files are gitignored — only sources are tracked.
- **Canonical outputs:** render the same `doc.md` to `report.pdf` and/or `report.docx`. Do not create
  task-tagged variants such as `report-check.*` or `report-limpio.*`; use `make clean` for temp files.

## Requirements

- **Pandoc** — Markdown → LaTeX/Word front-end. `sudo apt install pandoc` (check: `pandoc --version`).
- **A Unicode-capable LaTeX engine** — TinyTeX/TeX Live provides `xelatex`. Check: `xelatex --version`.
  (`pdflatex` is **not** used: the matrices contain glyphs such as `≥`, `→`, `↔` and Spanish accents.)
- **DejaVu fonts** — set as main/mono font so those glyphs render. Check: `fc-match "DejaVu Serif"`.

## Quick start (Makefile)

From this folder (`report/`):

```bash
make          # builds report.pdf  (same as: make pdf)
make docx     # builds report.docx (editable Word — matrices stay editable)
make both     # builds both
make tex      # builds report.tex only
make clean    # removes outputs and LaTeX temp files
```

`make` only rebuilds when `doc.md` is newer than `report.pdf`.

## Verification (the running word count and the rubric gate)

```bash
make wordcount   # body word count + per-section breakdown (the 6,000–8,000 gauge)
make check       # full verification pass: word count, sections, tables, sources, placeholders
```

Both call `tools/check_report.py` at the repo root and exit non-zero when a hard check fails,
so they can be used as a gate before a commit or before submission.

`make wordcount` counts only the body (sections 1–10) and **excludes the reference list and the
AI appendix**. It prints the same slice measured in the rendered `report.docx`, so the figure can
be checked against Word's own counter, and it breaks the count down per section:

```
Body word count (sections 1-10, references excluded): 4350
Rendered .docx (same slice): 4343
Target: 6000-8000 -> 1650 words still to write

Per section:
     299  1. Introduction and scope of defensive design
     ...
```

`make check` runs the whole checklist: word count in range, the 10 mandatory headings present,
the 13 table captions numbered and referenced in the text, no leftover `[..]` placeholders, no
images (the rubric forbids screenshots of matrices), no section symbol, and the source mix
(≥8 entries, ≥3 course resources, ≥3 technical frameworks) with bidirectional citation checks.

## Quick start (raw commands)

```bash
# PDF
pandoc doc.md -o report.pdf \
  -f markdown+autolink_bare_uris \
  --pdf-engine=xelatex \
  --toc -V toc-title="Contents" \
  -H header.tex \
  -V documentclass=article \
  -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" \
  -V fontsize=12pt -V papersize=a4 \
  -V geometry:margin=2.54cm \
  -V parskip=4pt -V indent=false

# Editable Word
pandoc doc.md -o report.docx -f markdown+autolink_bare_uris --toc -V toc-title="Contents"
```

Result: `report.pdf` / `report.docx` in this folder. Re-run after every edit to `doc.md`.

## What the flags do

| Flag | Effect |
|---|---|
| `-o report.pdf` | Output file. |
| `--pdf-engine=xelatex` | LaTeX engine with Unicode support (TeX Live's `xelatex`). |
| `-V mainfont=...` / `-V monofont=...` | DejaVu fonts so symbols (`≥`, `→`) and accents render. |
| `--toc -V toc-title="Contents"` | Insert a table of contents with this heading. |
| `-H header.tex` | Extra LaTeX: `graphicx`, `float`, `booktabs`, `longtable`, `array` and figure sizing so the wide matrices fit. |
| `-V documentclass=article` | Base LaTeX class. |
| `-V geometry:...` | Tight page margins for a slim layout. |
| `-V indent=false` | No first-line paragraph indentation. |

## Structure

```
doc.md        report content (10 mandatory sections + AI appendix)
Makefile      render targets (pdf / docx / tex / wordcount / check / clean)
header.tex    LaTeX preamble extras (tables)
README.md     this file
../tools/check_report.py  verification script (word count + rubric checks)
```

## Table inventory (editable matrices → rubric criterion)

Every matrix is a native Markdown table in `doc.md`, titled, numbered and referenced in the text.
`plan.md` Section 4 uses the same numbers, so both files point at the same object.

| Table | In `doc.md` | Content | Rubric |
|---|---|---|---|
| 1 | Section 2.1 | Asset classification by domain (A-01…A-08) | C2.a |
| 2 | Section 2.2 | Attack vectors from Challenge 2 (10) | C2.a/Section 2 |
| 3 | Section 2.3 | Vulnerability matrix (CVE/CWE · CVSS) | Section 2 |
| 4 | Section 3 | Risk prioritization (6 criteria, descending) | C2.b |
| 5 | Section 4 | Traceability matrix vector–control (10 fields + vector label) | C2.c |
| 6 | Section 5.1 | Hardening a) Web / LAMP (≥4) | C2.d |
| 7 | Section 5.2 | Hardening b) IT / Windows (≥4) | C2.d |
| 8 | Section 5.3 | Hardening c) IoT / OT (≥4) | C2.d |
| 9 | Section 6.1 | SIEM/XDR detection rules (≥6) | C2.e |
| 10 | Section 6.2 | Monitoring and alerting plan | C2.e |
| 11 | Section 7 | DevSecOps practices (≥4) | C2.g |
| 12 | Section 8 | NIST SP 800-61 playbook (life cycle → 6 rubric steps) | C2.f |
| 13 | Section 9 | Validation criteria for the authorized Cyber Range (≥5) | C2.h |

## Before submitting (rubric C1 / C3)

Run `make check` — it verifies every item below automatically.

- Word count of the body, **excluding references**, is **6,000–8,000**.
- The **10 sections** have visible headings; every table is **titled, numbered and referenced** in
  the text; all tables are **editable** (no screenshots, no external links).
- Include the **no-test declaration** and the **AI-usage declaration/log**.
- References in **APA** with **≥8 sources** (≥3 course resources + ≥3 technical frameworks).
