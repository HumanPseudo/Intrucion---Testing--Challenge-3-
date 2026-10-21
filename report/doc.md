---
title: "Challenge 3 — Design of detection, defense and cyber-attack management strategies for IT and IoT environments"
author: "Camilo David Lasso Guzmán"
subtitle: "Intrusión y Testing (203028113) · Challenge 3 · ECBTI–UNAD"
date: "2026-10-25"
lang: en
---

# 1. Introducción y alcance del diseño defensivo (Introduction and scope)

This report presents the defensive design required by Challenge 3 of *Intrusión y Testing*
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

**Declaration of no tests executed (rubric C3.e).** No tests, exploitation attempts or live
validation were executed at any point of this challenge: no vulnerability was exploited, no
payload was delivered against the portal, no credential was used against the corporate network, no
command was sent to the irrigation controller and no social-engineering action was carried out.
This is a design-only deliverable: every control is a proposal whose effectiveness is described as
*expected evidence*, and its verification is deferred in full to the authorized Cyber Range of
Challenge 4, under the rules of engagement established there. The report therefore contains no
test results — only the validation criteria and the evidence that will be required.

**AI-usage declaration (rubric C3.b).** The complete AI-usage declaration and prompt log —
tool, purpose, prompts, verification and own adjustments — is included as the appendix at the end
of this document.

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

> **[to complete — 1 paragraph + table]** Reuse the 7 Kill-Chain phases (Reconnaissance →
> Actions on Objectives) and the 13 techniques in 7 tactics (T1595, T1589, T1566, T1190, T1059,
> T1543.003, T1110.001, T1552.001, T1539, T1606.001, T1021.002, T1210, T0855). Highlight that
> *Impair Process Control* (T0855) is the only tactic with no control — the argument for
> prioritizing IoT/OT defense.

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

> **[to complete — intro paragraph]** State that hardening follows CIS Controls and OWASP, and that
> every action names the vector it mitigates. **Tables 6–8** are the per-domain hardening
> checklists; **Section 5.4** covers the application-layer controls.

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

> **[to complete — 1 paragraph]** Define the SIEM/XDR strategy and how the use cases correlate.
> **Table 9** holds the detection rules and **Table 10** the monitoring/alerting plan.

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

> **[to complete — 1 paragraph]** Chosen prioritized scenario: **[portal compromise *or* irrigation
> manipulation — choose one]**. **Table 12** applies NIST SP 800-61.

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

> **[to complete — 1 paragraph]** No tests are run here; define what will be verified in the Cyber
> Range. **Table 13** lists the criteria.

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

> **[to complete — 1 paragraph]** Contributions, limitations, recommendations for later validation.

## References (APA)

> **[to complete — APA 7, ≥8 sources: ≥3 course resources + ≥3 technical frameworks]**

**Course resources (planned):**

- Crespo-Martínez, E. (2021). Análisis de vulnerabilidades con SQLMAP aplicada a entornos APEX 5. *Ingenius, Revista de Ciencia y Tecnología*, (25), 104–113. https://doi.org/10.17163/ings.n25.2021.10
- Lu, H.-J., & Yu, Y. (2021). Research on WiFi penetration testing with Kali Linux. *Complexity, 2021*, Article 5570001. https://doi.org/10.1155/2021/5570001
- Benavides-Astudillo, E., Fuertes-Díaz, W., & Sánchez-Gordon, S. (2020). Un experimento para crear conciencia en las personas acerca de los ataques de Ingeniería Social. *Revista Ciencia UNEMI, 13*(32), 27–40. https://doi.org/10.29076/issn.2528-7737vol13iss32.2020pp27-40p
- Benavides, E., Fuertes, W., & Sánchez, S. (2020). Caracterización de los ataques de phishing y técnicas para mitigarlos. Ataques: una revisión sistemática de la literatura. *Revista Ciencia y Tecnología, 13*(1), 97–104. https://doi.org/10.18779/cyt.v13i1.357
- Albininé Budavári, E., Albini, A., & Mester, G. (2023). The role of social engineering in the energy balance of systems. *Interdisciplinary Description of Complex Systems, 21*(2), 168–173. https://doi.org/10.7906/indecs.21.2.5
- Prado Díaz, J. P. (2021). Ingeniería social, un ejemplo práctico. *Revista ODIGOS, 2*(3), 47–76. https://doi.org/10.35290/ro.v2n3.2021.493
- Palomo Luna, D. F., Zambrano Hernández, L. F., Moreno Molano, S. X., & Peña Hidalgo, H. J. (2024). Una mirada a metodologías para pruebas de penetración en ciberseguridad. *CSIRT Académico UNAD, Boletín Informativo N.º 28*. https://selloeditorial.unad.edu.co/images/Documentos/ciberseguridad/Boletin/Octubre_2024.pdf
- Zambrano, L. F. (2026). *Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT* [OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/83223 — **[to be verified: handle returns 404]**
- Zambrano, L. F. (2026). *Vectores de ataque y estrategias de defensa* [OVA]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/83229 — **[to be verified: handle returns 404]**

**Technical frameworks (to add — real, verifiable, cited; ≥3):** CIS Controls; NIST CSF; NIST SP 800-61; ISO/IEC 27001; OWASP ASVS/WSTG + Top 10 (A03:2021); MITRE ATT&CK; NVD.

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
