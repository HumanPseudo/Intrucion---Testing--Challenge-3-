---
title: "Challenge 3 — Design of detection, defense and cyber-attack management strategies for IT and IoT environments"
author: "Camilo David Lasso Guzmán"
subtitle: "Intrusión y Testing (203028113) · Challenge 3 · ECBTI–UNAD"
date: "2026-10-25"
lang: en
---

# 1. Introduction and scope

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

# 2. Synthesis of the Challenge 2 offensive analysis

Challenge 2 completed a systematic offensive analysis of AgroSmart del Sumapaz S.A.S. using penetration-testing methodologies, enumerating eight critical assets across three domains (DMZ/Web LAMP, corporate IT, IoT/OT), identifying eleven exposure surfaces at the network perimeter and inside the infrastructure, and tracing ten attack vectors from initial reconnaissance through execution and actions on objectives. The analysis yielded a nine-row CVE/CVSS matrix anchored to the National Vulnerability Database and the MITRE ATT&CK framework, mapping thirteen threat techniques across seven Kill Chain phases — from reconnaissance (passive and active information gathering) through initial access (exploitation and phishing), execution, persistence, credential access, lateral movement, and finally to impairment of process control in the OT domain. Table 1 classifies the eight assets by their domain, function and criticality (using the Confidentiality–Integrity–Availability triad); Table 2 lists the ten attack vectors with their preconditions and evidence; Table 3 summarizes the CVE/CVSS scores and alternative CWE vulnerability categories where a CVE is not assigned. The synthesis feeds directly into the traceability matrix of Section 4, which inherits the vector names, affected assets, Kill Chain phases and MITRE techniques as row labels and control anchors.

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
| 8 | SMB lateral movement with null session | A-03 | SMBv1 unsigned + null session | Share read | `enum4linux`/`smbclient -N`; `red_credenciales.txt` (Sec. 3.9a-b) |
| 9 | OT command manipulation via MQTT/Modbus | A-07/A-08 | Anonymous broker; Modbus without auth | Unauthorized irrigation opening | `PUBLISH invernadero/riego/cmd` (Sec. 3.6, 3.11) |
| 10 | Outdated client components and weak TLS | A-01 | jQuery 1.7.2, Bootstrap 3.3.7, SHA-1 cert | Client XSS / interception | `whatweb`, `ssl-cert` NSE (Sec. 3.7a) |

## 2.3 Vulnerability matrix (CVE / CVSS)

**Table 3 — Vulnerability matrix: CVE / CWE · CVSS.**

| Asset | Finding | CVE/reference | CVSS v3.1 vector | Score/Severity |
|-------|---------|--------------|---------------------------|--------------|
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

# 3. Risk prioritization matrix

Table 4 scores every Challenge 2 vector on the six criteria required by the rubric and orders the
rows by the resulting priority. The primary score is the product of probability and impact (P×I) on
the 1–5 scale of the Challenge 2 risk instrument; the other four criteria are not decorative: they
break ties and explain why vectors with the same P×I do not receive the same urgency. Asset
criticality is the C–I–D sum from Table 1, CVSS is the NVD score where a CVE exists and the
asterisked CWE estimate from Table 3 where it does not, exposure is the trust boundary from Section
2.2, and cross-domain propagation records whether the vector can move from DMZ to IT or from IT to
IoT/OT. The bands follow the same instrument: 20–25 Critical, 15–19 High, 8–14 Medium and 1–7 Low.
Vector 9 is first because it scores 20 and its propagation is physical/OT; vectors 2 and 1 also score
20, but their impact is business/data, and vector 2 precedes vector 1 because SQLi exposes orders and
PII with a single parameter, whereas vector 1 requires a public exploit. Vectors 3 and 4 are
alternative paths inside that same portal-compromise scenario (20 in instrument 2.9), but they keep
their own conservative scores: IDOR discloses PII without full database extraction, and JWT forgery
requires a token, so the scenario's full weight is carried by vector 2, the direct SQLi path. Vectors
4 and 8 (16 each)
follow, with vector 4 first because it is Internet-facing; the 12-point vectors 5 and 3 are separated
by propagation (5 crosses A-01→A-03), and the 9-point vectors 6 and 7 by the same rule (6 reaches
OT). The highest CVSS does not by itself determine the order: CVSS measures technical severity, not
the probability or the physical consequence for this organization.

```{=latex}
\clearpage
```

**Table 4 — Risk prioritization matrix (6 criteria; one row per vector, ordered descending).**

| Rank | Vector (Challenge 2) | Asset criticality | Impact | Probability | CVSS severity | Exposure | Cross-domain propagation | Priority |
|------|--------------------|---------------|--------|------------|------------|-----------|-------------------------|---------------|
| 1 | 9 · OT command manipulation (MQTT/Modbus) | 13 / 11 | 5 | 4 | 9.1* | Internal | High (OT→physical) | 20 · Critical |
| 2 | 2 · SQLi in `productos.php` | 13 | 4 | 5 | 9.8* | Internet | Medium | 20 · Critical |
| 3 | 1 · Web app exploitation (Apache 2.4.49) | 13 | 4 | 5 | 9.8 | Internet | Medium | 20 · Critical |
| 4 | 4 · JWT `alg:none` session forgery | 13 | 4 | 4 | 8.1* | Internet | Medium | 16 · High |
| 5 | 8 · SMB lateral movement (null session) | 12 | 4 | 4 | 8.8 | Internal | High (IT→DMZ) | 16 · High |
| 6 | 5 · Credential theft from `.bak`/`.git` | 13 → 12 | 3 | 4 | — | Internet | Medium | 12 · Medium |
| 7 | 3 · IDOR in the API | 13 | 3 | 4 | 7.5* | Internet | Low | 12 · Medium |
| 8 | 6 · Default credentials on the gateway | 10 | 3 | 3 | — | Internal | High (IoT→OT) | 9 · Medium |
| 9 | 7 · Phishing / pretexting | 10 | 3 | 3 | — | Email | Medium | 9 · Medium |
| 10 | 10 · Outdated components and weak TLS | 13 | 2 | 4 | — | Internet | Low | 8 · Medium |

> Priority = P × I on the 1–5 scale of the Challenge 2 risk instrument (2.9); bands: 20–25 Critical,
> 15–19 High, 8–14 Medium, 1–7 Low. `*` marks a CWE-based CVSS estimate, not an NVD CVE score
> (Table 3).

# 4. Traceability matrix vector–control

Table 5 is the spine of the report. Each row starts from a Challenge 2 vector and ends in an
observable artefact; the control columns are split into preventive, detective and corrective so that
no vector depends on a single measure. The frameworks named in each control — CIS Controls v8, OWASP
Top 10, NIST CSF 2.0 and ISO/IEC 27001:2022 — supply the *how*, while the vector and the affected
asset supply the *what for* (Center for Internet Security, 2021; OWASP Foundation, 2021; NIST, 2024;
ISO/IEC, 2022). The matrix preserves the nine required fields of the rubric and adds the
expected-evidence field requested by the guide, with the vector as the row label; each row can be
read by a defender (what to do), by a SOC analyst (what to watch) and by the Cyber Range (what to
prove). The evidence column is written
as an artefact, not as a test result: a log line, a configuration state, a blocked request, a hash or
a ticket. When the control is organizational (vector 7), the evidence is a policy or awareness
artefact; when the vector ends in a physical action (vector 9), the evidence includes the OT log and
the manual-override record. Nothing in this table has been executed; it is the contract for
Challenge 4.

**Table 5 — Traceability matrix vector–control (Annex 1 instrument 3.1; ≥8 vector rows, 10 fields).**

#### Vector 1: Web app exploitation (Apache 2.4.49 RCE)

| Field | Content |
|-------|---------|
| **Probable cause** | Apache 2.4.49 unpatched |
| **Affected asset** | A-01 |
| **Impact** | RCE in DMZ |
| **Kill Chain phase** | Exploitation |
| **MITRE technique** | T1190 |
| **CVE/reference** | CVE-2021-41773 |
| **Preventive control** | Upgrade Apache to ≥2.4.51; WAF virtual patch for CVE-2021-41773/42013; restrict HTTP methods and `/cgi-bin` (CIS 16; OWASP A06) |
| **Detective control** | WAF/`access.log` rule for encoded traversal (`%2e%2e`, `.%2e`) plus vulnerability re-scan alert |
| **Corrective control** | Isolate A-01; restore golden image; rotate secrets; re-scan before return |
| **Expected evidence** | `Server: Apache/2.4.51+`; WAF block event with payload; NSE `http-vuln-cve2021-41773` not vulnerable; golden-image hash |

#### Vector 2: SQLi in `productos.php`

| Field | Content |
|-------|---------|
| **Probable cause** | Unsanitized `categoría` parameter |
| **Affected asset** | A-01 |
| **Impact** | DB extraction |
| **Kill Chain phase** | Exploitation |
| **MITRE technique** | T1190 |
| **CVE/reference** | CWE-89 |
| **Preventive control** | Prepared statements in `productos.php`; allowlist `categoría`; WAF SQLi rules (OWASP A03; CIS 16) |
| **Detective control** | WAF SQLi alert correlated with `error.log` 500/`PDOException`; DB audit for UNION query to information_schema |
| **Corrective control** | WAF block; restore DB snapshot; rotate DB credentials; code rollback |
| **Expected evidence** | WAF block log; no mysqli fetch array trace in `error.log`; clean DB audit; diff with `PDO::prepare` |

#### Vector 3: IDOR in the API

| Field | Content |
|-------|---------|
| **Probable cause** | Missing object-level authorization |
| **Affected asset** | A-01 |
| **Impact** | PII disclosure |
| **Kill Chain phase** | Actions on Objectives |
| **MITRE technique** | — |
| **CVE/reference** | CWE-639 |
| **Preventive control** | Object-level authorization on `/api/v1/usuario`; opaque IDs; deny-by-default API gateway (OWASP A01; CIS 16) |
| **Detective control** | API gateway alert for sequential `id` enumeration and 200 on foreign records |
| **Corrective control** | Revoke sessions; patch authorization; notify DPO; add regression test |
| **Expected evidence** | 403 for foreign `id`; SIEM enumeration alert; CI test case; DPO notification record |

#### Vector 4: JWT `alg:none` session forgery

| Field | Content |
|-------|---------|
| **Probable cause** | Unsigned token accepted |
| **Affected asset** | A-01 |
| **Impact** | Role forgery |
| **Kill Chain phase** | Credential Access |
| **MITRE technique** | T1606.001 |
| **CVE/reference** | CWE-347 |
| **Preventive control** | Verify JWT signature with fixed `alg` allowlist; validate `iss/aud/exp`; rotate keys; HttpOnly, Secure, SameSite cookies (OWASP A07; CIS 16) |
| **Detective control** | SIEM rule for alg:none / unsigned token; role-claim anomaly; auth log for `superadmin` |
| **Corrective control** | Invalidate sessions; rotate signing keys; force re-auth; patch library |
| **Expected evidence** | Forged token returns 401; SIEM alert with decoded header; key-rotation log; `Set-Cookie` flags |

#### Vector 5: Credential theft from `.bak`/`.git`

| Field | Content |
|-------|---------|
| **Probable cause** | `.bak`/`.git` exposed |
| **Affected asset** | A-01→A-03 |
| **Impact** | Credential reuse |
| **Kill Chain phase** | Credential Access |
| **MITRE technique** | T1552.001 |
| **CVE/reference** | — |
| **Preventive control** | Remove `.bak`, `.git`, `/backup`, directory listing; secrets to vault; rotate exposed credentials; block dotfiles (OWASP A05; CIS 16) |
| **Detective control** | `access.log` alert for `.bak`, `.git`, `/backup`; FIM on web root; secret scanning in CI |
| **Corrective control** | Rotate DB/DevOps credentials; revoke sessions; restore config from vault; forensic review |
| **Expected evidence** | 404/403 on sensitive paths; clean secret scan; rotation ticket; access-log alert |

#### Vector 6: Default credentials on the gateway

| Field | Content |
|-------|---------|
| **Probable cause** | Telnet/panel without MFA |
| **Affected asset** | A-05 |
| **Impact** | OT segment access |
| **Kill Chain phase** | Initial Access |
| **MITRE technique** | T1078 |
| **CVE/reference** | — |
| **Preventive control** | Unique credentials plus MFA on gateway; disable Telnet 23; HTTPS only; management VLAN/allowlist (CIS 4/5; NIST CSF PR.AA) |
| **Detective control** | Auth-log alert for `admin/admin` and `root/12345`; Telnet connection alert; new-admin login anomaly |
| **Corrective control** | Lock account; isolate A-05; reimage; rotate all IoT credentials |
| **Expected evidence** | Telnet 23 closed; default login rejected; MFA enforced; SIEM alert |

#### Vector 7: Phishing / pretexting

| Field | Content |
|-------|---------|
| **Probable cause** | Vendor-impersonating email |
| **Affected asset** | A-04 |
| **Impact** | Business credential |
| **Kill Chain phase** | Initial Access |
| **MITRE technique** | T1566 |
| **CVE/reference** | — |
| **Preventive control** | SPF/DKIM/DMARC; impersonation filtering; awareness plus non-destructive phishing simulation; callback verification (CIS 14; NIST CSF PR.AT) |
| **Detective control** | Email-gateway alert for lookalike domain/attachment; user report button; SIEM correlation of login after email |
| **Corrective control** | Quarantine; reset credentials; revoke sessions; block sender/domain; retrain |
| **Expected evidence** | DMARC reject report; simulation click rate; reported-email ticket; blocked sender |

#### Vector 8: SMB lateral movement (null session)

| Field | Content |
|-------|---------|
| **Probable cause** | SMBv1 unsigned + null session |
| **Affected asset** | A-03 |
| **Impact** | Share read |
| **Kill Chain phase** | Lateral Movement |
| **MITRE technique** | T1021.002 |
| **CVE/reference** | CVE-2017-0143 |
| **Preventive control** | Disable SMBv1; enforce signing; block null sessions; restrict 445; patch MS17-010; tiered admin (CIS 4/12; NIST CSF PR.IR) |
| **Detective control** | Windows 4625/4624 plus Sysmon 3; null-session audit; SIEM alert for DMZ→IT SMB |
| **Corrective control** | Isolate A-03; block SMB at firewall; restore backup; rotate domain credentials; remove exposed share file |
| **Expected evidence** | `smbclient -N` fails; `smb-security-mode` shows signing required/SMBv1 off; SIEM alert; firewall deny log |

#### Vector 9: OT command manipulation (MQTT/Modbus)

| Field | Content |
|-------|---------|
| **Probable cause** | Anonymous MQTT; Modbus without auth |
| **Affected asset** | A-07/A-08 |
| **Impact** | Unauthorized irrigation |
| **Kill Chain phase** | Actions on Objectives |
| **MITRE technique** | T0855 |
| **CVE/reference** | CWE-306 |
| **Preventive control** | MQTT auth + TLS + per-topic ACL; disable anonymous; OT VLAN/allowlist; PLC command allowlist (CIS 4/12; NIST CSF PR.IR/PR.AA) |
| **Detective control** | Broker log for anonymous CONNECT/PUBLISH on `invernadero/riego/cmd`; OT IDS for Modbus write; SIEM alert |
| **Corrective control** | Block broker/PLC at firewall; manual irrigation; restore PLC config; rotate MQTT credentials; preserve pcap |
| **Expected evidence** | Anonymous publish rejected; ACL log; OT IDS alert; manual-override record; pcap hash |

#### Vector 10: Outdated components / weak TLS

| Field | Content |
|-------|---------|
| **Probable cause** | jQuery and Bootstrap old; SHA-1 cert |
| **Affected asset** | A-01 |
| **Impact** | Client XSS / interception |
| **Kill Chain phase** | Exploitation |
| **MITRE technique** | T1557 |
| **CVE/reference** | — |
| **Preventive control** | Update jQuery and Bootstrap; TLS 1.2+ with strong ciphers; valid certificate (no SHA-1); HSTS/CSP; remove `phpinfo.php` (OWASP A06/A02; CIS 16) |
| **Detective control** | SCA alert for outdated versions; TLS scan alert for SHA-1/expired cert; SIEM TLS anomaly |
| **Corrective control** | Patch/upgrade; reissue certificate; revoke old cert; redeploy |
| **Expected evidence** | `whatweb` shows updated versions; `testssl.sh` no SHA-1/expired; valid chain; clean SCA report |

# 5. Design of defensive controls

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
| Update Apache to ≥2.4.51; WAF virtual patch for CVE-2021-41773/42013 | Y | 1 | CIS 16 / OWASP A06 | `Server: Apache/2.4.51+`; NSE `http-vuln-cve2021-41773` returns "not vulnerable"; WAF rule active |
| Remove `/dbadmin`, `/backup`, `/.git` from public exposure; block dotfiles | Y | 5 | CIS 16 | 404/403 on `GET /.git/config`, `/backup`, `/dbadmin`; directory listing disabled |
| Add security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options) | Y | 10 | OWASP A06 | Response headers present: `Strict-Transport-Security: max-age=31536000`; `X-Frame-Options: DENY`; `Content-Security-Policy: default-src 'self'` |
| Validate file uploads (MIME type, extension whitelist, virus scanning) | Y | 2 | OWASP A04 | Upload rejects non-image files; `Content-Type` verified server-side; no executable upload succeeds |
| Harden TLS (disable SHA-1, enforce TLS 1.2+, strong ciphers) | Y | 10 | CIS 4 | `testssl.sh` output: no SHA-1, no MD5; TLS 1.2 minimum; ECDHE/RSA with AES-GCM only |
| Move backups out of web root; restrict file access via FIM + ACL | Y | 5 | CIS 16 | Backups in `/opt/backups` (outside web root); 700 permissions; FIM alert on unauthorized modification |

## 5.2 Hardening — b) IT / Windows (≥4 actions) · instrument 3.2b

**Table 7 — Hardening b) IT / Windows (instrument 3.2b).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|------------------|----------------|---------------------|-----------|--------------|
| Disable SMBv1; enforce signing on SMBv2/3; patch MS17-010 (CVE-2017-0143) | Y | 8 | CIS 4 / NIST CSF PR.IR | `smb-security-mode` NSE: "signing required"; `smbclient -N` fails with "Cannot connect"; `Get-WindowsOptionalFeature -FeatureName SMB1Protocol` returns Disabled |
| Block null sessions via Group Policy; restrict registry key `LanmanServer\Parameters RestrictNullSessAccess=1` | Y | 8 | CIS 5 | `enum4linux -N` fails; 139/445 block null connections; Windows 4624 events show credential requirement |
| RDP hardening: enforce Network Level Authentication (NLA); require MFA; account lockout policy (3 failures in 15 min) | Y | 8 | CIS 5 / NIST CSF PR.AA | NLA enabled in `Group Policy → Computer Configuration → Administrative Templates → System → Credentials Delegation`; MFA enforced via Windows Hello or RADIUS; 4625 logs show lockout after 3 failed attempts |
| Segment IT (VLAN 20) ↔ IoT/OT (VLAN 30) with firewall rules; restrict cross-VLAN SMB/SSH | Y | 8 | NIST CSF PR.IR / ISO 27001 A.13 | Firewall ACL blocks 139/445/3389 from VLAN 30 to VLAN 20; VLAN isolation confirmed via `show vlan`; routing table shows separate gateways per VLAN |

## 5.3 Hardening — c) IoT / OT (≥4 actions) · instrument 3.2c

**Table 8 — Hardening c) IoT / OT (instrument 3.2c).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|------------------|----------------|---------------------|-----------|--------------|
| Disable Telnet (23) on gateway; enforce SSH (22) + HTTPS (8080) with key authentication | Y | 6 | CIS 4 / NIST CSF PR.AC | Port 23 closed: `nmap -p 23 10.10.30.5` shows closed; SSH port 22 open with pubkey-only auth; HTTP 8080 redirects to HTTPS; certificate valid |
| Change gateway default credentials (`admin:admin`, `root:12345`) to strong unique passwords; implement MFA on admin panel | Y | 6 | CIS 5 | Login attempts with default creds rejected; admin audit log shows only authorized accounts; MFA prompt on admin login to 10.10.30.5:8080 |
| MQTT broker authentication + per-topic ACL; disable anonymous access | Y | 9 | NIST CSF PR.AA / ISO 27001 A.9 | Broker rejects anonymous CONNECT; `mosquitto_pub` without credentials fails; ACL file restricts `invernadero/riego/cmd` to authenticated PLC user only; MQTT broker config shows `allow_anonymous false` |
| Isolate Modbus/PLC (10.10.30.30:502) on separate OT VLAN (VLAN 30); firewall restricts access to gateway + authorized clients only | Y | 9 | NIST CSF PR.IR / CIS 4 | PLC isolated to VLAN 30; firewall rule allows only TCP 502 from gateway (10.10.30.5) and Modbus client IP; unauthorized hosts cannot reach port 502; network diagram confirms physical/logical isolation |
| Update camera firmware from 5.2.0 to latest stable; remove EOL RTSP server | Y | 6 | CIS 3 / NIST CSF ID.RA | Camera firmware version checked: `curl http://10.10.30.21:81/info` shows current build; EOL components removed; security advisory check shows no active CVEs for deployed version |

## 5.4 Web-application controls

The application-layer defense operates at the boundary between user input and database storage, between privilege levels within the application and between components of the distributed architecture (frontend, API, backend). The OWASP Top 10:2021 and the OWASP Application Security Verification Standard (ASVS) v4.0 supply the framework; Challenge 2 vectors 2, 3, 4 and 10 supply the specific cases. For vector 2 (SQLi), prepared statements with parameterized queries are the primary control: all dynamic SQL in `productos.php`, the order-search and inventory endpoints must use PHP PDO or MySQLi prepared statements with placeholders, never string concatenation. For vectors 3 and 4 (IDOR and JWT), object-level authorization must be enforced: every `/api/v1/usuario`, `/api/v1/pedidos` and `/api/v1/inventario` endpoint must verify that the authenticated user owns the object before returning it, and the authorization library must use an allowlist (deny-by-default) rather than a blacklist. JWT tokens must carry a fixed `alg` field (RS256 or HS256, never `none`), include standard claims (`iss`, `aud`, `exp`), and be validated before each use. For vector 10 (outdated components), a Software Composition Analysis (SCA) scan must be integrated into the CI/CD pipeline to alert on jQuery and Bootstrap versions with known CVEs. File uploads (vector 2 in the CWE-434 dimension) must be validated on both client and server: accept only expected MIME types (image/jpeg, image/png), reject executable extensions, scan for malware signatures and store uploads outside the web root. Database credentials, API keys and encryption secrets must not be stored in the codebase: `config.php` must read from environment variables set at deployment time, and a secrets management tool (e.g., Vault, HashiCorp Consul) must be used for shared credentials. These controls are integrated into the DevSecOps pipeline described in Section 7.

# 6. Monitoring and detection proposal

The monitoring layer is designed as a detection pipeline, not as a log-collection exercise: sources
(Apache, Windows/Sysmon, MQTT broker, firewall and camera) feed correlation rules that turn isolated
events into incident candidates, following the sequence used by the course OVI — logs and events,
network traffic, IoT telemetry, SIEM correlation and alerts (Zambrano Hernández, 2026). Each rule in
Table 9 is bound to a Kill Chain phase and a MITRE technique from Challenge 2, so a detection gap can
be read as a missing ATT&CK coverage (Strom et al., 2018). Severity and thresholds are set so that the
first alert triggers a containment action rather than a report; Table 10 assigns the source, the
frequency, the threshold and the owner. The detection strategy prioritizes the cross-domain vectors: brute-force and SQLi attacks on the DMZ portal (Table 4, vectors 1–2) must be caught before exfiltration can succeed; lateral movement within IT (vector 8) must trigger immediate isolation; and OT command manipulation (vector 9) must alert the operator and the security team in parallel, because manual override of the irrigation controller is faster than automated remediation. Thresholds are set conservatively: a single anonymous MQTT PUBLISH to `/cmd/*` is Critical severity, not because one command succeeds but because the precondition (unauthenticated broker) indicates that the entire OT segment may be under attack.

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
| WAF / web logs | Injection, brute force | Real time | ≥3 SQLi blocks in 60s; ≥5 POST `/admin/login` from same IP in 120s | SOC |
| EDR/SIEM (IT) | Anomalous logon, new services | Real time | ≥3 failed logons (4625) same user different IPs in 300s; new service 7045 from `C:\Temp\` | SOC |
| MQTT broker logs | Anonymous connect / command publish | Real time | Single anonymous CONNECT or PUBLISH to `*/cmd/*` topic (Critical); ≥2 failed auth in 60s | OT team |
| Firewall | Cross-zone flows, C2 egress | Real time | Any connection DMZ↔IT port 445/3389/22; any outbound 1883 from IT subnet; any VLAN 20↔VLAN 30 except approved gateways | Network team |

# 7. DevSecOps proposal

DevSecOps integrates security validation into the application lifecycle — code, build, test, deployment, runtime — so that each vector from Challenge 2 is caught as early as possible and does not recur. The five practices in Table 11 map to the NIST CSF Govern function (policy and risk management) and the Identify function (asset and vulnerability baseline). Static Application Security Testing (SAST) runs before merge, catching injection vulnerabilities (CWE-89) and insecure API patterns (CWE-639) in the source code; Dynamic Application Security Testing (DAST) runs on a staging environment after deployment, validating that input validation and parameterized queries are actually enforced in the running application (vectors 1, 10). Software Composition Analysis (SCA) scans dependencies at build time, alerting to jQuery, Bootstrap and transitive library versions with known CVEs (vector 10). Pre-commit secret scanning detects credentials (`config.php.bak`, private keys, API tokens) before they reach the repository (vector 5), preventing exposure via `.git`. Change control ensures that every release is reviewed, tested and signed off before production deployment — a governance checkpoint that interrupts the propagation of any unvalidated control. The DevSecOps pipeline feeds results into Table 9 (SIEM/XDR rules) so that runtime behavior can be correlated with expected alerts: if SAST says the code has no SQLi, but SIEM logs a SQL syntax error, that evidence of an attempted attack becomes an incident signal.

**Table 11 — DevSecOps practices (≥4, with lifecycle stage).**

| Practice | Description | Lifecycle stage | Vector/reference it prevents |
|----------|-------------|-----------------|------------------------------|
| SAST | Static analysis of source before merge | Code / build | 2, 3 (CWE-89/639) |
| DAST | Dynamic analysis on a staging deploy | Test | 1, 10 |
| SCA | Dependency and component scanning | Build | 10 (jQuery/Bootstrap) |
| Secret scanning | Detect credentials before commit | Pre-commit / CI | 5 (`config.php.bak`, `.git`) |
| Change control | Reviewed, gated releases | Release | all vectors |

# 8. Incident response plan

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
| **Preparation** | Pre-incident: MQTT broker auth enabled; per-topic ACL in place; MQTT broker logs > syslog > SIEM; OT IDS rule for Modbus unauthorized write deployed; playbook team trained on roles and escalation (OT eng, security, management); backup of PLC config and MQTT broker config held offline | Security + OT team | MQTT broker config file; OT IDS signature; team-training sign-off; offline backup hash (SHA-256) |
| **Detection and analysis** | SIEM alert: anonymous CONNECT attempt + PUBLISH to `invernadero/riego/cmd`; OR OT IDS signature triggers on unauthorized Modbus write command to holding register 100-103 (irrigation valve control); security analyst correlates broker log timestamp with SIEM and PLC log; manual valve position check confirms unexpected state (open when should be closed) | SOC analyst + OT operator | SIEM alert ID + timestamp; broker log entry; PLC audit log; manual inspection record; initial severity assessment (Critical) |
| **Containment** | **Short-term:** Isolate MQTT broker at L2/L3 (block port 1883); stop all telemetry ingestion; manual override: verify manual valve operator can close the irrigation line; issue OT alert via radio/SMS to greenhouse staff. **Medium-term:** Revoke any newly created MQTT credentials; check broker logs for lateral-movement attempts (other topics); monitor IT egress to 1883 | OT lead + Security ops | Network ACL modification log; manual-override record with timestamp; OT alert dispatch log; MQTT user audit |
| **Eradication** | Restore MQTT broker from clean backup (pre-incident config); verify no unauthorized users in ACL; rotate MQTT credentials for all clients (sensors, PLC, application); patch/update broker if vulnerability suspected; review and enforce firewall rule blocking 1883 from IT/DMZ to OT; run full vulnerability scan on gateway and broker | OT team + Security | Broker restore log; version check; credential rotation audit; firewall rule diff; vulnerability scan report (Nessus/OpenVAS) |
| **Recovery** | Restart MQTT broker; validate connectivity to all authorized clients (PLC, sensors, application) via health checks; manually verify irrigation is responding to commands; restore telemetry stream; test failover to backup broker; monitor for anomalies for 72 hours | OT team + application team | Broker startup log; health-check results; PLC response test log; telemetry flow confirmation; 72-hour anomaly-free monitoring log |
| **Lessons learned** | Post-incident review (within 1 week): root-cause analysis (how was broker access enabled?); timeline reconstruction; control-gap review (why was the alert delayed?); update incident response plan; training brief for all staff on MQTT security. Document in wiki/runbook; assign owner for each preventive action from Section 5.3 | Manager + team | Incident report (IR-YYYY-MMDD-001); updated runbook; training attendance sheet; action-item tracker (JIRA/Linear) with owners and due dates |

# 9. Validation criteria for Challenge 4

Validation is written as a set of falsifiable hypotheses, not as a test log: each row of Table 13
names the control, the evidence that would prove it works and the method to obtain that evidence in
the Cyber Range. The Cyber Range activity included in the course OVA (OVA 3) insists on rules of
engagement, authorized scope, controlled validation and evidence retention before any technical
action (Mantilla Torres, 2025c), while the OVI frames evidence as the link between a finding and a
defensible decision (Zambrano Hernández, 2026). The six validation criteria in Table 13 span the three
domains (DMZ, IT, IoT/OT) and cover both preventive and detective controls, ensuring that the next
phase has a measurable yardstick for each major control. No criterion is executed here; the table is the
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

# 10. Conclusions and references

This report converts the Challenge 2 offensive findings into a defensive design that is traceable end to end: each control starts from a vector, a probable cause and an affected asset, and ends in an expected evidence line. The contribution is the chain vector → probable cause → control → evidence, organized by the CSF 2.0 functions and operationalized through the course OVI's detection and response sequence. The traceability matrix (Table 5) ensures that no vector is left undefended and no control is imposed without a corresponding threat; the hardening checklists (Tables 6–8) prioritize the actions with the highest impact on the AgroSmart case; the SIEM rules (Table 9) and the DevSecOps pipeline (Table 11) close the loop by detecting and preventing recurrence. The incident-response playbook (Table 12) operationalizes the six NIST SP 800-61 phases into concrete actions for the priority vector (OT command manipulation), and the validation criteria (Table 13) provide the falsifiable hypotheses that will be tested in the Cyber Range.

The main limitation is that no control has been validated: thresholds, correlation rules, playbook times and architectural assumptions are design hypotheses to be tested in Challenge 4. A second limitation is the reliance on course materials and framework guidance rather than measured results from this organization; the OVA/OVI and the NIST, CIS and OWASP references orient the design but do not substitute for validation on the actual AgroSmart infrastructure. A third limitation is that the IoT/OT hardening and monitoring proposal (Section 5.3, Tables 8–9) assumes that firmware updates and protocol changes are possible; if the PLC or MQTT broker cannot be patched due to operational constraints, the detection and containment strategies become the primary defense, and the risk profile shifts. The next step is to execute Table 13 under the Challenge 4 rules of engagement, validate each control's effectiveness and measurable impact, and feed the empirical results back into Tables 5, 9 and 12 to refine the design.

# Appendix — AI-usage declaration / log

| Field | Response |
|-------|----------|
| AI tool used |  |
| What it was used for |  |
| Main prompt(s) |  |
| Output obtained |  |
| How it was verified |  |
| Critical adjustments made |  |
| Approx. % of the deliverable supported by AI |  |

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
- Zambrano Hernández, L. F. (2026). *Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT* [OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/83223

**Technical frameworks**

- Center for Internet Security. (2021). *CIS Controls Version 8: Implementation guidance for enterprises* (CIS Critical Security Controls). https://www.cisecurity.org/controls/v8
- Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2012). *Computer security incident handling guide* (NIST SP 800-61 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2
- International Organization for Standardization. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC 27001:2022). https://www.iso.org/standard/27001
- NIST. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSF 2.0; NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- NIST. (n.d.). *National Vulnerability Database* (NVD) [Database]. Retrieved October 22, 2026, from https://nvd.nist.gov/
- OWASP Foundation. (2021). *OWASP Top 10: 2021 — The ten most critical web application security risks*. https://owasp.org/Top10/
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018). *MITRE ATT&CK: Design and philosophy*. The MITRE Corporation. https://doi.org/10.13140/RG.2.2.13778.58565
