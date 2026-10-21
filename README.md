# Challenge 3 — Defensive design (Intrusión y Testing)

**Camilo David Lasso Guzmán** · UNAD · ECBTI · Intrusión y Testing (203028113)

---

## What this phase is

Design of detection, defense and cyber-attack management strategies for the case
**AgroSmart del Sumapaz S.A.S.** in its three domains: **DMZ/Web LAMP**, **corporate IT** and
**IoT/OT** (smart greenhouse). The work is **individual** and builds on the Challenge 2 offensive
analysis. Score: **125 points**, midterm. Deliverable: a **technical defensive-design report** of
**6,000–8,000 words** (references excluded) with **10 mandatory sections**.

- **Start:** Monday, September 28, 2026
- **Close:** Sunday, October 25, 2026
- **Independent work:** 30 h
- **No technical tests are executed** — validation is deferred to the Cyber Range of Challenge 4.

## Governing rule — traceability

Every proposed control must answer a **vector, asset or probable cause** identified in Challenge 2.
A generic list of good practices is not graded; coherence between threat and defense is.

## Planned deliverable structure

Canonical titles live in `report/doc.md` and are mirrored verbatim in `plan.md` Section 3; the **Table**
column points at the matrices (Tables 1–13) inventoried in `report/README.md`.

| # | Section (canonical title in `report/doc.md`) | Table(s) | Content |
|---|---|---|---|
| 1 | Introducción y alcance del diseño defensivo (Introduction and scope) | — | Purpose, three domains, link to Challenge 2, no-test declaration |
| 2 | Síntesis del análisis ofensivo del Reto 2 (Synthesis of the Challenge 2 offensive analysis) | 1–3 | Assets, surfaces, vectors, CVE/CVSS, Kill Chain, MITRE |
| 3 | Matriz de priorización de riesgos (Risk prioritization matrix) | 4 | The 6 criteria, ordered descending |
| 4 | Matriz de trazabilidad vector–control (Traceability matrix vector–control) | 5 | ≥8 vectors, 10 columns (9 rubric + expected evidence) |
| 5 | Diseño de controles defensivos (Design of defensive controls) | 6–8 | Hardening LAMP / IT / IoT-OT (≥4 each) + web-app controls |
| 6 | Propuesta de monitoreo y detección (Monitoring and detection proposal) | 9–10 | ≥6 SIEM/XDR use cases + monitoring plan |
| 7 | Propuesta DevSecOps (DevSecOps proposal) | 11 | ≥4 practices with lifecycle stage |
| 8 | Plan básico de respuesta ante incidentes (Incident response plan) | 12 | 6 NIST SP 800-61 phases for ≥1 scenario |
| 9 | Criterios de validación para el Reto 4 (Validation criteria for Challenge 4) | 13 | ≥5 criteria for the Cyber Range |
| 10 | Conclusiones y referencias (Conclusions and references) | — | APA ≥8 sources + AI declaration (appendix) |

## Structure

```
plan.md            PROCESS: operational checklist (phases, rubric, schedule)
report/doc.md      PRODUCT: report content → report.pdf / report.docx
report/README.md   how to render + Table 1–13 inventory
AGENTS.md          agent guide (rules, errata, pipeline, verification)
README.md          this file (task summary + artifacts map)
md/                converted course material, Challenge 2 inputs and instruments
resources/         original course PDFs, references.md and the Challenge 3 audit
```

### Artifacts map — one object, three views

`plan.md`, `report/doc.md` and the READMEs are **not** merged (they have distinct roles); they stay
coherent by sharing the same **section titles** and the same **Table 1–13** numbers:

| Object | Lives in | Meaning |
|---|---|---|
| Section title (10) | `report/doc.md` headings ≡ `plan.md` Section 3 ≡ this README | The graded structure. |
| Table 1–13 | `report/doc.md` (built) ≡ `report/README.md` (inventory) ≡ `plan.md` Section 4 (rubric) | The editable matrices. |
| Phase 1–6 / schedule | `plan.md` Sections 2 and 6 | How the product gets written. |
| Rubric C1, C2.a–i, C3.a–e | `plan.md` Section 4 (authoritative thresholds) | What is scored. |

- `md/` and `resources/` hold **local reference material** (course guides, rubric, converted
  articles, original PDFs) and the Challenge 2 inputs. They are the base of the design; nothing is
  re-invented in the report.
- The deliverable sources live in `report/` (see its `README.md`).

## Rules

- Use **only** case data from `md/reto2/` and the Annex 1 case (`md/reto2/fuentes/Anexo 1 - Caso
  AgroSmart del Sumapaz.md`). Do not invent assets, vectors or CVEs.
- Matrices are **editable tables** inside the document; no screenshots, image-tables or external
  links as substitutes (rubric).
- APA citations; **≥8 sources** (≥3 course resources + ≥3 technical frameworks).
- Declare explicitly that **no tests/exploitation were executed** and that verification is deferred
  to the authorized Cyber Range.
- Include the **AI-usage declaration/log**.

## Working method

`plan.md` is the operational checklist: 6 phases over the 15 guide steps (~30 h), a rubric
checklist and a day-by-day schedule to Oct 25, 2026 (complete-draft milestone on Oct 22).
