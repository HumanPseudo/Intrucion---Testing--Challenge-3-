---
title: "Challenge 3 — Design of detection, defense and cyber-attack management strategies for IT and IoT environments"
author: "Camilo David Lasso Guzmán"
subtitle: "Intrusión y Testing (203028113) · Challenge 3 · ECBTI–UNAD"
date: "2026-10-25"
lang: en
---

# 1. Introducción y alcance del diseño defensivo (Introduction and scope)

This report presents the defensive design strategy analysis required by Challenge 3 of *Intrusión y Testing*
(203028113) and is the direct continuation of the offensive analysis delivered in Challenge 2.
Its purpose is to demonstrate learning outcome RA2 by designing an integral scheme of detection,
identification, hardening, monitoring, containment and response, built from the offensive
techniques and the adversarial thinking already applied to the case. The design covers the three
domains of AgroSmart del Sumapaz S.A.S. — the **DMZ/Web LAMP** environment, the **corporate IT**
network and the **IoT/OT** layer of the smart greenhouse — and every control, hardening action and
detection rule is traceable to a vector, asset or probable cause identified in Challenge 2 and
anchored in Annex 1; nothing about the case is re-invented here.

**Case.** AgroSmart del Sumapaz S.A.S. — a single case shared by Challenges 2–5 (systems and data
come from Annex 1 and the Challenge 2 instruments).

**Relation with the Challenge 2 findings.** The offensive analysis is consumed here, not repeated.
Challenge 2 delivered eight critical assets (A-01…A-08) with their exposure surfaces, ten attack
vectors, a nine-row CVE/CVSS matrix with its CWE mappings, the seven phases of the Cyber Kill Chain
and thirteen MITRE ATT&CK techniques bound to those phases. Those findings are the input of this
report: the vectors become the rows of the traceability matrix, the assets become the unit of
criticality, and the techniques become the anchor of each detection rule. The attack paths were
built with the penetration-testing methodologies reviewed in the course (Palomo Luna et al., 2024;
Lu & Yu, 2021) and with web-application vulnerability analysis (Crespo-Martínez, 2021); the human
factor present in vector 7 was characterized following the social-engineering and phishing
literature of the course (Albininé Budavári et al., 2023; Benavides et al., 2020; Benavides-Astudillo
et al., 2020; Prado Díaz, 2021).

**Defensive frame of reference.** The design is organized around the six functions of the NIST
Cybersecurity Framework (CSF) 2.0 — Govern, Identify, Protect, Detect, Respond and Recover — because
that taxonomy lets each Challenge 2 vector travel from exposure to response without inventing a
parallel control catalogue (NIST, 2024; Mantilla Torres, 2025a, 2025b, 2025c). The course OVI on
detection and management of attacks in IT/IoT environments supplies the operational reading of that
frame: it links attack vectors and adversarial thinking with the Cyber Kill Chain and MITRE ATT&CK,
and it orders detection and incident response around evidence rather than around tools (Zambrano
Hernández, 2026). The report therefore uses CSF 2.0 for the architecture of the defense, the OVI for
the detection-and-response logic, and NIST SP 800-61 for the incident-response phases (Cichonski et
al., 2012).

**Scope and exclusions.** This deliverable is design only, and the following are explicitly outside
its scope: (a) exploitation of any vulnerability, whether proof of concept or complete; (b) live
testing of the production assets described in Annex 1; (c) validation of exploitation on a virtual
machine or laboratory; (d) destructive or availability-impacting actions, including denial of
service against the portal, the MQTT broker or the irrigation controller; (e) real or simulated data
exfiltration; and (f) any executed social-engineering action against the staff of AgroSmart del
Sumapaz S.A.S. No activity of that kind was carried out and no argument in this report depends on
one: every control is argued from the Challenge 2 findings and from the technical literature, and
every verification step is written as a criterion to be executed later, in the authorized Cyber
Range.

**Declaration of no tests executed (rubric C3.e).** No test, exploitation attempt or live validation
was executed at any point in this challenge: no vulnerability was exploited, no payload was delivered
against the portal, no credential was used against the corporate network, no command was sent to the
irrigation controller and no social-engineering action was carried out. The report therefore
contains no test results — only the validation criteria and the expected evidence that will be
required. The verification of every proposed control is deferred in full to the authorized Cyber
Range of Challenge 4, under the rules of engagement established there.

**AI-usage declaration (rubric C3.b).** The complete AI-usage declaration and prompt log —
tool, purpose, prompts, verification and own adjustments — is included as the appendix at the end
of this document.

**Structure, method and evidence conventions.** The deliverable is an individual technical report of
6,000–8,000 words (excluding the reference list), delivered as .docx or PDF and organized in the ten
titled sections of the rubric. Every matrix is an editable table integrated in this document, with a
title, a number and a reference in the text; no screenshot, image of a table or link to an external
repository substitutes the requested content. Control proposals follow the preventive, detective and
corrective taxonomy of the traceability matrix, and each one is anchored both in the corresponding
Annex 1 instrument and in a recognized framework — CIS Controls, NIST CSF, NIST SP 800-61,
ISO/IEC 27001, OWASP ASVS/WSTG, MITRE ATT&CK and the National Vulnerability Database records (NVD,
n.d.). Citations and the reference list follow APA 7.

# 2. Síntesis del análisis ofensivo del Reto 2 (Synthesis of the Challenge 2 offensive analysis)

> **[to complete — 1–2 paragraphs]** Condense the offensive analysis: assets, exposure surfaces,
> vectors, CVE/CVSS, Cyber Kill Chain phases and MITRE ATT&CK techniques. Reuse, do not re-analyse.
> Refer to the instruments built here: **Table 1** classifies the assets, **Table 2** lists the
> vectors and **Table 3** the vulnerabilities.

## 2.1 Asset classification by domain

**Table 1 — Asset classification by domain (rubric C2.a).**

| ID | Asset | Domain | Function | Criticality (C-I-D) | Exposure |
|----|-------|--------|----------|---------------------|----------|
| A-01 | Portal AgroSmart (web) | DMZ/Web LAMP | B2B orders + customer data | Critical (13) | Internet |
| A-02 | DB web manager (phpMyAdmin) | DMZ/Web LAMP | Direct production DB management | Critical (14) — max | Internet |
| A-03 | FILESRV01 file/domain server | IT | Business files + AGROSMART domain | Critical (12) | Internal |
| A-04 | CONTA-PC accounting workstation | IT | Billing and quotes | Medium-high (10) | Internal |
| A-05 | IoT gateway | IoT/OT | Links sensors to the network | Medium-high (10) | Internal |
| A-06 | IP greenhouse camera | IoT/OT | Greenhouse surveillance | Medium (8) | Internal |
| A-07 | Irrigation controller (PLC) | IoT/OT | Crop irrigation control | Critical (13) | Internal |
| A-08 | Telemetry broker (MQTT) | IoT/OT | Carries telemetry and commands | Critical (11) | Internal |

## 2.2 Attack vectors (10)

**Table 2 — Attack vectors from Challenge 2 (10).**

| # | Vector | Asset | Precondition | Result | Evidence |
|---|--------|-------|--------------|--------|----------|
| 1 | Web app exploitation (Apache 2.4.49) | A-01 | Vulnerable banner reachable | RCE in DMZ | Nmap/NSE (Sec. 3.2, 3.7a) |
| 2 | SQL injection in `productos.php` | A-01 | `categoría` parameter unsanitized | Orders DB extraction | SQL error 500 (Sec. 3.3c) |
| 3 | IDOR in the API | A-01 | Endpoint accepts any `id` | Third-party PII disclosure | `GET /api/v1/usuario?id=…` (Sec. 3.8c) |
| 4 | Session forgery (JWT `alg:none`) | A-01 | Portal accepts `alg:none` | Forge any role | `Set-Cookie: token=…` (Sec. 3.8d) |
| 5 | Credential theft from exposed file | A-01→A-03 | `.bak` and `.git` accessible | DB and DevOps credentials | `config.php.bak`, `.git/config` (Sec. 3.8b-c) |
| 6 | Default credentials on the gateway | A-05 | Telnet 23 and panel without MFA | Gateway access → OT segment | `admin:admin`, `root:12345` (Sec. 3.5, 3.10d) |
| 7 | Phishing / pretexting | A-04 | Email impersonating the IT vendor | Business credentials (reusable over SMB) | Reported email (Sec. 3.4) |
| 8 | SMB lateral movement with null session | A-03 | SMBv1 unsigned + null session | Share read (`red_credenciales.txt`) | `enum4linux`/`smbclient -N` (Sec. 3.9a-b) |
| 9 | OT command manipulation via MQTT/Modbus | A-07/A-08 | Anonymous broker; Modbus without auth | Unauthorized irrigation opening | `PUBLISH invernadero/riego/cmd` (Sec. 3.6, 3.11) |
| 10 | Outdated client components and weak TLS | A-01 | jQuery 1.7.2, Bootstrap 3.3.7, SHA-1 cert | Client XSS / interception | `whatweb`, `ssl-cert` NSE (Sec. 3.7a) |

## 2.3 Vulnerability matrix (CVE / CVSS)

**Table 3 — Vulnerability matrix: CVE / CWE · CVSS.**

| Asset | Finding | CVE/reference | CVSS v3.1 vector | Score/Severity |
|-------|---------|---------------|------------------|----------------|
| A-01 Web | Apache 2.4.49 path traversal/RCE | CVE-2021-41773 | `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` | 9.8 Critical |
| A-01 Web | Incomplete 2.4.50 patch (bypass) | CVE-2021-42013 | idem | 9.8 Critical |
| A-03 IT | SMBv1 unsigned | CVE-2017-0143 (MS17-010) | `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` | 8.8 High |
| A-06 IoT | Old Boa camera (fw 5.2.0) | CVE-2017-9833 (disputed) | `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | 7.5 High |
| A-01 Web | SQL error in `productos.php` | CWE-89 (OWASP A03:2021) | Remote, unprivileged | 9.8 Critical* |
| A-01 Web | API returns other users' data | CWE-639 | Change `id` returns another record | 7.5 High* |
| A-01 Web | JWT signed with `alg:none` | CWE-347 | Portal accepts unsigned token | 8.1 High* |
| A-01 Web | File upload without validation | CWE-434 | Accepts any file | 8.8 High* |
| A-08 IoT/OT | Anonymous MQTT broker | CWE-306 | Connects/publishes without credential | 9.1 Critical* |

> Alternative camera CVE: CVE-2022-45956 (5.3 Medium, `HEAD` auth bypass) — verify if firmware is
> inspected. CVE-2021-41773, CVE-2021-42013 and CVE-2017-0143 are in the CISA KEV catalog.

## 2.4 Cyber Kill Chain and MITRE ATT&CK

The course OVI reads Cyber Kill Chain and MITRE ATT&CK as complementary rather than
interchangeable: the first narrates the sequence of an intrusion from reconnaissance to actions on
objectives, while the second names the tactics and techniques observable at each stage (Zambrano
Hernández, 2026; Strom et al., 2018). The 13 techniques retained from Challenge 2 distribute across
seven tactics: reconnaissance (T1595, T1589); initial access (T1566, T1190); execution (T1059);
persistence (T1543.003); credential access (T1110.001, T1552.001, T1539, T1606.001); lateral movement
(T1021.002, T1210); and impairment of process control (T0855). The last one is the only technique with
no preventive or detective control in the Challenge 2 matrix, and it is the reason the IoT/OT domain is
prioritized in Section 3: an authorized command published to the MQTT broker can open the irrigation
valve without touching the corporate network.

# 3. Matriz de priorización de riesgos (Risk prioritization matrix)

> **[to complete — 1 paragraph]** Score every vector on the six mandated criteria and justify the
> order. Priority rule: the physical-operational risk (irrigation) and the business/data risk
> (portal) come first. **Table 4** shows the scored matrix.

**Table 4 — Risk prioritization matrix (6 criteria; one row per vector, ordered descending).**

| Rank | Vector (Challenge 2) | Asset criticality | Impact | Probability | CVSS severity | Exposure | Cross-domain propagation | Priority |
|------|----------------------|-------------------|--------|-------------|---------------|----------|--------------------------|----------|
| 1 | 9 · OT command manipulation (MQTT/Modbus) | [..] | 5 | 4 | 9.1 | Internal | High (OT→physical) | [..] |
| 2 | 2 · SQLi in `productos.php` | [..] | 4 | 5 | 9.8 | Internet | Medium | [..] |
| 3 | 1 · Web app exploitation (Apache 2.4.49) | [..] | 4 | 5 | 9.8 | Internet | Medium | [..] |
| 4 | 4 · JWT `alg:none` session forgery | [..] | 4 | 4 | 8.1 | Internet | Medium | [..] |
| 5 | 8 · SMB lateral movement (null session) | [..] | 4 | 4 | 8.8 | Internal | High (IT→DMZ) | [..] |
| 6 | 5 · Credential theft from `.bak`/`.git` | [..] | 3 | 4 | — | Internet | Medium | [..] |
| 7 | 3 · IDOR in the API | [..] | 3 | 4 | 7.5 | Internet | Low | [..] |
| 8 | 6 · Default credentials on the gateway | [..] | 3 | 3 | — | Internal | High (IoT→OT) | [..] |
| 9 | 7 · Phishing / pretexting | [..] | 3 | 3 | — | Email | Medium | [..] |
| 10 | 10 · Outdated components and weak TLS | [..] | 2 | 4 | — | Internet | Low | [..] |

> **[to complete]** Replace the `[..]` cells with the numeric scores and the final priority value,
> then state the decision rule used (e.g., weighted sum or risk = P×I with domain multipliers).

# 4. Matriz de trazabilidad vector–control (Traceability matrix vector–control)

> **[to complete — 1 paragraph]** This is the articulating instrument. **Decision on columns:** the
> rubric lists **9** columns and the guide adds **"expected evidence"**, giving **10**; deliver all
> 10 (a superset that satisfies both). Every control must map to a vector/asset/cause. **Table 5**
> is the spine of the report.

**Table 5 — Traceability matrix vector–control (Annex 1 instrument 3.1; ≥8 vector rows, 10 columns).**

| Vector | Probable cause | Affected asset | Impact | Kill Chain phase | MITRE technique | CVE/reference | Preventive control | Detective control | Corrective control | Expected evidence |
|--------|----------------|----------------|--------|------------------|-----------------|---------------|--------------------|-------------------|--------------------|-------------------|
| 1 · Web app exploitation | Apache 2.4.49 unpatched | A-01 | RCE in DMZ | Exploitation | T1190 | CVE-2021-41773 | [..] | [..] | [..] | [..] |
| 2 · SQLi | Unsanitized `categoría` parameter | A-01 | DB extraction | Exploitation | T1190 | CWE-89 | [..] | [..] | [..] | [..] |
| 3 · IDOR in API | Missing object-level authorization | A-01 | PII disclosure | Actions on Objectives | — | CWE-639 | [..] | [..] | [..] | [..] |
| 4 · JWT `alg:none` | Unsigned token accepted | A-01 | Role forgery | Credential Access | T1606.001 | CWE-347 | [..] | [..] | [..] | [..] |
| 5 · Credential theft | `.bak`/`.git` exposed | A-01→A-03 | Credential reuse | Credential Access | T1552.001 | — | [..] | [..] | [..] | [..] |
| 6 · Default credentials (gateway) | Telnet/panel without MFA | A-05 | OT segment access | Initial Access | T1078 | — | [..] | [..] | [..] | [..] |
| 7 · Phishing / pretexting | Vendor-impersonating email | A-04 | Business credential | Initial Access | T1566 | — | [..] | [..] | [..] | [..] |
| 8 · SMB lateral movement | SMBv1 unsigned + null session | A-03 | Share read | Lateral Movement | T1021.002 | CVE-2017-0143 | [..] | [..] | [..] | [..] |
| 9 · OT command manipulation | Anonymous MQTT; Modbus without auth | A-07/A-08 | Unauthorized irrigation | Actions on Objectives | T0855 | CWE-306 | [..] | [..] | [..] | [..] |
| 10 · Outdated components / weak TLS | jQuery/Bootstrap old; SHA-1 cert | A-01 | Client XSS/interception | Exploitation | T1557 | — | [..] | [..] | [..] | [..] |

# 5. Diseño de controles defensivos (Design of defensive controls)

The control design follows the CSF 2.0 functions so that each action has a defensive purpose before
it has a tool: Govern assigns roles and supplier risk, Identify fixes the asset and vulnerability
baseline, Protect contains the hardening actions of Table 6 (web/LAMP), Table 7 (corporate IT) and
Table 8 (IoT/OT), Detect feeds Section 6, Respond feeds Section 8 and Recover closes the loop
through backups and restoration tests (NIST, 2024; Mantilla Torres, 2025a, 2025b). The technical
baseline is taken from the CIS Critical Security Controls v8 for the hardening items and from the
OWASP Top 10 for the application layer (Center for Internet Security, 2021; OWASP Foundation, 2021),
while ISO/IEC 27001:2022 provides the management-system anchor for roles, suppliers and continual
improvement (ISO/IEC, 2022). The CSF function is the *why*, the CIS/OWASP control is the *how*, and
the Challenge 2 vector is the *what for*; no action enters Tables 6, 7 or 8 without all three.

## 5.1 Hardening — a) Web / LAMP (≥4 actions) · instrument 3.2a

**Table 6 — Hardening a) Web / LAMP (instrument 3.2a).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|------------------|----------------|---------------------|-----------|--------------|
| Update Apache to a version without the identified CVE | [..] | 1 | CIS 16 / OWASP | [..] |
| Remove `/dbadmin` and `/backup` from public exposure | [..] | 5 | CIS 16 | [..] |
| Add security headers (CSP, HSTS, X-Frame-Options) | [..] | 10 | OWASP | [..] |
| Validate file uploads (type/MIME/extension) | [..] | 2 | OWASP | [..] |
| Harden TLS (disable SHA-1, strong ciphers) | [..] | 10 | CIS | [..] |
| Move backups out of the web root; restrict access | [..] | 5 | CIS | [..] |

## 5.2 Hardening — b) IT / Windows (≥4 actions) · instrument 3.2b

**Table 7 — Hardening b) IT / Windows (instrument 3.2b).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|------------------|----------------|---------------------|-----------|--------------|
| Disable SMBv1 and enable SMB signing | [..] | 8 | CIS / NIST CSF | [..] |
| Block null sessions / anonymous access | [..] | 8 | CIS | [..] |
| RDP hardening (NLA, MFA) and lockout policy | [..] | 8 | CIS | [..] |
| Segment IT ↔ IoT/OT (VLAN/firewall) | [..] | 8 | NIST CSF / ISO 27001 | [..] |

## 5.3 Hardening — c) IoT / OT (≥4 actions) · instrument 3.2c

**Table 8 — Hardening c) IoT / OT (instrument 3.2c).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|------------------|----------------|---------------------|-----------|--------------|
| Close Telnet (23) on the gateway; use SSH/HTTPS | [..] | 6 | CIS / NIST CSF | [..] |
| Change default credentials of cameras/gateway | [..] | 6 | CIS | [..] |
| Authenticate/segment MQTT; disable anonymous access | [..] | 9 | NIST CSF / ISO 27001 | [..] |
| Isolate Modbus/PLC in the OT network with access control | [..] | 9 | NIST CSF | [..] |
| Update firmware; remove unsupported components | [..] | 6 | CIS | [..] |

## 5.4 Web-application controls

> **[to complete — 1 paragraph + list]** Input validation, parameterized queries, output
> encoding, session/JWT verification, IDOR/API access control, file-upload validation, secret
> management — each tied to vectors 2, 3, 4 and 10 and to CWE-89/639/347/434.

# 6. Propuesta de monitoreo y detección (Monitoring and detection proposal)

The monitoring layer is designed as a detection pipeline, not as a log-collection exercise: sources
(Apache, Windows/Sysmon, MQTT broker, firewall and camera) feed correlation rules that turn isolated
events into incident candidates, following the sequence used by the course OVI — logs and events,
network traffic, IoT telemetry, SIEM correlation and alerts (Zambrano Hernández, 2026). Each rule in
Table 9 is bound to a Kill Chain phase and a MITRE technique from Challenge 2, so a detection gap can
be read as a missing ATT&CK coverage (Strom et al., 2018). Severity and thresholds are set so that the
first alert triggers a containment action rather than a report; Table 10 assigns the source, the
frequency, the threshold and the owner.

## 6.1 SIEM/XDR use cases (≥6)

**Table 9 — SIEM/XDR detection rules (instrument 3.3).**

| # | Rule name | Log source | Trigger condition | Severity | Expected event | Initial action |
|---|-----------|-----------|-------------------|----------|----------------|----------------|
| 1 | Brute force on `/admin` | Apache `access.log` | ≥ N POST `/admin/login` in < T s from same IP | High | Repeated 401/200 on login | Alert + temporary block |
| 2 | IT credential spraying | Windows 4625 | Multiple 4625 same user from different origins | High | Failed logons spike | SOC alert |
| 3 | Unauthorized MQTT | MQTT broker | Anonymous CONNECT + PUBLISH on a `/cmd` topic | Critical | Command topic write | Block + OT alert |
| 4 | Sensitive path probing | Apache `access.log` | Requests to `.bak`, `.git`, `/backup`, `/dbadmin` | High | 200/403 on sensitive paths | Alert + WAF rule |
| 5 | SQLi pattern in requests | WAF / `error.log` | SQL metacharacters / `PDOException` in logs | High | 500 + SQL syntax error | WAF block + alert |
| 6 | New service persistence | Windows 7045 + Sysmon 1 | Service installed from `C:\Windows\Temp\*` | Critical | `WinHlp32Svc` created | Isolate host + alert |
| 7 | Suspicious outbound C2 | Sysmon 3 / firewall | Outbound connection to `:1883` from IT hosts | High | Unexpected MQTT egress | Investigate + block |
| 8 | Camera anomaly | Camera / RTSP logs | Repeated auth failures or streams to new hosts | Medium | Abnormal camera access | Alert |

## 6.2 Monitoring and alerting plan · instrument 3.4

**Table 10 — Monitoring and alerting plan (instrument 3.4).**

| Source / sensor | What it watches | Frequency | Alert threshold | Owner |
|-----------------|-----------------|-----------|-----------------|-------|
| WAF / web logs | Injection, brute force | Real time | [..] | SOC |
| EDR/SIEM (IT) | Anomalous logon, new services | Real time | [..] | SOC |
| MQTT broker logs | Anonymous connect / command publish | Real time | [..] | OT team |
| Firewall | Cross-zone flows, C2 egress | Real time | [..] | Network team |

# 7. Propuesta DevSecOps (DevSecOps proposal)

> **[to complete — 1 paragraph]** Integrate security into the app lifecycle to reduce recurrence.
> **Table 11** lists the practices at their lifecycle stage.

**Table 11 — DevSecOps practices (≥4, with lifecycle stage).**

| Practice | Description | Lifecycle stage | Vector/reference it prevents |
|----------|-------------|-----------------|------------------------------|
| SAST | Static analysis of source before merge | Code / build | 2, 3 (CWE-89/639) |
| DAST | Dynamic analysis on a staging deploy | Test | 1, 10 |
| SCA | Dependency and component scanning | Build | 10 (jQuery/Bootstrap) |
| Secret scanning | Detect credentials before commit | Pre-commit / CI | 5 (`config.php.bak`, `.git`) |
| Change control | Reviewed, gated releases | Release | all vectors |

# 8. Plan básico de respuesta ante incidentes (Incident response plan)

The prioritized scenario is vector 9, unauthorized command manipulation through the anonymous MQTT
broker and the unauthenticated Modbus PLC (Table 4, rank 1). The playbook follows the six NIST SP
800-61 phases — preparation, detection and analysis, containment, eradication, recovery and lessons
learned (Cichonski et al., 2012) — and the operational sequence used by the course OVI: identify,
contain, eradicate, recover and learn (Zambrano Hernández, 2026). The CSF 2.0 Respond and Recover
functions supply the governance interface: who declares the incident, who authorizes an OT shutdown
and what evidence must survive recovery (NIST, 2024; Mantilla Torres, 2025b). Table 12 translates each
phase into AgroSmart-specific actions, owner and evidence.

**Table 12 — Incident-response playbook (instrument 3.5; NIST SP 800-61, 6 phases).**

| NIST SP 800-61 phase | Concrete actions in AgroSmart | Owner | Evidence/log |
|----------------------|-------------------------------|-------|--------------|
| Preparation | [..] | [..] | [..] |
| Detection and analysis | [..] | [..] | [..] |
| Containment | [..] | [..] | [..] |
| Eradication | [..] | [..] | [..] |
| Recovery | [..] | [..] | [..] |
| Lessons learned | [..] | [..] | [..] |

# 9. Criterios de validación para el Reto 4 (Validation criteria for Challenge 4)

Validation is written as a set of falsifiable hypotheses, not as a test log: each row of Table 13
names the control, the evidence that would prove it works and the method to obtain that evidence in
the Cyber Range. The Cyber Range activity included in the course OVA (OVA 3) insists on rules of
engagement, authorized scope, controlled validation and evidence retention before any technical
action (Mantilla Torres, 2025c), while the OVI frames evidence as the link between a finding and a
defensible decision (Zambrano Hernández, 2026). No criterion is executed here; the table is the
contract for Challenge 4.

**Table 13 — Validation criteria for Challenge 4 (≥5, with expected evidence and method).**

| # | Control / hypothesis to validate | Expected technical evidence | Verification method (Cyber Range) |
|---|----------------------------------|-----------------------------|-----------------------------------|
| 1 | Apache patched (≥2.4.51) blocks CVE-2021-41773/42013 | Traversal attempt fails (403/404) | `curl` / `nmap --script http-vuln-cve2021-41773` |
| 2 | SQLi mitigated by parameterized queries + WAF | Payload blocked, no SQL error | Manual payload + WAF log review |
| 3 | JWT signature verified (`alg:none` rejected) | Forged token rejected | Send `alg:none` token, expect 401 |
| 4 | SMBv1 disabled, signing on, null session blocked | `smbclient -N` fails; signing required | `smbclient` / `nmap --script smb-security-mode` |
| 5 | MQTT requires auth; anonymous publish denied | Anonymous `CONNECT` refused | `mosquitto_pub` with/without creds |
| 6 | Modbus/PLC isolated; unauthorized writes blocked | Write attempt rejected/no effect | Modbus client test in OT segment |

# 10. Conclusiones y referencias (Conclusions and references)

This report converts the Challenge 2 offensive findings into a defensive design that is traceable end
to end: each control starts from a vector, a probable cause and an affected asset, and ends in an
expected evidence line. The contribution is the chain vector → probable cause → control → evidence,
organized by the CSF 2.0 functions and operationalized through the course OVI's detection and response
sequence. The main limitation is that no control has been validated: thresholds, correlation rules and
playbook times are design hypotheses to be tested in the Cyber Range. A second limitation is the
reliance on course materials and framework guidance rather than measured results; the OVA/OVI and the
NIST, CIS and OWASP references orient the design but do not substitute for validation. The next step
is to execute Table 13 under the Challenge 4 rules of engagement and feed the results back into
Tables 5, 9 and 12.

## References (APA)

**Course resources**

- Albininé Budavári, E., Albini, A., & Mester, G. (2023). The role of social engineering in the energy balance of systems. *Interdisciplinary Description of Complex Systems, 21*(2), 168–173. https://doi.org/10.7906/indecs.21.2.5
- Benavides, E., Fuertes, W., & Sánchez, S. (2020). Caracterización de los ataques de phishing y técnicas para mitigarlos. Ataques: una revisión sistemática de la literatura. *Revista Ciencia y Tecnología, 13*(1), 97–104. https://doi.org/10.18779/cyt.v13i1.357
- Benavides-Astudillo, E., Fuertes-Díaz, W., & Sánchez-Gordon, S. (2020). Un experimento para crear conciencia en las personas acerca de los ataques de Ingeniería Social. *Revista Ciencia UNEMI, 13*(32), 27–40. https://doi.org/10.29076/issn.2528-7737vol13iss32.2020pp27-40p
- Crespo-Martínez, E. (2021). Análisis de vulnerabilidades con SQLMAP aplicada a entornos APEX 5. *Ingenius, Revista de Ciencia y Tecnología*, (25), 104–113. https://doi.org/10.17163/ings.n25.2021.10
- Lu, H.-J., & Yu, Y. (2021). Research on WiFi penetration testing with Kali Linux. *Complexity, 2021*, Article 5570001. https://doi.org/10.1155/2021/5570001
- Mantilla Torres, E. A. (2025a). *Marco de seguridad cibernética 2.0 del NIST para gestión de los riesgos de seguridad cibernética* (OVA 1) [OVA]. Universidad Nacional Abierta y a Distancia. https://view.genially.com/6a29f213dc375b9eff3ca8b8/presentation-ova-1-iyt-203028113
- Mantilla Torres, E. A. (2025b). *Marco de seguridad cibernética 2.0 del NIST para gestión de los riesgos de seguridad cibernética* (OVA 2) [OVA]. Universidad Nacional Abierta y a Distancia. https://view.genially.com/6a29fb634ab60d77b87d6b2c/presentation-ova-2-iyt-203028113
- Mantilla Torres, E. A. (2025c). *Marco de seguridad cibernética 2.0 del NIST para gestión de los riesgos de seguridad cibernética* (OVA 3) [OVA]. Universidad Nacional Abierta y a Distancia. https://view.genially.com/6a2c82d71c0297a142919615/presentation-ova-3-iyt-203028113
- Palomo Luna, D. F., Zambrano Hernández, L. F., Moreno Molano, S. X., & Peña Hidalgo, H. J. (2024). Una mirada a metodologías para pruebas de penetración en ciberseguridad. *CSIRT Académico UNAD, Boletín Informativo N.º 28*. https://selloeditorial.unad.edu.co/images/Documentos/ciberseguridad/Boletin/Octubre_2024.pdf
- Prado Díaz, J. P. (2021). Ingeniería social, un ejemplo práctico. *Revista ODIGOS, 2*(3), 47–76. https://doi.org/10.35290/ro.v2n3.2021.493
- Zambrano Hernández, L. F. (2026). *Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT* [OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/83223 [restricted access; local copy verified]

**Technical frameworks**

- Center for Internet Security. (2021). *CIS Controls Version 8 (CIS Critical Security Controls)*. https://www.cisecurity.org/controls/v8
- Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2012). *Computer security incident handling guide* (NIST SP 800-61 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2
- ISO/IEC. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC 27001:2022).
- NIST. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSF 2.0; NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- NIST. (n.d.). *National Vulnerability Database* (NVD) [Database]. Retrieved October 22, 2026, from https://nvd.nist.gov/
- OWASP Foundation. (2021). *OWASP Top 10:2021*. https://owasp.org/Top10/
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018). *MITRE ATT&CK: Design and philosophy*. The MITRE Corporation. https://doi.org/10.13140/RG.2.2.13778.58565

---

# Appendix — AI-usage declaration / log

> **[to complete — mandatory]** Record tool, purpose, prompts, output, how it was verified, and the
> critical adjustments made. If AI was not used, state so explicitly.

| Field | Response |
|-------|----------|
| AI tool used | [..] |
| What it was used for | [..] |
| Main prompt(s) | [..] |
| Output obtained | [..] |
| How it was verified (NVD, Exploit-DB, MITRE, course) | [..] |
| Critical adjustments made | [..] |
| Approx. % of the deliverable supported by AI | [..] |
