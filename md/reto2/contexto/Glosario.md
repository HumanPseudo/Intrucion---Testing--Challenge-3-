---
tags: [glosario, referencia]
---

# Glosario — hover de referencia

> Esta nota no es un entregable: es un diccionario para el vault. Pasa el mouse sobre
> cualquier término enlazado en las notas (`[[Glosario#PTES|PTES]]`, por ejemplo) y
> Obsidian te muestra aquí abajo la definición, sin salir de donde estás.
>
> Las **10 definiciones oficiales** que pide la Guía (Instrumento 1.C) están en
> [[02 - Instrumentos Reto 2/1.C Glosario operativo|1.C Glosario operativo]]; esta nota
> las incluye igual, más los términos técnicos y siglas que aparecen sueltos en el resto
> del vault.

## Metodologías

## PTES
**Penetration Testing Execution Standard.** Metodología operativa de pentesting: *Pre-Engagement, Intelligence Gathering, Threat Modeling, Vulnerability Analysis, Exploitation, Post-Exploitation, Reporting*. Describe comandos concretos, no solo fases — es la que mejor explica cómo se ejecutó el reconocimiento del caso (Sec. 3.2, 3.9).

## OWASP WSTG
**OWASP Web Security Testing Guide.** Guía de pruebas específica para aplicaciones web. Cubre solo el portal (A-01/A-02); no dice nada de red, Windows ni IoT/OT. Es la que explica por qué el SQLi, el IDOR y el JWT `alg:none` son fallos de la aplicación, no del servidor.

## OSSTMM
**Open Source Security Testing Methodology Manual.** Marco de medición de la seguridad operativa con métricas cuantificables, no solo narrativas. Es la única de las cuatro metodologías del caso que exige umbrales numéricos — útil para justificar prioridades con un número, como en [[02 - Instrumentos Reto 2/2.9 Impacto y riesgo]].

## NIST SP 800-115
**Technical Guide to Information Security Testing and Assessment.** Guía neutral del NIST, con cuatro fases: *Planning, Discovery, Attack, Reporting*. Publicada en **2008**. Es el marco de referencia del caso completo: separa lo autorizado de lo ejecutado y le da lenguaje al ROE.

## Marcos y modelos

## Cyber Kill Chain
**CKC.** Modelo de Lockheed Martin de 7 fases que ordena un compromiso en secuencia: *Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives*. Sirve para ver qué fase falta y dónde cortar el ataque. Ver [[02 - Instrumentos Reto 2/2.6 Cyber Kill Chain]].

## MITRE ATT&CK
Catálogo público de tácticas y técnicas de adversario, con identificadores estables (`Txxxx`). A diferencia de la CKC, no propone una secuencia: cataloga qué se puede hacer en cada táctica. Tiene una matriz **Enterprise** (IT) y otra **ICS** (control industrial) — el caso usa las dos. Ver [[02 - Instrumentos Reto 2/2.7 MITRE ATT&CK]].

## ROE
**Rules of Engagement / Reglas de compromiso.** El documento que define qué está autorizado (in-scope), qué no (out-of-scope), qué técnicas se permiten y cuál es el criterio de parada de emergencia. En este caso: [[00 - Contexto/Marco legal y ROE]].

## Vulnerabilidades

## CVE
**Common Vulnerabilities and Exposures.** Identificador único (`CVE-AAAA-NNNNN`) para una vulnerabilidad concreta en un producto y versión específicos, catalogada en [nvd.nist.gov](https://nvd.nist.gov/). Se diferencia del CWE: el CVE es la instancia, el CWE es el tipo de defecto.

## CVSS
**Common Vulnerability Scoring System.** Escala de 0 a 10 que mide la severidad **técnica** de una vulnerabilidad — no si será explotada. Sus métricas incluyen *Attack Complexity*, *Privileges Required* y *User Interaction*; un vector `AC:L/PR:N/UI:N` suele acompañar puntajes altos (9.x).

## CWE
**Common Weakness Enumeration.** Taxonomía de **tipos** de debilidad de software (ej. `CWE-89` inyección SQL), distinta del CVE. Se usa cuando el hallazgo es real pero no hay un CVE asignado a ese producto — el caso marca esas filas con asterisco en [[02 - Instrumentos Reto 2/2.3 Matriz CVE-CVSS]].

## CISA KEV
**Known Exploited Vulnerabilities catalog**, de la Cybersecurity and Infrastructure Security Agency (EE. UU.). Lista de CVE con **explotación activa confirmada** en el mundo real — no es lo mismo que "tiene un exploit publicado" (eso es Exploit-DB). Que un CVE esté en KEV es la evidencia más fuerte de madurez de explotación.

## Exploit-DB
**Exploit Database** (exploit-db.com), mantenida por OffSec. Archivo público de exploits y pruebas de concepto (PoC). Que un CVE tenga una entrada aquí no prueba que se haya usado contra un objetivo real, solo que existe una PoC pública.

## PoC
**Proof of Concept.** Código o procedimiento que demuestra que una vulnerabilidad es explotable, sin necesariamente ser un exploit "listo para producción". Se usa para evaluar madurez/explotabilidad, no como plan de ataque.

## Superficie de ataque
Conjunto de puntos por los que un atacante puede entrar o moverse: puertos, rutas web, protocolos, interfaces. En AgroSmart no es solo "lo que está abierto", sino **lo que está abierto sin control de autenticación en su frontera**. Ver [[02 - Instrumentos Reto 2/2.2 Superficie de exposición]].

## Vector de ataque
Mecanismo concreto que convierte una debilidad en un resultado para el atacante. Se diferencia de la vulnerabilidad: la vulnerabilidad es el defecto, el vector es el camino para usarla. Ver [[02 - Instrumentos Reto 2/2.4 Vectores de ataque]].

## Frontera de confianza
Línea donde cambia el nivel de garantía entre dos segmentos de red. Cruzarla sin control de autenticación convierte un acceso legítimo en un acceso de atacante — es el hallazgo central de [[02 - Instrumentos Reto 2/2.2 Superficie de exposición]].

## Escalada de privilegios
Cualquier transición que da a un atacante **más permisos de los que tenía**. Distinta según el mecanismo: una vulnerabilidad sin parchear (ej. `T1210`) y una credencial forjada (ej. `T1606.001`) son técnicas y controles distintos, aunque el efecto se parezca.

## Riesgo = P × I
Modelo de dos factores para priorizar remediación: **probabilidad** de que el escenario ocurra × **impacto** si ocurre. Deliberadamente simple — pierde precisión, gana comunicabilidad. La probabilidad **no** se hereda del CVSS: mide si el escenario se materializa en *esta* organización, no la gravedad técnica del fallo. Ver [[02 - Instrumentos Reto 2/2.9 Impacto y riesgo]].

## Fallos de aplicación web

## IDOR
**Insecure Direct Object Reference.** El sistema entrega un recurso (registro, archivo) confiando en un identificador que el usuario controla, sin validar que tenga permiso sobre él. En el caso: cambiar `id=1` por `id=2` en `/api/v1/usuario` devuelve datos de otro usuario.

## XSS
**Cross-Site Scripting.** Inyección de script en una página que otros usuarios visitan, normalmente porque el sitio no sanea la entrada o usa componentes de cliente desactualizados (`jQuery`, `Bootstrap` antiguos, como en el vector 10 del caso).

## JWT
**JSON Web Token.** Token de sesión firmado, compuesto de cabecera, cuerpo y firma. Si el servidor acepta `"alg":"none"` (sin firma), cualquiera puede reescribir el cuerpo del token sin que el servidor lo detecte — es el fallo central del vector 4 del caso.

## Redes y protocolos

## DMZ
**Zona Desmilitarizada.** Segmento de red expuesto a Internet, aislado de la red interna por un firewall. En AgroSmart aloja el portal web (A-01) y el gestor de base de datos (A-02).

## SMB
**Server Message Block.** Protocolo de Windows para compartir archivos e impresoras. La versión 1 (SMBv1) tiene vulnerabilidades críticas históricas (familia EternalBlue/MS17-010) y, en el caso, además permite sesión nula (acceso sin credencial a los recursos compartidos).

## RDP
**Remote Desktop Protocol.** Protocolo de escritorio remoto de Windows. Sin NLA (Network Level Authentication) habilitado, expone más superficie de ataque antes de pedir credencial.

## NLA
**Network Level Authentication.** Exige autenticación **antes** de establecer la sesión gráfica de RDP. Si está deshabilitada (como en A-04), un atacante llega más lejos en el protocolo sin credencial válida.

## MQTT
Protocolo de mensajería publicar/suscribir usado en IoT. Si acepta `CONNECT anonymous` (como el broker A-08 del caso), cualquiera puede leer telemetría o publicar comandos sin autenticarse.

## Modbus
Protocolo de comunicación industrial (OT) para leer y escribir registros en controladores (PLC). No tiene autenticación nativa: quien alcanza el puerto 502 puede leer o **escribir** registros, como el PLC de riego (A-07) del caso.

## TLS
**Transport Layer Security** (sucesor de SSL). Cifra el tráfico en tránsito. Su ausencia, o un certificado autofirmado/expirado/con SHA-1, permite interceptar credenciales en claro (MITRE: *Adversary-in-the-Middle*).

## Personas y datos

## OSINT
**Open Source Intelligence.** Información obtenida de fuentes públicas (redes sociales, metadatos de documentos, ofertas de empleo, registros DNS) sin tocar ningún sistema. En el caso: metadatos de un PDF revelan un usuario y una ruta interna antes de enviar el primer correo de phishing.

## Ingeniería social
Uso de la persuasión, la autoridad o el contexto para que una persona entregue algo que un atacante no podría tomar técnicamente. Se analiza como **debilidad de proceso**, nunca como atributo del individuo. Ver [[02 - Instrumentos Reto 2/2.5 Ingeniería social]].

## PII
**Personally Identifiable Information** / datos personales. En Colombia, su manejo está regulado por la Ley 1581 de 2012 (habeas data) — exige confidencialidad y minimización, no solo en el sistema, también en cómo se documenta el hallazgo.

## Herramientas y artefactos de log

## Sysmon
**System Monitor** (Sysinfo/Microsoft). Herramienta de logging extendido de Windows que registra creación de procesos, conexiones de red y más detalle que el log de seguridad estándar. En el caso, Sysmon 1 y Sysmon 3 son la evidencia que conecta la persistencia (evento 7045) con la conexión al broker MQTT.

---

Relaciona: [[02 - Instrumentos Reto 2/1.C Glosario operativo]] · [[00 - Contexto/Review - verificación paso a paso]] · [[index]]
