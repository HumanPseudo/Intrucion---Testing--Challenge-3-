<!-- Archivo original: Anexo 1 Caso AgroSmart del Sumapaz.pdf -->
<!-- Paginas: 48 -->
<!-- Metodo de extraccion: PyMuPDF (texto ordenado) + pdfplumber (tablas) + OCR tesseract spa+eng (paginas imagen) -->
<!-- ADVERTENCIAS DE CALIDAD: Paginas sin capa de texto util (requirieron OCR): [31, 36] -->
<!-- DOCUMENTO MAESTRO DEL CURSO. Contiene el caso AgroSmart, los 13 artefactos y las fichas de los Retos 2-5. La seccion del RETO 3 esta en pp. 32-35. -->


---

### [p. 1]

RETO INTEGRADOR DE INTRUSIÓN Y TESTING
Caso de estudio: AgroSmart del Sumapaz S.A.S.
Un ecosistema híbrido IT · IoT/OT
Propósito del documento 
Este documento es el insumo único y autocontenido que articula los retos del 
curso (Retos 2 al 5) en torno a un mismo escenario de compromiso. 
 
El estudiante asume el rol de pentester ético y, a partir de las pistas, artefactos 
de reconocimiento, informe OSINT, inventarios y logevidencias que aquí se 
entregan, debe investigar de forma autónoma fuentes públicas (NVD/CVE, 
Exploit-DB, MITRE ATT&CK, Cyber Kill Chain) y metodologías de pruebas de 
penetración éticas.  
 
No se requiere disponer de una máquina virtual para los retos 2, 3 y 4, todos 
los insumos para razonar el reto están provistos. La validación práctica 
controlada se realiza en el Reto 5 sobre el Cyber Range descrito en el Anexo 
A (blueprint del entorno objetivo). 
 
 
Recurso educativo diseñado por:  
Profesor Luis Fernando Zambrano Hernández, con apoyo de la inteligencia 
artificial Claude (Anthropic).  
Curso Intrusión y Testing — Maestría en Ciberseguridad, ECBTI–UNAD

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 2]

Cómo leer y usar este documento
El reto integrador está diseñado bajo la estrategia de Aprendizaje Basado en 
Retos articulada con el modelo de aprendizaje experiencial de Kolb. Cada reto 
corresponde a una fase del ciclo y se construye sobre el anterior: lo que usted 
analiza en el Reto 2 alimenta el diseño defensivo del Reto 3, y ambos orientan 
la planificación del Reto 4 y la ejecución controlada del Reto 5. Por eso el caso 
es uno solo.
Reto 
Fase de Kolb 
Lo que usted produce 
Evidencia 
Reto 
1 
Experiencia 
concreta
Apropiación 
conceptual: 
metodologías, 
fases, 
alcance, 
reglas de compromiso, superficie 
de 
ataque 
y 
pensamiento 
adversarial.
Reto 
2 
Observación 
reflexiva
Análisis del escenario ofensivo: 
activos 
críticos, 
superficies, 
vectores, 
ingeniería 
social, 
vulnerabilidades 
(CVE/CVSS), 
rutas de ataque, impacto.
Reto 
3 
Conceptualización 
abstracta
Diseño 
defensivo: 
controles 
preventivos/detectivos, 
hardening, monitoreo, reglas de 
detección y respuesta, trazables a 
los vectores del Reto 2.
Reto 
4 
Conceptualización 
abstracta 
aplicada
Planificación del compromiso y 
emulación adversaria: alcance y 
ROE, mapeo ATT&CK, validación 
documental de los controles del 
Reto 3, métricas de postura y 
brechas de detección.
Reto 
5 
Experimentación 
activa
Ejecución ética en Cyber Range: 
ROE, reconocimiento, validación 
controlada, evidencias, severidad 
y mitigación.
Convenciones del documento.
Las cajas con fondo naranja son la Declaración de uso de IA (omita estas si 
no uso esta tecnología).
Las tablas con filas en blanco son instrumentos para diligenciar. Los bloques 
en negro simulan salidas de consola o artefactos de reconocimiento.
Cuestionario 
tipo 
POC resuelto
Video 
académico/técnico
Informe técnico de 
diseño defensivo
Informe técnico de 
planificación 
y 
emulación 
adversaria
Informe 
técnico 
final de intrusión

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Reto |  |  | Fase de Kolb |  |  | Lo que usted produce |  |  | Evidencia |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reto 1 |  |  | Experiencia concreta |  |  | Apropiación conceptual: metodologías, fases, alcance, reglas de compromiso, superficie de ataque y pensamiento adversarial. |  |  | Cuestionario tipo POC resuelto |  |  |
| Reto 2 |  |  | Observación reflexiva |  |  | Análisis del escenario ofensivo: activos críticos, superficies, vectores, ingeniería social, vulnerabilidades (CVE/CVSS), rutas de ataque, impacto. |  |  | Video académico/técnico |  |  |
| Reto 3 |  |  | Conceptualización abstracta |  |  | Diseño defensivo: controles preventivos/detectivos, hardening, monitoreo, reglas de detección y respuesta, trazables a los vectores del Reto 2. |  |  | Informe técnico de diseño defensivo |  |  |
| Reto 4 |  |  | Conceptualización abstracta aplicada |  |  | Planificación del compromiso y emulación adversaria: alcance y ROE, mapeo ATT&CK, validación documental de los controles del Reto 3, métricas de postura y brechas de detección. |  |  | Informe técnico de planificación y emulación adversaria |  |  |
| Reto 5 |  |  | Experimentación activa |  |  | Ejecución ética en Cyber Range: ROE, reconocimiento, validación controlada, evidencias, severidad y mitigación. |  |  | Informe técnico final de intrusión |  |  |

---

### [p. 3]

Las cajas azules contienen contexto o reglas. Los identificadores CVE, técnicas 
MITRE (Txxxx) y referencias son pistas a investigar: el documento no entrega 
la respuesta resuelta, entrega el rastro.
La abreviatura “Sec. X” (p. ej. Sec. 3.2) es una referencia cruzada a la sección 
X de este mismo documento, para que usted ubique rápidamente el artefacto 
o la pista mencionada.
Principio rector 
Pensamiento adversarial ético
Pensar como el atacante, actuar como el defensor. Todo análisis ofensivo de 
este reto tiene como finalidad anticipar el compromiso y fortalecer la postura 
de seguridad de la organización. La ejecución práctica solo ocurre dentro del 
Cyber Range autorizado del Reto 5, jamás sobre sistemas reales o de terceros

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 4]

Contenido
Cómo leer y usar este documento ........................................................... 2
1. Marco ético-legal y reglas de compromiso (ROE) .................................. 7
1.1 Marco legal aplicable (Colombia) .................................................... 7
1.2 Reglas de compromiso (Rules of Engagement) del caso ..................... 7
Instrumento 1.A — Acta de reglas de compromiso (para diligenciar en Reto 
4 — Planificación) ............................................................................ 8
2. El caso: AgroSmart del Sumapaz S.A.S. .............................................. 9
2.1 Contexto organizacional ................................................................ 9
2.2 Arquitectura del ecosistema (tres dominios) ..................................... 9
3. Informe de insumos (artefactos para analizar).................................... 11
3.1 Inventario de activos (entregado) ................................................. 11
3.2 Reconocimiento de red (salida simulada de escaneo) ...................... 11
3.3 Artefactos de la aplicación web (Portal AgroSmart LAMP) ................. 12
3.4 Informe OSINT e ingeniería social ................................................. 13
3.5 Inventario IoT/OT (firmware y exposición) ..................................... 14
3.6 Extractos de logs (correlación) ..................................................... 14
3.7 Reconocimiento web profundo (artefactos ampliados) ..................... 15
a) Escaneo Nmap con scripts de vulnerabilidad (NSE) ........................ 15
b) Fuerza bruta de directorios (gobuster).......................................... 15
c) Identificación de tecnologías (whatweb) y robots.txt completo ......... 15
3.8 Hallazgos sensibles en el servidor web .......................................... 16
a) Listado del directorio /backup/ .................................................... 16
b) Contenido de config.php.bak (copia de respaldo expuesta) ............. 16
c) Repositorio Git expuesto y endpoint de API verboso ....................... 17
d) Token de sesión emitido por el portal (JWT) .................................. 17
3.9 Enumeración del segmento IT / Windows ...................................... 17
a) Descubrimiento de sistema y comparticiones (SMB) ....................... 17
b) Exploración de un recurso accesible sin credenciales ...................... 18
c) Política de contraseñas y escritorio remoto .................................... 18
d) Eventos de Windows correlacionables (Sysmon/Security) ............... 18
3.10 Telemetría e industrial: IoT / OT en profundidad ........................... 19
a) Volcado de tópicos del broker MQTT (telemetría y comandos) ......... 19
b) Lectura del controlador de riego por Modbus/TCP .......................... 19

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 5]

c) Cámara IP (servidor Boa) y prueba de acceso ................................ 19
d) Telnet del gateway y cadenas del firmware ................................... 19
3.11 Captura de tráfico de red (protocolos en claro) ............................. 20
3.12 OSINT e inteligencia de fuentes abiertas (ampliado) ...................... 20
a) Recolección de correos y hosts (theHarvester) ............................... 20
b) Banner público tipo motor de búsqueda de dispositivos (Shodan-like) y 
fuga en paste ................................................................................ 21
c) Metadatos de documentos públicos (exiftool) ................................. 21
3.13 Tabla maestra de pistas → investigación ...................................... 21
RETO 2:  Análisis de vectores de ataque, ingeniería social y escenarios de 
compromiso ....................................................................................... 23
1.1 Núcleo conceptual....................................................................... 23
Instrumento 1.B — Comparación de metodologías (para diligenciar) .... 24
Instrumento 1.C — Glosario operativo (plantee 10 definicones de 
conceptos que considere importantes) .............................................. 24
Análisis de vectores de ataque, ingeniería social y escenarios de compromiso
 ........................................................................................................ 26
2.1 Identificación y valoración de activos críticos ................................. 26
2.2 Superficie de exposición .............................................................. 26
2.3 Matriz de vulnerabilidades (CVE / CVSS) ....................................... 26
2.4 Vectores de ataque ..................................................................... 28
2.5 Análisis de ingeniería social .......................................................... 28
2.6 Mapeo a Cyber Kill Chain ............................................................. 28
2.7 Mapeo a MITRE ATT&CK .............................................................. 29
2.8 Ruta probable de ataque (attack path) .......................................... 29
2.9 Impacto y riesgo ........................................................................ 29
Guion sugerido para el video (evidencia del Reto 2) ........................... 30
RETO 3 — Diseño de detección, defensa y fortalecimiento de la postura .... 32
3.1 Matriz de trazabilidad vector → control .......................................... 32
3.2 Hardening por dominio (checklist para diligenciar) .......................... 32
a) Web / LAMP .............................................................................. 32
b) IT / Windows............................................................................. 33
c) IoT / OT .................................................................................... 33
3.3 Reglas de detección .................................................................... 34
3.4 Plan de monitoreo y alertamiento ................................................. 34

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 6]

3.5 Procedimiento básico de respuesta (NIST SP 800-61) ..................... 34
RETO 5 — Ejecución de pruebas de intrusión en Cyber Range .................. 46
• 
Valor: 125 puntos. ..................................................................... 46
5.1 Estructura del informe final (plantilla) ........................................... 46
5.2 Plantilla de ejecución por fase (para diligenciar) ............................. 46
5.3 Bitácora de evidencias ................................................................. 47
5.4 Matriz de hallazgos y priorización del riesgo ................................... 47

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 7]

1. Marco ético-legal y reglas de compromiso (ROE)
Antes de cualquier análisis técnico, el pentester ético delimita el alcance 
autorizado y firma las reglas de compromiso. En este reto académico usted 
opera siempre dentro de un entorno simulado; aun así debe razonar y 
documentar el encuadre ético y legal como lo haría en un compromiso 
profesional real.
1.1 Marco legal aplicable (Colombia)
Norma 
Qué regula 
Relevancia para el
pentester 
Ley 1273 de 2009 
Delitos informáticos: acceso 
abusivo a sistema (art. 269A), 
interceptación, 
daño 
informático, uso de software 
malicioso, violación de datos 
personales.
El acceso, la interceptación 
o 
la 
afectación 
SIN 
autorización son delito. La 
autorización escrita y el 
alcance acotado son lo que 
separa el pentest de la 
conducta delictiva. 
Ley 1581 de 2012 
Protección 
de 
datos 
personales (habeas data).
El 
manejo 
de 
datos 
hallados 
(correos, 
credenciales, 
PII) 
exige 
confidencialidad 
y 
minimización. 
Ley 1341 de 2009 
Marco de las TIC. 
Encuadre 
sectorial 
de 
servicios y operadores. 
Contrato/Autorización Mandato 
del 
cliente 
y 
consentimiento informado.
Define 
qué 
activos, 
ventanas 
de 
tiempo, 
técnicas 
permitidas 
y 
exclusiones aplican.
1.2 Reglas de compromiso (Rules of Engagement) del caso
Autorización simulada: AgroSmart del Sumapaz S.A.S. 
AgroSmart del Sumapaz S.A.S. (“el cliente”) autoriza al estudiante-pentester 
a ejecutar, exclusivamente dentro del Cyber Range provisto por el curso, 
actividades de reconocimiento, enumeración, identificación y validación 
controlada de vulnerabilidades sobre los activos descritos en el Anexo A. 
 
Alcance autorizado (in-scope): segmento DMZ (portal web LAMP), 
segmento corporativo IT y segmento IoT/OT del laboratorio.

> [Imagen(es) en la pagina: 1 | xref162 2028x222px]

**Tabla detectada (formato Markdown):**

| Norma | Qué regula |  | Relevancia para el |  |
| --- | --- | --- | --- | --- |
|  |  |  | pentester |  |
| Ley 1273 de 2009 | Delitos informáticos: acceso abusivo a sistema (art. 269A), interceptación, daño informático, uso de software malicioso, violación de datos personales. | El acceso, la interceptación o la afectación SIN autorización son delito. La autorización escrita y el alcance acotado son lo que separa el pentest de la conducta delictiva. |  |  |
| Ley 1581 de 2012 | Protección de datos personales (habeas data). | El manejo de datos hallados (correos, credenciales, PII) exige confidencialidad y minimización. |  |  |
| Ley 1341 de 2009 | Marco de las TIC. | Encuadre sectorial de servicios y operadores. |  |  |
| Contrato/Autorización | Mandato del cliente y consentimiento informado. | Define qué activos, ventanas de tiempo, técnicas permitidas y exclusiones aplican. |  |  |

---

### [p. 8]

Fuera de alcance (out-of-scope): cualquier IP, dominio, persona o servicio 
real ajeno al laboratorio; ataques de denegación de servicio destructivos; 
exfiltración real de datos; ingeniería social ejecutada sobre personas reales 
(solo se analiza y simula). 
 
Técnicas permitidas: escaneo, enumeración, fuzzing controlado, validación 
de vulnerabilidades con herramientas estándar (Nmap, Nikto, Burp Suite, 
SQLMap, Metasploit en módulos autorizados) dentro del rango. 
Regla de oro: si no está explícitamente dentro del alcance, está fuera. Ante la 
duda, no se ejecuta.
Instrumento 1.A — Acta de reglas de compromiso (para diligenciar 
en Reto 4 — Planificación)
Elemento de la ROE1 
Definición acordada por el estudiante 
Objetivos del compromiso 
  
Activos 
en 
alcance 
(IP/host/servicio)
Activos excluidos 
  
Ventana de ejecución 
  
Técnicas prohibidas 
  
Manejo 
y 
custodia 
de 
evidencias
Contacto de escalamiento 
ante incidente
Criterio 
de 
“parada 
de 
emergencia”
1 Reglas de Compromiso

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Elemento de la ROE1 |  |  | Definición acordada por el estudiante |  |
| --- | --- | --- | --- | --- | --- |
| Objetivos del compromiso |  |  |  |  |  |
| Activos en alcance (IP/host/servicio) |  |  |  |  |  |
| Activos excluidos |  |  |  |  |  |
| Ventana de ejecución |  |  |  |  |  |
| Técnicas prohibidas |  |  |  |  |  |
| Manejo y custodia de evidencias |  |  |  |  |  |
| Contacto de escalamiento ante incidente |  |  |  |  |  |
| Criterio de “parada de emergencia” |  |  |  |  |  |

---

### [p. 9]

2. El caso: AgroSmart del Sumapaz S.A.S.
2.1 Contexto organizacional
AgroSmart del Sumapaz S.A.S. es una empresa agroindustrial mediana 
ubicada en la región del Sumapaz (Cundinamarca). Produce y comercializa 
hortalizas y frutales bajo un modelo de agricultura inteligente: invernaderos 
instrumentados con sensores, riego automatizado y cámaras de vigilancia, 
integrados a una plataforma web que permite a clientes mayoristas hacer 
pedidos y a los agrónomos monitorear los cultivos en tiempo real. En los 
últimos meses la empresa creció rápido, conectó dispositivos IoT comprados 
a distintos proveedores y publicó su portal en internet sin una revisión de 
seguridad formal.
La gerencia, tras un susto con un correo sospechoso recibido por el área 
contable y una alerta de su proveedor de internet, contrató una evaluación de 
seguridad ofensiva. Usted es el analista asignado. Su misión: pensar como un 
adversario para anticipar cómo podría ser comprometida AgroSmart y, con 
ello, recomendar cómo blindarla.
Lo que la gerencia le dijo (literal)
“Tenemos la página de pedidos, los computadores de la oficina, y todos esos
sensores y cámaras del invernadero conectados. No sabemos por dónde nos 
podrían entrar. Necesitamos que alguien lo mire con ojos de atacante… pero
sin tumbarnos nada.”
2.2 Arquitectura del ecosistema (tres dominios)
El ambiente combina deliberadamente los tres mundos que el curso integra. 
Esta arquitectura es también el plano sobre el cual se construirá la 
máquina/laboratorio del Reto 5 (ver Anexo A).
Dominio 
Componentes 
Por qué importa 
DMZ 
/ 
Web 
(LAMP)
Servidor Linux con Apache + 
MariaDB + PHP que aloja el “Portal 
AgroSmart” 
(pedidos 
B2B 
+ 
dashboard de sensores). Incluye 
panel administrativo y gestor de 
base de datos web.
Corporativo 
/ 
IT
Servidor de archivos y dominio 
(Windows), estaciones de trabajo 
de administración y contabilidad, 
escritorio remoto, comparticiones 
de red.
IoT 
/ 
OT 
(invernadero)
Gateway 
IoT, 
estación 
meteorológica, 
sensores 
de
Es 
la 
cara 
expuesta 
a 
internet: primera superficie 
de ataque y vía típica de 
compromiso inicial.
Donde viven los datos del 
negocio y desde donde se 
hace movimiento lateral tras 
un acceso inicial.
Dispositivos 
heterogéneos, 
con firmware desactualizado

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Dominio |  |  | Componentes |  |  | Por qué importa |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DMZ / Web (LAMP) |  |  | Servidor Linux con Apache + MariaDB + PHP que aloja el “Portal AgroSmart” (pedidos B2B + dashboard de sensores). Incluye panel administrativo y gestor de base de datos web. |  |  | Es la cara expuesta a internet: primera superficie de ataque y vía típica de compromiso inicial. |  |  |
| Corporativo / IT |  |  | Servidor de archivos y dominio (Windows), estaciones de trabajo de administración y contabilidad, escritorio remoto, comparticiones de red. |  |  | Donde viven los datos del negocio y desde donde se hace movimiento lateral tras un acceso inicial. |  |  |
| IoT / OT (invernadero) |  |  | Gateway IoT, estación meteorológica, sensores de |  |  | Dispositivos heterogéneos, con firmware desactualizado |  |  |

---

### [p. 10]

humedad, controlador de riego 
(PLC), cámaras IP, broker de 
mensajería de telemetría.
y credenciales por defecto: 
superficie 
emergente 
y 
frecuentemente olvidada. 
 
Diagrama lógico (descripción para construir). Internet → Firewall 
perimetral → DMZ (Portal LAMP, IP pública). El firewall conecta a una red 
interna conmutada donde coexisten el segmento IT (Windows + estaciones) 
y el segmento IoT/OT (gateway + sensores + cámaras + PLC). La 
segmentación entre IT e IoT es débil (mismo plano de difusión en varios 
casos).
Como instrumento del Reto 2, usted deberá dibujar este diagrama e identificar 
las fronteras de confianza.

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 11]

3. Informe de insumos (artefactos para analizar)
A continuación, se entregan los artefactos que un equipo de reconocimiento 
ya recolectó. Son su materia prima: no necesita una máquina para empezar 
a razonar. Cada artefacto contiene pistas. Su trabajo analítico consiste en 
interpretarlas, correlacionarlas y convertirlas en hallazgos sustentados con 
fuentes públicas (NVD, Exploit-DB, MITRE).
3.1 Inventario de activos (entregado)
ID 
Activo 
Dominio 
IP (lab) 
Servicio 
principal 
A-01 
Portal AgroSmart (web) 
DMZ 
10.10.10.20 
HTTP/HTTPS 
(80/443) 
A-02 
Gestor BD web (admin) 
DMZ 
10.10.10.20 
HTTP 
(/dbadmin) 
A-03 
Servidor 
de 
archivos/dominio
IT 
10.10.20.10 
SMB 
(445), 
LDAP 
A-04 
Estación contabilidad 
IT 
10.10.20.51 
RDP (3389) 
A-05 
Gateway IoT 
IoT/OT 
10.10.30.5 
HTTP 
admin 
(8080) 
A-06 
Cámara IP invernadero 
IoT/OT 
10.10.30.21 
RTSP 
(554)/HTTP 
(81) 
A-07 
Controlador 
de 
riego 
(PLC)
IoT/OT 
10.10.30.30 
Modbus/TCP 
(502) 
A-08 
Broker de telemetría 
IoT/OT 
10.10.30.40 
MQTT (1883)
3.2 Reconocimiento de red (salida simulada de escaneo)
Extracto de un escaneo de descubrimiento de servicios y versiones sobre el 
laboratorio. Lea con atención los banners de versión: son la principal pista 
para investigar CVE.
$ nmap -sV -sC 10.10.10.20 10.10.20.10 10.10.30.0/24 
  
Nmap scan report for 10.10.10.20  (Portal AgroSmart - DMZ) 
PORT    STATE SERVICE  VERSION 
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 
80/tcp  open  http     Apache httpd 2.4.49 ((Unix)) 
443/tcp open  ssl/http Apache httpd 2.4.49 
|_http-server-header: Apache/2.4.49 (Unix) PHP/7.2.24 
|_http-title: Portal AgroSmart :: Acceso clientes 
3306/tcp open  mysql    MariaDB 10.3 
| http-robots.txt: 2 disallowed entries 
|_/dbadmin/  /backup/ 
  
Nmap scan report for 10.10.20.10  (IT)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| ID | Activo | Dominio | IP (lab) |  | Servicio |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | principal |  |
| A-01 | Portal AgroSmart (web) | DMZ | 10.10.10.20 | HTTP/HTTPS (80/443) |  |  |
| A-02 | Gestor BD web (admin) | DMZ | 10.10.10.20 | HTTP (/dbadmin) |  |  |
| A-03 | Servidor de archivos/dominio | IT | 10.10.20.10 | SMB (445), LDAP |  |  |
| A-04 | Estación contabilidad | IT | 10.10.20.51 | RDP (3389) |  |  |
| A-05 | Gateway IoT | IoT/OT | 10.10.30.5 | HTTP admin (8080) |  |  |
| A-06 | Cámara IP invernadero | IoT/OT | 10.10.30.21 | RTSP (554)/HTTP (81) |  |  |
| A-07 | Controlador de riego (PLC) | IoT/OT | 10.10.30.30 | Modbus/TCP (502) |  |  |
| A-08 | Broker de telemetría | IoT/OT | 10.10.30.40 | MQTT (1883) |  |  |

**Tabla detectada (formato Markdown):**

| $ nmap -sV -sC 10.10.10.20 10.10.20.10 10.10.30.0/24 |
| --- |
| Nmap scan report for 10.10.10.20 (Portal AgroSmart - DMZ) |
| PORT STATE SERVICE VERSION |
| 22/tcp open ssh OpenSSH 8.2p1 Ubuntu |
| 80/tcp open http Apache httpd 2.4.49 ((Unix)) |
| 443/tcp open ssl/http Apache httpd 2.4.49 |
| |_http-server-header: Apache/2.4.49 (Unix) PHP/7.2.24 |
| |_http-title: Portal AgroSmart :: Acceso clientes |
| 3306/tcp open mysql MariaDB 10.3 |
| | http-robots.txt: 2 disallowed entries |
| |_/dbadmin/ /backup/ |
| Nmap scan report for 10.10.20.10 (IT) |

---

### [p. 12]

PORT     STATE SERVICE       VERSION 
445/tcp  open  microsoft-ds  Windows Server 2016 (SMBv1 enabled) 
3389/tcp open  ms-wbt-server Microsoft Terminal Services 
|_smb-security-mode: message_signing disabled 
  
Nmap scan report for 10.10.30.5   (Gateway IoT) 
8080/tcp open  http  lighttpd 1.4.45  (admin panel, no TLS) 
23/tcp   open  telnet (login prompt) 
  
Nmap scan report for 10.10.30.21  (Camara IP) 
554/tcp  open  rtsp 
81/tcp   open  http  Boa/0.94 (IP camera web)  fw v5.2.0 
Nmap scan report for 10.10.30.30  (PLC riego) 
502/tcp  open  modbus  (unit id 1 responds, no auth) 
Nmap scan report for 10.10.30.40  (Broker) 
1883/tcp open  mqtt  (anonymous connect allowed)
3.3 Artefactos de la aplicación web (Portal AgroSmart LAMP)
Capturas de comportamiento del portal recolectadas por el equipo de 
reconocimiento.
a) robots.txt: Disallow: /dbadmin/ y /backup/ — pistas de rutas sensibles 
expuestas.
b) Encabezados de respuesta HTTP: Server: Apache/2.4.49 (Unix) · X-
Powered-By: PHP/7.2.24 · ausencia de Content-Security-Policy, X-Frame-
Options y HSTS.
c) Mensaje de error al manipular un parámetro de búsqueda:
GET /productos.php?categoria=hortalizas'  HTTP/1.1 
  
Warning: mysqli_fetch_array(): SQL syntax error near 
'hortalizas''' at line 1 in /var/www/html/productos.php on line 88 
d) Formulario de acceso administrativo: /admin con usuario y 
contraseña; el campo recuerda credenciales y no tiene bloqueo por intentos 
fallidos. Un volcado de prueba mostró el uso de credenciales triviales en un 
entorno de demo (admin / admin123).
e) Carga de archivos: el módulo “adjuntar certificado fitosanitario” acepta 
archivos sin validar la extensión real ni el tipo MIME.
Pistas web a investigar (no resueltas)
• 
El mensaje de error revela inyección en consulta SQL → técnica de prueba con 
SQLMap; concepto OWASP A03:2021-Injection.
• 
El banner Apache 2.4.49 corresponde a una versión con vulnerabilidad pública de path 
traversal/ejecución → investigue su identificador CVE en NVD y su entrada en Exploit-
DB.

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| PORT STATE SERVICE VERSION |
| --- |
| 445/tcp open microsoft-ds Windows Server 2016 (SMBv1 enabled) |
| 3389/tcp open ms-wbt-server Microsoft Terminal Services |
| |_smb-security-mode: message_signing disabled |
| Nmap scan report for 10.10.30.5 (Gateway IoT) |
| 8080/tcp open http lighttpd 1.4.45 (admin panel, no TLS) |
| 23/tcp open telnet (login prompt) |
| Nmap scan report for 10.10.30.21 (Camara IP) |
| 554/tcp open rtsp |
| 81/tcp open http Boa/0.94 (IP camera web) fw v5.2.0 |
| Nmap scan report for 10.10.30.30 (PLC riego) |
| 502/tcp open modbus (unit id 1 responds, no auth) |
| Nmap scan report for 10.10.30.40 (Broker) |
| 1883/tcp open mqtt (anonymous connect allowed) |

**Tabla detectada (formato Markdown):**

| GET /productos.php?categoria=hortalizas' HTTP/1.1 |
| --- |
| Warning: mysqli_fetch_array(): SQL syntax error near |
| 'hortalizas''' at line 1 in /var/www/html/productos.php on line 88 |

**Tabla detectada (formato Markdown):**

|  | Pistas web a investigar (no resueltas) |  |
| --- | --- | --- |
|  | • El mensaje de error revela inyección en consulta SQL → técnica de prueba con |  |
|  | SQLMap; concepto OWASP A03:2021-Injection. |  |
|  | • El banner Apache 2.4.49 corresponde a una versión con vulnerabilidad pública de path |  |
|  | traversal/ejecución → investigue su identificador CVE en NVD y su entrada en Exploit- |  |
|  | DB. |  |

---

### [p. 13]

• 
El gestor de BD web bajo /dbadmin sugiere un panel tipo phpMyAdmin → revise CVE 
históricos de LFI/ejecución del gestor.
• 
La carga de archivos sin validación habilita web shell → mapéelo a una técnica MITRE 
de la táctica de ejecución/persistencia.
3.4 Informe OSINT e ingeniería social
Información de fuentes abiertas recolectada sobre AgroSmart (simulada para 
fines del caso). Es el insumo del análisis de ingeniería social del Reto 2.
Hallazgo OSINT 
Detalle 
Uso potencial por el 
adversario 
Estructura de correo 
nombre.apellido@agrosmart-
sumapaz.co (visible en la web 
pública).
Construcción 
de 
objetivos de phishing y 
pulverización 
de 
contraseñas. 
Organigrama parcial 
Gerencia 
(Lucía 
R.), 
Contabilidad (Andrés M.), TI 
tercerizada 
(proveedor 
“SoporteYa”).
Redes sociales 
Publicación 
con 
foto 
del 
invernadero 
mostrando 
la 
marca de las cámaras IP y una 
pantalla 
con 
el 
panel 
del 
gateway.
Metadatos de PDF 
Cotización pública con autor 
“amunoz” y software “Office 
2016”; 
ruta 
interna 
\\FILESRV01\cotizaciones.
Nombres de usuario y 
rutas 
internas 
para 
spear-phishing 
y 
enumeración. 
Ofertas de empleo 
Vacante pide experiencia en 
“MariaDB y PHP 7” y “cámaras 
Boa”.
Confirma 
stack 
tecnológico y antigüedad 
del software. 
 
Correo sospechoso reportado por Contabilidad (pretexto). “Asunto: 
Actualización urgente de credenciales del portal — Soporte TI”. Remitente que 
imita a SoporteYa, enlace a un dominio parecido (agrosmart-portal[.]co), 
urgencia y autoridad. Este artefacto es su caso base para analizar 
phishing/pretexting y mapearlo a la Cyber Kill Chain (entrega/explotación).
Suplantación 
de 
proveedor 
de 
TI 
(pretexto creíble).
Identificación 
de 
modelo/firmware 
de 
dispositivos IoT.

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | • El gestor de BD web bajo /dbadmin sugiere un panel tipo phpMyAdmin → revise CVE |  |
| --- | --- | --- |
|  | históricos de LFI/ejecución del gestor. |  |
|  | • La carga de archivos sin validación habilita web shell → mapéelo a una técnica MITRE |  |
|  | de la táctica de ejecución/persistencia. |  |

**Tabla detectada (formato Markdown):**

| Hallazgo OSINT | Detalle |  | Uso potencial por el |  |
| --- | --- | --- | --- | --- |
|  |  |  | adversario |  |
| Estructura de correo | nombre.apellido@agrosmart- sumapaz.co (visible en la web pública). | Construcción de objetivos de phishing y pulverización de contraseñas. |  |  |
| Organigrama parcial | Gerencia (Lucía R.), Contabilidad (Andrés M.), TI tercerizada (proveedor “SoporteYa”). | Suplantación de proveedor de TI (pretexto creíble). |  |  |
| Redes sociales | Publicación con foto del invernadero mostrando la marca de las cámaras IP y una pantalla con el panel del gateway. | Identificación de modelo/firmware de dispositivos IoT. |  |  |
| Metadatos de PDF | Cotización pública con autor “amunoz” y software “Office 2016”; ruta interna \\FILESRV01\cotizaciones. | Nombres de usuario y rutas internas para spear-phishing y enumeración. |  |  |
| Ofertas de empleo | Vacante pide experiencia en “MariaDB y PHP 7” y “cámaras Boa”. | Confirma stack tecnológico y antigüedad del software. |  |  |

---

### [p. 14]

3.5 Inventario IoT/OT (firmware y exposición)
Dispositivo 
Detalle técnico 
Pista de seguridad 
Gateway 
IoT 
(lighttpd)
Panel admin en 8080 sin TLS; 
Telnet (23) abierto.
Credenciales por defecto / 
servicios heredados tipo 
Mirai; 
investigue 
exposición de Telnet en 
IoT. 
Cámara IP (Boa, 
fw v5.2.0)
Servidor Boa embebido; RTSP sin 
contraseña fuerte.
Familia de cámaras con 
CVE 
de 
bypass 
de 
autenticación (acceso a 
snapshots/config). 
Investigue 
el 
CVE 
asociado a esta familia. 
Controlador 
de 
riego (PLC)
Modbus/TCP 
en 
502 
sin 
autenticación.
Modbus 
no 
autentica: 
lectura/escritura 
de 
registros. Riesgo OT físico 
(riego). 
Broker 
de 
telemetría
MQTT 
1883 
permite 
conexión 
anónima; tópicos de sensores y 
comandos.
Suscripción/publicación 
no 
autorizada; 
manipulación 
de 
telemetría y comandos. 
Estación 
meteorológica
Reporta por MQTT al broker. 
Inyección de datos falsos 
que alteren decisiones de 
riego.
3.6 Extractos de logs (correlación)
# Apache access.log (DMZ) 
10.0.0.66 - - "GET /productos.php?categoria=hortalizas' HTTP/1.1" 500 
10.0.0.66 - - "GET /dbadmin/ HTTP/1.1" 200 
10.0.0.66 - - "POST /admin/login.php HTTP/1.1" 302   (x37 en 40s) 
  
# Windows Security (IT)  - eventos 
4625  Logon fallido  usuario: amunoz  origen: 10.10.10.20   (x12) 
4624  Logon exitoso  usuario: amunoz  tipo 3 (red) 
7045  Servicio nuevo instalado  nombre aleatorio 
  
# Broker MQTT 
CONNECT anonymous  topic SUB: invernadero/# 
PUBLISH invernadero/riego/cmd  payload: {"valve":"open"}
Lectura adversarial de los logs (guía de análisis) 
Estos registros sugieren una cadena: error SQL en el portal → acceso al 
gestor de BD/panel admin (fuerza bruta sin bloqueo) → reutilización de 
credencial “amunoz” contra el segmento IT (logon de red) → instalación de 
servicio (persistencia) → manipulación del riego vía MQTT. Su tarea en el

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Dispositivo |  |  | Detalle técnico |  |  | Pista de seguridad |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gateway IoT (lighttpd) |  |  | Panel admin en 8080 sin TLS; Telnet (23) abierto. |  |  | Credenciales por defecto / servicios heredados tipo Mirai; investigue exposición de Telnet en IoT. |  |  |
| Cámara IP (Boa, fw v5.2.0) |  |  | Servidor Boa embebido; RTSP sin contraseña fuerte. |  |  | Familia de cámaras con CVE de bypass de autenticación (acceso a snapshots/config). Investigue el CVE asociado a esta familia. |  |  |
| Controlador de riego (PLC) |  |  | Modbus/TCP en 502 sin autenticación. |  |  | Modbus no autentica: lectura/escritura de registros. Riesgo OT físico (riego). |  |  |
| Broker de telemetría |  |  | MQTT 1883 permite conexión anónima; tópicos de sensores y comandos. |  |  | Suscripción/publicación no autorizada; manipulación de telemetría y comandos. |  |  |
| Estación meteorológica |  |  | Reporta por MQTT al broker. |  |  | Inyección de datos falsos que alteren decisiones de riego. |  |  |

**Tabla detectada (formato Markdown):**

| # Apache access.log (DMZ) |
| --- |
| 10.0.0.66 - - "GET /productos.php?categoria=hortalizas' HTTP/1.1" 500 |
| 10.0.0.66 - - "GET /dbadmin/ HTTP/1.1" 200 |
| 10.0.0.66 - - "POST /admin/login.php HTTP/1.1" 302 (x37 en 40s) |
| # Windows Security (IT) - eventos |
| 4625 Logon fallido usuario: amunoz origen: 10.10.10.20 (x12) |
| 4624 Logon exitoso usuario: amunoz tipo 3 (red) |
| 7045 Servicio nuevo instalado nombre aleatorio |
| # Broker MQTT |
| CONNECT anonymous topic SUB: invernadero/# |
| PUBLISH invernadero/riego/cmd payload: {"valve":"open"} |

**Tabla detectada (formato Markdown):**

|  | Lectura adversarial de los logs (guía de análisis) |  |
| --- | --- | --- |
|  | Estos registros sugieren una cadena: error SQL en el portal → acceso al |  |
|  | gestor de BD/panel admin (fuerza bruta sin bloqueo) → reutilización de |  |
|  | credencial “amunoz” contra el segmento IT (logon de red) → instalación de |  |
|  | servicio (persistencia) → manipulación del riego vía MQTT. Su tarea en el |  |

---

### [p. 15]

Reto 2 es reconstruir y sustentar esta ruta probable de ataque, no asumirla: 
cada salto debe quedar respaldado por una pista del informe y mapeado a 
Cyber Kill Chain y MITRE ATT&CK.
3.7 Reconocimiento web profundo (artefactos ampliados)
Los siguientes artefactos amplían el reconocimiento del Portal AgroSmart (A-
01, 10.10.10.20). Léalos como un atacante: cada línea inusual es una puerta 
o una pista. Su tarea es correlacionarlos con los CVE, técnicas MITRE y 
controles que se piden en los Retos 2, 3, 4 y 5.
a) Escaneo Nmap con scripts de vulnerabilidad (NSE)
$ nmap -p80,443,3306 --script "http-enum,http-headers,ssl-cert,vuln" 10.10.10.20 
  
PORT   STATE SERVICE 
80/tcp open  http  Apache httpd 2.4.49 ((Unix)) 
| http-enum: 
|   /admin/: Admin login page 
|   /dbadmin/: phpMyAdmin 
|   /backup/: Potentially interesting (directory listing) 
|   /uploads/: Writable upload directory 
|   /.git/: Git repository found! 
|_  /api/v1/: REST endpoint (verbose errors) 
| http-server-header: Apache/2.4.49 (Unix) PHP/7.2.24 
| http-csp-header: ERROR: No Content-Security-Policy 
|_http-cookie-flags: PHPSESSID: httponly flag NOT set; secure flag NOT set 
443/tcp open ssl/http 
| ssl-cert: Subject: commonName=portal.agrosmart.local 
|   Not valid after:  2023-11-02  (EXPIRED, self-signed) 
|_  signature: sha1WithRSAEncryption (weak) 
| http-vuln-cve2021-41773: 
|_  VULNERABLE: Apache 2.4.49 path traversal (needs confirmation)
b) Fuerza bruta de directorios (gobuster)
$ gobuster dir -u http://10.10.10.20 -w common.txt 
  
/index.php            (Status: 200) 
/admin                (Status: 301)  -> /admin/ 
/dbadmin              (Status: 301)  -> /dbadmin/ 
/backup               (Status: 200)  [Directory listing enabled] 
/uploads              (Status: 200)  [Directory listing enabled] 
/config.php.bak       (Status: 200)  [text/plain] 
/phpinfo.php          (Status: 200) 
/.git/config          (Status: 200) 
/api                  (Status: 301)  -> /api/ 
/login.php            (Status: 200) 
/robots.txt           (Status: 200)
c) Identificación de tecnologías (whatweb) y robots.txt completo
$ whatweb http://10.10.10.20 
http://10.10.10.20 [200 OK] Apache[2.4.49], PHP[7.2.24],

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Reto 2 es reconstruir y sustentar esta ruta probable de ataque, no asumirla: |  |
| --- | --- | --- |
|  | cada salto debe quedar respaldado por una pista del informe y mapeado a |  |
|  | Cyber Kill Chain y MITRE ATT&CK. |  |

**Tabla detectada (formato Markdown):**

| $ nmap -p80,443,3306 --script "http-enum,http-headers,ssl-cert,vuln" 10.10.10.20 |
| --- |
| PORT STATE SERVICE |
| 80/tcp open http Apache httpd 2.4.49 ((Unix)) |
| | http-enum: |
| | /admin/: Admin login page |
| | /dbadmin/: phpMyAdmin |
| | /backup/: Potentially interesting (directory listing) |
| | /uploads/: Writable upload directory |
| | /.git/: Git repository found! |
| |_ /api/v1/: REST endpoint (verbose errors) |
| | http-server-header: Apache/2.4.49 (Unix) PHP/7.2.24 |
| | http-csp-header: ERROR: No Content-Security-Policy |
| |_http-cookie-flags: PHPSESSID: httponly flag NOT set; secure flag NOT set |
| 443/tcp open ssl/http |
| | ssl-cert: Subject: commonName=portal.agrosmart.local |
| | Not valid after: 2023-11-02 (EXPIRED, self-signed) |
| |_ signature: sha1WithRSAEncryption (weak) |
| | http-vuln-cve2021-41773: |
| |_ VULNERABLE: Apache 2.4.49 path traversal (needs confirmation) |

**Tabla detectada (formato Markdown):**

| $ gobuster dir -u http://10.10.10.20 -w common.txt |
| --- |
| /index.php (Status: 200) |
| /admin (Status: 301) -> /admin/ |
| /dbadmin (Status: 301) -> /dbadmin/ |
| /backup (Status: 200) [Directory listing enabled] |
| /uploads (Status: 200) [Directory listing enabled] |
| /config.php.bak (Status: 200) [text/plain] |
| /phpinfo.php (Status: 200) |
| /.git/config (Status: 200) |
| /api (Status: 301) -> /api/ |
| /login.php (Status: 200) |
| /robots.txt (Status: 200) |

**Tabla detectada (formato Markdown):**

| $ whatweb http://10.10.10.20 |
| --- |
| http://10.10.10.20 [200 OK] Apache[2.4.49], PHP[7.2.24], |

---

### [p. 16]

JQuery[1.7.2], Bootstrap[3.3.7], Cookies[PHPSESSID], 
  HTTPServer[Unix], X-Powered-By[PHP/7.2.24], Title[Portal AgroSmart] 
  
$ curl -s http://10.10.10.20/robots.txt 
User-agent: * 
Disallow: /dbadmin/ 
Disallow: /backup/ 
Disallow: /admin/ 
Disallow: /uploads/ 
# TODO (dev): quitar phpinfo.php antes de produccion
Pistas a investigar — Sec. 3.7
• 
Apache 2.4.49 + path traversal: confirme el CVE en NVD y su madurez de explotación en 
Exploit-DB; estime el CVSS.
• 
jQuery 1.7.2 y Bootstrap 3.3.7 son componentes antiguos: busque vulnerabilidades de 
cliente (XSS) asociadas a esas versiones.
• 
Certificado expirado, autofirmado y SHA-1: mapee el riesgo de confidencialidad/MITM y la 
mitigación (TLS moderno, HSTS).
• 
Cookie de sesión sin HttpOnly ni Secure: relacione con robo de sesión vía XSS y con un 
control del Reto 3.
• 
Listados de directorio habilitados, /backup, /.git y phpinfo.php expuestos: técnica MITRE 
de descubrimiento/recolección; cada uno es un hallazgo independiente.
3.8 Hallazgos sensibles en el servidor web
El reconocimiento anterior reveló rutas peligrosas. Aquí están los contenidos 
que un atacante encontraría al visitarlas. Recuerde: estos archivos NO 
deberían ser accesibles; su exposición es, en sí misma, un hallazgo de alta 
severidad.
a) Listado del directorio /backup/
$ curl -s http://10.10.10.20/backup/ 
Index of /backup 
[ ] db_agrosmart_2024.sql.gz      4.2M 
[ ] config.php.bak                3.1K 
[ ] portal_full_backup.tar.gz     38M 
[ ] .htpasswd                     112 
[ ] notas_admin.txt               240
b) Contenido de config.php.bak (copia de respaldo expuesta)
$ curl -s http://10.10.10.20/config.php.bak 
<?php 
// Configuracion de conexion - Portal AgroSmart 
define('DB_HOST', '127.0.0.1'); 
define('DB_NAME', 'db_agrosmart'); 
define('DB_USER', 'webapp'); 
define('DB_PASS', 'Agro2024*');      // <-- credencial en claro 
define('ADMIN_USER', 'admin'); 
define('ADMIN_PASS_MD5', '0192023a7bbd73250516f069df18b500'); // hash debil

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| JQuery[1.7.2], Bootstrap[3.3.7], Cookies[PHPSESSID], |
| --- |
| HTTPServer[Unix], X-Powered-By[PHP/7.2.24], Title[Portal AgroSmart] |
| $ curl -s http://10.10.10.20/robots.txt |
| User-agent: * |
| Disallow: /dbadmin/ |
| Disallow: /backup/ |
| Disallow: /admin/ |
| Disallow: /uploads/ |
| # TODO (dev): quitar phpinfo.php antes de produccion |

**Tabla detectada (formato Markdown):**

|  | Pistas a investigar — Sec. 3.7 |  |
| --- | --- | --- |
|  | • Apache 2.4.49 + path traversal: confirme el CVE en NVD y su madurez de explotación en |  |
|  | Exploit-DB; estime el CVSS. |  |
|  | • jQuery 1.7.2 y Bootstrap 3.3.7 son componentes antiguos: busque vulnerabilidades de |  |
|  | cliente (XSS) asociadas a esas versiones. |  |
|  | • Certificado expirado, autofirmado y SHA-1: mapee el riesgo de confidencialidad/MITM y la |  |
|  | mitigación (TLS moderno, HSTS). |  |
|  | • Cookie de sesión sin HttpOnly ni Secure: relacione con robo de sesión vía XSS y con un |  |
|  | control del Reto 3. |  |
|  | • Listados de directorio habilitados, /backup, /.git y phpinfo.php expuestos: técnica MITRE |  |
|  | de descubrimiento/recolección; cada uno es un hallazgo independiente. |  |

**Tabla detectada (formato Markdown):**

| $ curl -s http://10.10.10.20/backup/ |
| --- |
| Index of /backup |
| [ ] db_agrosmart_2024.sql.gz 4.2M |
| [ ] config.php.bak 3.1K |
| [ ] portal_full_backup.tar.gz 38M |
| [ ] .htpasswd 112 |
| [ ] notas_admin.txt 240 |

**Tabla detectada (formato Markdown):**

| $ curl -s http://10.10.10.20/config.php.bak |
| --- |
| <?php |
| // Configuracion de conexion - Portal AgroSmart |
| define('DB_HOST', '127.0.0.1'); |
| define('DB_NAME', 'db_agrosmart'); |
| define('DB_USER', 'webapp'); |
| define('DB_PASS', 'Agro2024*'); // <-- credencial en claro |
| define('ADMIN_USER', 'admin'); |
| define('ADMIN_PASS_MD5', '0192023a7bbd73250516f069df18b500'); // hash debil |

---

### [p. 17]

define('DEBUG', true);                // errores verbosos activados 
?>
c) Repositorio Git expuesto y endpoint de API verboso
$ curl -s http://10.10.10.20/.git/config 
[remote "origin"] 
  url = http://devops:t3mp0ral@git.agrosmart.local/portal.git 
  
$ curl -s "http://10.10.10.20/api/v1/usuario?id=1" 
{"id":1,"user":"admin","email":"admin@agrosmart-sumapaz.co","rol":"superadmin"} 
$ curl -s "http://10.10.10.20/api/v1/usuario?id=2" 
{"id":2,"user":"amunoz","email":"amunoz@agrosmart-sumapaz.co","rol":"contador"} 
$ curl -s "http://10.10.10.20/api/v1/usuario?id=9999" 
{"error":"PDOException: 
SQLSTATE[42S02] 
table 
not 
found 
in 
/var/www/html/api/db.php:14"}
d) Token de sesión emitido por el portal (JWT)
Set-Cookie: token=eyJhbGciOiJub25lIn0.eyJ1c2VyIjoiYW11bm96Iiwicm9sIjoiY29udGFkb3IifQ. 
# Cabecera decodificada:  {"alg":"none"} 
# Cuerpo decodificado:    {"user":"amunoz","rol":"contador"}
Pistas a investigar — Sec. 3.8
• 
Credenciales en claro en config.php.bak y en la URL del repositorio Git: enlace con 
reutilización de credenciales hacia el segmento IT (vea el usuario amunoz en los logs, Sec. 
3.6).
• 
Hash MD5 0192023a... : investigue por qué MD5 sin sal es débil y a qué valor corresponde 
(uso de bases públicas de hashes). Conclúyalo como hallazgo, no lo “crackee” fuera del 
laboratorio.
• 
API que devuelve datos de otros usuarios cambiando el id: identifique la técnica (referencia 
directa a objeto insegura / acceso indebido) y su categoría OWASP.
• 
Error de base de datos verboso (DEBUG=true): fuga de información que facilita la 
inyección; conéctelo con la cabecera DEBUG y el Reto 3.
• 
JWT con “alg”:none : razone por qué permite falsificar el rol (escalada de privilegios) y 
cómo se detecta/mitiga.
3.9 Enumeración del segmento IT / Windows
Artefactos recolectados en el segmento corporativo (A-03 servidor 
10.10.20.10, A-04 estación 10.10.20.51). Son la base para razonar el 
movimiento lateral y la persistencia del Reto 2.
a) Descubrimiento de sistema y comparticiones (SMB)
$ nmap -p445 --script smb-os-discovery,smb-security-mode 10.10.20.10 
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 
|   Computer name: FILESRV01 
|   Domain: AGROSMART 
|_  FQDN: FILESRV01.agrosmart.local 
| smb-security-mode:

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| define('DEBUG', true); // errores verbosos activados |
| --- |
| ?> |

**Tabla detectada (formato Markdown):**

| $ curl -s http://10.10.10.20/.git/config |
| --- |
| [remote "origin"] |
| url = http://devops:t3mp0ral@git.agrosmart.local/portal.git |
| $ curl -s "http://10.10.10.20/api/v1/usuario?id=1" |
| {"id":1,"user":"admin","email":"admin@agrosmart-sumapaz.co","rol":"superadmin"} |
| $ curl -s "http://10.10.10.20/api/v1/usuario?id=2" |
| {"id":2,"user":"amunoz","email":"amunoz@agrosmart-sumapaz.co","rol":"contador"} |
| $ curl -s "http://10.10.10.20/api/v1/usuario?id=9999" |
| {"error":"PDOException: SQLSTATE[42S02] table not found in |
| /var/www/html/api/db.php:14"} |

**Tabla detectada (formato Markdown):**

| Set-Cookie: token=eyJhbGciOiJub25lIn0.eyJ1c2VyIjoiYW11bm96Iiwicm9sIjoiY29udGFkb3IifQ. |
| --- |
| # Cabecera decodificada: {"alg":"none"} |
| # Cuerpo decodificado: {"user":"amunoz","rol":"contador"} |

**Tabla detectada (formato Markdown):**

|  | Pistas a investigar — Sec. 3.8 |  |
| --- | --- | --- |
|  | • Credenciales en claro en config.php.bak y en la URL del repositorio Git: enlace con |  |
|  | reutilización de credenciales hacia el segmento IT (vea el usuario amunoz en los logs, Sec. |  |
|  | 3.6). |  |
|  | • Hash MD5 0192023a... : investigue por qué MD5 sin sal es débil y a qué valor corresponde |  |
|  | (uso de bases públicas de hashes). Conclúyalo como hallazgo, no lo “crackee” fuera del |  |
|  | laboratorio. |  |
|  | • API que devuelve datos de otros usuarios cambiando el id: identifique la técnica (referencia |  |
|  | directa a objeto insegura / acceso indebido) y su categoría OWASP. |  |
|  | • Error de base de datos verboso (DEBUG=true): fuga de información que facilita la |  |
|  | inyección; conéctelo con la cabecera DEBUG y el Reto 3. |  |
|  | • JWT con “alg”:none : razone por qué permite falsificar el rol (escalada de privilegios) y |  |
|  | cómo se detecta/mitiga. |  |

**Tabla detectada (formato Markdown):**

| $ nmap -p445 --script smb-os-discovery,smb-security-mode 10.10.20.10 |
| --- |
| | smb-os-discovery: |
| | OS: Windows Server 2016 Standard |
| | Computer name: FILESRV01 |
| | Domain: AGROSMART |
| |_ FQDN: FILESRV01.agrosmart.local |
| | smb-security-mode: |

---

### [p. 18]

|_  message_signing: disabled (dangerous) 
|   SMBv1: enabled 
  
$ enum4linux -a 10.10.20.10 
[+] Sesion nula permitida (null session) 
[+] Recursos compartidos: 
    cotizaciones   Disk   (Everyone: READ) 
    respaldos      Disk   (Everyone: READ/WRITE) 
    NETLOGON       Disk 
[+] Usuarios del dominio: 
    Administrador, amunoz, lrojas, jsoporte, svc_backup
b) Exploración de un recurso accesible sin credenciales
$ smbclient //10.10.20.10/respaldos -N 
smb: \> dir 
  passwords.xlsx        18432  2024-10-03 
  red_credenciales.txt    980  2024-09-21 
  imagen_estacion.vhdx  ... 
smb: \> get red_credenciales.txt 
# (archivo de texto con credenciales de servicios internos)
c) Política de contraseñas y escritorio remoto
$ Get-ADDefaultDomainPasswordPolicy   (extraido por sesion autenticada de prueba) 
MinPasswordLength       : 6 
LockoutThreshold        : 0     (sin bloqueo por intentos fallidos) 
ComplexityEnabled       : False 
MaxPasswordAge          : (nunca) 
  
$ nmap -p3389 --script rdp-ntlm-info 10.10.20.51 
|   Target_Name: AGROSMART 
|   NetBIOS_Computer_Name: CONTA-PC 
|_  NLA (Network Level Authentication): disabled
d) Eventos de Windows correlacionables (Sysmon/Security)
4625  Logon fallido   amunoz   origen 10.10.10.20   (x12 en 60s) 
4624  Logon exitoso   amunoz   tipo 3 (red)         origen 10.10.10.20 
4672  Privilegios especiales asignados a amunoz 
7045  Servicio nuevo  "WinHlp32Svc"  ruta C:\Windows\Temp\w.exe 
1     (Sysmon) ProcessCreate  parent: services.exe  cmd: w.exe -s 
3     (Sysmon) NetworkConnect  w.exe -> 10.10.30.40:1883  (hacia IoT)
Pistas a investigar — Sec. 3.9
• 
SMBv1 + firma deshabilitada: investigue los CVE críticos históricos de SMBv1 y su técnica 
MITRE de movimiento lateral.
• 
Sesión nula y recurso “respaldos” con escritura para Everyone: hallazgo de exposición de 
credenciales; conéctelo con passwords.xlsx y la cadena de compromiso.
• 
Política de contraseñas débil y LockoutThreshold=0: habilita fuerza bruta/pulverización; 
relaciónelo con los 4625 del log.
• 
NLA deshabilitado en RDP: amplía el riesgo de acceso remoto; proponga el control en el 
Reto 3.

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| |_ message_signing: disabled (dangerous) |
| --- |
| | SMBv1: enabled |
| $ enum4linux -a 10.10.20.10 |
| [+] Sesion nula permitida (null session) |
| [+] Recursos compartidos: |
| cotizaciones Disk (Everyone: READ) |
| respaldos Disk (Everyone: READ/WRITE) |
| NETLOGON Disk |
| [+] Usuarios del dominio: |
| Administrador, amunoz, lrojas, jsoporte, svc_backup |

**Tabla detectada (formato Markdown):**

| $ smbclient //10.10.20.10/respaldos -N |
| --- |
| smb: \> dir |
| passwords.xlsx 18432 2024-10-03 |
| red_credenciales.txt 980 2024-09-21 |
| imagen_estacion.vhdx ... |
| smb: \> get red_credenciales.txt |
| # (archivo de texto con credenciales de servicios internos) |

**Tabla detectada (formato Markdown):**

| $ Get-ADDefaultDomainPasswordPolicy (extraido por sesion autenticada de prueba) |
| --- |
| MinPasswordLength : 6 |
| LockoutThreshold : 0 (sin bloqueo por intentos fallidos) |
| ComplexityEnabled : False |
| MaxPasswordAge : (nunca) |
| $ nmap -p3389 --script rdp-ntlm-info 10.10.20.51 |
| | Target_Name: AGROSMART |
| | NetBIOS_Computer_Name: CONTA-PC |
| |_ NLA (Network Level Authentication): disabled |

**Tabla detectada (formato Markdown):**

| 4625 Logon fallido amunoz origen 10.10.10.20 (x12 en 60s) |
| --- |
| 4624 Logon exitoso amunoz tipo 3 (red) origen 10.10.10.20 |
| 4672 Privilegios especiales asignados a amunoz |
| 7045 Servicio nuevo "WinHlp32Svc" ruta C:\Windows\Temp\w.exe |
| 1 (Sysmon) ProcessCreate parent: services.exe cmd: w.exe -s |
| 3 (Sysmon) NetworkConnect w.exe -> 10.10.30.40:1883 (hacia IoT) |

**Tabla detectada (formato Markdown):**

|  | Pistas a investigar — Sec. 3.9 |  |
| --- | --- | --- |
|  | • SMBv1 + firma deshabilitada: investigue los CVE críticos históricos de SMBv1 y su técnica |  |
|  | MITRE de movimiento lateral. |  |
|  | • Sesión nula y recurso “respaldos” con escritura para Everyone: hallazgo de exposición de |  |
|  | credenciales; conéctelo con passwords.xlsx y la cadena de compromiso. |  |
|  | • Política de contraseñas débil y LockoutThreshold=0: habilita fuerza bruta/pulverización; |  |
|  | relaciónelo con los 4625 del log. |  |
|  | • NLA deshabilitado en RDP: amplía el riesgo de acceso remoto; proponga el control en el |  |
|  | Reto 3. |  |

---

### [p. 19]

• 
Evento 7045 + Sysmon: persistencia (servicio) y, ojo, conexión saliente al broker MQTT 
(10.10.30.40): aquí IT toca OT/IoT. Mapee esta pivotación.
3.10 Telemetría e industrial: IoT / OT en profundidad
El invernadero es la superficie más novedosa y la que conecta lo digital con lo 
físico (riego). Estos artefactos permiten razonar cómo un adversario 
manipularía el proceso.
a) Volcado de tópicos del broker MQTT (telemetría y comandos)
$ mosquitto_sub -h 10.10.30.40 -p 1883 -t '#' -v        (conexion anonima OK) 
invernadero/sensor/humedad      62.4 
invernadero/sensor/temperatura  21.8 
invernadero/estacion/viento     5.2 
invernadero/camara/estado       online 
invernadero/riego/estado        closed 
invernadero/riego/cmd           {"valve":"closed","by":"plc"} 
sistema/version                 gw-firmware 1.4.2
b) Lectura del controlador de riego por Modbus/TCP
$ mbpoll -m tcp -a 1 -r 1 -c 8 10.10.30.30     (sin autenticacion) 
[1]:  0   (valvula riego: 0=cerrada,1=abierta) 
[2]:  1   (bomba principal) 
[3]:  620 (humedad objetivo x10) 
[4]:  1   (modo automatico) 
[5..8]: 0 
-- Registros de escritura (holding) accesibles: SI
c) Cámara IP (servidor Boa) y prueba de acceso
$ curl -s http://10.10.30.21:81/system.ini?loginuse&loginpas 
[Network] 
  user=admin 
  pass=admin 
[Firmware] 
  version=5.2.0  model=BoaCam-IPC 
$ curl -I rtsp://10.10.30.21:554/live.sdp 
RTSP/1.0 200 OK   (stream accesible sin credenciales robustas)
d) Telnet del gateway y cadenas del firmware
$ telnet 10.10.30.5 
BusyBox v1.21 login: 
# (prompt sin TLS; banner de gateway IoT) 
  
$ strings gw-firmware-1.4.2.bin | grep -i -E "pass|user|telnet" 
admin:admin 
root:12345 
/bin/telnetd -l /bin/sh 
CONFIG_DEFAULT_PASS=admin
Pistas a investigar — Sec. 3.10

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | • Evento 7045 + Sysmon: persistencia (servicio) y, ojo, conexión saliente al broker MQTT |  |
| --- | --- | --- |
|  | (10.10.30.40): aquí IT toca OT/IoT. Mapee esta pivotación. |  |

**Tabla detectada (formato Markdown):**

| $ mosquitto_sub -h 10.10.30.40 -p 1883 -t '#' -v (conexion anonima OK) |
| --- |
| invernadero/sensor/humedad 62.4 |
| invernadero/sensor/temperatura 21.8 |
| invernadero/estacion/viento 5.2 |
| invernadero/camara/estado online |
| invernadero/riego/estado closed |
| invernadero/riego/cmd {"valve":"closed","by":"plc"} |
| sistema/version gw-firmware 1.4.2 |

**Tabla detectada (formato Markdown):**

| $ mbpoll -m tcp -a 1 -r 1 -c 8 10.10.30.30 (sin autenticacion) |
| --- |
| [1]: 0 (valvula riego: 0=cerrada,1=abierta) |
| [2]: 1 (bomba principal) |
| [3]: 620 (humedad objetivo x10) |
| [4]: 1 (modo automatico) |
| [5..8]: 0 |
| -- Registros de escritura (holding) accesibles: SI |

**Tabla detectada (formato Markdown):**

| $ curl -s http://10.10.30.21:81/system.ini?loginuse&loginpas |
| --- |
| [Network] |
| user=admin |
| pass=admin |
| [Firmware] |
| version=5.2.0 model=BoaCam-IPC |
| $ curl -I rtsp://10.10.30.21:554/live.sdp |
| RTSP/1.0 200 OK (stream accesible sin credenciales robustas) |

**Tabla detectada (formato Markdown):**

| $ telnet 10.10.30.5 |
| --- |
| BusyBox v1.21 login: |
| # (prompt sin TLS; banner de gateway IoT) |
| $ strings gw-firmware-1.4.2.bin | grep -i -E "pass|user|telnet" |
| admin:admin |
| root:12345 |
| /bin/telnetd -l /bin/sh |
| CONFIG_DEFAULT_PASS=admin |

---

### [p. 20]

• 
MQTT anónimo con tópicos de comando (riego/cmd): un PUBLISH malicioso podría abrir 
la válvula. Mapee a la táctica de Impacto (afectación de proceso) y proponga 
autenticación/segmentación.
• 
Modbus sin autenticación con registros de escritura accesibles: razone el impacto físico 
(riego/bomba) y los controles OT (lista blanca, zona OT aislada).
• 
Cámara Boa que filtra usuario/clave por una ruta: investigue el CVE de bypass de 
autenticación de esa familia de cámaras y su severidad.
• 
Telnet abierto + credenciales por defecto embebidas en el firmware (admin/admin, 
root/12345): vincúlelo con botnets tipo Mirai y con el cierre de Telnet en el Reto 3.
• 
Firmware 1.4.2 (gw): consulte si la versión tiene avisos de seguridad publicados por el 
fabricante o en bases de CVE.
3.11 Captura de tráfico de red (protocolos en claro)
Extractos de una captura pasiva en el segmento (tipo Wireshark/tcpdump). 
Muestran por qué los protocolos sin cifrado son un hallazgo en sí mismos: un 
atacante en la red lee credenciales y comandos.
# HTTP Basic Auth hacia /admin (en claro, base64) 
GET /admin/ HTTP/1.1 
Authorization: Basic YWRtaW46QWdybzIwMjQq 
# (Basic = base64; decodifica a usuario:clave -> hallazgo de credencial en transito) 
  
# Telnet hacia el gateway IoT (texto plano) 
10.0.0.66 -> 10.10.30.5  "admin" 
10.10.30.5 -> 10.0.0.66  "Password:" 
10.0.0.66 -> 10.10.30.5  "admin" 
  
# MQTT sin TLS (puerto 1883) 
PUBLISH invernadero/riego/cmd  {"valve":"open"}  QoS0  (sin auth)
Pistas a investigar — Sec. 3.11
• 
Autenticación HTTP Basic en claro: relacione con la necesidad de TLS/HSTS y con la 
interceptación (MITRE: Adversary-in-the-Middle).
• 
Telnet transmite credenciales en texto plano: argumente el reemplazo por SSH y el 
monitoreo del puerto 23.
• 
MQTT sin TLS ni autenticación: confidencialidad e integridad de la telemetría 
comprometidas; proponga TLS + ACL en el broker.
3.12 OSINT e inteligencia de fuentes abiertas (ampliado)
Información pública adicional (simulada) sobre AgroSmart. Alimenta el 
análisis de ingeniería social y la fase de reconocimiento de la Cyber Kill Chain.
a) Recolección de correos y hosts (theHarvester)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | • MQTT anónimo con tópicos de comando (riego/cmd): un PUBLISH malicioso podría abrir |  |
| --- | --- | --- |
|  | la válvula. Mapee a la táctica de Impacto (afectación de proceso) y proponga |  |
|  | autenticación/segmentación. |  |
|  | • Modbus sin autenticación con registros de escritura accesibles: razone el impacto físico |  |
|  | (riego/bomba) y los controles OT (lista blanca, zona OT aislada). |  |
|  | • Cámara Boa que filtra usuario/clave por una ruta: investigue el CVE de bypass de |  |
|  | autenticación de esa familia de cámaras y su severidad. |  |
|  | • Telnet abierto + credenciales por defecto embebidas en el firmware (admin/admin, |  |
|  | root/12345): vincúlelo con botnets tipo Mirai y con el cierre de Telnet en el Reto 3. |  |
|  | • Firmware 1.4.2 (gw): consulte si la versión tiene avisos de seguridad publicados por el |  |
|  | fabricante o en bases de CVE. |  |

**Tabla detectada (formato Markdown):**

| # HTTP Basic Auth hacia /admin (en claro, base64) |
| --- |
| GET /admin/ HTTP/1.1 |
| Authorization: Basic YWRtaW46QWdybzIwMjQq |
| # (Basic = base64; decodifica a usuario:clave -> hallazgo de credencial en transito) |
| # Telnet hacia el gateway IoT (texto plano) |
| 10.0.0.66 -> 10.10.30.5 "admin" |
| 10.10.30.5 -> 10.0.0.66 "Password:" |
| 10.0.0.66 -> 10.10.30.5 "admin" |
| # MQTT sin TLS (puerto 1883) |
| PUBLISH invernadero/riego/cmd {"valve":"open"} QoS0 (sin auth) |

**Tabla detectada (formato Markdown):**

|  | Pistas a investigar — Sec. 3.11 |  |
| --- | --- | --- |
|  | • Autenticación HTTP Basic en claro: relacione con la necesidad de TLS/HSTS y con la |  |
|  | interceptación (MITRE: Adversary-in-the-Middle). |  |
|  | • Telnet transmite credenciales en texto plano: argumente el reemplazo por SSH y el |  |
|  | monitoreo del puerto 23. |  |
|  | • MQTT sin TLS ni autenticación: confidencialidad e integridad de la telemetría |  |
|  | comprometidas; proponga TLS + ACL en el broker. |  |

---

### [p. 21]

$ theHarvester -d agrosmart-sumapaz.co -b all 
[*] Emails: 
  lrojas@agrosmart-sumapaz.co   (Gerencia) 
  amunoz@agrosmart-sumapaz.co   (Contabilidad) 
  jsoporte@agrosmart-sumapaz.co (TI tercerizada - SoporteYa) 
[*] Hosts y subdominios: 
  www.agrosmart-sumapaz.co 
  portal.agrosmart-sumapaz.co 
  dev.agrosmart-sumapaz.co      (entorno de pruebas expuesto) 
  vpn.agrosmart-sumapaz.co 
  mail.agrosmart-sumapaz.co
b) Banner público tipo motor de búsqueda de dispositivos (Shodan-
like) y fuga en paste
# Resultado de busqueda por organizacion "AgroSmart Sumapaz" 
10.10.10.20  Apache/2.4.49  PHP/7.2.24  (Portal :: Acceso clientes) 
10.10.30.21  Boa/0.94  IP Camera (login default) 
  
# Hallazgo en sitio publico de pegado de texto (paste): 
"backup db agrosmart: webapp / Agro2024*  -- no olvidar rotar"
c) Metadatos de documentos públicos (exiftool)
$ exiftool cotizacion_agrosmart.pdf 
Author              : amunoz 
Creator Tool        : Microsoft Office 2016 
Company             : AgroSmart del Sumapaz S.A.S. 
Comments            : ruta interna \\FILESRV01\cotizaciones 
Create Date         : 2024:10:03
Pistas a investigar — Sec. 3.12
• 
Subdominio dev expuesto: los entornos de pruebas suelen tener menos controles; trátelo 
como superficie adicional.
• 
Correos por rol: insumo directo para el escenario de phishing/pretexting del Reto 2; defina 
objetivo, canal y pretexto.
• 
Credencial filtrada en un paste público (webapp/Agro2024*) que coincide con 
config.php.bak: ejemplo claro de cómo el OSINT se cruza con el hallazgo técnico.
• 
Metadatos que revelan usuario (amunoz), software y ruta interna FILESRV01: enriquecen 
el spear-phishing y la enumeración. Proponga la mitigación (limpieza de metadatos).
3.13 Tabla maestra de pistas → investigación
Consolide aquí todo lo que descubrió en el informe. Algunas filas vienen 
sembradas como ejemplo; complete las demás investigando en NVD, Exploit-
DB y MITRE ATT&CK. Esta tabla es el puente entre el informe (Sec. 3) y los 
instrumentos del Reto 2.
Pista 
(artefacto)
Dónde 
aparece
Hipótesis de 
vulnerabilidad
CVE / ref. 
Fuente a 
consultar
Técnica
MITRE

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| $ theHarvester -d agrosmart-sumapaz.co -b all |
| --- |
| [*] Emails: |
| lrojas@agrosmart-sumapaz.co (Gerencia) |
| amunoz@agrosmart-sumapaz.co (Contabilidad) |
| jsoporte@agrosmart-sumapaz.co (TI tercerizada - SoporteYa) |
| [*] Hosts y subdominios: |
| www.agrosmart-sumapaz.co |
| portal.agrosmart-sumapaz.co |
| dev.agrosmart-sumapaz.co (entorno de pruebas expuesto) |
| vpn.agrosmart-sumapaz.co |
| mail.agrosmart-sumapaz.co |

**Tabla detectada (formato Markdown):**

| # Resultado de busqueda por organizacion "AgroSmart Sumapaz" |
| --- |
| 10.10.10.20 Apache/2.4.49 PHP/7.2.24 (Portal :: Acceso clientes) |
| 10.10.30.21 Boa/0.94 IP Camera (login default) |
| # Hallazgo en sitio publico de pegado de texto (paste): |
| "backup db agrosmart: webapp / Agro2024* -- no olvidar rotar" |

**Tabla detectada (formato Markdown):**

| $ exiftool cotizacion_agrosmart.pdf |
| --- |
| Author : amunoz |
| Creator Tool : Microsoft Office 2016 |
| Company : AgroSmart del Sumapaz S.A.S. |
| Comments : ruta interna \\FILESRV01\cotizaciones |
| Create Date : 2024:10:03 |

**Tabla detectada (formato Markdown):**

|  | Pistas a investigar — Sec. 3.12 |  |
| --- | --- | --- |
|  | • Subdominio dev expuesto: los entornos de pruebas suelen tener menos controles; trátelo |  |
|  | como superficie adicional. |  |
|  | • Correos por rol: insumo directo para el escenario de phishing/pretexting del Reto 2; defina |  |
|  | objetivo, canal y pretexto. |  |
|  | • Credencial filtrada en un paste público (webapp/Agro2024*) que coincide con |  |
|  | config.php.bak: ejemplo claro de cómo el OSINT se cruza con el hallazgo técnico. |  |
|  | • Metadatos que revelan usuario (amunoz), software y ruta interna FILESRV01: enriquecen |  |
|  | el spear-phishing y la enumeración. Proponga la mitigación (limpieza de metadatos). |  |

**Tabla detectada (formato Markdown):**

|  | Pista |  |  | Dónde |  |  | Hipótesis de |  | CVE / ref. |  | Fuente a |  |  | Técnica |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (artefacto) |  |  | aparece |  |  | vulnerabilidad |  |  |  | consultar |  |  | MITRE |  |

---

### [p. 22]

Apache 2.4.49 Sec. 3.2
Path traversal / RCE 
(investigar) NVD 
+ 
Exploit-
DB
/ 3.7
Error 
SQL 
productos.php
Sec. 3.3 
Inyección SQL 
App 
(OWASP 
A03)
config.php.bak 
expuesto
Sec. 3.8 
Exposición 
de 
credenciales
SMBv1 
habilitado
Sec. 3.2 
/ 3.9
RCE / lateral 
(investigar) NVD 
/ 
MSRC
Cámara 
Boa 
fw 5.2.0
Sec. 3.5 
/ 3.10
Bypass 
de 
autenticación
MQTT 
anónimo
Sec. 3.5 
/ 3.10
Acceso/manipulación 
OT
JWT alg=none 
Sec. 3.8 
Escalada 
de 
privilegios
Cómo usar esta tabla 
Por cada fila:  
1) confirme la versión/condición en el artefacto;
2) busque el CVE en NVD y registre su CVSS;  
3) verifique en Exploit-DB la existencia/madurez de pruebas de concepto 
(para evaluar explotabilidad, no para ejecutar fuera del laboratorio);  
4) asigne la táctica/técnica MITRE;  
5) anote la mitigación que llevará al Reto 3. Lo no resuelto por usted debe 
quedar justificado.
T1190
OWASP / 
SQLMap 
docs
T1190
(sin CVE) 
OWASP 
A05
T1552
T1210
(investigar) NVD 
+ 
Exploit-
DB
T1190
(sin CVE) 
Doc. 
MQTT 
/ 
OWASP 
IoT
T0855
(sin CVE) 
OWASP 
JWT
T1548

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Apache 2.4.49 | Sec. 3.2 / 3.7 | Path traversal / RCE | (investigar) | NVD + Exploit- DB | T1190 |
| --- | --- | --- | --- | --- | --- |
| Error SQL productos.php | Sec. 3.3 | Inyección SQL | App (OWASP A03) | OWASP / SQLMap docs | T1190 |
| config.php.bak expuesto | Sec. 3.8 | Exposición de credenciales | (sin CVE) | OWASP A05 | T1552 |
| SMBv1 habilitado | Sec. 3.2 / 3.9 | RCE / lateral | (investigar) | NVD / MSRC | T1210 |
| Cámara Boa fw 5.2.0 | Sec. 3.5 / 3.10 | Bypass de autenticación | (investigar) | NVD + Exploit- DB | T1190 |
| MQTT anónimo | Sec. 3.5 / 3.10 | Acceso/manipulación OT | (sin CVE) | Doc. MQTT / OWASP IoT | T0855 |
| JWT alg=none | Sec. 3.8 | Escalada de privilegios | (sin CVE) | OWASP JWT | T1548 |

**Tabla detectada (formato Markdown):**

|  | Cómo usar esta tabla |  |
| --- | --- | --- |
|  | Por cada fila: |  |
|  | 1) confirme la versión/condición en el artefacto; |  |
|  | 2) busque el CVE en NVD y registre su CVSS; |  |
|  | 3) verifique en Exploit-DB la existencia/madurez de pruebas de concepto |  |
|  | (para evaluar explotabilidad, no para ejecutar fuera del laboratorio); |  |
|  | 4) asigne la táctica/técnica MITRE; |  |
|  | 5) anote la mitigación que llevará al Reto 3. Lo no resuelto por usted debe |  |
|  | quedar justificado. |  |

---

### [p. 23]

RETO 2:  Análisis de vectores de ataque, ingeniería social y escenarios 
de compromiso
Nota aclaratoria*: Las matrices e instrumentos diligenciados son 
insumos de análisis para preparar el video expositivo. LO que significa 
que estos debe usarlos para estructurar su exposición integrándolos 
como soporte dentro de la presentación, sin sustituir el producto 
principal solicitado (Video). 
 
Ficha del Reto 2
• 
RAC 1: Evaluar vulnerabilidades en infraestructuras digitales mediante la aplicación de 
metodologías de intrusión, pruebas de penetración e ingeniería social, interpretando 
críticamente los vectores de ataque para anticipar escenarios de compromiso y fortalecer la 
postura de seguridad.
• 
Actividad: Analizar el escenario de compromiso: activos críticos, superficies de exposición, 
vectores de ataque, técnicas de ingeniería social, vulnerabilidades, rutas probables e 
impactos.
• 
Evidencia: Video académico/técnico exponiendo el análisis ofensivo con comunicación clara, 
ética y técnicamente sustentada.
• 
Valor: 125 puntos.
1.1 Núcleo conceptual
Consolide estos bloques conceptuales usando los recursos del curso y las 
fuentes públicas que se indican. El objetivo es que cada concepto pueda 
anclarse al caso AgroSmart.
Bloque 
Conceptos clave 
Anclaje en el caso 
Metodologías 
de 
pentesting
PTES, OSSTMM, OWASP WSTG, 
NIST SP 800-115, PTES; fases 
comunes.
¿Qué 
fase 
explica 
el 
escaneo Nmap de la Sec. 
3.2? 
Fases del testing 
ético
Reconocimiento, 
enumeración, 
análisis 
de 
vulnerabilidades, 
explotación, 
post-explotación, 
reporte.
Alcance y ROE 
In-scope / out-of-scope, ventanas, 
técnicas permitidas, parada de 
emergencia.
Superficie 
de 
ataque
Activos, 
puntos 
de 
entrada, 
exposición, fronteras de confianza.
Inventario 
Sec. 
3.1 
y 
diagrama Sec. 2.2. 
Análisis 
de 
vulnerabilidades
CVE, 
CVSS, 
NVD, 
Exploit-DB, 
severidad, priorización.
Banners de la Sec. 3.2 → 
CVE a investigar. 
Marcos de mapeo 
Cyber Kill Chain (Lockheed Martin) 
y 
MITRE 
ATT&CK 
(tácticas/técnicas).
Ubique cada artefacto del 
informe en su fase.
ROE de la Sec. 1.2 del 
caso.
Logs Sec. 3.6 → fases y 
técnicas.

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Bloque |  |  | Conceptos clave |  |  | Anclaje en el caso |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metodologías de pentesting |  |  | PTES, OSSTMM, OWASP WSTG, NIST SP 800-115, PTES; fases comunes. |  |  | ¿Qué fase explica el escaneo Nmap de la Sec. 3.2? |  |  |
| Fases del testing ético |  |  | Reconocimiento, enumeración, análisis de vulnerabilidades, explotación, post-explotación, reporte. |  |  | Ubique cada artefacto del informe en su fase. |  |  |
| Alcance y ROE |  |  | In-scope / out-of-scope, ventanas, técnicas permitidas, parada de emergencia. |  |  | ROE de la Sec. 1.2 del caso. |  |  |
| Superficie de ataque |  |  | Activos, puntos de entrada, exposición, fronteras de confianza. |  |  | Inventario Sec. 3.1 y diagrama Sec. 2.2. |  |  |
| Análisis de vulnerabilidades |  |  | CVE, CVSS, NVD, Exploit-DB, severidad, priorización. |  |  | Banners de la Sec. 3.2 → CVE a investigar. |  |  |
| Marcos de mapeo |  |  | Cyber Kill Chain (Lockheed Martin) y MITRE ATT&CK (tácticas/técnicas). |  |  | Logs Sec. 3.6 → fases y técnicas. |  |  |

---

### [p. 24]

Pensamiento 
adversarial
Ver el sistema como atacante para 
anticipar el compromiso.
Lectura adversarial de los 
logs. 
Ética y legalidad 
Ley 
1273/2009, 
autorización, 
confidencialidad, 
divulgación 
responsable.
Instrumento 1.B — Comparación de metodologías (para diligenciar)
Complete el cuadro contrastando al menos tres metodologías. Servirá de base 
argumental para justificar el enfoque que aplicará en los retos siguientes.
Metodología Enfoque/alcance 
Fases 
principales
usaría en 
AgroSmart 
PTES 
  
  
  
  
OWASP 
WSTG
NIST 
SP 
800-115
Instrumento 1.C — Glosario operativo (plantee 10 definicones de 
conceptos que considere importantes)
Término 
Definición en sus palabras 
Fuente (APA) 
Superficie 
de 
ataque
CVSS
Marco Sec. 1.
Fortalezas 
Cuándo la

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Pensamiento adversarial | Ver el sistema como atacante para anticipar el compromiso. | Lectura adversarial de los logs. |
| --- | --- | --- |
| Ética y legalidad | Ley 1273/2009, autorización, confidencialidad, divulgación responsable. | Marco Sec. 1. |

**Tabla detectada (formato Markdown):**

| Metodología | Enfoque/alcance | Fases principales | Fortalezas |  | Cuándo la |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | usaría en |  |
|  |  |  |  |  | AgroSmart |  |
| PTES |  |  |  |  |  |  |
| OWASP WSTG |  |  |  |  |  |  |
| NIST SP 800-115 |  |  |  |  |  |  |

**Tabla detectada (formato Markdown):**

| Fases |
| --- |
| principales |

**Tabla detectada (formato Markdown):**

|  | Término |  |  | Definición en sus palabras |  |  | Fuente (APA) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Superficie de ataque |  |  |  |  |  |  |  |  |
| CVSS |  |  |  |  |  |  |  |  |

---

### [p. 25]

DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 2
Herramienta 
de 
IA 
utilizada
(p. 
ej. 
Claude, 
ChatGPT, 
Copilot, 
Gemini, 
VictorIA/DOBOT)
(tarea concreta: lluvia de ideas, resumir, explicar un 
CVE, 
revisar 
redacción, 
generar 
tabla, 
depurar 
comando, etc.)
¿Para qué la usé en 
este reto?
Prompt(s) 
principal(es) 
que 
escribí
(transcribir literalmente la(s) instrucción(es) clave)
Resultado/salida que 
me arrojó 
(síntesis del resultado y/o fragmento textual relevante)
¿Cómo 
verifiqué/validé 
esa 
salida?
(fuente cruzada: NVD, ExploitDB, MITRE, lectura del 
curso, prueba propia)
Ajustes críticos que 
hice
(qué corregí, descarté o reinterpreté por criterio propio 
y por qué)
% 
aproximado 
del 
entregable 
apoyado 
en IA
(estimación 
honesta 
y 
declaración 
de 
autoría 
intelectual)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 2 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Herramienta de IA |  |  | (p. ej. Claude, ChatGPT, Copilot, Gemini, |  |
|  | utilizada |  |  | VictorIA/DOBOT) |  |
| ¿Para qué la usé en este reto? |  |  | (tarea concreta: lluvia de ideas, resumir, explicar un CVE, revisar redacción, generar tabla, depurar comando, etc.) |  |  |
| Prompt(s) principal(es) que escribí |  |  | (transcribir literalmente la(s) instrucción(es) clave) |  |  |
| Resultado/salida que me arrojó |  |  | (síntesis del resultado y/o fragmento textual relevante) |  |  |
| ¿Cómo verifiqué/validé esa salida? |  |  | (fuente cruzada: NVD, ExploitDB, MITRE, lectura del curso, prueba propia) |  |  |
|  | Ajustes críticos que |  |  | (qué corregí, descarté o reinterpreté por criterio propio |  |
|  | hice |  |  | y por qué) |  |
| % aproximado del entregable apoyado en IA |  |  | (estimación honesta y declaración de autoría intelectual) |  |  |

**Tabla detectada (formato Markdown):**

| ¿Para qué la usé en |
| --- |
| este reto? |

**Tabla detectada (formato Markdown):**

| ¿Cómo |
| --- |
| verifiqué/validé esa |

**Tabla detectada (formato Markdown):**

| (fuente cruzada: NVD, ExploitDB, MITRE, lectura del |
| --- |
| curso, prueba propia) |

**Tabla detectada (formato Markdown):**

| (estimación honesta y declaración de autoría |
| --- |
| intelectual) |

**Tabla detectada (formato Markdown):**

| entregable apoyado |
| --- |
| en IA |

---

### [p. 26]

Análisis de vectores de ataque, ingeniería social y escenarios de 
compromiso
Este es el reto analítico central. Usted no explota nada todavía: razona como 
adversario sobre los insumos de la Sec. 3 y deja todo documentado en los 
instrumentos siguientes. Cada celda que llene debe poder defenderse con una 
pista del informe y una fuente pública.
2.1 Identificación y valoración de activos críticos
Valore cada activo por su criticidad en confidencialidad, integridad y 
disponibilidad (C/I/D), de 1 (baja) a 5 (alta), y justifique.
ID/Activo 
Función de
negocio
A-01 
Portal 
web
Pedidos 
B2B 
/ 
dashboard
A-07 PLC riego Riego 
del 
cultivo 
(OT)
2.2 Superficie de exposición
Liste los puntos de entrada y fronteras de confianza. Acompañe con el 
diagrama lógico que usted dibuje de la Sec. 2.2.
Punto de
Dominio 
(DMZ/IT/IoT)
entrada
pista 
Apache 
2.4.49 
(80/443)
DMZ 
Internet 
Banner 
de 
versión 
vulnerable (Sec. 3.2)
2.3 Matriz de vulnerabilidades (CVE / CVSS)
Para cada hallazgo, investigue el CVE en NVD, valide en Exploit-DB y registre 
el vector y puntaje CVSS. Recuerde: el informe le da la pista 
(banner/comportamiento); usted aporta el identificador y la severidad. No se 
incluyen exploits: se documenta la vulnerabilidad y su severidad.
C 
I 
D 
Criticidad y justificación
Exposición 
(Internet/Interna)
Observación /

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| ID/Activo |  | Función de |  | C | I | D | Criticidad y justificación |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | negocio |  |  |  |  |  |
| A-01 Portal web | Pedidos B2B / dashboard |  |  |  |  |  |  |
| A-07 PLC riego | Riego del cultivo (OT) |  |  |  |  |  |  |

**Tabla detectada (formato Markdown):**

|  | Punto de |  |  | Dominio |  |  | Exposición |  |  | Observación / |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | entrada |  |  | (DMZ/IT/IoT) |  |  | (Internet/Interna) |  |  | pista |  |
| Apache 2.4.49 (80/443) |  |  | DMZ |  |  | Internet |  |  | Banner de versión vulnerable (Sec. 3.2) |  |  |

---

### [p. 27]

Activo 
Hallazgo (pista
CVE / 
referencia
del informe)
A-01 Web 
Apache 
2.4.49 
(banner)
Sec. 3.2
A-01 Web 
Error 
SQL 
en 
productos.php
App flaw (sin 
CVE)
A-03 IT 
SMBv1 habilitado 
  
  
  
Sec. 3.2 
A-06 IoT 
Cámara 
Boa 
fw 
v5.2.0
Sec. 3.5
Cómo investigar un CVE (procedimiento sugerido) 
1) Tome el producto y versión del banner.  
2) Búsquelo en NVD (nvd.nist.gov) y registre el CVE-ID.
3) Lea el vector CVSS y deduzca por qué tiene esa severidad.  
4) Verifique en Exploit-DB si existe PoC pública (a efectos de evaluar 
explotabilidad/madurez, no para ejecutarla aquí).
5) Mapee a una técnica MITRE ATT&CK.  
6) Anote la recomendación de mitigación para el Reto 3.
Vector 
CVSS v3.1
Punt./Sev. Evidencia
Sec. 3.3c

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Activo |  | Hallazgo (pista |  |  | CVE / |  |  | Vector |  | Punt./Sev. | Evidencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | del informe) |  |  | referencia |  |  | CVSS v3.1 |  |  |  |
| A-01 Web | Apache 2.4.49 (banner) |  |  |  |  |  |  |  |  |  | Sec. 3.2 |
| A-01 Web | Error SQL en productos.php |  |  | App flaw (sin CVE) |  |  |  |  |  |  | Sec. 3.3c |
| A-03 IT | SMBv1 habilitado |  |  |  |  |  |  |  |  |  | Sec. 3.2 |
| A-06 IoT | Cámara Boa fw v5.2.0 |  |  |  |  |  |  |  |  |  | Sec. 3.5 |

**Tabla detectada (formato Markdown):**

|  | Cómo investigar un CVE (procedimiento sugerido) |  |
| --- | --- | --- |
|  | 1) Tome el producto y versión del banner. |  |
|  | 2) Búsquelo en NVD (nvd.nist.gov) y registre el CVE-ID. |  |
|  | 3) Lea el vector CVSS y deduzca por qué tiene esa severidad. |  |
|  | 4) Verifique en Exploit-DB si existe PoC pública (a efectos de evaluar |  |
|  | explotabilidad/madurez, no para ejecutarla aquí). |  |
|  | 5) Mapee a una técnica MITRE ATT&CK. |  |
|  | 6) Anote la recomendación de mitigación para el Reto 3. |  |

---

### [p. 28]

2.4 Vectores de ataque
Vector 
Activo 
objetivo
Precondición 
Resultado 
para 
el 
adversario
Inyección SQL 
A-01 
Parámetro 
no 
saneado
2.5 Análisis de ingeniería social
Use el informe OSINT (Sec. 3.4) y el correo sospechoso reportado por 
Contabilidad. Analice; no ejecute ingeniería social sobre personas reales.
Técnica 
(phishing/pretextin
Objetivo
(rol)
g/…)
Pretexting 
(suplantar 
TI)
Contabilid
ad
Concientizac
ión 
+ 
verificación
2.6 Mapeo a Cyber Kill Chain
Reconstruya la cadena del compromiso probable (apoyándose en la lectura 
adversarial de los logs, Sec. 3.6). Asocie cada fase con una acción, un activo 
y la pista que la sustenta.
Fase (Lockheed
Acción del adversario en
Activo 
Pista / 
evidencia 
1. Reconnaissance 
  
  
  
2. Weaponization 
  
  
  
3. Delivery 
  
  
  
4. Exploitation 
  
  
  
5. Installation
Martin)
AgroSmart
Pista que lo 
respalda
Acceso/lectura 
de BD
Sec. 3.3c
Can
Pretexto 
Indicador
Mitigación
al
de 
comprom
humana
iso
Corr
eo
“Actualice 
credencial
es”
Dominio 
similar 
/ 
urgencia

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Vector | Activo objetivo | Precondición | Resultado para el adversario |  | Pista que lo respalda |
| --- | --- | --- | --- | --- | --- |
| Inyección SQL | A-01 | Parámetro no saneado | Acceso/lectura de BD |  | Sec. 3.3c |

**Tabla detectada (formato Markdown):**

| Activo |
| --- |
| objetivo |

**Tabla detectada (formato Markdown):**

| Pista que lo |
| --- |
| respalda |

**Tabla detectada (formato Markdown):**

| Técnica (phishing/pretextin g/…) | Objetivo (rol) | Can al | Pretexto |  | Indicador |  | Mitigación humana |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | de |  |  |
|  |  |  |  |  | comprom |  |  |
|  |  |  |  |  | iso |  |  |
| Pretexting (suplantar TI) | Contabilid ad | Corr eo | “Actualice credencial es” | Dominio similar / urgencia |  |  | Concientizac ión + verificación |

**Tabla detectada (formato Markdown):**

| Técnica |
| --- |
| (phishing/pretextin |
| g/…) |

**Tabla detectada (formato Markdown):**

| Objetivo |
| --- |
| (rol) |

**Tabla detectada (formato Markdown):**

| Can |
| --- |
| al |

**Tabla detectada (formato Markdown):**

| Mitigación |
| --- |
| humana |

**Tabla detectada (formato Markdown):**

|  | Fase (Lockheed |  |  | Acción del adversario en AgroSmart | Activo |  | Pista / |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Martin) |  |  |  |  |  | evidencia |  |
| 1. Reconnaissance |  |  |  |  |  |  |  |  |
| 2. Weaponization |  |  |  |  |  |  |  |  |
| 3. Delivery |  |  |  |  |  |  |  |  |
| 4. Exploitation |  |  |  |  |  |  |  |  |
| 5. Installation |  |  |  |  |  |  |  |  |

---

### [p. 29]

6. 
Command 
& 
Control
7. 
Actions 
on 
Objectives
2.7 Mapeo a MITRE ATT&CK
Para cada paso de la ruta de ataque, identifique la táctica, la técnica (ID 
Txxxx) y el procedimiento observado/inferido.
Táctica 
Técnica (ID +
nombre)
Initial Access 
T1190 Exploit Public-
Facing App
Initial Access 
T1566 Phishing 
  
Contabilidad 
Lateral 
Movement
T____  
  
A-03
Persistence 
T____ 
(servicio 
nuevo, evento 7045)
Impact / OT 
T____ (manipulación 
de proceso)
2.8 Ruta probable de ataque (attack path)
Narre, paso a paso, la trayectoria más plausible del compromiso (acceso inicial 
→ escalamiento/lateralidad → objetivo en IT y OT/IoT). Acompañe con un 
diagrama de la ruta. Cada salto debe citar la pista que lo habilita.
Paso 
Descripción del salto 
Habilitado por
3)
2.9 Impacto y riesgo
Valore probabilidad e impacto (1–5) y derive el nivel de riesgo. Considere 
impactos de negocio (pedidos), de datos (PII de clientes) y físicos/OT 
(riego/cultivo).
Procedimiento en el
Activo
caso
A-01
A-03
A-07/A-08
Detección
(pista)
posible 
(insumo Reto

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| 6. Command & Control |  |  |  |
| --- | --- | --- | --- |
| 7. Actions on Objectives |  |  |  |

**Tabla detectada (formato Markdown):**

| Táctica |  | Técnica (ID + |  |  | Procedimiento en el |  | Activo |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | nombre) |  |  | caso |  |  |
| Initial Access | T1190 Exploit Public- Facing App |  |  |  |  |  | A-01 |
| Initial Access | T1566 Phishing |  |  |  |  |  | Contabilidad |
| Lateral Movement | T____ |  |  |  |  |  | A-03 |
| Persistence | T____ (servicio nuevo, evento 7045) |  |  |  |  |  | A-03 |
| Impact / OT | T____ (manipulación de proceso) |  |  |  |  |  | A-07/A-08 |

**Tabla detectada (formato Markdown):**

| Paso | Descripción del salto | Habilitado por (pista) |  | Detección |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | posible |  |
|  |  |  |  | (insumo Reto |  |
|  |  |  |  | 3) |  |

**Tabla detectada (formato Markdown):**

| Habilitado por |
| --- |
| (pista) |

---

### [p. 30]

Escenario 
de 
compromiso
Probabilidad Impacto 
Riesgo 
(PxI)
Tipo 
de 
impacto 
(negocio/datos/OT) 
Compromiso 
del 
portal y robo de 
pedidos
Negocio/Datos
Apertura 
no 
autorizada de riego 
(MQTT/PLC)
OT/físico
Guion sugerido para el video (evidencia del Reto 2)
1. Presentación y encuadre ético (alcance, ROE, finalidad defensiva). 
2. Activos críticos y superficie de exposición (con el diagrama). 
3. Vulnerabilidades priorizadas con CVE/CVSS y su sustento. 
4. Ingeniería social: pretexto y por qué funcionaría. 
5. Ruta de ataque mapeada a Cyber Kill Chain y MITRE ATT&CK. 
6. Impacto/riesgo y mensaje de cierre: qué debería preocupar a la gerencia 
y por qué.
DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 2
Herramienta 
de 
IA 
utilizada
(p. 
ej. 
Claude, 
ChatGPT, 
Copilot, 
Gemini, 
VictorIA/DOBOT)
(tarea concreta: lluvia de ideas, resumir, explicar un 
CVE, 
revisar 
redacción, 
generar 
tabla, 
depurar 
comando, etc.)
¿Para qué la usé en 
este reto?
Prompt(s) 
principal(es) 
que 
escribí
(transcribir literalmente la(s) instrucción(es) clave)
Resultado/salida que 
me arrojó 
(síntesis del resultado y/o fragmento textual relevante)
¿Cómo 
verifiqué/validé 
esa 
salida?
(fuente cruzada: NVD, ExploitDB, MITRE, lectura del 
curso, prueba propia)
Ajustes críticos que 
hice
(qué corregí, descarté o reinterpreté por criterio propio 
y por qué)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Escenario de |  | Probabilidad | Impacto |  | Riesgo |  |  | Tipo de impacto |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | compromiso |  |  |  |  | (PxI) |  |  | (negocio/datos/OT) |  |
| Compromiso del portal y robo de pedidos |  |  |  |  |  |  |  | Negocio/Datos |  |  |
| Apertura no autorizada de riego (MQTT/PLC) |  |  |  |  |  |  |  | OT/físico |  |  |

**Tabla detectada (formato Markdown):**

| DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 2 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Herramienta de IA |  |  | (p. ej. Claude, ChatGPT, Copilot, Gemini, |  |
|  | utilizada |  |  | VictorIA/DOBOT) |  |
| ¿Para qué la usé en este reto? |  |  | (tarea concreta: lluvia de ideas, resumir, explicar un CVE, revisar redacción, generar tabla, depurar comando, etc.) |  |  |
| Prompt(s) principal(es) que escribí |  |  | (transcribir literalmente la(s) instrucción(es) clave) |  |  |
| Resultado/salida que me arrojó |  |  | (síntesis del resultado y/o fragmento textual relevante) |  |  |
| ¿Cómo verifiqué/validé esa salida? |  |  | (fuente cruzada: NVD, ExploitDB, MITRE, lectura del curso, prueba propia) |  |  |
|  | Ajustes críticos que |  |  | (qué corregí, descarté o reinterpreté por criterio propio |  |
|  | hice |  |  | y por qué) |  |

**Tabla detectada (formato Markdown):**

| ¿Para qué la usé en |
| --- |
| este reto? |

**Tabla detectada (formato Markdown):**

| (fuente cruzada: NVD, ExploitDB, MITRE, lectura del |
| --- |
| curso, prueba propia) |

---

### [p. 31]

> _Pagina sin capa de texto: contenido transcrito por OCR._

of,
¥ 7 WN Y
ww Vv
Y 5
M eee Vv

Universidad Nacional
Y), abierta y 2 Distancia \4

Ni, acreDITADA
Bl) EN ALTA CALIDAD &

AUTODIRIGIDOS

y declaraci6n de_  autoria

aproximado' del . - h
entregable apoyado (estimacion honesta
en IA intelectual)

%

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | % aproximado del |  | (estimación honesta y declaración de autoría intelectual) |
| --- | --- | --- | --- |
|  | entregable apoyado |  |  |
|  | en IA |  |  |

**Tabla detectada (formato Markdown):**

| (estimación honesta y declaración de autoría |
| --- |
| intelectual) |

---

### [p. 32]

RETO 3: Diseño de detección, defensa y fortalecimiento de la postura
Ficha del Reto 3
• RAC 2: Diseñar esquemas integrales de detección, identificación y 
gestión de ataques. 
• Actividad: Diseñar estrategias de detección, defensa, hardening, 
monitoreo, alerta, mitigación y respuesta, a partir de los vectores y 
escenarios del Reto 2.
• Evidencia: Informe técnico de diseño defensivo con controles 
preventivos y detectivos, monitoreo, reglas de detección, hardening y 
respuesta básica.
• Valor: 125 puntos.
La clave de este reto es la trazabilidad: cada control que proponga debe 
responder a un vector identificado en el Reto 2. No se evalúa una lista genérica 
de buenas prácticas, sino la coherencia entre amenaza y defensa.
3.1 Matriz de trazabilidad vector → control
Este es el instrumento articulador del informe. Vincule cada vector del Reto 2 
con controles preventivos y detectivos y con un marco de referencia (CIS 
Controls, NIST CSF o ISO/IEC 27001).
Vector 
(Reto 2)
Control 
preventivo
Activo 
protegido 
SQLi 
en 
portal
Validación/consultas 
parametrizadas; 
WAF
Alerta 
por 
patrón 
SQL 
en WAF/log
3.2 Hardening por dominio (checklist para diligenciar)
a) Web / LAMP
Acción de hardening 
¿Aplica?
(S/N)
Actualizar Apache a versión 
sin la CVE identificada
S
Control 
detectivo
Marco 
(CIS/NIST/ISO)
CIS 16 / OWASP 
A-01
Justificación / vector
Verificación
que mitiga

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Vector |  |  | Control |  |  | Control |  |  | Marco |  |  | Activo |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (Reto 2) |  |  | preventivo |  |  | detectivo |  |  | (CIS/NIST/ISO) |  |  | protegido |  |
| SQLi en portal |  |  | Validación/consultas parametrizadas; WAF |  |  | Alerta por patrón SQL en WAF/log |  |  | CIS 16 / OWASP |  |  | A-01 |  |  |

**Tabla detectada (formato Markdown):**

| Acción de hardening |  | ¿Aplica? |  |  | Justificación / vector |  | Verificación |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | (S/N) |  |  | que mitiga |  |  |
| Actualizar Apache a versión sin la CVE identificada | S |  |  |  |  |  |  |

---

### [p. 33]

Quitar /dbadmin y /backup 
de exposición pública
Cabeceras 
de 
seguridad 
(CSP, 
HSTS, 
X-Frame-
Options)
Validación 
de 
carga 
de 
archivos 
(tipo/MIME/extensión)
b) IT / Windows
Acción de hardening 
¿Aplica? 
Justificación / vector
Deshabilitar SMBv1 
  
  
  
Política 
de 
bloqueo 
por 
intentos fallidos / MFA en 
RDP
Segmentación 
IT 
↔ 
IoT 
(VLAN/firewall)
c) IoT / OT
Acción de hardening 
¿Aplica? 
Justificación / vector
Cerrar 
Telnet 
(23) 
en 
gateway; usar SSH/HTTPS
Cambiar 
credenciales 
por 
defecto de cámaras/gateway
Autenticar/segregar MQTT; 
deshabilitar acceso anónimo
Aislar Modbus/PLC en red OT 
con control de acceso
Verificación
que mitiga
Verificación
que mitiga

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Quitar /dbadmin y /backup de exposición pública |  |  |  |
| --- | --- | --- | --- |
| Cabeceras de seguridad (CSP, HSTS, X-Frame- Options) |  |  |  |
| Validación de carga de archivos (tipo/MIME/extensión) |  |  |  |

**Tabla detectada (formato Markdown):**

| Acción de hardening | ¿Aplica? |  | Justificación / vector |  | Verificación |
| --- | --- | --- | --- | --- | --- |
|  |  |  | que mitiga |  |  |
| Deshabilitar SMBv1 |  |  |  |  |  |
| Política de bloqueo por intentos fallidos / MFA en RDP |  |  |  |  |  |
| Segmentación IT ↔ IoT (VLAN/firewall) |  |  |  |  |  |

**Tabla detectada (formato Markdown):**

| Acción de hardening | ¿Aplica? |  | Justificación / vector |  | Verificación |
| --- | --- | --- | --- | --- | --- |
|  |  |  | que mitiga |  |  |
| Cerrar Telnet (23) en gateway; usar SSH/HTTPS |  |  |  |  |  |
| Cambiar credenciales por defecto de cámaras/gateway |  |  |  |  |  |
| Autenticar/segregar MQTT; deshabilitar acceso anónimo |  |  |  |  |  |
| Aislar Modbus/PLC en red OT con control de acceso |  |  |  |  |  |

---

### [p. 34]

3.3 Reglas de detección
Defina la lógica de detección para los eventos clave del caso. Puede expresarla 
en pseudo-Sigma/Snort (descriptiva): fuente de log, condición y respuesta. 
No requiere desplegarla; debe ser técnicamente correcta y trazable al vector.
Nombre de la
Fuente de
Condición de disparo
regla
log
alerta 
Fuerza bruta en 
/admin
Apache 
access.log
≥ N POST /admin/login 
en < T seg desde misma 
IP
Alta 
Alerta + 
bloqueo 
temporal 
Pulverización 
de credenciales 
IT
Windows 
4625 
Múltiples 
4625 
mismo 
usuario distintos orígenes
MQTT 
no 
autorizado
Broker MQTT CONNECT 
anónimo 
+ 
PUBLISH en topic /cmd
Crítica 
Bloqueo 
+ alerta 
OT
3.4 Plan de monitoreo y alertamiento
Fuente /
Qué vigila 
Frecuencia 
Umbral de
sensor
WAF / logs web 
Inyección, fuerza 
bruta
EDR/SIEM IT 
Logon 
anómalo, 
servicios nuevos
3.5 Procedimiento básico de respuesta (NIST SP 800-61)
Trace el playbook para el escenario más crítico del caso (a su elección: 
compromiso del portal o manipulación del riego).
Fase (NIST
800-61) 
Acciones concretas en
AgroSmart
Preparación
Severidad Acción /
(lógica)
Alta 
Alerta 
SOC
Responsable
alerta
Tiempo real
Tiempo real
Responsable Evidencia/registro

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Nombre de la |  |  | Fuente de |  |  | Condición de disparo |  | Severidad |  | Acción / |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | regla |  |  | log |  |  | (lógica) |  |  |  | alerta |  |
| Fuerza bruta en /admin |  |  | Apache access.log |  |  | ≥ N POST /admin/login en < T seg desde misma IP |  |  | Alta | Alerta + bloqueo temporal |  |  |
| Pulverización de credenciales IT |  |  | Windows 4625 |  |  | Múltiples 4625 mismo usuario distintos orígenes |  |  | Alta | Alerta SOC |  |  |
| MQTT no autorizado |  |  | Broker MQTT |  |  | CONNECT anónimo + PUBLISH en topic /cmd |  |  | Crítica | Bloqueo + alerta OT |  |  |

**Tabla detectada (formato Markdown):**

|  | Fuente / |  | Qué vigila | Frecuencia |  | Umbral de |  | Responsable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | sensor |  |  |  |  | alerta |  |  |
| WAF / logs web |  |  | Inyección, fuerza bruta | Tiempo real |  |  |  |  |
| EDR/SIEM IT |  |  | Logon anómalo, servicios nuevos | Tiempo real |  |  |  |  |

**Tabla detectada (formato Markdown):**

|  | Fase (NIST |  |  | Acciones concretas en |  | Responsable | Evidencia/registro |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 800-61) |  |  | AgroSmart |  |  |  |
| Preparación |  |  |  |  |  |  |  |

---

### [p. 35]

Detección 
y 
análisis
Contención 
  
  
  
Erradicación 
  
  
  
Recuperación 
  
  
  
Lecciones 
aprendidas
Criterio de calidad 
El informe se valora por: coherencia con el análisis del Reto 2, pertinencia 
de los controles, calidad técnica, viabilidad de implementación y aporte real 
al fortalecimiento de la postura. Evite controles genéricos sin vínculo con 
un vector concreto.
DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 3
Herramienta 
de 
IA 
utilizada
(p. 
ej. 
Claude, 
ChatGPT, 
Copilot, 
Gemini, 
VictorIA/DOBOT)
(tarea concreta: lluvia de ideas, resumir, explicar un 
CVE, 
revisar 
redacción, 
generar 
tabla, 
depurar 
comando, etc.)
¿Para qué la usé en 
este reto?
Prompt(s) 
principal(es) 
que 
escribí
(transcribir literalmente la(s) instrucción(es) clave)
Resultado/salida que 
me arrojó 
(síntesis del resultado y/o fragmento textual relevante)
¿Cómo 
verifiqué/validé 
esa 
salida?
(fuente cruzada: NVD, ExploitDB, MITRE, lectura del 
curso, prueba propia)
Ajustes críticos que 
hice
(qué corregí, descarté o reinterpreté por criterio propio 
y por qué)
% 
aproximado 
del 
entregable 
apoyado 
en IA
(estimación 
honesta 
y 
declaración 
de 
autoría 
intelectual)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Detección y análisis |  |  |  |
| --- | --- | --- | --- |
| Contención |  |  |  |
| Erradicación |  |  |  |
| Recuperación |  |  |  |
| Lecciones aprendidas |  |  |  |

**Tabla detectada (formato Markdown):**

|  | Criterio de calidad |  |
| --- | --- | --- |
|  | El informe se valora por: coherencia con el análisis del Reto 2, pertinencia |  |
|  | de los controles, calidad técnica, viabilidad de implementación y aporte real |  |
|  | al fortalecimiento de la postura. Evite controles genéricos sin vínculo con |  |
|  | un vector concreto. |  |

**Tabla detectada (formato Markdown):**

| DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 3 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Herramienta de IA |  |  | (p. ej. Claude, ChatGPT, Copilot, Gemini, |  |
|  | utilizada |  |  | VictorIA/DOBOT) |  |
| ¿Para qué la usé en este reto? |  |  | (tarea concreta: lluvia de ideas, resumir, explicar un CVE, revisar redacción, generar tabla, depurar comando, etc.) |  |  |
| Prompt(s) principal(es) que escribí |  |  | (transcribir literalmente la(s) instrucción(es) clave) |  |  |
| Resultado/salida que me arrojó |  |  | (síntesis del resultado y/o fragmento textual relevante) |  |  |
| ¿Cómo verifiqué/validé esa salida? |  |  | (fuente cruzada: NVD, ExploitDB, MITRE, lectura del curso, prueba propia) |  |  |
|  | Ajustes críticos que |  |  | (qué corregí, descarté o reinterpreté por criterio propio |  |
|  | hice |  |  | y por qué) |  |
| % aproximado del entregable apoyado en IA |  |  | (estimación honesta y declaración de autoría intelectual) |  |  |

**Tabla detectada (formato Markdown):**

| ¿Para qué la usé en |
| --- |
| este reto? |

**Tabla detectada (formato Markdown):**

| (fuente cruzada: NVD, ExploitDB, MITRE, lectura del |
| --- |
| curso, prueba propia) |

**Tabla detectada (formato Markdown):**

| (estimación honesta y declaración de autoría |
| --- |
| intelectual) |

**Tabla detectada (formato Markdown):**

| entregable apoyado |
| --- |
| en IA |

---

### [p. 36]

> _Pagina sin capa de texto: contenido transcrito por OCR._

y y
Vv y,
Wy iW
WA WA
w WA
Y, Universidad Nacional \%
yY Abierta y a Distancia \4
N \7
Sj) ACREDITADA

SY AC IF
AUTODIRIGIDOS

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 37]

RETO 4: Planificación de la intrusión y emulación adversaria
Recordatorio ético y de alcance (obligatorio) 
Este reto no requiere máquina virtual ni ejecución de herramientas 
ofensivas. Toda la emulación adversaria es documental: usted declara el 
procedimiento que un adversario ejecutaría, la señal que ese procedimiento 
dejaría en los registros del caso y si el control diseñado en el Reto 3 
alcanzaría a detectarlo. 
La ejecución técnica real ocurre exclusivamente en el Reto 5, dentro del 
Cyber Range autorizado del Anexo A. Está prohibido ejecutar cualquier 
técnica contra sistemas reales, de la universidad o de terceros. Respete la 
ROE de la Sec. 1.2 y el criterio de parada de emergencia.
La ingeniería social se analiza y se emula en papel: no se contacta, no se 
prueba y no se envía nada a personas reales.
Ficha del Reto 4
• RAC 3: Construir estrategias técnicas de protección y respuesta ante 
eventos o incidentes de ciberseguridad, articulando herramientas 
especializadas con marcos de trabajo defensivos y ofensivos, 
promoviendo la innovación, la acción ética y la mejora continua en la 
defensa de los activos informáticos. 
• Actividad: Planificar el ejercicio de intrusión y validar el diseño 
defensivo del Reto 3 mediante emulación adversaria controlada sobre el 
caso AgroSmart del Sumapaz S.A.S., definiendo alcance, reglas de 
compromiso y autorización ética, mapeando las técnicas adversarias con 
MITRE ATT&CK y Cyber Kill Chain, contrastando cada técnica emulada 
con los controles y reglas de detección propuestos, y estableciendo 
métricas de postura que orienten la ejecución posterior en el Cyber 
Range. 
• Evidencia: Informe técnico de planificación y emulación adversaria, en 
el que el estudiante construye estrategias técnicas de protección y 
respuesta articulando marcos ofensivos y defensivos, al definir el 
alcance y las reglas de compromiso del ejercicio, verificar la capacidad 
real de detección de los controles diseñados y proponer métricas y 
brechas priorizadas que sustenten la mejora continua y la actuación 
ética en la defensa de los activos informáticos. 
• Valor: 100 puntos.

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Recordatorio ético y de alcance (obligatorio) |  |
| --- | --- | --- |
|  | Este reto no requiere máquina virtual ni ejecución de herramientas |  |
|  | ofensivas. Toda la emulación adversaria es documental: usted declara el |  |
|  | procedimiento que un adversario ejecutaría, la señal que ese procedimiento |  |
|  | dejaría en los registros del caso y si el control diseñado en el Reto 3 |  |
|  | alcanzaría a detectarlo. |  |
|  | La ejecución técnica real ocurre exclusivamente en el Reto 5, dentro del |  |
|  | Cyber Range autorizado del Anexo A. Está prohibido ejecutar cualquier |  |
|  | técnica contra sistemas reales, de la universidad o de terceros. Respete la |  |
|  | ROE de la Sec. 1.2 y el criterio de parada de emergencia. |  |
|  | La ingeniería social se analiza y se emula en papel: no se contacta, no se |  |
|  | prueba y no se envía nada a personas reales. |  |

---

### [p. 38]

4.1 Propósito y encuadre del reto
En el Reto 2 usted reconstruyó cómo podría ser comprometida AgroSmart. En 
el Reto 3 propuso cómo defenderla. Este reto responde a la pregunta que 
ningún diseño defensivo puede eludir: ¿el control que usted propuso 
realmente vería pasar el ataque que usted mismo describió?
La emulación adversaria consiste en tomar técnicas concretas de un 
adversario, declarar el procedimiento con el que se materializarían sobre los 
activos del caso y confrontarlo con la telemetría disponible y las reglas de 
detección diseñadas. Su resultado no es un compromiso demostrado, sino un 
veredicto de visibilidad: la técnica se detecta, se detecta parcialmente o no 
deja rastro alguno. Ese tercer resultado, la brecha, es el hallazgo más valioso 
del reto.
El producto de esta fase es, además, el plan que gobierna el Reto 5. Un pentest 
sin alcance escrito, sin ventana de ejecución, sin manejo de evidencias y sin 
criterio de parada no es un pentest: es una intrusión. Aquí se redacta ese 
encuadre.
4.2 Instrumento 4.A — Acta de alcance y reglas de compromiso
Complete el Instrumento 1.A de la Sec. 1.2 con el nivel de detalle de un 
compromiso profesional. Esta acta se anexa al informe y se confirma, sin 
modificaciones sustanciales, al inicio del Reto 5.
Elemento de la
Definición acordada por el
ROE
estudiante
legal 
Objetivo 
del 
compromiso
Activos en alcance 
(ID, IP, servicio)
Activos y segmentos 
excluidos
Técnicas permitidas 
 
 
Técnicas prohibidas 
 
 
Ventana de ejecución  
 
Manejo, custodia e 
integridad 
de 
evidencias
Tratamiento de datos 
personales 
hallados 
(Ley 1581 de 2012)
Justificación técnica o

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Elemento de la |  |  | Definición acordada por el |  |  | Justificación técnica o |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ROE |  |  | estudiante |  |  | legal |  |
| Objetivo del compromiso |  |  |  |  |  |  |  |  |
| Activos en alcance (ID, IP, servicio) |  |  |  |  |  |  |  |  |
| Activos y segmentos excluidos |  |  |  |  |  |  |  |  |
| Técnicas permitidas |  |  |  |  |  |  |  |  |
| Técnicas prohibidas |  |  |  |  |  |  |  |  |
| Ventana de ejecución |  |  |  |  |  |  |  |  |
| Manejo, custodia e integridad de evidencias |  |  |  |  |  |  |  |  |
| Tratamiento de datos personales hallados (Ley 1581 de 2012) |  |  |  |  |  |  |  |  |

---

### [p. 39]

Elemento de la
Definición acordada por el
ROE
estudiante
legal 
Contacto 
de 
escalamiento 
ante 
incidente
Criterio de parada de 
emergencia
4.3 Instrumento 4.B — Plan de pruebas de intrusión
Defina el plan que ejecutará en el Reto 5. Cada decisión debe estar justificada 
frente al escenario LAMP, IT e IoT/OT del caso; no se aceptan metodologías 
nombradas sin argumento de pertinencia.
Componente del plan 
Definición 
Criterio de decisión
aplicado 
Metodología 
seleccionada 
(PTES, 
OWASP WSTG, NIST SP 
800-115, OSSTMM)
Fases 
previstas 
y 
entregable de cada fase
Priorización de objetivos 
por dominio (DMZ, IT, 
IoT/OT)
Herramientas por fase y 
justificación de uso
Restricciones operativas 
sobre el segmento OT
Estimación de esfuerzo y 
secuencia de ejecución
Riesgos 
del 
propio 
ejercicio y medidas de 
contención
Criterios de éxito del 
compromiso
Riesgo del ejercicio sobre entornos OT 
El controlador de riego (A-07, Modbus/TCP sin autenticación) y el broker de 
telemetría (A-08) son activos ciberfísicos: una prueba mal calibrada no 
genera un error de aplicación, genera una consecuencia física sobre el 
cultivo. Su plan debe declarar explícitamente qué operaciones sobre OT
Justificación técnica o

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Elemento de la |  |  | Definición acordada por el |  |  | Justificación técnica o |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ROE |  |  | estudiante |  |  | legal |  |
| Contacto de escalamiento ante incidente |  |  |  |  |  |  |  |  |
| Criterio de parada de emergencia |  |  |  |  |  |  |  |  |

**Tabla detectada (formato Markdown):**

| Componente del plan | Definición |  | Criterio de decisión |  |
| --- | --- | --- | --- | --- |
|  |  |  | aplicado |  |
| Metodología seleccionada (PTES, OWASP WSTG, NIST SP 800-115, OSSTMM) |  |  |  |  |
| Fases previstas y entregable de cada fase |  |  |  |  |
| Priorización de objetivos por dominio (DMZ, IT, IoT/OT) |  |  |  |  |
| Herramientas por fase y justificación de uso |  |  |  |  |
| Restricciones operativas sobre el segmento OT |  |  |  |  |
| Estimación de esfuerzo y secuencia de ejecución |  |  |  |  |
| Riesgos del propio ejercicio y medidas de contención |  |  |  |  |
| Criterios de éxito del compromiso |  |  |  |  |

**Tabla detectada (formato Markdown):**

|  | Riesgo del ejercicio sobre entornos OT |  |
| --- | --- | --- |
|  | El controlador de riego (A-07, Modbus/TCP sin autenticación) y el broker de |  |
|  | telemetría (A-08) son activos ciberfísicos: una prueba mal calibrada no |  |
|  | genera un error de aplicación, genera una consecuencia física sobre el |  |
|  | cultivo. Su plan debe declarar explícitamente qué operaciones sobre OT |  |

---

### [p. 40]

quedan restringidas a lectura y por qué. En un entorno productivo real, esa 
decisión se documenta y se firma antes de tocar el primer registro.
4.4 Instrumento 4.C — Selección de casos de emulación adversaria
Seleccione entre ocho y diez técnicas para emular, distribuidas en los tres 
dominios del caso y en al menos cuatro tácticas distintas de MITRE ATT&CK. 
La tabla trae cuatro filas sembradas como referencia de formato y profundidad 
esperada; complete las restantes a partir de su propio análisis del Reto 2. Los 
identificadores de técnica deben verificarse en la matriz oficial de MITRE 
(Enterprise e ICS, según corresponda).
# 
Táctica 
ATT&CK
Técnica (ID y
nombre)
sustenta 
E-01 
Acceso 
inicial
T1190 
— 
Explotación 
de 
aplicación 
expuesta
E-02 
Acceso con 
credenciales
T1110 — Fuerza 
bruta 
/ 
pulverización
DMZ + IT 
37 POST a /admin/login en 40 s (Sec. 
3.6) y eventos 4625 del usuario 
amunoz 
E-03 
Persistencia 
T1505.003 
— 
Componente 
de 
servidor web (web 
shell)
E-04 
Impacto 
(ICS)
T0855 — Mensaje 
de 
comando 
no 
autorizado
IoT / OT 
Modbus/TCP sin autenticación (Sec. 
3.5) 
y 
PUBLISH 
en 
invernadero/riego/cmd (Sec. 3.6) 
E-05 
 
 
 
 
E-06 
 
 
 
 
E-07 
 
 
 
 
E-08 
 
 
 
 
E-09 
 
 
 
 
E-10
4.5 Instrumento 4.D — Matriz de emulación adversaria y validación 
de controles
Es el instrumento central del reto. Para cada técnica seleccionada en 4.C, 
declare el procedimiento de emulación, el control que usted diseñó en el Reto 
3 para contenerla o detectarla, la señal que debería quedar registrada y el 
veredicto de visibilidad. Un control que no produce señal observable no es un 
control detectivo: es una intención.
Convención del veredicto: D = detectado (existe regla y fuente de log que la 
alimenta) · P = parcial (hay evidencia pero no alerta, o la alerta llega tarde o
Dominio 
del caso
Artefacto del anexo que la
DMZ / Web 
LAMP
Banner Apache 2.4.49 (Sec. 3.2) y 
error SQL en productos.php (Sec. 
3.3.c)
DMZ / Web 
LAMP
Carga de archivos sin validación de 
MIME ni extensión (Sec. 3.3.e)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | quedan restringidas a lectura y por qué. En un entorno productivo real, esa |  |
| --- | --- | --- |
|  | decisión se documenta y se firma antes de tocar el primer registro. |  |

**Tabla detectada (formato Markdown):**

| # |  | Táctica |  |  | Técnica (ID y |  |  | Dominio |  |  | Artefacto del anexo que la |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | ATT&CK |  |  | nombre) |  |  | del caso |  |  | sustenta |  |
| E-01 | Acceso inicial |  |  | T1190 — Explotación de aplicación expuesta |  |  | DMZ / Web LAMP |  |  | Banner Apache 2.4.49 (Sec. 3.2) y error SQL en productos.php (Sec. 3.3.c) |  |  |
| E-02 | Acceso con credenciales |  |  | T1110 — Fuerza bruta / pulverización |  |  | DMZ + IT |  |  | 37 POST a /admin/login en 40 s (Sec. 3.6) y eventos 4625 del usuario amunoz |  |  |
| E-03 | Persistencia |  |  | T1505.003 — Componente de servidor web (web shell) |  |  | DMZ / Web LAMP |  |  | Carga de archivos sin validación de MIME ni extensión (Sec. 3.3.e) |  |  |
| E-04 | Impacto (ICS) |  |  | T0855 — Mensaje de comando no autorizado |  |  | IoT / OT |  |  | Modbus/TCP sin autenticación (Sec. 3.5) y PUBLISH en invernadero/riego/cmd (Sec. 3.6) |  |  |
| E-05 |  |  |  |  |  |  |  |  |  |  |  |  |
| E-06 |  |  |  |  |  |  |  |  |  |  |  |  |
| E-07 |  |  |  |  |  |  |  |  |  |  |  |  |
| E-08 |  |  |  |  |  |  |  |  |  |  |  |  |
| E-09 |  |  |  |  |  |  |  |  |  |  |  |  |
| E-10 |  |  |  |  |  |  |  |  |  |  |  |  |

---

### [p. 41]

sin contexto) · N = no detectado (no hay fuente, regla ni registro que lo 
revele).
# 
Técnica 
Procedimiento
Control del
de emulación
Reto 3 
asociado
declarado
E-
01 
T1190 
Solicitud 
manipulada sobre 
el 
parámetro 
categoria 
de 
productos.php 
para provocar el 
error de sintaxis 
SQL descrito en el 
anexo
Consultas 
parametrizadas, 
WAF 
y 
actualización de 
Apache
E-
02 
T1110 
Serie de intentos 
de 
autenticación 
contra 
/admin/login.php 
sin 
bloqueo 
por 
reintentos 
y 
reutilización de la 
credencial 
contra 
el segmento IT
Bloqueo 
por 
intentos 
fallidos, MFA en 
RDP y política 
de contraseñas
E-
03
E-
04
E-
05
E-
06
E-
07
E-
08
E-
09
E-
10
4.6 Instrumento 4.E — Tablero de métricas de postura
Traduzca el resultado de la matriz 4.D a indicadores que un comité directivo 
pueda leer. Declare la fórmula empleada: una métrica sin fórmula no es 
verificable ni comparable en el tiempo.
Indicador 
Fórmula o método
Interpretación 
para la gerencia 
Cobertura 
ATT&CK 
global
de cálculo
Técnicas 
con 
veredicto D / técnicas 
emuladas
Fuente de log
Veredicto 
Brecha 
identificada
y señal 
esperada
Apache 
access.log 
y 
error.log: patrón 
de 
comilla 
simple 
con 
respuesta 
500 
desde 
una 
misma IP
Apache 
access.log 
(umbral N/T) y 
Windows 
Security 
4625 
seguido de 4624 
tipo 3
Resultado
obtenido

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| # | Técnica |  | Procedimiento |  |  | Control del |  |  | Fuente de log |  | Veredicto | Brecha identificada |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | de emulación |  |  | Reto 3 |  |  | y señal |  |  |  |
|  |  |  | declarado |  |  | asociado |  |  | esperada |  |  |  |
| E- 01 | T1190 | Solicitud manipulada sobre el parámetro categoria de productos.php para provocar el error de sintaxis SQL descrito en el anexo |  |  | Consultas parametrizadas, WAF y actualización de Apache |  |  | Apache access.log y error.log: patrón de comilla simple con respuesta 500 desde una misma IP |  |  |  |  |
| E- 02 | T1110 | Serie de intentos de autenticación contra /admin/login.php sin bloqueo por reintentos y reutilización de la credencial contra el segmento IT |  |  | Bloqueo por intentos fallidos, MFA en RDP y política de contraseñas |  |  | Apache access.log (umbral N/T) y Windows Security 4625 seguido de 4624 tipo 3 |  |  |  |  |
| E- 03 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 04 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 05 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 06 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 07 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 08 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 09 |  |  |  |  |  |  |  |  |  |  |  |  |
| E- 10 |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla detectada (formato Markdown):**

| Brecha |
| --- |
| identificada |

**Tabla detectada (formato Markdown):**

| Indicador |  | Fórmula o método |  |  | Resultado |  |  | Interpretación |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | de cálculo |  |  | obtenido |  |  | para la gerencia |  |
| Cobertura ATT&CK global | Técnicas con veredicto D / técnicas emuladas |  |  |  |  |  |  |  |  |

---

### [p. 42]

Indicador 
Fórmula o método
Interpretación 
para la gerencia 
Cobertura 
por 
dominio (DMZ, IT, 
IoT/OT)
de cálculo
Tasa de detección 
parcial
Técnicas 
sin 
visibilidad 
(brecha 
crítica)
Tiempo estimado de 
detección (MTTD)
Fuentes 
de 
log 
requeridas frente a 
fuentes disponibles
Indicador propuesto 
por el estudiante
Sobre la honestidad de la métrica 
Una cobertura del 100 % en un primer ejercicio de emulación casi siempre 
significa que las técnicas se eligieron para confirmar el diseño propio, no 
para ponerlo a prueba. El valor académico y profesional de este reto está 
en encontrar dónde el diseño defensivo del Reto 3 se queda ciego, y el 
segmento IoT/OT del caso, con protocolos sin autenticación y sin registro 
nativo, suele ser ese lugar.
4.7 Instrumento 4.F — Brechas de detección priorizadas y plan de 
cierre
Documente únicamente las brechas con veredicto P o N. Cada una debe tener 
una acción de cierre concreta, un responsable funcional y un criterio de 
verificación.
ID 
Brecha de 
visibilidad
Dominio 
Riesgo 
asociado si
se 
materializa
Resultado
obtenido
Acción de
Prioridad 
Cómo se 
verifica el
cierre 
propuesta
cierre

> [Imagen(es) en la pagina: 1 | xref162 2028x222px]

**Tabla detectada (formato Markdown):**

| Indicador |  | Fórmula o método de cálculo | Resultado obtenido |  |  | Interpretación |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | para la gerencia |  |
| Cobertura por dominio (DMZ, IT, IoT/OT) |  |  |  |  |  |  |  |
| Tasa de detección parcial |  |  |  |  |  |  |  |
| Técnicas sin visibilidad (brecha crítica) |  |  |  |  |  |  |  |
| Tiempo estimado de detección (MTTD) |  |  |  |  |  |  |  |
| Fuentes de log requeridas frente a fuentes disponibles |  |  |  |  |  |  |  |
| Indicador propuesto por el estudiante |  |  |  |  |  |  |  |

**Tabla detectada (formato Markdown):**

|  | Sobre la honestidad de la métrica |  |
| --- | --- | --- |
|  | Una cobertura del 100 % en un primer ejercicio de emulación casi siempre |  |
|  | significa que las técnicas se eligieron para confirmar el diseño propio, no |  |
|  | para ponerlo a prueba. El valor académico y profesional de este reto está |  |
|  | en encontrar dónde el diseño defensivo del Reto 3 se queda ciego, y el |  |
|  | segmento IoT/OT del caso, con protocolos sin autenticación y sin registro |  |
|  | nativo, suele ser ese lugar. |  |

**Tabla detectada (formato Markdown):**

| ID | Brecha de visibilidad | Dominio |  | Riesgo |  | Acción de cierre propuesta | Prioridad | Cómo se verifica el cierre |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | asociado si |  |  |  |  |
|  |  |  |  | se |  |  |  |  |
|  |  |  |  | materializa |  |  |  |  |

**Tabla detectada (formato Markdown):**

| Brecha de |
| --- |
| visibilidad |

**Tabla detectada (formato Markdown):**

| Cómo se |
| --- |
| verifica el |
| cierre |

---

### [p. 43]

4.8 Instrumento 4.G — Criterios de validación técnica para el Reto 5
Este instrumento es el puente formal entre la planificación y la ejecución. 
Traslade al Reto 5 únicamente las hipótesis que requieren comprobación 
práctica, indicando qué evidencia se considerará suficiente. En el informe final 
del Reto 5 deberá responder, una por una, a las hipótesis aquí planteadas.
ID 
Hipótesis técnica a 
validar en Cyber Range
Activo 
objetivo
suficiente
4.9 Estructura del informe técnico (plantilla del entregable)
El entregable es un informe técnico en formato Word o PDF, con tablas 
editables incrustadas, redacción técnica y referencias en normas APA. No se 
aceptan capturas de tablas, enlaces a repositorios externos ni matrices en 
archivos separados.
Sección del informe 
Contenido mínimo esperado 
1. Resumen ejecutivo 
Propósito del ejercicio de planificación, estado general de 
visibilidad de la organización y las tres brechas más 
relevantes, en lenguaje comprensible para la gerencia. 
2. 
Alcance, 
ROE 
y 
encuadre ético-legal
Instrumento 4.A completo, con referencia a la Ley 1273 
de 2009 y a la Ley 1581 de 2012 en el tratamiento de 
los datos hallados. 
3. Plan de pruebas de 
intrusión
Instrumento 4.B, con justificación de la metodología 
frente al escenario híbrido del caso. 
4. Selección de casos de 
emulación
Instrumento 4.C, con la trazabilidad de cada técnica al 
artefacto del anexo que la sustenta. 
5. Matriz de emulación y 
validación de controles
Instrumento 4.D completo, acompañado del análisis 
narrativo de los resultados por dominio. 
6. Mapeo a Cyber Kill 
Chain
Ubicación de las técnicas emuladas en las fases del 
modelo y lectura de en qué fase la organización pierde 
visibilidad. 
7. Tablero de métricas 
de postura
Instrumento 
4.E, 
con 
fórmulas 
declaradas 
e 
interpretación gerencial.
Método de 
validación no
Evidencia que se
considerará
destructivo

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| ID | Hipótesis técnica a validar en Cyber Range | Activo objetivo |  | Método de |  |  | Evidencia que se |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | validación no |  |  | considerará |  |
|  |  |  |  | destructivo |  |  | suficiente |  |

**Tabla detectada (formato Markdown):**

| Hipótesis técnica a |
| --- |
| validar en Cyber Range |

**Tabla detectada (formato Markdown):**

| Activo |
| --- |
| objetivo |

**Tabla detectada (formato Markdown):**

|  | Sección del informe |  |  | Contenido mínimo esperado |  |
| --- | --- | --- | --- | --- | --- |
| 1. Resumen ejecutivo |  |  | Propósito del ejercicio de planificación, estado general de visibilidad de la organización y las tres brechas más relevantes, en lenguaje comprensible para la gerencia. |  |  |
| 2. Alcance, ROE y encuadre ético-legal |  |  | Instrumento 4.A completo, con referencia a la Ley 1273 de 2009 y a la Ley 1581 de 2012 en el tratamiento de los datos hallados. |  |  |
| 3. Plan de pruebas de intrusión |  |  | Instrumento 4.B, con justificación de la metodología frente al escenario híbrido del caso. |  |  |
| 4. Selección de casos de emulación |  |  | Instrumento 4.C, con la trazabilidad de cada técnica al artefacto del anexo que la sustenta. |  |  |
| 5. Matriz de emulación y validación de controles |  |  | Instrumento 4.D completo, acompañado del análisis narrativo de los resultados por dominio. |  |  |
| 6. Mapeo a Cyber Kill Chain |  |  | Ubicación de las técnicas emuladas en las fases del modelo y lectura de en qué fase la organización pierde visibilidad. |  |  |
| 7. Tablero de métricas de postura |  |  | Instrumento 4.E, con fórmulas declaradas e interpretación gerencial. |  |  |

---

### [p. 44]

Sección del informe 
Contenido mínimo esperado 
8. Brechas priorizadas y 
plan de cierre
Instrumento 4.F, con acciones verificables enlazadas a 
los controles del Reto 3. 
9. 
Criterios 
de 
validación para el Reto 5
Instrumento 4.G, con hipótesis formuladas en términos 
comprobables. 
10. 
Conclusiones 
y 
limitaciones
Aporte del ejercicio a la postura de seguridad, límites de 
la emulación documental frente a la validación práctica y 
aprendizajes metodológicos. 
11. Referencias 
Fuentes técnicas y académicas en normas APA: MITRE 
ATT&CK, NVD, metodologías de pruebas de penetración 
y bibliografía del curso. 
12. Declaración de uso 
de IA
Diligenciada según el formato que cierra esta sección, si 
aplica.
Extensión: entre 3.500 y 5.000 palabras, sin contar portada, tablas, 
referencias ni anexos.
Criterio de calidad 
El informe se valora por: rigor y completitud del alcance, las reglas de 
compromiso y la autorización ética; trazabilidad demostrable entre el vector 
analizado en el Reto 2, el control diseñado en el Reto 3 y la técnica emulada 
en este reto; corrección del mapeo a MITRE ATT&CK y Cyber Kill Chain; 
pertinencia y verificabilidad de las métricas propuestas; y capacidad crítica 
para identificar y priorizar las brechas del propio diseño defensivo.
Se penaliza el optimismo no sustentado: declarar como detectada una 
técnica sin identificar la fuente de log que la evidencia y la regla que la 
dispara. Se valora, en cambio, reconocer con argumento técnico dónde el 
diseño propio no alcanza.
DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 4
Herramienta 
de 
IA 
utilizada
(p. 
ej. 
Claude, 
ChatGPT, 
Copilot, 
Gemini, 
VictorIA/DOBOT)
¿Para qué la usé en 
este reto?
(tarea concreta: identificar técnicas ATT&CK, revisar la 
lógica de una regla de detección, contrastar métricas, 
revisar redacción, etc.)
Prompt(s) 
principal(es) 
que 
escribí
(transcribir literalmente la(s) instrucción(es) clave)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Sección del informe |  |  | Contenido mínimo esperado |  |
| --- | --- | --- | --- | --- | --- |
| 8. Brechas priorizadas y plan de cierre |  |  | Instrumento 4.F, con acciones verificables enlazadas a los controles del Reto 3. |  |  |
| 9. Criterios de validación para el Reto 5 |  |  | Instrumento 4.G, con hipótesis formuladas en términos comprobables. |  |  |
| 10. Conclusiones y limitaciones |  |  | Aporte del ejercicio a la postura de seguridad, límites de la emulación documental frente a la validación práctica y aprendizajes metodológicos. |  |  |
| 11. Referencias |  |  | Fuentes técnicas y académicas en normas APA: MITRE ATT&CK, NVD, metodologías de pruebas de penetración y bibliografía del curso. |  |  |
| 12. Declaración de uso de IA |  |  | Diligenciada según el formato que cierra esta sección, si aplica. |  |  |

**Tabla detectada (formato Markdown):**

|  | Criterio de calidad |  |
| --- | --- | --- |
|  | El informe se valora por: rigor y completitud del alcance, las reglas de |  |
|  | compromiso y la autorización ética; trazabilidad demostrable entre el vector |  |
|  | analizado en el Reto 2, el control diseñado en el Reto 3 y la técnica emulada |  |
|  | en este reto; corrección del mapeo a MITRE ATT&CK y Cyber Kill Chain; |  |
|  | pertinencia y verificabilidad de las métricas propuestas; y capacidad crítica |  |
|  | para identificar y priorizar las brechas del propio diseño defensivo. |  |
|  | Se penaliza el optimismo no sustentado: declarar como detectada una |  |
|  | técnica sin identificar la fuente de log que la evidencia y la regla que la |  |
|  | dispara. Se valora, en cambio, reconocer con argumento técnico dónde el |  |
|  | diseño propio no alcanza. |  |

**Tabla detectada (formato Markdown):**

|  | DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 4 |  |  |
| --- | --- | --- | --- |
| Herramienta de IA utilizada |  | (p. ej. Claude, ChatGPT, Copilot, Gemini, VictorIA/DOBOT) |  |
| ¿Para qué la usé en este reto? |  | (tarea concreta: identificar técnicas ATT&CK, revisar la lógica de una regla de detección, contrastar métricas, revisar redacción, etc.) |  |
| Prompt(s) principal(es) que escribí |  | (transcribir literalmente la(s) instrucción(es) clave) |  |

---

### [p. 45]

Resultado/salida que 
me arrojó
(síntesis del resultado y/o fragmento textual relevante)
¿Cómo 
verifiqué/validé 
esa 
salida?
(fuente cruzada: MITRE ATT&CK, NVD, ExploitDB, 
lectura del curso, criterio propio)
Ajustes críticos que 
hice
(qué corregí, descarté o reinterpreté por criterio propio 
y por qué)
% 
aproximado 
del 
entregable 
apoyado 
en IA
(estimación 
honesta 
y 
declaración 
de 
autoría 
intelectual)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Resultado/salida que me arrojó | (síntesis del resultado y/o fragmento textual relevante) |
| --- | --- |
| ¿Cómo verifiqué/validé esa salida? | (fuente cruzada: MITRE ATT&CK, NVD, ExploitDB, lectura del curso, criterio propio) |
| Ajustes críticos que hice | (qué corregí, descarté o reinterpreté por criterio propio y por qué) |
| % aproximado del entregable apoyado en IA | (estimación honesta y declaración de autoría intelectual) |

---

### [p. 46]

RETO 5: Ejecución de pruebas de intrusión en Cyber Range
Recordatorio ético (obligatorio) 
La ejecución ocurre exclusivamente dentro del Cyber Range autorizado del 
Anexo A. Está prohibido ejecutar cualquier técnica contra sistemas reales, 
de la universidad o de terceros. Respete la ROE de la Sec. 1.2 y la parada 
de emergencia.
Ficha del Reto 5
• RAC 3: Construir estrategias técnicas de protección y respuesta, 
articulando herramientas con marcos ofensivos y defensivos, con acción 
ética y mejora continua.
• Actividad: Ejecutar pruebas de intrusión ética en el Cyber Range: 
reconocimiento, identificación de vulnerabilidades, validación controlada 
de vectores, recolección de evidencias, análisis de hallazgos, 
clasificación de severidad y recomendaciones. 
• Evidencia: Informe técnico final de ejecución en Cyber Range.
• Valor: 125 puntos.
5.1 Estructura del informe final (plantilla)
7. Resumen ejecutivo (para la gerencia, sin jerga). 
8. Alcance y ROE confirmados (Instrumentos 1.A y 4.A). 
9. Metodología aplicada (la justificada en el Reto 1). 
10. Reconocimiento y enumeración (hallazgos, no solo comandos). 
11. Identificación y validación controlada de vulnerabilidades. 
12. Bitácora de evidencias con trazabilidad. 
13. Análisis de hallazgos y clasificación de severidad. 
14. Recomendaciones de mitigación (enlazadas a los Retos 3 y 4). 
15. Conclusiones y aporte a la postura de seguridad.
5.2 Plantilla de ejecución por fase (para diligenciar)
Fase 
Objetivo 
Actividad 
realizada
Herramienta 
Resultado 
/ hallazgo 
Reconocimiento 
Mapear 
superficie
Enumeración 
Servicios/versión   
  
  
Análisis de vuln. 
Confirmar CVE
Nmap

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Recordatorio ético (obligatorio) |  |
| --- | --- | --- |
|  | La ejecución ocurre exclusivamente dentro del Cyber Range autorizado del |  |
|  | Anexo A. Está prohibido ejecutar cualquier técnica contra sistemas reales, |  |
|  | de la universidad o de terceros. Respete la ROE de la Sec. 1.2 y la parada |  |
|  | de emergencia. |  |

**Tabla detectada (formato Markdown):**

| Fase | Objetivo |  | Actividad |  | Herramienta |  | Resultado |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | realizada |  |  |  | / hallazgo |  |
| Reconocimiento | Mapear superficie |  |  |  | Nmap |  |  |  |
| Enumeración | Servicios/versión |  |  |  |  |  |  |  |
| Análisis de vuln. | Confirmar CVE |  |  |  |  |  |  |  |

---

### [p. 47]

Validación 
controlada
Probar el vector
Post 
(documentación)
Evidenciar 
impacto
5.3 Bitácora de evidencias
Cada evidencia debe ser trazable: marca de tiempo, acción, herramienta, 
resultado y un hash que garantice integridad.
# 
Fecha/hora 
Acción 
Herramienta 
Resultado 
Hash de 
evidencia
256)
5.4 Matriz de hallazgos y priorización del riesgo
ID 
Hallazgo 
CVE/ref. CVSS Severidad Riesgo de
(Reto 3)
Criterio de calidad  
Se valora la aplicación técnica, la trazabilidad de evidencias, el análisis de 
hallazgos, la priorización del riesgo, la pertinencia de las recomendaciones 
y la mejora de la postura. La calidad de la evidencia (clara, íntegra, 
reproducible) es determinante.
(SHA-
Mitigación
negocio

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| Validación controlada | Probar el vector |  |  |  |
| --- | --- | --- | --- | --- |
| Post (documentación) | Evidenciar impacto |  |  |  |

**Tabla detectada (formato Markdown):**

| # | Fecha/hora | Acción | Herramienta | Resultado | Resultado |  | Hash de |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | evidencia |  |
|  |  |  |  |  |  |  | (SHA- |  |
|  |  |  |  |  |  |  | 256) |  |

**Tabla detectada (formato Markdown):**

|  | Criterio de calidad |  |
| --- | --- | --- |
|  | Se valora la aplicación técnica, la trazabilidad de evidencias, el análisis de |  |
|  | hallazgos, la priorización del riesgo, la pertinencia de las recomendaciones |  |
|  | y la mejora de la postura. La calidad de la evidencia (clara, íntegra, |  |
|  | reproducible) es determinante. |  |

---

### [p. 48]

DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 5
Herramienta de IA 
utilizada
(p. 
ej. 
Claude, 
ChatGPT, 
Copilot, 
Gemini, 
VictorIA/DOBOT)
(tarea concreta: lluvia de ideas, resumir, explicar 
un CVE, revisar redacción, generar tabla, depurar 
comando, etc.)
¿Para qué la usé en 
este reto?
Prompt(s) 
principal(es) 
que 
escribí
(transcribir literalmente la(s) instrucción(es) clave)
Resultado/salida 
que me arrojó
(síntesis del resultado y/o fragmento textual 
relevante)
¿Cómo 
verifiqué/validé esa 
salida?
(fuente cruzada: NVD, ExploitDB, MITRE, lectura 
del curso, prueba propia)
Ajustes críticos que 
hice
(qué corregí, descarté o reinterpreté por criterio 
propio y por qué)
% aproximado del 
entregable apoyado 
en IA
(estimación honesta y declaración de autoría 
intelectual)

> [Imagen(es) en la pagina: 1 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

| DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL — Reto 5 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Herramienta de IA |  |  | (p. ej. Claude, ChatGPT, Copilot, Gemini, |  |
|  | utilizada |  |  | VictorIA/DOBOT) |  |
| ¿Para qué la usé en este reto? |  |  | (tarea concreta: lluvia de ideas, resumir, explicar un CVE, revisar redacción, generar tabla, depurar comando, etc.) |  |  |
| Prompt(s) principal(es) que escribí |  |  | (transcribir literalmente la(s) instrucción(es) clave) |  |  |
|  | Resultado/salida |  |  | (síntesis del resultado y/o fragmento textual |  |
|  | que me arrojó |  |  | relevante) |  |
| ¿Cómo verifiqué/validé esa salida? |  |  | (fuente cruzada: NVD, ExploitDB, MITRE, lectura del curso, prueba propia) |  |  |
|  | Ajustes críticos que |  |  | (qué corregí, descarté o reinterpreté por criterio |  |
|  | hice |  |  | propio y por qué) |  |
| % aproximado del entregable apoyado en IA |  |  | (estimación honesta y declaración de autoría intelectual) |  |  |

**Tabla detectada (formato Markdown):**

| ¿Para qué la usé en |
| --- |
| este reto? |

**Tabla detectada (formato Markdown):**

| (fuente cruzada: NVD, ExploitDB, MITRE, lectura |
| --- |
| del curso, prueba propia) |

**Tabla detectada (formato Markdown):**

| (estimación honesta y declaración de autoría |
| --- |
| intelectual) |

**Tabla detectada (formato Markdown):**

| entregable apoyado |
| --- |
| en IA |
