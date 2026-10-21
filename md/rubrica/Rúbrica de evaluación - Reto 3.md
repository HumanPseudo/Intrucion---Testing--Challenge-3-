<!-- Archivo original: Rúbrica de evaluación - Reto 3 - Diseño de estrategias de detección, defensa y fortalecimiento.pdf -->
<!-- Paginas: 9 -->
<!-- Metodo de extraccion: PyMuPDF (texto ordenado) + pdfplumber (tablas)  -->
<!-- RUBRICA - Reto 3 -->


---

### [p. 1]

Universidad Nacional Abierta y a Distancia
Vicerrectoría Académica y de Investigación
Unidad gestora: Escuela de Ciencias Básicas Tecnología e
Ingeniería ECBTI
Programa: Maestría en Ciberseguridad
Curso: Intrusión y Testing
Código: 203028113
Rúbrica de evaluación – Reto 3
Apreciado estudiante, esta rúbrica presenta los criterios y los niveles con 
los que se calificará su informe técnico. Léala antes de redactar, pues 
cada nivel describe condiciones verificables en el documento entregado.
Tenga en cuenta las siguientes indicaciones técnicas de entrega:
1) Informe técnico en formato Word (.docx) o PDF.
2) Extensión entre 6000 y 8000 palabras, sin contar las referencias 
bibliográficas.
3) El informe debe contener, con título de apartado visible, las siguientes 
diez (10) secciones:
1. Introducción y alcance del diseño defensivo: propósito del 
informe, dominios analizados (DMZ/Web LAMP, corporativo IT e 
IoT/OT) y relación con los hallazgos del Reto 2.
2. Síntesis del análisis ofensivo del Reto 2: activos críticos, 
superficies de exposición, vectores, CVE/CVSS, fases de la Cyber 
Kill Chain y técnicas MITRE ATT&CK.
3. Matriz de priorización de riesgos: clasificación de los vectores 
según criticidad del activo, impacto, probabilidad, severidad técnica, 
exposición y propagación entre dominios.
4. Matriz de trazabilidad vector–control: vector, causa probable, 
activo afectado, impacto, técnica ATT&CK, fase de la Kill Chain, 
controles preventivo, detectivo y correctivo, y evidencia esperada.
1

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 2]

5. Diseño de controles defensivos: hardening de Ubuntu, Apache, 
PHP y MariaDB/MySQL; controles de aplicación web, autenticación, 
sesiones, credenciales, directorios sensibles, backups y servicios 
expuestos; controles para IT e IoT/OT.
6. Propuesta de monitoreo y detección: casos de uso SIEM/XDR 
con fuente de log, condición de alerta, severidad, evento esperado, 
correlación y acción inicial.
7. Propuesta DevSecOps: validación de entradas, codificación 
segura, revisión de dependencias, SAST, DAST, SCA, escaneo de 
secretos y control de cambios.
8. Plan básico de respuesta ante incidentes: preparación, 
identificación, contención, erradicación, recuperación y lecciones 
aprendidas.
9. Criterios de validación para los retos posteriores: hipótesis y 
controles por verificar en el Cyber Range autorizado, evidencia 
técnica esperada y método de validación.
10. Conclusiones y referencias: aportes del diseño defensivo, 
limitaciones, recomendaciones y fuentes consultadas en normas 
APA.
4) Alcance: el reto no exige ejecutar pruebas ni validar explotación técnica 
sobre máquina virtual. Se evalúa el diseño defensivo argumentado, 
viable y trazable.
5) Trazabilidad: cada control propuesto debe responder a un vector, 
activo o causa probable identificado en el Reto 2. No se valoran listas 
genéricas de buenas prácticas.
6) Fuentes: citación y referencias en normas APA, con marcos técnicos 
reconocidos (CIS Controls, NIST CSF, NIST SP 800-61, ISO/IEC 27001, 
OWASP ASVS/WSTG, MITRE ATT&CK, NVD).
7) Tablas y matrices: diseñadas dentro del documento en formato 
editable, con título, numeración y referencia en el texto. No se aceptan 
capturas de pantalla, imágenes de tablas ni enlaces a repositorios 
externos como sustituto del contenido solicitado.
8) Integridad académica: si utilizó herramientas de inteligencia artificial, 
incluya la declaración o bitácora de uso con prompts, propósito,
2

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 3]

verificación y ajustes por criterio propio. Si no la utilizó, indíquelo 
expresamente.
Tabla 1. Rúbrica de evaluación
Elemento 
Descripción
Resultado de 
aprendizaje:
Resultado de aprendizaje 2: Diseñar 
esquemas integrales de detección, 
identificación y gestión de ataques 
cibernéticos, utilizando técnicas ofensivas y 
pensamiento adversarial, con el fin de aportar 
a la toma de decisiones tácticas y estratégicas 
en entornos organizacionales.
Tipo de actividad: 
Individual
Puntaje de la 
actividad:
125 puntos
Primer criterio de 
evaluación (de 
forma):
Nivel alto:
• El archivo entregado es Word (.docx) o PDF y 
el conteo de palabras del cuerpo, sin 
referencias, está entre 6000 y 8000.
El informe cumple el 
formato y la 
extensión 
solicitados y 
contiene, con título 
de apartado visible, 
las diez secciones 
exigidas, con 
matrices editables, 
rotuladas y 
referenciadas en el 
texto.
• El texto del documento contiene las 10 
secciones 
estructurales 
exigidas 
explícitamente: 
introducción 
y 
alcance, 
síntesis del Reto 2, matriz de priorización, 
matriz de trazabilidad vector–control, diseño 
de 
controles, 
monitoreo 
y 
detección, 
DevSecOps, 
respuesta 
ante 
incidentes, 
criterios de validación y conclusiones con 
referencias.
• Todas las tablas y matrices son editables 
dentro del documento y cada una tiene título, 
numeración y al menos una referencia en el 
texto.
Este criterio tiene 
una valoración 
máxima de: 25 
puntos, 
equivalentes al
3

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | Elemento |  |  | Descripción |  |
| --- | --- | --- | --- | --- | --- |
| Resultado de aprendizaje: |  |  | Resultado de aprendizaje 2: Diseñar esquemas integrales de detección, identificación y gestión de ataques cibernéticos, utilizando técnicas ofensivas y pensamiento adversarial, con el fin de aportar a la toma de decisiones tácticas y estratégicas en entornos organizacionales. |  |  |
| Tipo de actividad: |  |  | Individual |  |  |
| Puntaje de la actividad: |  |  | 125 puntos |  |  |
| Primer criterio de evaluación (de forma): El informe cumple el formato y la extensión solicitados y contiene, con título de apartado visible, las diez secciones exigidas, con matrices editables, rotuladas y referenciadas en el texto. Este criterio tiene una valoración máxima de: 25 puntos, equivalentes al |  |  | Nivel alto: • El archivo entregado es Word (.docx) o PDF y el conteo de palabras del cuerpo, sin referencias, está entre 6000 y 8000. • El texto del documento contiene las 10 secciones estructurales exigidas explícitamente: introducción y alcance, síntesis del Reto 2, matriz de priorización, matriz de trazabilidad vector–control, diseño de controles, monitoreo y detección, DevSecOps, respuesta ante incidentes, criterios de validación y conclusiones con referencias. • Todas las tablas y matrices son editables dentro del documento y cada una tiene título, numeración y al menos una referencia en el texto. |  |  |

---

### [p. 4]

20% del puntaje 
total de la 
actividad.
• No hay capturas de pantalla, imágenes de 
tablas ni enlaces a repositorios externos en 
lugar del contenido solicitado.
Si su trabajo se encuentra en este nivel 
puede obtener entre 20 puntos y 25 
puntos.
Nivel medio:
• El formato es correcto, pero la extensión se 
desvía hasta un 10% del rango (entre 5400 y 
6000 o entre 8000 y 8800 palabras).
• Faltan el título o el desarrollo de 1 o 2 de las 
10 secciones exigidas.
• Hasta dos tablas se presentan como imagen, 
o carecen de título, numeración o referencia 
en el texto.
Si su trabajo se encuentra en este nivel 
puede obtener entre 15 puntos y 19 
puntos.
Nivel bajo:
• Faltan 3 o más de las 10 secciones exigidas.
• El archivo no es .docx ni PDF, o la extensión 
es inferior a 5400 o superior a 8800 palabras.
• Las matrices se presentan como capturas de 
pantalla, provienen de hojas de cálculo 
externas o se remiten mediante enlaces.
Si su trabajo se encuentra en este nivel 
puede obtener entre 1 punto y 14 puntos.
Nivel no presentado:
Al no cumplir con ninguno de los parámetros de 
este criterio, su desempeño se entiende como 
“no presentado”. En este nivel se obtienen 0 
puntos.
4

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 5]

Segundo criterio 
de evaluación (de 
contenido):
Nivel alto:
• Menciona 
explícitamente 
los 
dominios 
“DMZ/Web LAMP”, “IT” e “IoT/OT” y clasifica 
en ellos al menos 8 activos del Anexo 1, 
indicando función, criticidad y exposición.
El informe clasifica 
los activos por 
dominio, prioriza los 
riesgos con criterios 
explícitos y 
construye una 
matriz de 
trazabilidad que 
vincula cada vector 
del Reto 2 con 
controles 
preventivos, 
detectivos y 
correctivos, junto 
con hardening, 
monitoreo, 
respuesta, 
DevSecOps y 
criterios de 
validación.
• La matriz de priorización valora cada vector 
con los 6 criterios exigidos (criticidad del 
activo, 
impacto, 
probabilidad, 
severidad 
CVSS, 
exposición 
y 
propagación 
entre 
dominios) y ordena los vectores de mayor a 
menor prioridad.
• La matriz de trazabilidad registra al menos 8 
vectores del Reto 2 y, para cada uno, las 9 
columnas exigidas: causa probable, activo 
afectado, impacto, fase de la Cyber Kill Chain, 
técnica MITRE ATT&CK con identificador 
Txxxx, CVE o referencia, control preventivo, 
control detectivo y control correctivo.
• Propone hardening para los tres dominios con 
al menos 4 acciones por dominio: LAMP 
(versión de Apache, listado de directorios, 
rutas 
sensibles, 
cabeceras 
HTTP, 
TLS, 
backups), IT (SMBv1, firma SMB, RDP, 
política de contraseñas, segmentación) e 
IoT/OT (Telnet, credenciales por defecto, ACL 
y TLS en MQTT, aislamiento de Modbus/PLC, 
firmware).
Este criterio tiene 
una valoración 
máxima de: 50 
puntos, 
equivalentes al 
40% del puntaje 
total de la 
actividad.
• Define al menos 6 casos de uso SIEM/XDR y 
cada uno indica fuente de log, condición de 
disparo, severidad, evento esperado y acción 
inicial de respuesta.
• El plan de respuesta desarrolla las 6 fases de 
NIST SP 800-61 (preparación, identificación, 
contención, 
erradicación, 
recuperación 
y 
lecciones aprendidas) para al menos un 
escenario priorizado del caso.
5

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 6]

• La propuesta DevSecOps nombra al menos 4 
prácticas (SAST, DAST, SCA, escaneo de 
secretos, revisión de dependencias o control 
de cambios) e indica el punto del ciclo en que 
se aplica cada una.
• Define al menos 5 criterios de validación para 
los retos posteriores, cada uno con la 
evidencia técnica esperada y el método de 
verificación en el Cyber Range.
• Todos los controles propuestos aparecen 
asociados a un vector, activo o causa del Reto 
2; no hay controles sin vector asociado.
Si su trabajo se encuentra en este nivel 
puede obtener entre 40 puntos y 50 
puntos.
Nivel medio:
• Menciona los tres dominios, pero clasifica 
entre 4 y 7 activos, o no indica criticidad y 
exposición en todos.
• La matriz de priorización aplica entre 3 y 5 de 
los 6 criterios exigidos, o no ordena los 
vectores por prioridad.
• La matriz de trazabilidad registra entre 4 y 7 
vectores, o deja sin diligenciar 1 o 2 de las 9 
columnas exigidas.
• Propone hardening para los tres dominios con 
menos de 4 acciones en alguno, o formula 
acciones sin indicar el vector que mitigan.
• Define entre 3 y 5 casos de uso SIEM/XDR, o 
alguno omite la condición de disparo, la 
severidad o la acción inicial.
• El plan de respuesta desarrolla entre 4 y 5 de 
las 6 fases exigidas.
6

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 7]

• La propuesta DevSecOps nombra 2 o 3 
prácticas, o no las ubica en el ciclo de 
desarrollo.
• Define entre 2 y 4 criterios de validación, o 
los enuncia sin evidencia esperada ni método.
Si su trabajo se encuentra en este nivel 
puede obtener entre 30 puntos y 39 
puntos.
Nivel bajo:
• No nombra los tres dominios o clasifica menos 
de 4 activos.
• No presenta matriz de priorización, o esta 
aplica 2 o menos criterios.
• La matriz de trazabilidad registra menos de 4 
vectores, o carece de las columnas de técnica 
ATT&CK, fase de la Kill Chain o control 
detectivo.
• El hardening se enuncia como lista genérica 
de buenas prácticas, sin vincularse a un 
vector o activo del caso, o cubre solo uno de 
los tres dominios.
• Define menos de 3 casos de uso SIEM/XDR, o 
los enuncia sin fuente de log.
• El plan de respuesta desarrolla 3 o menos 
fases, la propuesta DevSecOps nombra 1 o 
ninguna práctica, y no se definen criterios de 
validación.
Si su trabajo se encuentra en este nivel 
puede obtener entre 1 punto y 29 puntos.
Nivel no presentado:
Al no cumplir con ninguno de los parámetros de 
este criterio, su desempeño se entiende como 
“no presentado”. En este nivel se obtienen 0 
puntos.
7

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 8]

Tercer criterio de 
evaluación (de 
calidad 
académica):
Nivel alto:
• El documento incluye referencias bajo norma 
APA (al menos 8 fuentes: mínimo 3 de los 
recursos del curso y mínimo 3 marcos o 
fuentes técnicas como CIS Controls, NIST 
CSF, NIST SP 800-61, ISO/IEC 27001, 
OWASP ASVS/WSTG, MITRE ATT&CK o NVD) 
y una frase de declaración de uso de 
inteligencia artificial.
El informe respalda 
cada decisión 
defensiva en un 
marco de referencia 
reconocido y en una 
pista del Anexo 1, e 
incluye referencias 
en normas APA, 
correspondencia 
entre citas y 
referencias, 
declaración de uso 
de inteligencia 
artificial y 
delimitación ética 
del alcance.
• La declaración o bitácora de IA registra los 
prompts empleados, el propósito, la forma en 
que se verificó la salida y los ajustes hechos 
por criterio propio; si no se usó IA, lo indica 
explícitamente.
• Todas las fuentes del listado de referencias 
aparecen citadas en el texto y todas las citas 
del texto figuran en el listado.
• Cada control y cada regla de detección indica 
el marco de referencia que lo respalda y la 
sección o el artefacto del Anexo 1 que lo 
motiva.
Este criterio tiene 
una valoración 
máxima de: 50 
puntos, 
equivalentes al 
40% del puntaje 
total de la 
actividad.
• El informe declara explícitamente que no se 
ejecutaron pruebas ni explotación técnica y 
que la verificación se difiere al Cyber Range 
autorizado.
Si su trabajo se encuentra en este nivel 
puede obtener entre 40 puntos y 50 
puntos.
Nivel medio:
• Incluye entre 5 y 7 fuentes en referencias, o 
presenta errores de formato APA.
• Incluye la frase de declaración de uso de 
inteligencia artificial, pero omite los prompts, 
el propósito o la forma de verificación.
8

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 9]

• Existen fuentes en el listado que no se citan 
en el texto, o citas del texto que no figuran en 
el listado.
• Solo una parte de los controles o de las reglas 
de detección indica el marco de referencia o 
la pista del Anexo 1 que los respalda.
Si su trabajo se encuentra en este nivel 
puede obtener entre 30 puntos y 39 
puntos.
Nivel bajo:
• Presenta 
menos 
de 
5 
fuentes, 
o 
las 
referencias no siguen la norma APA.
• No incluye ninguna frase de declaración de 
uso de inteligencia artificial.
• Los controles y reglas de detección no se 
asocian a ningún marco de referencia ni a 
pistas del Anexo 1.
• No delimita el alcance ético del ejercicio o 
reporta 
pruebas 
de 
explotación 
no 
autorizadas en esta actividad.
Si su trabajo se encuentra en este nivel 
puede obtener entre 1 punto y 29 puntos.
Nivel no presentado:
Al no cumplir con ninguno de los parámetros de 
este criterio, su desempeño se entiende como 
“no presentado”. En este nivel se obtienen 0 
puntos.
9

> [Imagen(es) en la pagina: 2 | xref9 1268x139px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]
