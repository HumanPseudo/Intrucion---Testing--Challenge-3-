---
title: "Challenge 3 — Design of detection, defense and cyber-attack management strategies for IT and IoT environments"
author: "Camilo David Lasso Guzmán"
subtitle: "Intrusión y Testing (203028113) · Challenge 3 · ECBTI–UNAD"
date: "2026-10-25"
lang: en
---

# 1. Introduction and scope of defensive design

This report presents the defensive design strategy analysis required by Challenge 3 of *Intrusión y Testing*
(203028113) and is the direct continuation of the offensive analysis delivered in Challenge 2.
Its aim is to show that a relevant learning outcome has been met by designing a detection strategy,
identification, hardening, monitoring, containment and response, built from the offensive
techniques and the adversarial thinking. The design covers the three
domains of AgroSmart del Sumapaz S.A.S. — the **DMZ/Web LAMP** environment, the **corporate IT**
network and the **IoT/OT** layer of the smart greenhouse — and every control, hardening action and
detection rule is traceable to a vector, asset or probable cause identified.

**Case.** AgroSmart del Sumapaz S.A.S. — a single case shared by Challenges 2–5 (systems and data
come from Annex 1 and the Challenge 2 instruments; Zambrano Hernández, 2026b).

**Relation with the Challenge 2 findings.** The offensive analysis is incorporated here rather than
repeated: Section 2 synthesizes it from the case data (Tables 1–3), and therefore the earlier
deliverable need not be consulted as a separate source. That synthesis consolidated eight critical assets
(A-01…A-08) with their exposure surfaces, ten attack vectors, a ten-row CVE/CWE matrix (5 CVE, 5 CWE)
with its severity mappings, the seven phases of the Cyber Kill Chain and the fifteen MITRE ATT&CK
techniques bound to those phases (13 from Challenge 2's instrument plus T1078 and T1557, all justified in Section 2.4). Those findings are the input of this report: the vectors become the rows of
the traceability matrix, the assets become the unit of criticality, and the techniques become the
anchor of each detection rule. The attack paths were built with the penetration-testing
methodologies reviewed in the course (Palomo Luna et al., 2024;
Lu & Yu, 2021) and with web-application vulnerability analysis (Crespo-Martínez, 2021); the human
factor present in vector 7 was characterized following the social-engineering and phishing
literature of the course (Albininé Budavári et al., 2023; Benavides et al., 2020; Benavides-Astudillo
et al., 2020; Prado Díaz, 2021).

**Defensive frame of reference.** The design is organized around the six functions of the NIST
Cybersecurity Framework (CSF) 2.0 — Govern, Identify, Protect, Detect, Respond and Recover — because
that taxonomy allows each Challenge 2 vector to be traced from exposure to response without
establishing a parallel control catalogue (NIST, 2024; Mantilla Torres, 2025a, 2025b, 2025c). The course OVI on
detection and management of attacks in IT/IoT environments supplies the operational reading of that
frame: it links attack vectors and adversarial thinking with the Cyber Kill Chain and MITRE ATT&CK,
and it orders detection and incident response around evidence rather than around tools (Zambrano
Hernández, 2026a). The report therefore uses CSF 2.0 for the architecture of the defense, the OVI for
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

Challenge 2 completed a systematic offensive analysis of AgroSmart del Sumapaz S.A.S. using penetration-testing methodologies, enumerating eight critical assets across three domains (DMZ/Web LAMP, corporate IT, IoT/OT), identifying eleven exposure surfaces at the network perimeter and inside the infrastructure, and tracing ten attack vectors from initial reconnaissance through execution and actions on objectives. The analysis yielded a ten-row CVE/CWE matrix anchored to the National Vulnerability Database and the MITRE ATT&CK framework, mapping fifteen threat techniques across seven Kill Chain phases — from reconnaissance (passive and active information gathering) through initial access (exploitation and phishing), execution, persistence, credential access, lateral movement, and finally to impairment of process control in the OT domain. Table 1 classifies the eight assets by their domain, function and criticality (using the Confidentiality–Integrity–Availability triad); Table 2 lists the ten attack vectors with their preconditions and evidence; Table 3 summarizes the CVE/CVSS scores and alternative CWE vulnerability categories where a CVE is not assigned. The synthesis feeds directly into the traceability matrix of Section 4, which inherits the vector names, affected assets, Kill Chain phases and MITRE techniques as row labels and control anchors.

## 2.1 Asset classification by domain

**Table 1 — Asset classification by domain (rubric C2.a).**

| ID | Asset | Domain | Function | Criticality (C-I-D) | Exposure |
|---------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------|
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
|----------------|---------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
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

```{=latex}
\needspace{7\baselineskip}
```

**Table 3 — Vulnerability matrix: CVE / CWE · CVSS.**

```{=latex}
\begingroup
\renewcommand{\tablesize}{\footnotesize}
\breakslashes
```

| Asset | Finding | CVE/reference | CVSS v3.1 vector | Score/Severity |
|----------|--------------------------------------|-----------------|------------------|-----------------|
| A-01 Web | Apache 2.4.49 path traversal/RCE | CVE-2021-41773 | `AV:N/​AC:L/​PR:N/​UI:N/​S:U/​C:H/​I:H/​A:H` | 9.8 Critical |
| A-01 Web | Incomplete 2.4.50 patch (bypass) | CVE-2021-42013 | idem | 9.8 Critical |
| A-03 IT | SMBv1 unsigned | CVE-2017-0143 (MS17-010) | `AV:N/​AC:L/​PR:L/​UI:N/​S:U/​C:H/​I:H/​A:H` | 8.8 High |
| A-06 IoT | Old Boa camera (fw 5.2.0), path traversal via `FILECAMERA` | CVE-2017-9833 (disputed) | `AV:N/​AC:L/​PR:N/​UI:N/​S:U/​C:H/​I:N/​A:N` | 7.5 High |
| A-06 IoT | Old Boa camera (fw 5.2.0), `HEAD`-method auth bypass | CVE-2022-45956 (not in CISA KEV) | `AV:N/​AC:L/​PR:N/​UI:N/​S:U/​C:N/​I:L/​A:N` | 5.3 Medium |
| A-01 Web | SQL error in `productos.php` | CWE-89 (OWASP A03:2021) | Remote, unprivileged | 9.8 Critical* |
| A-01 Web | API returns other users' data | CWE-639 | Change `id` returns another record | 7.5 High* |
| A-01 Web | JWT signed with `alg:none` | CWE-347 | Portal accepts unsigned token | 8.1 High* |
| A-01 Web | File upload without validation | CWE-434 | Accepts any file | 8.8 High* |
| A-08 IoT/OT | Anonymous MQTT broker | CWE-306 | Connects/publishes without credential | 9.1 Critical* |

> All five CVE identifiers and their CVSS v3.1 vectors were independently verified against the NVD
> API, and the values above match the current NVD records. For CVE-2017-0143, NVD's primary (NIST)
> metric is `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` (8.8 High) — the same vector and score recorded in
> the Challenge 2 instrument, so no divergence arises. CVE-2021-41773, CVE-2021-42013 and
> CVE-2017-0143 are confirmed in the CISA KEV catalog (added 2021-11-03); CVE-2017-9833 and CVE-2022-45956 are confirmed
> absent from it. CVE-2022-45956 was recorded in Challenge 2 as the camera's alternative Boa CVE and is
> promoted to a matrix row here. CVE-2017-9833's NVD record carries a dispute note attributing the flaw to system integrators rather than
> to Boa itself, consistent with the "(disputed)" label used here.

```{=latex}
\endgroup
```

## 2.4 Cyber Kill Chain and MITRE ATT&CK

The course OVI reads Cyber Kill Chain and MITRE ATT&CK as complementary rather than
interchangeable: the first narrates the sequence of an intrusion from reconnaissance to actions on
objectives, while the second names the tactics and techniques observable at each stage (Zambrano
Hernández, 2026a; Strom et al., 2018). Challenge 2's ATT&CK instrument (2.7) verified 13 techniques
against the official MITRE data, distributed across seven tactics: reconnaissance (T1595, T1589);
initial access (T1566, T1190); execution (T1059); persistence (T1543.003); credential access
(T1110.001, T1552.001, T1539, T1606.001); lateral movement (T1021.002, T1210); and impair process
control (T0855). Two techniques used in Table 5 extend this inventory beyond what Challenge 2's
instrument mapped: **T1078 Valid Accounts** (initial access), for vector 6's use of default gateway
credentials, and **T1557 Adversary-in-the-Middle** (credential access / collection), for the
interception risk in vector 10's weak-TLS finding. Both are verified current MITRE ATT&CK Enterprise
techniques and are technically justified by the Challenge 2 vector descriptions even though the
original instrument did not enumerate them; the retained count is therefore **15 techniques**, not
13. Of these fifteen, the eight bound to a numbered vector appear in Table 5; the remaining seven are Challenge 2 Kill Chain context. One technique has also been renumbered since Challenge 2 was authored: **T0855 "Unauthorized
Command Message"** was revoked in ATT&CK for ICS v19.0 and consolidated into **T1692.001 "Command
Message"** (tactics: Evasion, Impair Process Control). Table 5 and this section cite the current ID,
T1692.001, while preserving the T0855 label historically used in Challenge 2's instrument for
traceability; it is the only technique with no preventive or detective control in the Challenge 2
matrix, and it is the reason the IoT/OT domain is prioritized in Section 3: an authorized command
published to the MQTT broker can open the irrigation valve without touching the corporate network.
Vector 3 (IDOR) has no assigned technique: Broken Object-Level Authorization is not catalogued as a
discrete Enterprise ATT&CK technique — the nearest adjacent technique, T1213 (Data from Information
Repositories), describes collecting data the adversary already has legitimate access to, not
exploiting a missing per-object check — and Challenge 2's own instrument likewise left it unmapped.
The applicable framework for vector 3 is OWASP's API Security Top 10 (API1:2023, Broken Object Level
Authorization), not MITRE ATT&CK.

# 3. Risk prioritization matrix

Table 4 scores every Challenge 2 vector on the six criteria required by the rubric and orders the
rows by the resulting priority. The primary score is the product of probability and impact (P×I) on
the 1–5 scale of the Challenge 2 risk instrument; the remaining four criteria are not merely illustrative: they
resolve ties and explain why vectors with the same P×I do not receive the same urgency. Asset
criticality is the C–I–D sum from Table 1, CVSS is the NVD score where a CVE exists and the
asterisked CWE estimate from Table 3 where it does not, exposure is the trust boundary from Section
2.2, and cross-domain propagation records whether the vector can move from DMZ to IT or from IT to
IoT/OT. The bands follow the same instrument: 20–25 Critical, 15–19 High, 8–14 Medium and 1–7 Low.
Vector 9 is first because it scores 20 and its propagation is physical/OT; vectors 2 and 1 also score
20, but their impact is business/data, and vector 2 precedes vector 1 because SQLi exposes orders and
PII with a single parameter, whereas vector 1 requires a public exploit. Vectors 3 and 4 are
alternative paths inside that same portal-compromise scenario (20 in instrument 2.9), but they keep
their own conservative scores: IDOR discloses PII without full database extraction, and JWT forgery
requires a token, so the full weight of the scenario falls to vector 2, the direct SQLi path. Vectors
4 and 8 (16 each)
follow, with vector 4 first because it is Internet-facing; the 12-point vectors 5 and 3 are separated
by propagation (5 crosses A-01→A-03), and the 9-point vectors 6 and 7 by the same rule (6 reaches
OT). The highest CVSS does not by itself determine the order: CVSS measures technical severity, not
the probability or the physical consequence for this organization.

```{=latex}
\needspace{8\baselineskip}
```

**Table 4 — Risk prioritization matrix (6 criteria; one row per vector, ordered descending).**

```{=latex}
\begingroup
\renewcommand{\tablesize}{\scriptsize}
\breakslashes
```

| Rank | Vector (Challenge 2) | Asset criticality | Impact | Probability | CVSS severity | Exposure | Cross-domain propagation | Priority |
|------------------------|--------------------------------------------------------------------------------|----------------------------------------------|----------------------------------|--------------------------------------------------------|----------------------------------------|------------------------------------------------|----------------------------------------------------------------------------|--------------------------------------------|
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

```{=latex}
\endgroup
```

The blank CVSS-severity cells for vectors 5, 6, 7 and 10 are not omissions: vectors 5 (exposed
backup/`.git` file), 6 (default/weak credentials) and 7 (phishing) are configuration and procedural
weaknesses, not software vulnerabilities, so Challenge 2's vulnerability matrix (Table 3) never
assigned them a CVE or CWE-based score — CVSS does not apply to this class of finding. Vector 10
(outdated jQuery/Bootstrap, weak TLS) also has no entry in Table 3; Challenge 2 documented the
finding qualitatively but did not assign it a CWE-based score, and none has been fabricated here. Instrument 2.9 scored six risk scenarios directly; the P×I values for vectors 3, 6, 7 and 10 are conservative design estimates on the same 1–5 scale, as those vectors were not among them. The 1–5
probability and impact scales are defined in Challenge 2's risk instrument (Annex 1, p. 29;
instrument 2.9), reproduced here for traceability:

**Probability and Impact (P/I) rating scales (Challenge 2 instrument 2.9, Annex 1 p. 29).**

| Level | Probability (P) | Impact (I) |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Requires an exceptional precondition | Reversible, no external effect |
| 2 | Requires unlikely conditions | Affects one user, no business effect |
| 3 | Plausible given the observed artefacts | Affects a secondary process or a dataset |
| 4 | High: matches an Annex clue directly | Affects the main process or sensitive data (PII, credentials) |
| 5 | Very high: needs no additional condition | Direct business loss or external physical damage |

# 4. Traceability matrix: vector to control

Table 5 is the structural axis of the report. Each row starts from a Challenge 2 vector and ends in an
observable artefact; the control columns are split into preventive, detective and corrective so that
no vector depends on a single measure. The frameworks named in each control — CIS Controls v8, OWASP
Top 10, NIST CSF 2.0 and ISO/IEC 27001:2022 — supply the method, whereas the vector and the affected
asset supply the purpose (Center for Internet Security, 2021; OWASP Foundation, 2021; NIST, 2024;
ISO/IEC, 2022). The matrix preserves the nine required fields of the rubric and adds the
expected-evidence field requested by the guide, with the vector as the row label; each row can be
read by a defender (what to do), by a SOC analyst (what to watch) and by the Cyber Range (what to
prove). The evidence column is written
as an artefact, not as a test result: a log line, a configuration state, a blocked request, a hash or
a ticket. When the control is organizational (vector 7), the evidence is a policy or awareness
artefact; when the vector ends in a physical action (vector 9), the evidence includes the OT log and
the manual-override record. Nothing in this table has been executed; it is the contract for
Challenge 4.

```{=latex}
\clearpage
\newgeometry{left=1cm,right=1cm,top=2.54cm,bottom=2.54cm}
\begingroup
\renewcommand{\tablesize}{\tiny}
\setlength{\tabcolsep}{2pt}
\breaktokens
```

**Table 5 — Traceability matrix vector–control (Annex 1 instrument 3.1; 10 vector rows, 11 fields).**

| Vector | Probable cause | Affected asset | Impact | Kill Chain phase | MITRE ATT&CK tactic/technique | CVE/reference | Preventive control | Detective control | Corrective control | Expected evidence |
|--------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------|
| 1 · Web app exploitation (Apache 2.4.49 RCE) | Apache 2.4.49 unpatched | A-01 | RCE in DMZ | Exploitation | Initial Access — T1190 Exploit Public-Facing Application | CVE-2021-41773 | Upgrade Apache to ≥2.4.51; WAF virtual patch for CVE-2021-41773/42013; restrict HTTP methods and `/cgi-bin` (CIS 16; OWASP A06) | WAF/`access.log` rule for encoded traversal (`%2e%2e`, `.%2e`) plus vulnerability re-scan alert | Isolate A-01; restore golden image; rotate secrets; re-scan before return | `Server: Apache/2.4.51+`; WAF block event with payload; NSE `http-vuln-cve2021-41773` not vulnerable; golden-image hash |
| 2 · SQLi in `productos.php` | Unsanitized `categoría` parameter | A-01 | DB extraction | Exploitation | Initial Access — T1190 Exploit Public-Facing Application | CWE-89 | Prepared statements in `productos.php`; allowlist `categoría`; WAF SQLi rules (OWASP A03; CIS 16) | WAF SQLi alert correlated with `error.log` 500/`PDOException`; DB audit for UNION query to information_schema | WAF block; restore DB snapshot; rotate DB credentials; code rollback | WAF block log; no mysqli fetch array trace in `error.log`; clean DB audit; diff with `PDO::prepare` |
| 3 · IDOR in the API | Missing object-level authorization | A-01 | PII disclosure | Actions on Objectives | N/A (no Txxxx) — Broken Object-Level Authorization has no discrete Enterprise ATT&CK technique; framework: OWASP API1:2023 (BOLA) | CWE-639 | Object-level authorization on `/api/v1/usuario`; opaque IDs; deny-by-default API gateway (OWASP A01; CIS 16) | API gateway alert for sequential `id` enumeration and 200 on foreign records | Revoke sessions; patch authorization; notify DPO; add regression test | 403 for foreign `id`; SIEM enumeration alert; CI test case; DPO notification record |
| 4 · JWT `alg:none` session forgery | Unsigned token accepted | A-01 | Role forgery | Exploitation | Credential Access — T1606.001 Forge Web Credentials: Web Cookies | CWE-347 | Verify JWT signature with fixed `alg` allowlist; validate `iss/aud/exp`; rotate keys; HttpOnly, Secure, SameSite cookies (OWASP A07; CIS 16) | SIEM rule for alg:none / unsigned token; role-claim anomaly; auth log for `superadmin` | Invalidate sessions; rotate signing keys; force re-auth; patch library | Forged token returns 401; SIEM alert with decoded header; key-rotation log; `Set-Cookie` flags |
| 5 · Credential theft from `.bak`/`.git` | `.bak`/`.git` exposed | A-01→A-03 | Credential reuse | Reconnaissance (Challenge 2's technical-variant route, instrument 2.8, step 5) | Credential Access — T1552.001 Unsecured Credentials: Credentials In Files | — | Remove `.bak`, `.git`, `/backup`, directory listing; secrets to vault; rotate exposed credentials; block dotfiles (OWASP A05; CIS 16) | `access.log` alert for `.bak`, `.git`, `/backup`; FIM on web root; secret scanning in CI | Rotate DB/DevOps credentials; revoke sessions; restore config from vault; forensic review | 404/403 on sensitive paths; clean secret scan; rotation ticket; access-log alert |
| 6 · Default credentials on the gateway | Telnet/panel without MFA | A-05 | OT segment access | Exploitation | Initial Access — T1078 Valid Accounts (not in Challenge 2's original 13-technique inventory; added here, Section 2.4) | — | Unique credentials plus MFA on gateway; disable Telnet 23; HTTPS only; management VLAN/allowlist (CIS 4/5; NIST CSF 2.0 PR.AA) | Auth-log alert for `admin/admin` and `root/12345`; Telnet connection alert; new-admin login anomaly | Lock account; isolate A-05; reimage; rotate all IoT credentials | Telnet 23 closed; default login rejected; MFA enforced; SIEM alert |
| 7 · Phishing / pretexting | Vendor-impersonating email | A-04 | Business credential | Delivery (Challenge 2's kill-chain, instrument 2.6, step 3) | Initial Access — T1566 Phishing | — | SPF/DKIM/DMARC; impersonation filtering; awareness; callback verification (CIS 14; NIST CSF 2.0 PR.AT); non-destructive phishing simulation as a future activity conditional on explicit authorization — not executed in Challenge 3 | Email-gateway alert for lookalike domain/attachment; user report button; SIEM correlation of login after email | Quarantine; reset credentials; revoke sessions; block sender/domain; retrain | DMARC reject report; reported-email ticket; blocked sender; simulation click rate only if a future authorized campaign is run — no campaign has been executed |
| 8 · SMB lateral movement (null session) | SMBv1 unsigned + null session | A-03 | Share read | Actions on Objectives (Challenge 2's technical-variant route, instrument 2.8, step 6) | Lateral Movement — T1021.002 SMB/Windows Admin Shares | CVE-2017-0143 | Disable SMBv1; enforce signing; block null sessions; restrict 445; patch MS17-010; tiered admin (CIS 4/12; NIST CSF 2.0 PR.IR) | Windows 4625/4624 plus Sysmon 3; null-session audit; SIEM alert for DMZ→IT SMB | Isolate A-03; block SMB at firewall; restore backup; rotate domain credentials; remove exposed share file | `smbclient -N` fails; `smb-security-mode` shows signing required/SMBv1 off; SIEM alert; firewall deny log |
| 9 · OT command manipulation (MQTT/Modbus) | Anonymous MQTT; Modbus without auth | A-07/A-08 | Unauthorized irrigation | Actions on Objectives | Impair Process Control / Evasion — T1692.001 Command Message (catalogued as T0855 "Unauthorized Command Message" in Challenge 2's instrument 2.7; revoked and renumbered in ATT&CK for ICS v19.0) | CWE-306 | MQTT auth + TLS + per-topic ACL; disable anonymous; OT VLAN/allowlist; PLC command allowlist (CIS 4/12; NIST CSF 2.0 PR.IR/PR.AA) | Broker log for anonymous CONNECT/PUBLISH on `invernadero/riego/cmd`; OT IDS for Modbus write; SIEM alert | Block broker/PLC at firewall; manual irrigation; restore PLC config; rotate MQTT credentials; preserve pcap | Anonymous publish rejected; ACL log; OT IDS alert; manual-override record; pcap hash |
| 10 · Outdated components / weak TLS | jQuery and Bootstrap old; SHA-1 cert | A-01 | Client XSS / interception | Exploitation | Credential Access / Collection — T1557 Adversary-in-the-Middle (not in Challenge 2's original 13-technique inventory; added here, Section 2.4) | — (no CVE/CWE score assigned to this finding in Table 3) | Update jQuery and Bootstrap; TLS 1.2+ with strong ciphers; valid certificate (no SHA-1); HSTS/CSP; remove `phpinfo.php` (OWASP A06/A02; CIS 16) | SCA alert for outdated versions; TLS scan alert for SHA-1/expired cert; SIEM TLS anomaly | Patch/upgrade; reissue certificate; revoke old cert; redeploy | `whatweb` shows updated versions; `testssl.sh` no SHA-1/expired; valid chain; clean SCA report |

```{=latex}
\endgroup
\restoregeometry
\clearpage
```

**Note on vector 7's phase.** The phishing email maps to Delivery (Challenge 2's reconstruction,
instrument 2.6, step 3: the message sent to Accounting), which agrees with the classic Cyber Kill
Chain; the credential it captures is reused at later phases (SMB lateral movement, vector 8).

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

## 5.1 Hardening — a) Web / LAMP · instrument 3.2a

**Table 6 — Hardening a) Web / LAMP (instrument 3.2a).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Update Apache to ≥2.4.51; WAF virtual patch for CVE-2021-41773/42013 | Y | 1 | CIS 16 / OWASP A06 / Anexo 1 — instrument 3.2a | `Server: Apache/2.4.51+`; NSE `http-vuln-cve2021-41773` returns "not vulnerable"; WAF rule active |
| Remove `/dbadmin`, `/backup`, `/.git` from public exposure; block dotfiles | Y | 5 | CIS 16 / Anexo 1 — instrument 3.2a | 404/403 on `GET /.git/config`, `/backup`, `/dbadmin`; directory listing disabled |
| Add security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options) | Y | — (indirect to 10: mitigates client-side XSS, not weak TLS/SHA-1) | OWASP A06 / Anexo 1 — instrument 3.2a | Response headers present: `Strict-Transport-Security: max-age=31536000`; `X-Frame-Options: DENY`; `Content-Security-Policy: default-src 'self'` |
| Validate file uploads (MIME type, extension whitelist, virus scanning) | Y | — (CWE-434, Table 3; general application-security control, not mapped to a numbered Challenge 2 vector) | OWASP A04 / Anexo 1 — instrument 3.2a | Upload rejects non-image files; `Content-Type` verified server-side; no executable upload succeeds |
| Harden TLS (disable SHA-1, enforce TLS 1.2+, strong ciphers) | Y | 10 | CIS 4 / Anexo 1 — instrument 3.2a | `testssl.sh` output: no SHA-1, no MD5; TLS 1.2 minimum; ECDHE/RSA with AES-GCM only |
| Move backups out of web root; restrict file access via FIM + ACL | Y | 5 | CIS 16 / Anexo 1 — instrument 3.2a | Backups in `/opt/backups` (outside web root); 700 permissions; FIM alert on unauthorized modification |

## 5.2 Hardening — b) IT / Windows · instrument 3.2b

**Table 7 — Hardening b) IT / Windows (instrument 3.2b).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Disable SMBv1; enforce signing on SMBv2/3; patch MS17-010 (CVE-2017-0143) | Y | 8 | CIS 4 / NIST CSF PR.IR / Anexo 1 — instrument 3.2b | `smb-security-mode` NSE: "signing required"; `smbclient -N` fails with "Cannot connect"; `Get-WindowsOptionalFeature -FeatureName SMB1Protocol` returns Disabled |
| Block null sessions via Group Policy; restrict registry key `LanmanServer\Parameters RestrictNullSessAccess=1` | Y | 8 | CIS 5 / Anexo 1 — instrument 3.2b | `enum4linux -N` fails; 139/445 block null connections; Windows 4624 events show credential requirement |
| RDP hardening: enforce Network Level Authentication (NLA); require MFA; account lockout policy (3 failures in 15 min) | Y | — (general IT hardening; indirect to 8 — both harden remote-access surfaces on A-03, RDP is not the observed SMB null-session mechanism) | CIS 5 / NIST CSF 2.0 PR.AA / Anexo 1 — instrument 3.2b | NLA enabled in `Group Policy → Computer Configuration → Administrative Templates → System → Credentials Delegation`; MFA enforced via Windows Hello or RADIUS; 4625 logs show lockout after 3 failed attempts |
| Segment IT (VLAN 20) ↔ IoT/OT (VLAN 30) with firewall rules; restrict cross-VLAN SMB/SSH | Y | 8 | NIST CSF 2.0 PR.IR / ISO/IEC 27001:2022 A.8.20 (Networks security) / Anexo 1 — instrument 3.2b | Firewall ACL blocks 139/445/3389 from VLAN 30 to VLAN 20; VLAN isolation confirmed via `show vlan`; routing table shows separate gateways per VLAN |

## 5.3 Hardening — c) IoT / OT · instrument 3.2c

**Table 8 — Hardening c) IoT / OT (instrument 3.2c).**

| Hardening action | Applies? (Y/N) | Vector it mitigates | Framework | Verification |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Disable Telnet (23) on gateway; enforce SSH (22) + HTTPS (8080) with key authentication | Y | 6 | CIS 4 / NIST CSF 2.0 PR.AA / Anexo 1 — instrument 3.2c | Port 23 closed: `nmap -p 23 10.10.30.5` shows closed; SSH port 22 open with pubkey-only auth; HTTP 8080 redirects to HTTPS; certificate valid |
| Change gateway default credentials (`admin:admin`, `root:12345`) to strong unique passwords; implement MFA on admin panel | Y | 6 | CIS 5 / Anexo 1 — instrument 3.2c | Login attempts with default creds rejected; admin audit log shows only authorized accounts; MFA prompt on admin login to 10.10.30.5:8080 |
| MQTT broker authentication + per-topic ACL; disable anonymous access | Y | 9 | NIST CSF 2.0 PR.AA / ISO/IEC 27001:2022 A.5.15 (Access control) / Anexo 1 — instrument 3.2c | Broker rejects anonymous CONNECT; `mosquitto_pub` without credentials fails; ACL file restricts `invernadero/riego/cmd` to authenticated PLC user only; MQTT broker config shows `allow_anonymous false` |
| Isolate Modbus/PLC (10.10.30.30:502) on separate OT VLAN (VLAN 30); firewall restricts access to gateway + authorized clients only | Y | 9 | NIST CSF PR.IR / CIS 4 / Anexo 1 — instrument 3.2c | PLC isolated to VLAN 30; firewall rule allows only TCP 502 from gateway (10.10.30.5) and Modbus client IP; unauthorized hosts cannot reach port 502; network diagram confirms physical/logical isolation |
| Update camera firmware from 5.2.0 to latest stable; remove EOL RTSP server | Y | — (general IoT hardening, not mapped to a numbered vector — Challenge 2's own risk instrument, 2.9 Impacto y riesgo, explicitly records A-06 as having no associated risk scenario; addresses CVE-2017-9833/CVE-2022-45956, Table 3, directly) | CIS 3 / NIST CSF 2.0 ID.RA / Anexo 1 — instrument 3.2c | Camera firmware version checked: `curl http://10.10.30.21:81/info` shows current build; EOL components removed; security advisory check shows no active CVEs for deployed version |

## 5.4 Web-application controls

The application-layer defense operates at the boundary between user input and database storage, between privilege levels within the application and between components of the distributed architecture (frontend, API, backend). The OWASP Top 10:2021 and the OWASP Application Security Verification Standard (ASVS) v4.0 supply the framework; Challenge 2 vectors 2, 3, 4 and 10 supply the specific cases. For vector 2 (SQLi), prepared statements with parameterized queries are the primary control: all dynamic SQL in `productos.php`, the order-search and inventory endpoints must use PHP PDO or MySQLi prepared statements with placeholders, never string concatenation. For vectors 3 and 4 (IDOR and JWT), object-level authorization must be enforced: every `/api/v1/usuario`, `/api/v1/pedidos` and `/api/v1/inventario` endpoint must verify that the authenticated user owns the object before returning it, and the authorization library must use an allowlist (deny-by-default) rather than a blacklist. JWT tokens must carry a fixed `alg` field (RS256 or HS256, never `none`), include standard claims (`iss`, `aud`, `exp`), and be validated before each use. For vector 10 (outdated components), a Software Composition Analysis (SCA) scan must be integrated into the CI/CD pipeline to alert on jQuery and Bootstrap versions with known CVEs. File uploads (vector 2 in the CWE-434 dimension) must be validated on both client and server: accept only expected MIME types (image/jpeg, image/png), reject executable extensions, scan for malware signatures and store uploads outside the web root. Database credentials, API keys and encryption secrets must not be stored in the codebase: `config.php` must read from environment variables set at deployment time, and a secrets management tool (e.g., Vault, HashiCorp Consul) must be used for shared credentials. These controls are integrated into the DevSecOps pipeline described in Section 7.

# 6. Monitoring and detection proposal

The monitoring layer is designed as a detection pipeline, not as a log-collection exercise: sources
(Apache, Windows/Sysmon, MQTT broker, firewall and camera) feed correlation rules that turn isolated
events into incident candidates, following the sequence used by the course OVI — logs and events,
network traffic, IoT telemetry, SIEM correlation and alerts (Zambrano Hernández, 2026a). Each rule in
Table 9 is bound to a Kill Chain phase and a MITRE technique from Challenge 2, so a detection gap can
be read as a missing ATT&CK coverage (Strom et al., 2018). Severity and thresholds are set so that the
first alert triggers a containment action rather than a report; Table 10 assigns the source, the
frequency, the threshold and the owner. The detection strategy prioritizes the cross-domain vectors: brute-force and SQLi attacks on the DMZ portal (Table 4, vectors 1–2) must be caught before exfiltration can succeed; lateral movement within IT (vector 8) must trigger immediate isolation; and OT command manipulation (vector 9) must alert the operator and the security team in parallel, because manual override of the irrigation controller is faster than automated remediation. Thresholds are set conservatively: a single anonymous MQTT PUBLISH to `/cmd/*` is Critical severity, not because one command succeeds but because the precondition (unauthenticated broker) indicates that the entire OT segment may be under attack.

## 6.1 SIEM/XDR use cases

```{=latex}
\needspace{7\baselineskip}
```

**Table 9 — SIEM/XDR detection rules (instrument 3.3).**

```{=latex}
\begingroup
\renewcommand{\tablesize}{\footnotesize}
\breakslashes
```

| # | Rule name | Log source | Trigger condition | Severity | Expected event | Initial action |
|-------|------------------------------------------------------|----------------------------------------|----------------------------------------------------------------|------------------------------|----------------------------------------------|----------------------------------------------|
| 1 | Brute force on `/admin` | Apache `access.log` | ≥10 POST `/admin/login` in 60 s from same IP | High | Repeated 401/200 on login | Alert + temporary block |
| 2 | IT credential spraying | Windows 4625 | Multiple 4625 same user from different origins | High | Failed logons spike | SOC alert |
| 3 | Unauthorized MQTT | MQTT broker | Anonymous CONNECT + PUBLISH on a `/cmd` topic | Critical | Command topic write | Block + OT alert |
| 4 | Sensitive path probing | Apache `access.log` | Requests to `.bak`, `.git`, `/backup`, `/dbadmin` | High | 200/403 on sensitive paths | Alert + WAF rule |
| 5 | SQLi pattern in requests | WAF / `error.log` | SQL metacharacters / `PDOException` in logs | High | 500 + SQL syntax error | WAF block + alert |
| 6 | New service persistence | Windows 7045 + Sysmon 1 | Service installed from `C:\Windows\Temp\*` | Critical | `WinHlp32Svc` created | Isolate host + alert |
| 7 | Suspicious outbound C2 | Sysmon 3 / firewall | Outbound connection to `:1883` from IT hosts | High | Unexpected MQTT egress | Investigate + block |
| 8 | Camera anomaly | Camera / RTSP logs | Repeated auth failures or streams to new hosts | Medium | Abnormal camera access | Alert |

```{=latex}
\endgroup
```

**Per-rule framework and Challenge 2 trace.** R1–R2: T1110.001; R3: vector 9 / T1692.001; R4: vector 5 / T1552.001; R5: vector 2 / T1190; R6: T1543.003; R7: vector 9 (MQTT C2); R8: A-06 / CVE-2017-9833 (MITRE ATT&CK; instrument 3.3).

**Rule 1 thresholds.** Challenge 2's own credential-access evidence (instrument 2.7) recorded 37
failed POSTs to `/admin/login.php` in 40 seconds with `LockoutThreshold 0`. A detection rule tuned to
fire well before that volume is proposed as **N = 10, T = 60 s** (10 POST attempts to `/admin/login`
from the same IP within 60 seconds). This is a proposed, uncalibrated design parameter, not a
validated threshold — tuning against production traffic is deferred to Challenge 4.

## 6.2 Monitoring and alerting plan · instrument 3.4

**Table 10 — Monitoring and alerting plan (instrument 3.4).**

| Source / sensor | What it watches | Frequency | Alert threshold | Owner |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| WAF / web logs | Injection, brute force | Real time | ≥3 SQLi blocks in 60s; ≥10 POST `/admin/login` from same IP in 60s | SOC |
| EDR/SIEM (IT) | Anomalous logon, new services | Real time | ≥3 failed logons (4625) same user different IPs in 300s; new service 7045 from `C:\Temp\` | SOC |
| MQTT broker logs | Anonymous connect / command publish | Real time | Single anonymous CONNECT or PUBLISH to `*/cmd/*` topic (Critical); ≥2 failed auth in 60s | OT team |
| Firewall | Cross-zone flows, C2 egress | Real time | Any connection DMZ↔IT port 445/3389/22; any outbound 1883 from IT subnet; any VLAN 20↔VLAN 30 except approved gateways | Network team |
| OT IDS (Modbus) | Unauthorized write commands to PLC holding registers | Real time | Any write to holding register 100–103 (irrigation valve control) from an unauthorized source | OT team |
| Camera / RTSP logs | Auth failures, streams to new hosts | Real time | ≥3 auth failures in 300s, or a stream opened to a host outside the approved viewer list | OT team |
| DevSecOps / change-control telemetry | CI pipeline results (SAST, DAST, SCA, secret scan) and release approvals | Per pipeline run | Any scan that reports a finding on a deployed artefact, or a release merged without recorded approval (Table 11) | Application team + SOC |

# 7. DevSecOps proposal

DevSecOps integrates security validation into the application lifecycle — code, build, test, deployment, runtime — so that each vector from Challenge 2 is caught as early as possible and does not recur. The five practices in Table 11 map to the NIST CSF Govern function (policy and risk management) and the Identify function (asset and vulnerability baseline). Static Application Security Testing (SAST) runs before merge, catching injection vulnerabilities (CWE-89) and insecure API patterns (CWE-639) in the source code; Dynamic Application Security Testing (DAST) runs on a staging environment after deployment, validating that input validation and parameterized queries are actually enforced in the running application (vectors 1, 10). Software Composition Analysis (SCA) scans dependencies at build time, alerting to jQuery, Bootstrap and transitive library versions with known CVEs (vector 10). Pre-commit secret scanning detects credentials (`config.php.bak`, private keys, API tokens) before they reach the repository (vector 5), preventing exposure via `.git`. Change control ensures that every release is reviewed, tested and signed off before production deployment — a governance checkpoint that interrupts the propagation of any unvalidated control. The DevSecOps pipeline feeds results into Table 9 (SIEM/XDR rules) so that runtime behavior can be correlated with expected alerts: if SAST says the code has no SQLi, but SIEM logs a SQL syntax error, that evidence of an attempted attack becomes an incident signal.

**Table 11 — DevSecOps practices (with lifecycle stage).**

| Practice | Description | Lifecycle stage | Vector/reference it prevents |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
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
contain, eradicate, recover and learn (Zambrano Hernández, 2026a). The CSF 2.0 Respond and Recover
functions supply the governance interface: who declares the incident, who authorizes an OT shutdown
and what evidence must survive recovery (NIST, 2024; Mantilla Torres, 2025b). Table 12 translates each
phase into AgroSmart-specific actions, owner and evidence.

```{=latex}
\needspace{8\baselineskip}
```

**Table 12 — Incident-response playbook (instrument 3.5; NIST SP 800-61, 6 phases).**

| NIST SP 800-61 phase | Concrete actions in AgroSmart | Owner | Evidence/log |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Preparation** | Pre-incident: MQTT broker auth enabled; per-topic ACL in place; MQTT broker logs > syslog > SIEM; OT IDS rule for Modbus unauthorized write deployed; playbook team trained on roles and escalation (OT eng, security, management); backup of PLC config and MQTT broker config held offline | Security + OT team | MQTT broker config file; OT IDS signature; team-training sign-off; offline backup hash (SHA-256) |
| **Detection and analysis** | SIEM alert: anonymous CONNECT attempt + PUBLISH to `invernadero/riego/cmd`; OR OT IDS signature triggers on unauthorized Modbus write command to holding register 100-103 (irrigation valve control); security analyst correlates broker log timestamp with SIEM and PLC log; manual valve position check confirms unexpected state (open when should be closed) | SOC analyst + OT operator | SIEM alert ID + timestamp; broker log entry; PLC audit log; manual inspection record; initial severity assessment (Critical) |
| **Containment** | **Short-term:** Isolate MQTT broker at L2/L3 (block port 1883) — requires **joint authorization by the OT lead and the Security lead/CISO** per Section 8 escalation path; stop all telemetry ingestion; manual override: verify manual valve operator can close the irrigation line; issue OT alert via radio/SMS to greenhouse staff. **Medium-term:** Revoke any newly created MQTT credentials; check broker logs for lateral-movement attempts (other topics); monitor IT egress to 1883 | OT lead + Security ops (with Security lead/CISO for shutdown) | Network ACL modification log; manual-override record with timestamp; OT alert dispatch log; MQTT user audit; authorization record (OT lead + Security lead/CISO) |
| **Eradication** | Restore MQTT broker from clean backup (pre-incident config); verify no unauthorized users in ACL; rotate MQTT credentials for all clients (sensors, PLC, application); patch/update broker if vulnerability suspected; review and enforce firewall rule blocking 1883 from IT/DMZ to OT; run full vulnerability scan on gateway and broker | OT team + Security | Broker restore log; version check; credential rotation audit; firewall rule diff; vulnerability scan report (Nessus/OpenVAS) |
| **Recovery** | Restart MQTT broker; validate connectivity to all authorized clients (PLC, sensors, application) via health checks; manually verify irrigation is responding to commands; restore telemetry stream; test failover to backup broker; monitor for anomalies for 72 hours | OT team + application team | Broker startup log; health-check results; PLC response test log; telemetry flow confirmation; 72-hour anomaly-free monitoring log |
| **Lessons learned** | Post-incident review (within 1 week): root-cause analysis (how was broker access enabled?); timeline reconstruction; control-gap review (why was the alert delayed?); update incident response plan; training brief for all staff on MQTT security. Document in wiki/runbook; assign owner for each preventive action from Section 5.3 | Manager + team | Incident report (IR-YYYY-MMDD-001); updated runbook; training attendance sheet; action-item tracker (JIRA/Linear) with owners and due dates |

**Escalation path.** Detection and initial triage run SOC analyst → OT lead (operational-impact
assessment) → security lead/CISO (security coordination and incident declaration) → management
(executive decisions, external notification). A manual emergency stop of the irrigation valve, when
physical safety or crop damage is imminent, may be executed immediately by the on-site OT operator
under existing operational procedures, independent of SOC sign-off. A planned OT shutdown as an
incident-response measure (e.g., isolating the MQTT broker) requires **joint authorization by the OT lead and the Security lead/CISO**. Activation of manual-operation/recovery mode is an OT-team decision under the OT lead. This joint authorization is declared here for the purposes of this design.

# 9. Validation criteria for Challenge 4

Validation is written as a set of falsifiable hypotheses, not as a test log: each row of Table 13
names the control, the evidence that would prove it works and the method to obtain that evidence in
the Cyber Range. The Cyber Range activity included in the course OVA (OVA 3) insists on rules of
engagement, authorized scope, controlled validation and evidence retention before any technical
action (Mantilla Torres, 2025c), while the OVI frames evidence as the link between a finding and a
defensible decision (Zambrano Hernández, 2026a). The nine validation criteria in Table 13 span the three
domains (DMZ, IT, IoT/OT) and cover both preventive and detective controls, ensuring that the next
phase has a measurable yardstick for each major control. No criterion is executed here; the table is the
contract for Challenge 4.

**Table 13 — Validation criteria for Challenge 4 (with expected evidence and method).**

| # | Control / hypothesis to validate | Expected technical evidence | Verification method (Cyber Range) |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Apache patched (≥2.4.51) blocks CVE-2021-41773/42013 | Traversal attempt fails (403/404) | `curl` / `nmap --script http-vuln-cve2021-41773` |
| 2 | SQLi mitigated by parameterized queries + WAF | Payload blocked, no SQL error | Manual payload + WAF log review |
| 3 | JWT signature verified (`alg:none` rejected) | Forged token rejected | Send `alg:none` token, expect 401 |
| 4 | SMBv1 disabled, signing on, null session blocked | `smbclient -N` fails; signing required | `smbclient` / `nmap --script smb-security-mode` |
| 5 | MQTT requires auth; anonymous publish denied | Anonymous `CONNECT` refused | `mosquitto_pub` with/without creds |
| 6 | Modbus/PLC isolated; unauthorized writes blocked | Write attempt rejected/no effect | Modbus client test in OT segment |
| 7 | DMZ detective: WAF/SIEM rule 5 (SQLi pattern) fires on a controlled injection test | WAF block log + SIEM alert within the rule's threshold window | Controlled SQLi payload sent to `productos.php` in the Cyber Range; expect WAF block + alert (pass) or no alert (fail) |
| 8 | IT detective: SIEM rule 2 (credential spraying) fires on an SMB null-session/anomalous-logon event | Windows 4625 correlation alert | Controlled null-session connection attempt from a non-authorized host; expect SOC alert (pass) or silence (fail) |
| 9 | IoT/OT detective: SIEM rule 3 (unauthorized MQTT) fires on an anonymous PUBLISH | Broker log entry + SIEM "Block + OT alert" | Anonymous `mosquitto_pub` to `invernadero/riego/cmd` in the isolated lab segment; expect block + alert (pass) or unblocked publish (fail) |

**No validation was executed in Challenge 3.** All nine rows above are falsifiable hypotheses
reserved for the authorized Cyber Range activity of Challenge 4; none has been run, and this table is
not a results report.

# 10. Conclusions and references

This report converts the Challenge 2 offensive findings into a defensive design that is traceable end to end: each control starts from a vector, a probable cause and an affected asset, and ends in an expected evidence line. The contribution is the chain vector → probable cause → control → evidence, organized by the CSF 2.0 functions and operationalized through the course OVI's detection and response sequence. The traceability matrix (Table 5) ensures that no vector is left undefended and no control is imposed without a corresponding threat; the hardening checklists (Tables 6–8) prioritize the actions with the highest impact on the AgroSmart case; the SIEM rules (Table 9) and the DevSecOps pipeline (Table 11) close the loop by detecting and preventing recurrence. The incident-response playbook (Table 12) operationalizes the six NIST SP 800-61 phases into concrete actions for the priority vector (OT command manipulation), and the validation criteria (Table 13) provide the falsifiable hypotheses that will be tested in the Cyber Range.

The main limitation is that no control has been validated: thresholds, correlation rules, playbook times and architectural assumptions are design hypotheses to be tested in Challenge 4. A second limitation is the reliance on course materials and framework guidance rather than measured results from this organization; the OVA/OVI and the NIST, CIS and OWASP references orient the design but do not substitute for validation on the actual AgroSmart infrastructure. A third limitation is that the IoT/OT hardening and monitoring proposal (Section 5.3, Tables 8–9) assumes that firmware updates and protocol changes are possible; if the PLC or MQTT broker cannot be patched due to operational constraints, the detection and containment strategies become the primary defense, and the risk profile shifts. T0855 was renumbered to T1692.001 in ATT&CK for ICS v19.0; Challenge 2's label is preserved for traceability. The next step is to execute Table 13 under the Challenge 4 rules of engagement, validate each control's effectiveness and measurable impact, and feed the empirical results back into Tables 5, 9 and 12 to refine the design.

# Appendix — AI-usage declaration / log

**Declaration of AI use.** AI assistants were used only for organizational, formatting, and editorial support; no AI output was used to assert any technical finding or substantiate any table. All substantive content derives from the course materials and the Challenge 2 analysis and was verified by the author.

| Field | Response |
| :-- | :-- |
| AI tool used | OpenCode and Claude (AI assistants). |
| Scope of use | Three strictly organizational/formatting/editorial tasks: (1) ordering the repository documentation; (2) producing the LaTeX template for PDF/DOCX rendering (Unicode `≥ → ↔` in the matrices); (3) style, grammar and APA 7 review of prose and references. |
| Prompts employed (with purpose) | `"Organize the repository documentation"` — navigate the course materials efficiently; `"Generate the LaTeX form for rendering the PDF"` — render `doc.md` to PDF/DOCX via Pandoc/XeLaTeX; `"Review writing style and references"` — flag minor style and APA 7 issues. |
| Output obtained | (1) A suggested listing for repository organization. (2) A draft LaTeX form for rendering. (3) Specific suggestions for minor writing corrections and notes regarding reference formatting. |
| Verification performed | Every suggestion was checked against the sources (Annex 1, Challenge 2 instruments, the rubric), APA 7 (corrected authorships, years, direct DOIs), the "design only / no tests" declaration, and correct `make` rendering with bidirectional citation–reference correspondence; anything touching technical content was confirmed against its original source first. |
| Adjustments made by the author's own judgment | Only structural/formatting/editorial suggestions were accepted after verification; any that would alter findings, traceability, MITRE/CVE/CWE mappings or thresholds, or add generic arguments, were rejected or rewritten manually. No AI-generated argument, control, or conclusion was adopted unmodified. |
| What was NOT generated by AI | No substance was AI-generated — findings, vectors, assets (A-01…A-08), MITRE/CVE/CWE mappings, the traceability and risk matrices, hardening, SIEM rules, thresholds, the response playbook, validation criteria and conclusions all come from Annex 1, the Challenge 2 instruments and the course materials. AI support is not quantified as a percentage. |

## References

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
- Zambrano Hernández, L. F. (2026a). *Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT* [OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/83223 (handle pending verification — returned HTTP 404 on last access)
- Zambrano Hernández, L. F. (2026b). *Reto integrador de Intrusión y Testing: Caso de estudio AgroSmart del Sumapaz S.A.S.* (Anexo 1) [Documento maestro del curso]. Universidad Nacional Abierta y a Distancia.

**Technical frameworks**

- Center for Internet Security. (2021). *CIS Controls Version 8: Implementation guidance for enterprises* (CIS Critical Security Controls). https://www.cisecurity.org/controls/v8
- Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2012). *Computer security incident handling guide* (NIST SP 800-61 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2
- ISO/IEC. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC 27001:2022). https://www.iso.org/standard/27001
- NIST. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSF 2.0; NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- NIST. (n.d.). *National Vulnerability Database* (NVD) [Database]. Retrieved October 22, 2026, from https://nvd.nist.gov/
- OWASP Foundation. (2021). *OWASP Top 10: 2021 — The ten most critical web application security risks*. https://owasp.org/Top10/
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018). *MITRE ATT&CK: Design and philosophy*. The MITRE Corporation. https://doi.org/10.13140/RG.2.2.13778.58565
