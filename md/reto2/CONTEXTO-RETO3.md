# Contexto consolidado para el Reto 3 — insumos del Reto 2

> **Propósito de este documento.** Reunir en un solo lugar **todo el contexto necesario** para redactar el informe técnico del Reto 3 (diseño defensivo), sin tener que abrir el vault del Reto 2.
>
> **Cómo usarlo.** Es un **mapa + resumen de datos**, no un reemplazo de las fuentes. Cada dato tiene enlace al `.md` de origen dentro de este paquete (`md/reto2/`). Los datos duros (activos, vectores, CVE, rutas) se reproducen aquí para consulta rápida; el argumentario completo está en los instrumentos citados.
>
> **Curso:** Intrusión y Testing (203028113) · UNAD · ECBTI. **Caso único:** AgroSmart del Sumapaz S.A.S. (los Retos 2-5 son fases del mismo caso).

---

## 0. El encadenamiento de los retos (por qué el Reto 2 alimenta al Reto 3)

Fuente: `md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md` (pág. 2, tabla de fases de Kolb).

| Reto | Fase de Kolb | Lo que produce | Evidencia |
|------|--------------|----------------|-----------|
| Reto 1 | Experiencia concreta | Apropiación conceptual (metodologías, alcance, ROE, superficie, pensamiento adversarial) | Cuestionario POC |
| **Reto 2** | **Observación reflexiva** | **Análisis del escenario ofensivo**: activos críticos, superficies, vectores, ingeniería social, CVE/CVSS, rutas, impacto | **Video académico/técnico** |
| **Reto 3** | **Conceptualización abstracta** | **Diseño defensivo**: controles preventivos/detectivos, hardening, monitoreo, reglas de detección y respuesta, **trazables a los vectores del Reto 2** | **Informe técnico de diseño defensivo** |
| Reto 4 | Conceptualización abstracta aplicada | Planificación del compromiso y emulación adversaria; valida documentalmente los controles del Reto 3 | Informe de planificación |
| Reto 5 | Experimentación activa | Ejecución ética en Cyber Range | Informe final de intrusión |

> **Regla de oro del Reto 3** (Anexo 1, pág. 32): *"La clave de este reto es la **trazabilidad**: cada control que proponga debe responder a un vector identificado en el Reto 2. No se evalúa una lista genérica de buenas prácticas, sino la coherencia entre amenaza y defensa."*

---

## 1. Requisitos del Reto 3 (fuente normativa)

### 1.1 Ficha del Reto 3 (Anexo 1, pág. 32; coincide con la Guía `md/actividad/Guía de aprendizaje - Reto 3.md`)

| Campo | Valor |
|-------|-------|
| Momento de la evaluación | Intermedio |
| Unidad gestora | ECBTI |
| Inicia | lunes, **28 de septiembre de 2026** |
| Finaliza | domingo, **25 de octubre de 2026** |
| Horas de trabajo independiente | **30 horas** |
| Interacciones | Foros de interacción entre estudiantes |
| Puntuación | **125 puntos** |
| Resultado de aprendizaje | **RA2**: Diseñar esquemas integrales de detección, identificación y gestión de ataques cibernéticos, utilizando técnicas ofensivas y pensamiento adversarial… |
| Entregable | **Informe técnico de diseño defensivo**, Word o PDF, **6.000-8.000 palabras** (sin referencias), individual |
| Restricción | **No** se ejecutan pruebas ni explotación técnica (eso es del Reto 5) |
| Formato | Tablas **editables** integradas en el documento; sin capturas, imágenes de tablas, enlaces externos ni repositorios |
| Citas | Normas **APA** |

### 1.2 Las 10 secciones mínimas del informe (Guía Reto 3, págs. 7-8)

1. Introducción y alcance del diseño defensivo (propósito + 3 dominios + relación con Reto 2)
2. Síntesis del análisis ofensivo del Reto 2 (activos, superficies, vectores, CVE/CVSS, CKC, MITRE)
3. Matriz de priorización de riesgos (criticidad, impacto, probabilidad, severidad, propagación)
4. **Matriz de trazabilidad vector–control** (causa, activo, impacto, técnica MITRE, fase CKC, control preventivo/detectivo/correctivo, evidencia esperada)
5. Diseño de controles defensivos (hardening Ubuntu/Apache/PHP/MariaDB, app web, autenticación/sesiones, credenciales, directorios/backups, IT, IoT/OT)
6. Propuesta de monitoreo y detección (casos de uso SIEM/XDR: fuente de log, condición, severidad, evento, correlación, acción inicial)
7. Propuesta DevSecOps (validación de entradas, codificación segura, SAST, DAST, SCA, escaneo de secretos, control de cambios)
8. Plan básico de respuesta a incidentes (preparación, identificación, contención, erradicación, recuperación, lecciones aprendidas)
9. Criterios de validación para el Reto 4 (hipótesis y controles a verificar en el Cyber Range)
10. Conclusiones y referencias (APA)

### 1.3 Los 5 instrumentos del Anexo 1 para el Reto 3 (págs. 32-35)

Estos son los **formularios** que el Anexo 1 trae redactados y que deben aparecer en el informe:

| Instrumento | Nombre | Qué se diligencia |
|-------------|--------|-------------------|
| **3.1** | Matriz de trazabilidad vector → control | Vector (Reto 2) · Control preventivo · Control detectivo · Marco (CIS/NIST/ISO) · Activo protegido |
| **3.2** | Hardening por dominio (checklist) | **a) Web/LAMP** (5 acciones) · **b) IT/Windows** (3) · **c) IoT/OT** (4) — cada una: ¿Aplica? S/N · Justificación/vector que mitiga · Verificación |
| **3.3** | Reglas de detección | Nombre de la regla · Fuente de log · Condición de disparo (pseudo-Sigma/Snort) · Severidad · Acción/alerta |
| **3.4** | Plan de monitoreo y alertamiento | Fuente/sensor · Qué vigila · Frecuencia · Umbral de alerta · Responsable |
| **3.5** | Procedimiento de respuesta (NIST SP 800-61) | Preparación · Detección y análisis · Contención · Erradicación · Recuperación · Lecciones aprendidas |
| — | Declaración de uso de IA | Herramienta · Para qué · Prompts · Salida · Verificación · Ajustes · % apoyado en IA |

> Las filas de ejemplo que trae el Anexo 1 (p. ej. `SQLi en portal → Validación/consultas parametrizadas; WAF → Alerta por patrón SQL → CIS 16 / OWASP → A-01`) sirven como **plantilla de formato**; el contenido se construye con los vectores reales del Reto 2.

---

## 2. El caso AgroSmart del Sumapaz S.A.S.

Fuente: `md/reto2/contexto/Contexto y arquitectura.md` y Anexo 1, Sec. 2 (págs. 9-10).

Empresa agroindustrial mediana (Sumapaz, Cundinamarca). Produce hortalizas y frutales con agricultura inteligente: invernaderos instrumentados, riego automatizado y cámaras. Creció rápido, conectó IoT de varios proveedores **sin revisión de seguridad** y publicó su portal en internet en las mismas condiciones.

### 2.1 Los tres dominios y las tres fronteras

| Dominio | Componentes | Frontera |
|---------|-------------|----------|
| **DMZ / Web (LAMP)** | Portal AgroSmart (Apache **2.4.49** + MariaDB **10.3** + PHP **7.2.24**), panel admin, phpMyAdmin | **F1** · firewall perimetral hacia Internet (80/443) |
| **IT corporativo** | FILESRV01 (SMB/LDAP, dominio AGROSMART), CONTA-PC (RDP) | **F2** · sin control de flujo entre DMZ e IT |
| **IoT / OT** | Gateway (Telnet/8080), cámara IP, PLC de riego (Modbus), broker MQTT | **F3** · frontera débil con IT (misma red conmutada) |

> **Hallazgo estructural clave** (`2.2 Superficie de exposición`): *ninguna* de las tres fronteras es un control de autenticación — son decisiones de enrutamiento. El atacante no las "rompe": las atraviesa con protocolos permitidos. **La segmentación de red es control prioritario.**

### 2.2 Inventario de activos (Anexo 1, Sec. 3.1, pág. 11)

| ID | Activo | Dominio | IP (lab) | Servicio principal |
|----|--------|---------|----------|--------------------|
| A-01 | Portal AgroSmart (web) | DMZ | 10.10.10.20 | HTTP/HTTPS (80/443) |
| A-02 | Gestor BD web (admin) | DMZ | 10.10.10.20 | HTTP (/dbadmin) |
| A-03 | Servidor de archivos/dominio | IT | 10.10.20.10 | SMB (445), LDAP |
| A-04 | Estación contabilidad | IT | 10.10.20.51 | RDP (3389) |
| A-05 | Gateway IoT | IoT/OT | 10.10.30.5 | HTTP admin (8080) |
| A-06 | Cámara IP invernadero | IoT/OT | 10.10.30.21 | RTSP (554)/HTTP (81) |
| A-07 | Controlador de riego (PLC) | IoT/OT | 10.10.30.30 | Modbus/TCP (502) |
| A-08 | Broker de telemetría | IoT/OT | 10.10.30.40 | MQTT (1883) |

### 2.3 Marco legal y ROE (Anexo 1, Sec. 1, págs. 7-8)

| Norma | Qué regula | Por qué importa |
|-------|-----------|-----------------|
| **Ley 1273/2009** | Delitos informáticos (art. 269A acceso abusivo…) | Acceso sin autorización es delito; la autorización escrita separa el pentest de la conducta delictiva |
| **Ley 1581/2012** | Protección de datos personales (habeas data) | Confidencialidad y minimización de los datos hallados (correos, credenciales, PII) |
| **Ley 1341/2009** | Marco de las TIC | Encuadre sectorial |

**ROE del caso:** AgroSmart autoriza reconocimiento, enumeración y validación controlada **únicamente dentro del Cyber Range del curso**. *In-scope:* los 8 activos y 3 dominios del laboratorio. *Out-of-scope:* cualquier IP/dominio/persona/servicio real; DoS destructivos; exfiltración real; ingeniería social **ejecutada**. **Regla de oro:** si no está explícito en el alcance, está fuera.

---

## 3. Insumos ofensivos del Reto 2 (lo que el Reto 3 debe defender)

> **Esta es la sección medular:** cada fila de aquí es candidata a una fila de la matriz de trazabilidad (instrumento 3.1).

### 3.1 Activos críticos C-I-D — `md/reto2/instrumentos/2.1 Activos críticos C-I-D.md`

Escala 1-5 (1 = poco relevante … 5 = crítico para el negocio).

| ID/Activo | Función | Dominio | C | I | D | Criticidad |
|-----------|---------|---------|---|---|---|------------|
| A-01 Portal AgroSmart | Pedidos B2B y datos de clientes | DMZ | 5 | 4 | 4 | **Crítico (13)** |
| A-02 phpMyAdmin | Gestión directa de la BD de producción | DMZ | 5 | 5 | 4 | **Crítico (14)** — máxima |
| A-03 FILESRV01 | Archivos de negocio y dominio AGROSMART | IT | 4 | 5 | 3 | **Crítico (12)** |
| A-04 CONTA-PC | Facturación y cotizaciones | IT | 3 | 4 | 3 | Medio-alto (10) |
| A-05 Gateway | Enlace de los sensores con la red | IoT/OT | 3 | 3 | 4 | Medio-alto (10) |
| A-06 Cámara IP | Vigilancia del invernadero | IoT/OT | 3 | 2 | 3 | Medio (8) |
| A-07 PLC de riego | Control del riego del cultivo | IoT/OT | 3 | 5 | 5 | **Crítico (13)** |
| A-08 Broker MQTT | Transporte de telemetría y comandos | IoT/OT | 3 | 4 | 4 | **Crítico (11)** |

**Lectura:** C e I se concentran en DMZ+IT (datos y credenciales); D se desplaza a IoT/OT (el PLC y el broker). → **Dos líneas de defensa distintas:** perímetro/patching en DMZ; segmentación/autenticación de protocolos en IoT/OT.

### 3.2 Superficie de exposición — `md/reto2/instrumentos/2.2 Superficie de exposición.md`

**11 puntos de entrada, 9 sin control de autenticación en su frontera.**

| Punto de entrada | Dominio | Exposición | Hallazgo / pista |
|------------------|---------|-----------|------------------|
| Apache 2.4.49 (80/443) | DMZ | Internet | Banner vulnerable; NSE `http-vuln-cve2021-41773`; faltan CSP, X-Frame-Options, HSTS |
| `/admin` y `/dbadmin` | DMZ | Internet | Sin bloqueo (37 POST/40 s); HTTP Basic sin TLS |
| `/backup`, `/.git`, `/config.php.bak` | DMZ | Internet | Listado de directorios, respaldos y Git accesibles; `phpinfo.php` |
| `/api/v1` (REST verboso) | DMZ | Internet | IDOR (`id=1\|2\|9999`) y fuga de `PDOException` |
| SSH 22 (OpenSSH 8.2p1) | DMZ | Host (sin confirmar) | Sí pide credencial |
| MariaDB 3306 | DMZ | Host (sin confirmar) | `config.php.bak` conecta por 127.0.0.1, pero el puerto se ve en la interfaz de red |
| SMB 445 + RDP 3389 | IT | Interna | SMBv1, message signing disabled, null session, NLA deshabilitada |
| Telnet 23 + panel 8080 | IoT/OT | Interna | `lighttpd 1.4.45` sin TLS; Telnet en texto plano |
| MQTT 1883 + Modbus 502 | IoT/OT | Interna | `CONNECT anonymous`; Modbus sin autenticación |

**Subdominio anotado:** `dev.agrosmart-sumapaz.co` (theHarvester) — entorno de pruebas sin servicio/banner confirmado.

### 3.3 Vectores de ataque — `md/reto2/instrumentos/2.4 Vectores de ataque.md`

**10 vectores** — cada uno es una fila de la matriz 3.1.

| # | Vector | Activo | Precondición | Resultado | Pista |
|---|--------|--------|--------------|-----------|-------|
| 1 | Explotación app web (Apache 2.4.49) | A-01 | Banner vulnerable alcanzable | RCE en DMZ | Nmap/NSE (Sec. 3.2, 3.7a) |
| 2 | Inyección SQL en `productos.php` | A-01 | Parámetro `categoría` sin sanear | Extracción de la BD de pedidos | Error SQL 500 (Sec. 3.3c) |
| 3 | IDOR en la API | A-01 | Endpoint acepta cualquier `id` | Lectura de PII de terceros | `GET /api/v1/usuario?id=…` (Sec. 3.8c) |
| 4 | Falsificación de sesión (JWT `alg:none`) | A-01 | Portal acepta `alg:none` | Forjar cualquier rol | `Set-Cookie: token=…` (Sec. 3.8d) |
| 5 | Robo de credenciales en archivo expuesto | A-01→A-03 | `.bak` y `.git` accesibles | Credencial de BD y DevOps | `config.php.bak`, `.git/config` (Sec. 3.8b-c, 3.12b) |
| 6 | Credenciales por defecto en el gateway | A-05 | Telnet 23 y panel sin MFA | Acceso al gateway → segmento OT | `admin:admin`, `root:12345` (Sec. 3.5, 3.10d) |
| 7 | Phishing / pretexting | A-04 | Correo que imita al proveedor de TI | Credencial de negocio (reutilizable en SMB) | Correo reportado (Sec. 3.4) |
| 8 | Movimiento lateral SMB con sesión nula | A-03 | SMBv1 sin firma + null session | Lectura de shares (`red_credenciales.txt`) | `enum4linux`/`smbclient -N` (Sec. 3.9a-b) |
| 9 | Manipulación de comandos OT vía MQTT/Modbus | A-07/A-08 | Broker anónimo; Modbus sin auth | Apertura no autorizada del riego | `PUBLISH invernadero/riego/cmd` (Sec. 3.6, 3.11) |
| 10 | Componentes cliente desactualizados y TLS débil | A-01 | jQuery 1.7.2, Bootstrap 3.3.7, cert SHA-1 | XSS cliente / interceptación | `whatweb`, `ssl-cert` NSE (Sec. 3.7a) |

### 3.4 Matriz CVE/CVSS — `md/reto2/instrumentos/2.3 Matriz CVE-CVSS.md`

**9 filas: 4 CVE verificados en NVD + 5 CWE sin CVE asignado.**

| Activo | Hallazgo | CVE/referencia | Vector CVSS v3.1 | Punt./Sev. |
|--------|----------|----------------|------------------|------------|
| A-01 Web | Apache 2.4.49 path traversal/RCE | **CVE-2021-41773** | `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` | **9.8 Crítico** |
| A-01 Web | Parche incompleto 2.4.50 (bypass) | **CVE-2021-42013** | idem | **9.8 Crítico** |
| A-03 IT | SMBv1 sin firma | **CVE-2017-0143** (MS17-010) | `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` | **8.8 Alto** |
| A-06 IoT | Cámara Boa antigua (fw 5.2.0) | **CVE-2017-9833** *(disputada)* | `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` | **7.5 Alto** |
| A-01 Web | Error SQL en `productos.php` | **CWE-89** (OWASP A03:2021) | Remoto, sin privilegios | 9.8 Crítico* |
| A-01 Web | API devuelve datos ajenos | **CWE-639** | Cambiar `id` entrega otro registro | 7.5 Alto* |
| A-01 Web | JWT firmado con `alg:none` | **CWE-347** | Portal acepta token sin firma | 8.1 Alto* |
| A-01 Web | Carga de archivos sin validar | **CWE-434** | Acepta cualquier archivo | 8.8 Alto* |
| A-08 IoT/OT | Broker MQTT anónimo | **CWE-306** | Conecta/publica sin credencial | 9.1 Crítico* |

**CVE alternativo de la cámara:** CVE-2022-45956 (5.3 Medio, bypass de autenticación por `HEAD`) — verificable si se inspecciona el firmware.

**Madurez de explotación (para priorizar):** CVE-2021-41773, CVE-2021-42013 y CVE-2017-0143 **están en el catálogo KEV de CISA** (explotación activa). CVE-2017-9833 y CVE-2022-45956 no.

### 3.5 Cyber Kill Chain — `md/reto2/instrumentos/2.6 Cyber Kill Chain.md`

| Fase (Lockheed Martin) | Acción en AgroSmart | Activo | Pista |
|------------------------|---------------------|--------|-------|
| 1. Reconnaissance | OSINT (correo, organigrama, metadatos PDF con `amunoz` y `\\FILESRV01\cotizaciones`) | A-01..A-08 | Sec. 3.4, 3.12 |
| 2. Weaponization | Pretexto "SoporteYa" (dominio parecido, urgencia, autoridad) | A-04 | Sec. 3.4 |
| 3. Delivery | Envío del correo a Contabilidad | A-04 | Sec. 3.4 |
| 4. Exploitation | 37 POST fallidos a `/admin/login.php` + login exitoso | A-01, A-03 | `access.log`; 4625/4624 |
| 5. Installation | Servicio `WinHlp32Svc` desde `C:\Windows\Temp\w.exe` | A-03 | Evento 7045 + Sysmon 1 |
| 6. Command & Control | Conexión saliente al broker | A-08 | Sysmon 3 → `:1883` |
| 7. Actions on Objectives | `PUBLISH invernadero/riego/cmd {"valve":"open"}` | A-07/A-08 | Sec. 3.6, 3.11 |

**Variante técnica** (sin phishing): Nmap → path traversal Apache → `.bak`/`.git` → null session SMB → `PUBLISH` MQTT.

### 3.6 Técnicas MITRE ATT&CK — `md/reto2/instrumentos/2.7 MITRE ATT&CK.md`

**13 técnicas en 7 tácticas** (Enterprise + ICS):

| Táctica | Técnica | Procedimiento | Activo |
|---------|---------|---------------|--------|
| Reconnaissance | **T1595** Active Scanning | `Nmap -sV -sC` + NSE | Toda la red |
| Reconnaissance | **T1589** Gather Victim Identity Info | Metadatos de PDF público | A-01/A-03 |
| Initial Access | **T1566** Phishing | Correo "SoporteYa" | A-04 |
| Initial Access | **T1190** Exploit Public-Facing App | Path traversal Apache 2.4.49 | A-01 |
| Execution | **T1059** Command and Scripting Interpreter | `w.exe -s` creado por `services.exe` | A-03 |
| Persistence | **T1543.003** Windows Service | Servicio `WinHlp32Svc` | A-03 |
| Credential Access | **T1110.001** Password Guessing | 37 POST; `LockoutThreshold 0` | A-01 |
| Credential Access | **T1552.001** Credentials In Files | `config.php.bak`; `red_credenciales.txt` | A-01/A-03 |
| Credential Access | **T1539** Steal Web Session Cookie | Cookie sin `HttpOnly`/`Secure` | A-01 |
| Credential Access | **T1606.001** Forge Web Credentials | JWT con `alg:none` | A-01 |
| Lateral Movement | **T1021.002** SMB/Windows Admin Shares | Sesión nula; shares | A-03 |
| Lateral Movement | **T1210** Exploitation of Remote Services | SMBv1 sin parche (**posible, no observado**) | A-03 |
| Impair Process Control (ICS) | **T0855** Unauthorized Command Message | `PUBLISH {"valve":"open"}` | A-07/A-08 |

> **El hueco del caso:** la única táctica **sin control** es *Impair Process Control* (T0855) — justo la que toca el proceso físico. Es el argumento central para priorizar la defensa IoT/OT.

### 3.7 Ruta probable de ataque (8 saltos) — `md/reto2/instrumentos/2.8 Ruta probable de ataque.md`

| Paso | Salto | Habilitado por | Detección posible (**insumo Reto 3**) |
|------|-------|----------------|----------------------------------------|
| 1 | OSINT (usuario y ruta interna) | Metadatos PDF público | No detectable técnicamente; control de publicación |
| 2 | Phishing a Contabilidad | Correo "SoporteYa" | Filtro de dominio similar + reporte de usuario |
| 3 | Fuerza bruta al login | 37 POST/40 s; `LockoutThreshold 0` | **Alerta por tasa de fallos** en `/admin/login.php` |
| 4 | Inyección SQL | `PDOException` línea 88 | WAF + consultas parametrizadas |
| 5 | Credenciales de `.bak`/`.git` | Archivos sin autenticación | **Escaneo web** de `.bak`/`.git`/listados |
| 6 | Movimiento lateral SMB (null session) | SMBv1 sin firma | Eventos 5140/5145; deshabilitar null session |
| 7 | Persistencia `WinHlp32Svc` | Evento 7045 + Sysmon 1 | **Alerta ante cualquier 7045** |
| 8 | C&C y `PUBLISH` en MQTT | Sysmon 3 → `:1883`; `CONNECT anonymous` | **Detección prioritaria:** publicación anónima en tópicos de comando |

**Punto de no retorno:** el paso 6 (cruce DMZ→IT). Todo control ubicado **antes** del paso 6 vale más que cualquiera posterior.

### 3.8 Impacto y riesgo — `md/reto2/instrumentos/2.9 Impacto y riesgo.md`

Escala P e I de 1-5, riesgo = P×I.

| Escenario | P | I | Riesgo | Tipo |
|-----------|---|---|--------|------|
| Apertura no autorizada del riego (MQTT/PLC) | 4 | 5 | **20** | **OT/físico** |
| Compromiso del portal y robo de pedidos | 5 | 4 | **20** | Negocio/Datos |
| Movimiento lateral al dominio AGROSMART | 4 | 4 | **16** | Datos |
| Escalada de privilegios vía JWT `alg:none` | 4 | 4 | **16** | Negocio/Datos |
| Robo de credenciales reutilizadas en IT | 4 | 3 | **12** | Datos |
| DoS sobre el broker MQTT | 3 | 3 | **9** | OT/físico |

**Recomendación de prioridad ya esbozada (base directa para el Reto 3):**

| Prioridad | Acción | Riesgo que reduce |
|-----------|--------|-------------------|
| 1 | Autenticar MQTT y PLC; segmentar TI↔OT | 20 (OT) y 9 |
| 2 | Corregir verificación de firma JWT | 16 |
| 3 | Retirar `.bak`/`.git`/listados; rotar credenciales | 12 y 16 |
| 4 | Deshabilitar SMBv1 y null session; activar firma | 16 |
| 5 | Parchear Apache a 2.4.51+; corregir SQLi/IDOR | 20 (negocio) |
| 6 | Bloqueo de intentos y cookies `HttpOnly`/`Secure` | 20 (negocio) |

### 3.9 Ingeniería social — `md/reto2/instrumentos/2.5 Ingeniería social.md`

4 técnicas (phishing, pretexting, spearphishing con OSINT, watering hole). **3 palancas:** autoridad, urgencia, familiaridad. Mitigación **procedimental** (canal alterno de verificación; no pedir contraseñas por correo) + concientización. Señales de alerta: dominio parecido, urgencia+autoridad, solicitud de credenciales, remitente dado de baja, rutas internas en mensaje externo, credencial en paste público.

---

## 4. Marco técnico defensivo que el Reto 3 debe usar

La Guía (págs. 2, 4-5) y el Anexo 1 (pág. 32) exigen alinear los controles con **marcos de referencia**:

| Marco | Uso en el Reto 3 |
|-------|------------------|
| **CIS Controls** | Base de los controles (p. ej. CIS 16 = Application Software Security) |
| **NIST CSF** | Organizar por Identificar/Proteger/Detectar/Responder/Recuperar |
| **NIST SP 800-61** | Playbook de respuesta a incidentes (instrumento 3.5) |
| **ISO/IEC 27001** | Marco de gestión |
| **OWASP** (ASVS/WSTG/Top 10) | Controles de aplicación web (SQLi = A03:2021, credenciales = A05) |
| **MITRE ATT&CK** | Trazar control ↔ técnica adversaria (ya mapeado en `2.7`) |

Tecnologías nombradas por la guía: **SIEM/XDR, hardening, DevSecOps, seguridad IoT/OT, gestión de vulnerabilidades, respuesta a incidentes**.

> ⚠️ **Brecha detectada en la auditoría:** los referentes bibliográficos del curso son **ofensivos** (pentest, SQLMAP, WiFi, phishing). Los marcos defensivos (CIS, NIST CSF, NIST SP 800-61, ISO 27001) **no vienen entre los materiales**; hay que aportarlos como fuentes complementarias. Ver `md/reto2/fuentes/Referencias y lectura.md` sección C y `REVISION_RETO3.md`.

---

## 5. Índice del paquete `md/reto2/`

### 5.1 Fuentes normativas y del caso

| Archivo | Qué es |
|---------|--------|
| `md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md` | **Documento maestro** (48 págs). Caso + 13 artefactos + fichas Retos 2-5. **Reto 3 en pp. 32-35.** |
| `md/reto2/fuentes/Guía de aprendizaje - Reto 2.md` | Guía del Reto 2 (6 págs, 9 pasos) |
| `md/reto2/fuentes/Guion del video.md` | Guion del entregable del Reto 2 (discurso, 22 diapositivas) — contexto argumentativo |
| `md/reto2/fuentes/Referencias y lectura.md` | Referentes del Reto 2 (APA 7) + herramientas + erratas |
| `md/actividad/Guía de aprendizaje - Reto 3.md` | Guía del Reto 3 (ya en el corpus de `resources/`) |
| `md/rubrica/Rúbrica de evaluación - Reto 3.md` | Rúbrica del Reto 3 |

### 5.2 Instrumentos del Reto 2 (los insumos directos)

| Archivo | Contenido |
|---------|-----------|
| `1.1 Núcleo conceptual.md` | Metodologías, fases del testing, ROE, superficie, pensamiento adversarial |
| `1.B Comparación de metodologías.md` | Comparación de marcos de pentesting |
| `1.C Glosario operativo.md` | 10 definiciones |
| `2.1 Activos críticos C-I-D.md` | Los 8 activos valorados |
| `2.2 Superficie de exposición.md` | 11 puntos, 3 fronteras |
| `2.3 Matriz CVE-CVSS.md` | 4 CVE + 5 CWE con CVSS v3.1 |
| `2.4 Vectores de ataque.md` | Los 10 vectores |
| `2.5 Ingeniería social.md` | 4 técnicas + señales de alerta |
| `2.6 Cyber Kill Chain.md` | 7 fases + variante |
| `2.7 MITRE ATT&CK.md` | 13 técnicas |
| `2.8 Ruta probable de ataque.md` | 8 saltos + diagrama |
| `2.9 Impacto y riesgo.md` | 6 escenarios P×I |
| `3.13 Tabla maestra de pistas.md` | Pistas → investigación (plantilla del Anexo) |
| `Declaracion uso de IA.md` | Modelo de declaración de IA |

### 5.3 Contexto del Reto 2

| Archivo | Contenido |
|---------|-----------|
| `Contexto y arquitectura.md` | AgroSmart: 3 dominios, 3 fronteras, diagrama |
| `Marco legal y ROE.md` | Leyes, in/out-of-scope, regla de oro |
| `Rúbrica de evaluación.md` | Rúbrica del Reto 2 (para contraste) |
| `Qué me piden y qué tengo que entregar.md` | Mapa requisito → ubicación |
| `Glosario.md` | Glosario ampliado |
| `Review - verificación paso a paso.md` | Verificación del Reto 2 contra la guía |
| `Contexto de la guía de aprendizaje.md` | Notas de la guía |
| `Prompt de verificación integral.md` | Prompt de auditoría usado |

---

## 6. Trazabilidad sugerida: vector del Reto 2 → dónde se defiende en el Reto 3

> **Punto de partida para la matriz 3.1.** Cada fila enlaza un vector con la sección del informe donde debe tener su control. El contenido de los controles se redacta en la siguiente etapa.

| Vector (Reto 2) | Activo | Técnica MITRE | Sección del informe (Reto 3) | Dominio |
|-----------------|--------|---------------|------------------------------|---------|
| 1 · Explotación Apache 2.4.49 | A-01 | T1190 | sección 5 Hardening Web/LAMP + sección 5 controles app | DMZ |
| 2 · Inyección SQL | A-01 | T1190 | sección 5 controles app web (DevSecOps/SAST) | DMZ |
| 3 · IDOR en API | A-01 | — | sección 5 control de acceso a la API | DMZ |
| 4 · JWT `alg:none` | A-01 | T1606.001 | sección 5 autenticación y sesiones | DMZ |
| 5 · Credenciales expuestas (`.bak`/`.git`) | A-01→A-03 | T1552.001 | sección 5 directorios/backups + gestión de secretos | DMZ/IT |
| 6 · Credenciales por defecto en gateway | A-05 | T1078 (por defecto) | sección 9 controles IoT/OT | IoT/OT |
| 7 · Phishing/pretexting | A-04 | T1566 | sección 5 controles organizativos + sección 6 monitoreo de correo | IT |
| 8 · Movimiento lateral SMB null session | A-03 | T1021.002 | sección 8 controles IT (SMBv1, firma, null session) | IT |
| 9 · Manipulación OT vía MQTT/Modbus | A-07/A-08 | T0855 | sección 6 (prioridad) sección 9 MQTT/Modbus + segmentación | IoT/OT |
| 10 · Cliente desactualizado y TLS débil | A-01 | T1557 (AitM) | sección 5 hardening TLS + gestión de dependencias | DMZ |

**Causas transversales** (aplican a varios vectores): falta de segmentación (F2/F3), ausencia de bloqueo por intentos, credenciales reutilizadas, ausencia de monitoreo en fuentes clave.

---

## 7. Estado y limitaciones de este paquete

- **Fuente:** vault `Obsidian/Brain/Test 2` (enlace `Test 2/Vault Obsidian - Test 2`).
- **Conversión:** Anexo 1 y Guía Reto 2 con `md/_convert.py` (PyMuPDF + pdfplumber + OCR). Los instrumentos 2.x se copiaron tal cual (ya eran Markdown de calidad, autoría del propio estudiante).
- **Fidelidad:** texto íntegro; en el Anexo 1 las **tablas** quedan con celdas fragmentadas por el diseño de 2 columnas del PDF (el contenido textual está completo; no hay pérdida de datos). Páginas 31 y 36 del Anexo requirieron OCR.
- **Lo que NO contiene este paquete:** el video MP4 ni el `.pptx` del Reto 2 (binarios); el Anexo A (blueprint del Cyber Range, para el Reto 5).
- **Verificado contra:** `REVISION_RETO3.md` (auditoría del Reto 3) — el "Anexo 1 faltante" que allí figura como crítico **existe** y queda incorporado aquí.

---

*Paquete de contexto generado para la elaboración del informe técnico del Reto 3. Próxima etapa: construir la matriz de trazabilidad 3.1 y el esqueleto del informe.*
