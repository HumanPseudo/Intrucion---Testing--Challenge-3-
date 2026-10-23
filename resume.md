# resume.md — From `md/referencias/` to the report and the enterprise

> **What this is:** an applied synthesis of the 7 articles, the 3 OVAs and the OVI in `md/referencias/`.
> **Why:** understand the framework, know what to put in Challenge 3, and what to run in an authorized
> enterprise context.
> **Challenge 3 rule:** this is **design, not testing**. The commands in Section 6.6 are only for
> Challenge 4 / Cyber Range; do not run them for this deliverable.
> **Original sources:** local in `md/referencias/` (copyrighted; not distributed).

---

## 0. 60-second read

- **Governing framework:** **NIST CSF 2.0** (February 2024) — 6 functions: **Govern, Identify, Protect,
  Detect, Respond, Recover**. It is not a checklist; it is a taxonomy of outcomes.
- **Operating framework:** the **OVI** connects attack and defense: exposure surface → Cyber Kill
  Chain + MITRE ATT&CK → detection (logs, network, IoT, SIEM, alerts) → response (identify, contain,
  eradicate, recover, learn).
- **Offensive method:** PTES / OWASP / OSSTMM / NIST SP 800-115 / CEH (Palomo Luna et al., 2024);
  WiFi in 4 phases (Lu & Yu, 2021); SQLi with SQLmap (Crespo-Martínez, 2021).
- **Human factor:** phishing and social engineering (Benavides et al., 2020; Benavides-Astudillo et
  al., 2020; Prado Díaz, 2021; Albininé Budavári et al., 2023).
- **In the report:** every control, rule or action must answer **a Challenge 2 vector** and **a CSF
  function**. Without that chain, the control is an orphan.
- **In the enterprise:** turn scattered tools into a **program**: governance, current vs. target
  profile, prioritization, controls, monitoring, response, recovery and metrics.

**If you only have 20 minutes:** read Sections 1, 4, 5, 6.1 and 8.

---

## 1. The framework on one page — NIST CSF 2.0

### 1.1 The six functions

| Function | Key question | What it produces | In the report | In the enterprise |
|---|---|---|---|---|
| **Govern (GV)** | Who decides, who is accountable, and under which policy? | Strategy, roles, policies, third-party risk, business alignment | Section 1, Section 5 (intro), Section 10 | Security committee, CISO, policies, supplier management |
| **Identify (ID)** | What do we have, what is it worth, and what risk does it face? | Inventory, criticality, risk assessment, dependencies | Section 2, Section 3, Tables 1–4 | CMDB, risk analysis, attack-surface map |
| **Protect (PR)** | Which safeguards reduce likelihood and impact? | Hardening, MFA, segmentation, backups, training | Section 5, Tables 6–8 | CIS/OWASP baseline, ISO/IEC 27001, access control |
| **Detect (DE)** | How do we know something is happening? | Logs, traffic, IoT telemetry, SIEM, use cases, alerts | Section 6, Tables 9–10 | SOC, continuous monitoring, MTTD |
| **Respond (RS)** | What do we do when an incident is confirmed? | Playbook, containment, communication, evidence | Section 8, Table 12 | Response plan, roles, escalation, crisis |
| **Recover (RC)** | How do we return to operations and what do we learn? | Backups, RTO/RPO, restoration, lessons learned | Section 8, Section 10 | BCP/DRP, restore tests, postmortem |

### 1.2 How it is actually used

- **Core:** 6 functions → **35 categories** → **108 subcategories**. Do not implement all 108: select
  the applicable ones, justify them and measure them.
- **Profiles:** **Current Profile** (what is achieved today) vs. **Target Profile** (what is to be
  achieved). A profile is a snapshot of outcomes, not a certification.
- **Tiers:** 1 **Partial** (ad hoc), 2 **Risk Informed** (management-approved), 3 **Repeatable**
  (formal policies, organization-wide approach), 4 **Adaptive** (risk-based, continuous improvement).
- **What is new in 2.0:** the **Govern** function; Quick Start Guides for SMEs; **supply-chain** risk;
  quantifiable **metrics**; integration with **ERM**; informative references and implementation
  examples.
- **Integration:** CSF relies on ISO/IEC 27001, CIS Controls, NIST SP 800-53 and regulations such as
  GDPR. **It does not replace them**: it orders the “what” and leaves the “how” to those frameworks.
- **Benefits:** common language, prioritization, avoiding duplicated effort and continuous improvement.

### 1.3 Three conceptual errors

1. **Confusing profile with tier.** The profile says *which outcomes* are achieved; the tier says *how
   rigorous* the practices are.
2. **Using CSF as a checklist.** It is an outcomes framework; selection and justification are yours.
3. **Believing CSF certifies.** It is not a certifiable standard; it is a voluntary, flexible framework.

---

## 2. The OVI: the bridge between attack and defense

1. **Exposure surface:** networks, applications and services, infrastructure, systems/data and IoT.
   Every connected component expands the surface.
2. **Reference models:** **Cyber Kill Chain** (7 phases, from reconnaissance to actions on objectives)
   + **MITRE ATT&CK** (tactics, techniques, sub-techniques, procedures and software). They are
   complementary: one tells the sequence; the other names what is observable.
3. **Detection:** logs and events + network traffic + device monitoring + **SIEM/correlation** + alerts
   + SOC. In IT/IoT, correlating and prioritizing is the key.
4. **Response:** **identification → containment → eradication → recovery → learning**. Detection is
   only the beginning; value lies in responding with evidence.
5. **Good practices:** governance and policies; risk management; people and culture; technology and
   controls; monitoring and continuous improvement.

**Practical rule:** every alert must declare **CKC phase + ATT&CK technique + log source + threshold +
initial action**. If one is missing, the rule is not operable.

---

## 3. What each source contributes

| Source | Main contribution | Where to use it |
|---|---|---|
| **Palomo Luna et al. (2024)** | Compares pentesting methodologies: **PTES, OWASP, OSSTMM, NIST SP 800-115 and CEH**; phases, scope, reporting and tools. | Section 1 (method), Section 2 (offensive synthesis), Section 9 (validation) |
| **Lu & Yu (2021)** | WiFi with Kali in **4 phases**: preparation, information gathering, simulated attack, reporting. | Section 2 (wireless surface), Section 5 (if WiFi exists), Section 9 |
| **Crespo-Martínez (2021)** | SQLmap against Oracle APEX 5; the result was **negative** and still valid: method, versions, scope and evidence matter. | Section 2 (SQLi), Section 5.4 (web controls), Section 9 (criteria) |
| **Benavides et al. (2020)** | **Phishing** taxonomy and mitigations: awareness + ML/DL. | Section 5 (training), Section 6 (email detection), Section 8 |
| **Benavides-Astudillo et al. (2020)** | Controlled social-engineering experiment: only **2%** suspected; it collected IP/OS/browser and scanned **80/22**. | Section 3 (human risk), Section 5 (awareness), Section 8 |
| **Prado Díaz (2021)** | Social-engineering campaign methodology: victim → sample → profiling → campaigns → evidence → report → risk grade → recommendations. | Section 3, Section 5, Section 8, Section 10 |
| **Albininé Budavári et al. (2023)** | Social engineering as a **system disturbance** (cybernetic loop, energy balance); it reinforces defense. | Section 1, Section 3, Section 10 |
| **OVA 1–3 (Mantilla Torres, 2025a–c)** | Common body: **CSF 2.0** (functions, categories, subcategories, profiles, tiers, SMEs, supply chain, metrics). Activities differ: OVA 1 pentesting/scope/evidence; OVA 2 vectors/defense/prioritization; OVA 3 Cyber Range/rules of engagement/evidence. | Section 1, Section 5, Section 8, Section 9 |
| **OVI (Zambrano Hernández, 2026)** | Detection and management of IT/IoT attacks: surface, CKC, ATT&CK, SIEM, IR, good practices. | Section 1, Section 2.4, Section 6, Section 8, Section 9, Section 10 |

> **Careful with the OVAs:** the three local OVAs are **Mantilla Torres (2025a–c)** and develop
> **CSF 2.0**. They are **not** the guide's OVA (`10596/83229`, Zambrano), which still returns 404.
> Do not cite them as if they were the same resource.

---

## 4. Report ↔ framework map

| Section | Table | CSF function | What must be clear |
|---|---|---|---|
| 1 | — | GV / ID | Purpose, three domains, scope, no-test declaration |
| 2 | 1–3 | ID | Assets A-01…A-08, surfaces, 10 vectors, CVE/CWE, CKC and ATT&CK |
| 3 | 4 | ID / GV | 6 criteria, descending priority, justification of the order |
| 4 | 5 | GV / PR | **Vector → control → evidence** chain (10 columns) |
| 5 | 6–8 | PR | LAMP / IT / IoT-OT hardening + application controls |
| 6 | 9–10 | DE | ≥6 SIEM/XDR use cases + monitoring and alerting plan |
| 7 | 11 | PR | DevSecOps across the life cycle |
| 8 | 12 | RS / RC | 6 NIST SP 800-61 phases for the prioritized scenario |
| 9 | 13 | DE / RS | ≥5 falsifiable criteria, expected evidence and method |
| 10 | — | GV / RC | Conclusions, limitations, references and AI log |

**Quality test:** if a row in Table 5 does not say which vector it mitigates, which control it applies
and which evidence it produces, it is incomplete.

---

## 5. Enterprise application: 30 / 60 / 90 route

| Horizon | CSF focus | Deliverable | Output metric |
|---|---|---|---|
| **0–30 days** | Govern + Identify | Sponsor, scope, inventory, current profile, attack-surface map | % of assets inventoried; risks prioritized |
| **31–60 days** | Protect | Baseline, MFA, segmentation, backups, awareness | % of controls implemented; % of critical patches |
| **61–90 days** | Detect + Respond + Recover | SIEM, use cases, playbook, restore test | MTTD, MTTR, RTO/RPO; % of logs covered |

**Monthly/quarterly routine:**

- Review the **target profile** and the gaps.
- Review **suppliers** and dependencies (supply chain).
- Test **restore** (having a backup is not enough).
- Run an **incident simulation** and update the playbook.
- Update **metrics**: MTTD, MTTR, % assets, % patches, phishing fail rate.
- Review accesses, changes and exceptions.

**Reading example (not case data):** if the assessment finds anonymous MQTT, Modbus without
authentication and no SIEM, the current profile cannot be described as “Repeatable”; the target
profile must set policies, segmentation, authentication, monitoring and a tested playbook.

---

## 6. Commands to run

### 6.1 For the deliverable (always)

```bash
cd report
make            # build report.pdf
make docx       # build editable report.docx
make both       # PDF + DOCX
make wordcount  # body 6,000–8,000, references excluded
make check      # full verification
make clean      # remove temporary files
```

If `make check` fails on word count or on `[..]`, it is **not a pipeline error**: sections or matrices
are still missing. Current state: ~3,358 words and pending cells.

```bash
git status --short
git diff -- report/doc.md plan.md
```

### 6.2 Enterprise — inventory and surface (Identify)

> Replace `NETWORK` and `HOST`. Run only against **authorized** assets.

```bash
nmap -sn 10.0.0.0/24
nmap -sV -sC -p- -oA scan HOST
whatweb http://HOST
nikto -h http://HOST
sudo ss -tulpn
sudo lsof -i -P -n
smbclient -N -L //HOST
enum4linux -a HOST
```

**What to look at:** ports and versions, headers, exposed files, SMB null sessions, IoT services
(MQTT/1883, Modbus/502, Telnet/23).

### 6.3 Enterprise — hardening verification (Protect)

```bash
apache2ctl -S
apache2ctl configtest
curl -I https://HOST
openssl s_client -connect HOST:443 -servername HOST
testssl.sh https://HOST
nmap --script ssl-enum-ciphers -p 443 HOST
sudo ufw status verbose
sudo lynis audit system
```

**What to look at:** TLS and ciphers, headers, vhosts, ports that should not be open, baseline
compliance. `lynis` is read-only; `ufw` and configuration changes require a window and approval.

### 6.4 Enterprise — detection (Detect)

```bash
sudo tail -f /var/log/apache2/access.log /var/log/apache2/error.log
sudo journalctl -u ssh -f
sudo tcpdump -i any -n port 1883 -w mqtt.pcap
sudo tshark -r mqtt.pcap -Y mqtt
sudo grep -E "Failed password|Accepted|sudo" /var/log/auth.log
sudo suricata -T -c /etc/suricata/suricata.yaml
```

**What to look at:** brute force, scans, anonymous MQTT, 4xx/5xx errors, traffic spikes, unexpected
IoT/OT commands.

### 6.5 Enterprise — response and evidence (Respond / Recover)

```bash
date -u +%Y-%m-%dT%H:%M:%SZ
sudo tcpdump -i any -w incident.pcap
sudo journalctl --since "2026-10-22 10:00" > incident.log
sha256sum evidence*
sudo cp --preserve=all evidence* /evidence/
sudo ufw deny from IP
sudo systemctl stop SERVICE
```

**Rule:** **evidence first**, containment second. `ufw deny` and `systemctl stop` only with
authorization and a change window. For restore:

```bash
tar -tzf backup.tar.gz
rsync -a --dry-run /backup/ /restore/
```

### 6.6 Challenge 4 / Cyber Range only (DO NOT run in Challenge 3)

> These commands **interrupt or exploit**. Only with scope, authorization and rules of engagement.

```bash
# WiFi (authorized lab)
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon
sudo aireplay-ng --deauth 5 -a BSSID wlan0mon
sudo aircrack-ng -w rockyou.txt capture.cap

# SQLi (authorized lab)
sqlmap -u "http://HOST/item?id=1" --batch --dbs

# SMB / MQTT
smbclient -N -L //HOST
mosquitto_sub -h BROKER -t '#' -C 10 -v
```

---

## 7. Application checklist

- [ ] Choose the **CSF function** and the **profile** (current/target).
- [ ] Inventory assets, surfaces and dependencies.
- [ ] Prioritize by criticality, impact, likelihood, CVSS, exposure and propagation.
- [ ] Define **control + vector + evidence**.
- [ ] Define the **detection use case** (source, threshold, severity, action).
- [ ] Define the **playbook** and roles.
- [ ] Define the **restore test**.
- [ ] Measure MTTD, MTTR, log coverage, patching and phishing.
- [ ] Review suppliers and the supply chain.
- [ ] Document lessons learned and update the profile.

---

## 8. Mistakes to avoid

- **CSF is not a checklist:** do not copy the 108 subcategories; select and justify.
- **Profile ≠ tier:** the profile is the gap; the tier is the rigor.
- **Control without a vector:** it does not count for Challenge 3.
- **Tool without evidence:** it does not count for Challenge 4.
- **Testing in production:** forbidden; use a lab or the Cyber Range.
- **Wrong OVA:** the local ones are Mantilla Torres (2025a–c), not Zambrano's OVA.
- **Citing the OVI without a caveat:** the handle returns 404; use the verified local copy.
- **Inventing case data:** assets, vectors, CVE/CWE and techniques come from `md/reto2/` and Annex 1.

---

## 9. Sources

| Short citation | Local file |
|---|---|
| Mantilla Torres (2025a, 2025b, 2025c) | `OVA 1/2/3 - Marco de Seguridad Cibernética 2.0 del NIST.md` |
| Zambrano Hernández (2026) | `OVI - Diseño de estrategias de detección y gestión de ataques cibernéticos.md` |
| Palomo Luna et al. (2024) | `Octubre_2024.md` |
| Lu & Yu (2021) | `Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.md` |
| Crespo-Martínez (2021) | `mquinde,+articulo10.md` |
| Benavides et al. (2020) | `EBSCO-FullText-10_19_2026 (1).md` |
| Benavides-Astudillo et al. (2020) | `EBSCO-FullText-10_19_2026.md` |
| Prado Díaz (2021) | `carla,+ODIGOS+V2-NUM3-2021-47-76.md` |
| Albininé Budavári et al. (2023) | `indecs2023-pp168-173.md` |
| NIST (2024), CSF 2.0 | Cited in the OVAs; DOI `10.6028/NIST.CSWP.29` |
| Cichonski et al. (2012), NIST SP 800-61r2 | Cited in the OVI and the report; DOI `10.6028/NIST.SP.800-61r2` |
| Strom et al. (2018), MITRE ATT&CK | Cited in the OVI and the report; DOI `10.13140/RG.2.2.13778.58565` |

**Frameworks used by the report but not stored in `md/referencias/`:** CIS Controls v8,
ISO/IEC 27001:2022, OWASP Top 10:2021 and NVD. They are in the APA list in `report/doc.md`.
