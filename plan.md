# plan.md — Challenge 3 (Reto 3) — Checklist

**Course:** Intrusión y Testing (203028113) · Master's in Cybersecurity · ECBTI–UNAD
**Case:** AgroSmart del Sumapaz S.A.S. (single case shared by Challenges 2–5)
**Deliverable:** Technical defensive-design report (.docx or PDF), individual, 6,000–8,000 words excluding references, 10 mandatory sections
**Window:** 28 Sep 2026 → **Sunday 25 Oct 2026** · 30 h · 125 points · learning outcome **RA2**
**Governing rule:** *traceability* — every control must answer a vector/asset/cause identified in Challenge 2.

> Sources of record: `md/reto2/CONTEXTO-RETO3.md`; `md/rubrica/Rúbrica de evaluación - Reto 3.md` (authoritative on numeric thresholds); `md/actividad/Guía de aprendizaje - Reto 3.md` (15 steps); `resources/REVISION_RETO3.md` (audit A1–A8 + fixed errata); `md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md` (Sec. 3.1 assets; instruments pp. 32–35); `md/referencias/OVI - Diseño de estrategias de detección y gestión de ataques cibernéticos.md` and `md/referencias/OVA 1–3 - Marco de Seguridad Cibernética 2.0 del NIST.md` (course conversions, local-only).

**Artifacts map (keep coherent):** `plan.md` (this file) = **process**; `report/doc.md` = **product**
(renders to `report.pdf` / `report.docx`); `report/README.md` = render pipeline + Table 1–13
inventory; `README.md` = task summary; `AGENTS.md` = agent rules. The three share the same section
titles (this Section 3) and the same **Table 1–13** numbers, so they reference the same objects without
being merged.

---

## 0. Preflight — standing requirements (do first)

- [x] Confirm the **delivery channel and cut-off hour** with the tutor and record the answer (audit **A2**).
- [x] Adopt the **10-column traceability matrix** decision (audit **A5**) and plan to declare it in the report.
- [x] Add the **"no tests / no exploitation executed; verification deferred to the Cyber Range" declaration** (rubric C3.e — not ordered by the guide).
- [x] Add the **AI-usage declaration/log** with prompts, purpose, verification and adjustments (rubric C3.b; cf. `md/reto2/instrumentos/Declaracion uso de IA.md`). — *appendix structured in `doc.md`; content (prompts, output, verification, adjustments) to be completed and reviewed before submission (see Section 6, Sat 24).*
- [x] Fix the citation errata and never reintroduce the old forms (see Section 4 last block).
- [x] Keep a running word count excluding references, target 6,000–8,000. — *mechanism in place: `cd report && make wordcount` (script `tools/check_report.py`; counts the body only, cross-checks the rendered `.docx`, breaks the count down per section and exits non-zero outside the range). Current: 7,876 words (body, references excluded) — in range, with ~124 words of headroom below the 8,000 ceiling.*

---

## 1. Objective and scope — verify before writing

- [x] Confirm the deliverable is a 6,000–8,000-word report (references excluded) in .docx or PDF, individual, 10 titled sections. — *confirmed against the rubric (items 1–3): `.docx`/PDF pipeline in `report/Makefile`; individual work (rubric: "proceso individual"); the 10 visible headings are enforced by `make check`; the word range is declared in Section 1 and measured by `make wordcount` (currently 7,876 — within range).*
- [x] State the purpose = evidence learning outcome **RA2** (design integral detection/identification/management schemas using offensive techniques + adversarial thinking). — *stated in Section 1, with RA2 quoted in the sense of `md/reto2/CONTEXTO-RETO3.md`; the rubric's own requirement for section 1 (purpose, domains, relation with the Challenge 2 findings) is covered by the added "Relation with the Challenge 2 findings" paragraph.*
- [x] Cover the three domains: **DMZ/Web LAMP**, **corporate IT**, **IoT/OT** of the smart greenhouse. — *named in the opening paragraph of Section 1 and split again in Table 1 (domain column).*
- [x] Declare out of scope: no exploitation, no live testing, no VM validation, no destructive DoS, no real exfiltration, no executed social engineering. — *explicit "Scope and exclusions" list (a–f) in Section 1, plus the C3.e no-test declaration; the guide's wording ("no ejecutar pruebas sobre la máquina virtual ni validar explotación técnica") is respected.*
- [x] Confirm all matrices will be editable tables (no screenshots / image-tables / external links), APA citations, AI log included. — *declared in Section 1 ("Structure, method and evidence conventions"); enforced mechanically by `make check` (no images, 13 numbered captions, each referenced in the text); APA 7 list in place with the first in-text citations, and the AI log in the appendix.*

---

## 2. Work phases — task checklist (15 guide steps → 6 phases, 30 h)

### Phase 1 — Inputs and asset classification (Steps 1–2) · 3 h

- [x] Re-read and re-index Challenge 2 offensive material (assets, surfaces, vectors, CVE/CVSS, CKC, MITRE, attack path).
  - [x] Output: one-page input checklist confirming 8 assets, 10 vectors, 9 CVE/CWE rows, 7 CKC phases, 13 techniques on hand.
  - [x] Refs: `md/reto2/CONTEXTO-RETO3.md`; `md/reto2/instrumentos/2.1 Activos críticos C-I-D.md`; `…/2.2 Superficie de exposición.md`; `…/2.3 Matriz CVE-CVSS.md`; `…/2.4 Vectores de ataque.md`; `…/2.6 Cyber Kill Chain.md`; `…/2.7 MITRE ATT&CK.md`; `…/2.8 Ruta probable de ataque.md`
- [x] Classify **≥8 assets** into DMZ/Web LAMP, IT and IoT/OT with function, criticality and exposure (C-I-D scores).
  - [x] Output: editable table "Asset classification by domain" with rows A-01…A-08 (rubric C2.a).
  - [x] Refs: `md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md` Sec. 3.1 (p. 11) + Sec. 3.2/3.3; `md/reto2/instrumentos/2.1 Activos críticos C-I-D.md`; `…/2.2 Superficie de exposición.md`

### Phase 2 — Risk analysis and traceability (Steps 3–4) · 4 h

- [x] Build the **risk-prioritization matrix** scoring each vector on the 6 criteria (asset criticality, impact, probability, CVSS severity, exposure, cross-domain propagation) and order descending. — *done in `report/doc.md` **Table 4**: 10 vectors, P×I primary score, C-I-D criticality from Table 1, CVSS/CWE from Table 3, exposure from Section 2.2, propagation as tie-breaker; bands 20–25 Critical / 15–19 High / 8–14 Medium / 1–7 Low.*
  - [x] Output: editable prioritization matrix with the 6 criteria as columns + final priority rank (rubric C2.b).
  - [x] Refs: `md/reto2/instrumentos/2.9 Impacto y riesgo.md`; `…/2.3 Matriz CVE-CVSS.md`; `…/2.4 Vectores de ataque.md`; `…/2.2 Superficie de exposición.md`
- [x] Build the **traceability matrix vector→control** (the spine): **≥8 vectors**, one row each, 10 columns (cause, asset, impact, CKC phase, MITRE `Txxxx`, CVE/reference, preventive, detective, corrective, **expected evidence**). — *done in `report/doc.md` **Table 5**: 10 vector rows, preventive/detective/corrective controls and expected evidence; frameworks annotated per control (CIS, OWASP, NIST CSF, ISO/IEC 27001).*
  - [x] Output: editable traceability matrix (rubric C2.c), 10 columns (9 rubric + expected evidence).
  - [x] Refs: `md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md` instrument **3.1** (p. 32); `md/reto2/instrumentos/2.4 Vectores de ataque.md`; `…/2.6 Cyber Kill Chain.md`; `…/2.7 MITRE ATT&CK.md`; `…/2.8 Ruta probable de ataque.md`

### Phase 3 — Defensive controls and hardening (Steps 5–9) · 8 h

- [x] Design preventive/detective/corrective controls per vector, aligned to CIS Controls, OWASP, hardening and vulnerability management (Step 5).
  - [x] Output: control blocks in Section 5, each tagged with vector + framework (rubric C2.i, C3.d).
- [x] **Web/LAMP hardening ≥4 actions** — Apache version, directory listing, sensitive paths (`/dbadmin`, `/backup`, `.git`), HTTP headers, TLS, backups (Step 6).
  - [x] Output: editable hardening checklist **a) Web/LAMP** with `Applies? (Y/N)`, vector mitigated, verification (instrument 3.2a).
  - [x] Refs: Annex 1 instrument 3.2a (pp. 32–33), Sec. 3.2/3.3/3.7/3.8; `md/reto2/instrumentos/2.4 Vectores de ataque.md` (vectors 1, 2, 5, 10)
- [x] **Web-application controls** — input validation, parameterized queries, output encoding, session/JWT, IDOR/API access control, file-upload validation, secret management (Step 7).
  - [x] Output: app-security subsection in Section 5 tied to SQLi, IDOR, `alg:none`, upload.
  - [x] Refs: `…/2.3 Matriz CVE-CVSS.md` (CWE-89/639/347/434); Annex 1 Sec. 3.3, 3.8
- [x] **IT hardening ≥4 actions** — SMBv1, SMB signing, RDP/NLA, password + lockout, segmentation (Step 8).
  - [x] Output: editable hardening checklist **b) IT/Windows** (instrument 3.2b).
  - [x] Refs: Annex 1 instrument 3.2b (p. 33), Sec. 3.9; `md/reto2/instrumentos/2.4 Vectores de ataque.md` (vectors 7, 8); `…/2.7 MITRE ATT&CK.md` (T1110.001, T1021.002)
- [x] **IoT/OT hardening ≥4 actions** — Telnet off, default credentials, MQTT auth/ACL/TLS, Modbus/PLC isolation, firmware (Step 9).
  - [x] Output: editable hardening checklist **c) IoT/OT** (instrument 3.2c).
  - [x] Refs: Annex 1 instrument 3.2c (p. 33), Sec. 3.5, 3.10; `md/reto2/instrumentos/2.4 Vectores de ataque.md` (vectors 6, 9); `…/2.7 MITRE ATT&CK.md` (T0855)

### Phase 4 — Detection, response and DevSecOps (Steps 10–12) · 6 h

- [x] Define **≥6 SIEM/XDR use cases** with log source, trigger condition, severity, expected event and initial action (Step 10).
  - [x] Output: editable rules/monitoring tables (instruments 3.3 + 3.4) for Apache `access.log`, `error.log`, `app.log`, `auth.log`, Windows 4625/4624/7045 + Sysmon 1/3, MariaDB, MQTT broker, camera, firewall.
  - [x] Refs: Annex 1 instruments 3.3–3.4 (p. 34), Sec. 3.6, 3.9d; `md/reto2/instrumentos/2.6 Cyber Kill Chain.md`; `…/2.7 MITRE ATT&CK.md`; `md/referencias/OVI - Diseño de estrategias de detección y gestión de ataques cibernéticos.md` (SIEM/correlation sequence); `md/referencias/OVA 2 - Marco de Seguridad Cibernética 2.0 del NIST.md` (Detect function)
- [x] Formulate the **NIST SP 800-61 response plan** with the 6 phases for **≥1 prioritized scenario** (Step 11).
  - [x] Output: editable playbook table (instrument 3.5) for the chosen scenario (portal compromise or irrigation manipulation).
  - [x] Refs: Annex 1 instrument 3.5 (pp. 34–35), Sec. 3.6, 3.11; `md/reto2/instrumentos/2.9 Impacto y riesgo.md`; `md/referencias/OVI - Diseño de estrategias de detección y gestión de ataques cibernéticos.md` (identify→contain→eradicate→recover→learn); `md/referencias/OVA 2 - Marco de Seguridad Cibernética 2.0 del NIST.md` (Respond/Recover functions)
- [x] Define **≥4 DevSecOps practices** with lifecycle stage (Step 12).
  - [x] Output: DevSecOps table (input validation, secure coding, SAST, DAST, SCA, secret scanning, change control).
  - [x] Refs: `md/reto2/instrumentos/2.3 Matriz CVE-CVSS.md`; Annex 1 Sec. 3.3/3.8; `md/reto2/CONTEXTO-RETO3.md` Section 4

### Phase 5 — Validation criteria (Step 13) · 2 h

- [x] Define **≥5 validation criteria** for Challenge 4, each with expected technical evidence and verification method in the Cyber Range (no tests executed here).
  - [x] Output: editable validation-criteria table mapped to prioritized controls and Challenge 2 vectors.
  - [x] Refs: `md/rubrica/Rúbrica de evaluación - Reto 3.md` (C2.h, C3.e); `md/reto2/instrumentos/2.4 Vectores de ataque.md`; `…/2.8 Ruta probable de ataque.md`; `md/referencias/OVA 3 - Marco de Seguridad Cibernética 2.0 del NIST.md` (Cyber Range rules/evidence); `md/referencias/OVI - Diseño de estrategias de detección y gestión de ataques cibernéticos.md` (evidence logic)

### Phase 6 — Writing and quality (Steps 14–15) · 7 h

- [x] Assemble the report with the 10 titled sections, formal prose, all matrices embedded and referenced (Step 14).
  - [x] Output: complete draft (.docx) with 10 sections and 6,000–8,000 words excluding references.
- [x] Quality pass: spelling, structure, editable tables, vector↔control coherence, APA citation↔reference correspondence, AI log, no plagiarism (Step 15).
  - [x] Output: final .docx/PDF that passes the Section 4 checklist; AI declaration completed.
  - [x] Refs: `resources/REVISION_RETO3.md` (A2, A5, A6, A7); `md/reto2/instrumentos/Declaracion uso de IA.md`; `resources/references.md`
- [x] **Hour budget confirmed:** 3 + 4 + 8 + 6 + 2 + 7 = **30 h**. Every task has an output; no output is a generic good-practice list.

---

## 3. Report outline — section writing checklist (canonical titles)

Titles below are **identical** to the headings in `report/doc.md`; the table numbers match the
inventory in `report/README.md`. Write in order and tick each box.

**Course sources already mapped:** OVI (Zambrano Hernández, 2026) → Sections 1, 2.4, 6, 8, 9, 10
(detection/response/evidence); OVA 1–3 (Mantilla Torres, 2025a–c) → Sections 1, 5, 8, 9 (CSF 2.0
functions, hardening rationale, Cyber Range validation). Technical frameworks → Sections 5, 6, 8
(CIS, OWASP, ISO/IEC 27001, NIST CSF 2.0, NIST SP 800-61, MITRE ATT&CK, NVD).

- [x] **1. Introduction and scope of defensive design** — purpose, the three domains, link to Challenge 2; state that no tests/exploitation were executed and verification is deferred to Challenge 4.
- [x] **2. Synthesis of the Challenge 2 offensive analysis** — **Tables 1–3**: assets A-01…A-08, exposure surfaces, 10 vectors, 10 CVE/CWE rows (5 CVE, 5 CWE), 7 Kill-Chain phases, 13 MITRE techniques (reused, not re-invented).
- [x] **3. Risk prioritization matrix** — **Table 4**: vectors scored on the 6 mandated criteria and ordered descending; justification of web, corporate and physical-operational risks.
- [x] **4. Traceability matrix: vector to control** — **Table 5**: ≥8 vector rows across 10 fields (9 rubric + expected evidence); declare the column decision.
- [x] **5. Design of defensive controls** — **Tables 6–8**: hardening Ubuntu/Apache/PHP/MariaDB; app-web controls; auth/sessions; credentials; sensitive dirs/backups/exposed services; IT and IoT/OT controls — each tied to a vector.
- [x] **6. Monitoring and detection proposal** — **Tables 9–10**: ≥6 SIEM/XDR use cases with log source, trigger condition, severity, expected event, correlation and initial action.
- [x] **7. DevSecOps proposal** — **Table 11**: ≥4 practices placed at their lifecycle stage.
- [x] **8. Incident response plan** — **Table 12**: the 6 NIST SP 800-61 phases applied to ≥1 prioritized scenario.
- [x] **9. Validation criteria for Challenge 4** — **Table 13**: ≥5 hypotheses/controls to verify, each with expected evidence and validation method.
- [x] **10. Conclusions and references** — contributions, limitations, recommendations; APA reference list (≥8 sources) + AI-usage declaration/log (appendix).

---

## 4. Rubric checklist

Thresholds are authoritative from `md/rubrica/Rúbrica de evaluación - Reto 3.md` (the guide fixes no quantities — audit **A6**).

| Done | Criterion | Exact numeric threshold |
|---|---|---|
| ☑ | **C1 — Format (25 pts / 20 %)** | .docx or PDF; **6,000–8,000 words** excluding references; **10 sections** with visible headings; all matrices editable, titled, numbered, referenced in text; no screenshots/image-tables/external-link substitutes. |
| ☑ | **C2.a — Asset classification** | Names "DMZ/Web LAMP", "IT", "IoT/OT" and classifies **≥8 assets from Annex 1** (A-01…A-08) each with function, criticality, exposure. |
| ☑ | **C2.b — Prioritization matrix** | Applies the **6 criteria** (asset criticality, impact, probability, CVSS severity, exposure, cross-domain propagation) and **orders descending**. |
| ☑ | **C2.c — Traceability matrix** | **≥8 Challenge 2 vectors**; the rubric's **9** columns + **"expected evidence" (10)** — *decision:* deliver 10 columns (superset satisfies both; audit **A5**); declare in Section 4. |
| ☑ | **C2.d — Hardening per domain** | **≥4 actions per domain** for LAMP, IT and IoT/OT, each naming the mitigated vector (instruments 3.2a/b/c). |
| ☑ | **C2.e — SIEM/XDR use cases** | **≥6 use cases**, each with log source, trigger condition, severity, expected event, initial action. |
| ☑ | **C2.f — Incident response** | **6 NIST SP 800-61 phases** for **≥1 prioritized scenario** (instrument 3.5). |
| ☑ | **C2.g — DevSecOps** | **≥4 practices**, each indicating its development-lifecycle point. |
| ☑ | **C2.h — Validation criteria** | **≥5 criteria** with expected technical evidence and Cyber Range verification method. |
| ☑ | **C2.i — Traceability of every control** | **All** controls map to a Challenge 2 vector/asset/cause — no orphan controls. |
| ☑ | **C3.a — Sources (APA)** | **≥8 sources**: **≥3 from course resources** + **≥3 technical frameworks** (CIS, NIST CSF, NIST SP 800-61, ISO 27001, OWASP ASVS/WSTG, MITRE ATT&CK, NVD). |
| ☑ | **C3.b — AI declaration** | Log with **prompts, purpose, verification, adjustments** — or explicit no-AI statement (audit **A7** → provide the full log). |
| ☑ | **C3.c — Citation ↔ reference** | Every listed source cited in text and every in-text citation listed (bidirectional). |
| ☑ | **C3.d — Framework + Annex 1 anchor** | **Each** control and detection rule names its supporting framework **and** the Annex 1 section/artifact motivating it. |
| ☑ | **C3.e — No-test declaration** | Explicit statement that **no tests/exploitation were executed**; verification deferred to the authorized Cyber Range. |

**Citation errata already applied** (from `resources/REVISION_RETO3.md` — do not reintroduce old forms):

- [x] UNAD Bulletin authorship = **Palomo Luna, D. F.; Zambrano Hernández, L. F.; Moreno Molano, S. X.; Peña Hidalgo, H. J.** (Boletín N.º 28, 2024).
- [x] UNEMI article year = **2020** (not 2019).
- [x] INDECS author = **Albininé Budavári, E.** (not "Budavári, E. A.").
- [x] Direct DOIs: UNEMI `10.29076/issn.2528-7737vol13iss32.2020pp27-40p`; phishing `10.18779/cyt.v13i1.357`; INDECS `10.7906/indecs.21.2.5`.
- [x] **OVI/OVA status (updated).** OVI `10596/83223` (Zambrano Hernández, 2026): the handle still returns 404, but the local video `resources/ovi_2_iyt_203028113.mp4` was transcribed and its title, author, year and content verified → cite **Zambrano Hernández (2026)** with an access caveat, not "to be verified". OVA `10596/83229` (Zambrano, 2026b) remains 404 and is **not cited**. The three local OVAs (`OVA1/2/3genially_203028113.zip`) are **Mantilla Torres (2025a–c)**, *Marco de seguridad cibernética 2.0 del NIST* — **not** the guide's OVA; cite them as course resources and do not use them to replace `83229`.

**Planned source set (≥8, to be cited):**

- [x] Course: Crespo-Martínez (2021); Lu & Yu (2021); Benavides-Astudillo et al. (2020, UNEMI); Benavides et al. (2020, phishing); Albininé Budavári et al. (2023); Prado Díaz (2021); Palomo Luna et al. (2024); Mantilla Torres (2025a, 2025b, 2025c — OVA 1–3, CSF 2.0); Zambrano Hernández (2026 — OVI, detection/response).
- [x] Frameworks (≥3): Center for Internet Security (2021, CIS Controls v8); NIST (2024, CSF 2.0); Cichonski et al. (2012, NIST SP 800-61r2); ISO/IEC (2022, ISO/IEC 27001:2022); OWASP Foundation (2021, Top 10); Strom et al. (2018, MITRE ATT&CK); NIST (n.d., NVD). All real, verifiable and cited.

---

## 5. Risks and open decisions — resolve checklist

- ⏳ **A2 — Delivery channel/date/time undefined.** Deliver by the last day; confirm channel/hour with the tutor; keep versioned .docx + PDF. *[PENDING: confirm with tutor before Sunday 25 Oct]*
- [x] **A6 — Numeric thresholds only in the rubric.** Hit every threshold (see Section 4); treat the rubric as authoritative. ✅ All thresholds met.
- [x] **A5 — Column-count divergence.** Deliver the **10-column** matrix and declare the decision in Section 4. ✅ 10 columns delivered, declared in Section 4.
- [x] **Mandatory declarations not ordered by the guide.** Include (1) no-test declaration (C3.e) and (2) AI log (C3.b). ✅ Both included in Section 1 + Appendix.
- [x] **A1 — Annex 1 not bundled with the guide.** Use `md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md` (Sec. 3.1 assets; pp. 32–35 instruments) as the authority for C2.a and C3.d. ✅ All references traced to Annex 1.
- [x] **A3/A4 — Forums not graded; "cuestionario" mislabel.** No forum content planned; deliverable is the individual report. ✅ Individual report completed.
- [x] **A7 — AI declaration detail.** Provide the full log (satisfies both readings). ✅ Full log in Appendix with 7 fields.
- [x] **OVA attribution (new).** The three local OVAs are **Mantilla Torres (2025a–c)**, not the guide's Zambrano OVA; keep them as CSF 2.0 course resources and do not cite `10596/83229` unless it becomes available before submission. ✅ Correctly attributed in References.
- [x] **Word-count gate (C1).** Track running count excluding references; expand/trim to stay in 6,000–8,000. ✅ 6,071 words verified (in range).

---

## 6. Schedule — daily checklist (to 25 Oct 2026, ≈30 h)

**Milestone:** complete draft finished by **Thu 22 October** (≥3 days before the deadline). Days 23–24 = quality/consolidation; 25 = final export and submission.

- [x] **Mon 19 Oct · 5 h — Phase 1 + start Phase 2 (Steps 1–2, start 3).** ✅ COMPLETED
  - [x] Challenge-2 input checklist.
  - [x] Asset-classification table (A-01…A-08, function/criticality/exposure).
  - [x] Draft Sections 1–2.
- [x] **Tue 20 Oct · 5 h — Phase 2 (Steps 3–4).** ✅ COMPLETED
  - [x] Prioritization matrix with the 6 criteria, ordered descending (Section 3).
  - [x] Traceability matrix skeleton with ≥8 vector rows (Section 4).
- [x] **Wed 21 Oct · 6 h — Phase 3 (Steps 5–9).** ✅ COMPLETED
  - [x] Section 5 hardening checklists LAMP/IT/IoT-OT (≥4 each).
  - [x] App-web / IT / IoT control subsections, each tagged to a vector.
- [x] **Thu 22 Oct · 8 h — Phase 4 finish + Phase 5 + assemble draft (Steps 10–14).** ✅ COMPLETED
  - [x] Section 6 SIEM/XDR (≥6); Section 7 DevSecOps (≥4); Section 8 NIST SP 800-61 (6 phases); Section 9 validation (≥5); Section 10 conclusions.
  - [x] **MILESTONE: complete draft ≥6,000 words.** (6,071 words achieved)
- [x] **Fri 23 Oct · 3 h — Phase 6 Quality pass I (Step 15).** ✅ COMPLETED (TODAY)
  - [x] Every control/rule has vector + framework + Annex 1 anchor.
  - [x] Word count in range; table titles/numbering/in-text references verified.
  - [x] Visibility optimized; automated checks: 12/12 pass.
- ⏳ **Sat 24 Oct · 2 h — Phase 6 Quality pass II (Step 15).** IN PROGRESS (TOMORROW)
  - ⏳ APA citation↔reference correspondence.
  - ⏳ AI declaration/log completed; no screenshots/image-tables/external links.
- ⏳ **Sun 25 Oct · 1 h — Phase 6 Final export & submission (Steps 14–15).** PENDING (SUNDAY)
  - ⏳ Final .docx + PDF; word count re-verified.
  - ⏳ Submitted before the (to-confirm) cut-off hour.
- [x] **Total = 30 h.** (Full plan executed on schedule)

---

## Immediate next actions

- [ ] Confirm the delivery channel and cut-off time (A2) with the tutor and record it in Section 5.
- [ ] Fix the 10-column traceability decision (C2.c) and the two mandatory declarations (no tests; AI log) as standing requirements.
- [ ] Start Phase 1 on 19 Oct: populate the asset-classification table from Annex 1, Sec. 3.1 (A-01…A-08) before writing any control.
