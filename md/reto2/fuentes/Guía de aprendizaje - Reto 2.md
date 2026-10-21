<!-- Archivo original: Guía de aprendizaje - Reto 2 - Análisis de vectores de ataque.pdf -->
<!-- Paginas: 6 -->
<!-- Metodo de extraccion: PyMuPDF (texto ordenado) + pdfplumber (tablas)  -->
<!-- ACTIVIDAD - Guia de aprendizaje Reto 2 -->


---

### [p. 1]

Universidad Nacional Abierta y a Distancia
Vicerrectoría Académica y de Investigación
Curso: Intrusión y testing
Código: 203028113
Cursos Virtuales Unadista Automatizados y Autodirigidos -
CuVUnAD
Guía de aprendizaje–  Reto 2 - Análisis de vectores de ataque,
ingeniería social y escenarios de compromiso
1. Datos del Reto
Tabla 1. Tabla de descripción
1. Momento de la
Evaluación
2. Unidad gestora
Escuela de Ciencias Básicas 
Tecnología e Ingeniería ECBTI 
3. El Reto   inicia el:
lunes, 31 de agosto de 2026 
4. El Reto finaliza el:
domingo, 27 de septiembre de 
2026 
5. Horas de trabajo
independiente del
estudiante
6. Tipos de interacciones
Foros de interacción entre 
estudiantes 
7. Puntuación del
cuestionario de
evaluación de este Reto
2. Descripción detallada del Reto
Con el desarrollo de esta Reto se espera que se alcance el siguiente 
resultado de aprendizaje:
Resultado 
de 
aprendizaje 
1: 
Evaluar 
vulnerabilidades 
en 
infraestructuras digitales mediante la aplicación de metodologías de 
intrusión, pruebas de penetración e ingeniería social, interpretando
Intermedio
45 horas
125

> [Imagen(es) en la pagina: 2 | xref5 2028x222px [recurrente: posible encabezado/pie/logo]; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

**Tabla detectada (formato Markdown):**

|  | 1. Momento de la |  | Intermedio |
| --- | --- | --- | --- |
|  | Evaluación |  |  |
| 2. Unidad gestora | 2. Unidad gestora |  | Escuela de Ciencias Básicas Tecnología e Ingeniería ECBTI |
|  | 3. El Reto inicia el: |  | lunes, 31 de agosto de 2026 |
| 4. El Reto finaliza el: | 4. El Reto finaliza el: |  | domingo, 27 de septiembre de 2026 |
|  | 5. Horas de trabajo |  | 45 horas |
|  | independiente del |  |  |
|  | estudiante |  |  |
| 6. Tipos de interacciones | 6. Tipos de interacciones |  | Foros de interacción entre estudiantes |
|  | 7. Puntuación del |  | 125 |
|  | cuestionario de |  |  |
|  | evaluación de este Reto |  |  |

---

### [p. 2]

críticamente los vectores de ataque para anticipar escenarios de 
compromiso y fortalecer la postura de seguridad.
El Reto  consiste en:
Este Reto consiste en analizar el escenario de compromiso presentado en 
el Anexo 1 - Caso de estudio AgroSmart del Sumapaz S.A.S., 
correspondiente a un ecosistema híbrido conformado por una aplicación 
web LAMP, un entorno corporativo IT y componentes IoT - OT asociados 
a un invernadero inteligente. A partir de los artefactos entregados en el 
caso, inventario de activos, reconocimiento de servicios, OSINT, pistas 
web, logs simulados y evidencias preliminares, el estudiante deberá 
identificar activos críticos, superficies de exposición, vectores de ataque, 
técnicas de ingeniería social, vulnerabilidades asociadas a CVE/CVSS, 
fases de la Cyber Kill Chain, técnicas MITRE ATT&CK, rutas probables de 
compromiso e impactos organizacionales.
Para el desarrollo de esta actividad se requieren los siguientes materiales 
y recursos:
Acceso digital
Crespo Martínez, E. (2021). Análisis de vulnerabilidades con SQLMAP 
aplicada a entornos APEX 5. Ingenius, Revista Ciencia y Tecnología, (pp. 
104-113). https://doi.org/10.17163/ings.n25.2021.10
He Jun, L., & Yang, Y. (2021). Pruebas de penetración a redes WiFi con 
Kali 
Linux. 
(pp. 
1-8). 
https://bibliotecavirtual.unad.edu.co/login?url=https://search.ebscohost
.com/login.aspx?direct=true&db=edb&AN=151025183&lang=es&site=e
ds-live&scope=site
Ingeniería Social
Benavides Astudillo, E., Fuertes Díaz, W., & Sánchez Gordon, S. (2019). 
Un experimento para crear conciencia en las personas acerca de los 
ataques de Ingeniería Social. Revista Ciencia UNEMI, (pp. 27-40). 
https://bibliotecavirtual.unad.edu.co/login?url=https://search.ebscohost
.com/login.aspx?direct=true&db=fap&AN=141492530&lang=es&site=ed
s-live&scope=site
Benavides Astudillo, E., Fuertes Díaz, W., & Sánchez Gordon, S. (2020). 
Caracterización de los ataques de phishing y técnicas para mitigarlos. 
Ataques: una revisión sistemática de la literatura. Revista Ciencia y 
Tecnología, 
13, 
(pp. 
97-104). 
https://bibliotecavirtual.unad.edu.co/login?url=https://search.ebscohost
2

> [Imagen(es) en la pagina: 2 | xref10 2028x63px [recurrente: posible encabezado/pie/logo]; xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 3]

.com/login.aspx?direct=true&db=asn&AN=144901559&lang=es&site=e
ds-live&scope=site
Budavári, E. A., Albini, A., & Mester, G. (2023). The Role of Social 
Engineering in the Energy Balance of Systems. Interdisciplinary 
Description 
of 
Complex 
Systems, 
21(2), 
168–173. 
https://doi-
org.bibliotecavirtual.unad.edu.co/10.7906/indecs.21.2.5
Prado Díaz, J. P. (2021). Ingeniería social, un ejemplo práctico. Revista 
ODIGOS, 2, 47-76. https://doi.org/10.35290/ro.v2n3.2021.493
Zambrano Hernández, L. F., Peña Hidalgo, H. J., & Cárdenas Corral, N. R. 
(2024). Una Mirada a Metodologías Para Pruebas de Penetración en 
Ciberseguridad. Centro de respuestas a incidentes informáticos. 
https://selloeditorial.unad.edu.co/images/Documentos/ciberseguridad/B
oletin/Octubre_2024.pdf
Zambrano, L. F. (2025). Metodologías de pruebas de penetración éticas 
en Ciberseguridad. [Objeto_virtual_de_Informacion_OVI]. Repositorio 
Institucional UNAD. https://repository.unad.edu.co/handle/10596/69877
Zambrano, L. F. (2026). Metodologías de intrusión y testing ético. 
[Objeto_virtual_de_aprendizaje_OVA]. Repositorio Institucional UNAD. 
https://repository.unad.edu.co/handle/10596/83447
Para el desarrollo de este Reto debe realizar los siguientes pasos:
Paso 1. Leer el Anexo 1 y ubicar los dominios DMZ/Web, IT e IoT/OT: 
Realice una lectura completa del Anexo 1 - Caso de estudio AgroSmart 
del 
Sumapaz 
S.A.S. 
Identifique 
los 
componentes 
tecnológicos 
mencionados y organícelos según correspondan a los dominios DMZ/Web, 
IT e IoT/OT. Establezca qué sistemas, dispositivos y servicios pertenecen 
a cada dominio y observe las posibles relaciones o conexiones existentes 
entre ellos.
Paso 2. Identificar activos críticos y superficies de exposición: A partir de 
los componentes identificados, seleccione los activos que considere más 
relevantes para la operación de la organización. Para cada uno, determine 
su función, ubicación dentro del escenario y posibles mecanismos de 
acceso o exposición. Organice los resultados de manera que sea posible 
reconocer cuáles activos presentan mayor interés desde la perspectiva de 
un posible atacante.
Paso 3. Analizar los artefactos técnicos: Revise individualmente los 
resultados de Nmap, robots.txt, errores SQL, headers, información 
OSINT, logs, SMB, MQTT, Modbus y cámara IP. Identifique los datos
3

> [Imagen(es) en la pagina: 2 | xref10 2028x63px [recurrente: posible encabezado/pie/logo]; xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 4]

relevantes presentes en cada artefacto y relaciónelos con los activos 
previamente identificados. Registre los hallazgos que puedan indicar 
servicios expuestos, configuraciones inseguras, información sensible o 
posibles puntos de entrada.
Paso 4. Consultar fuentes públicas para asociar CVE, CVSS y madurez de 
explotación: Seleccione las tecnologías, servicios o versiones encontradas 
durante el análisis y consulte fuentes técnicas confiables para identificar 
vulnerabilidades relacionadas. Registre el CVE, CVSS y la información 
disponible sobre su explotación. Verifique que cada vulnerabilidad 
investigada tenga relación con los componentes presentes en el caso y 
diferencie aquellas confirmadas de las que requieren validación adicional.
Paso 5. Mapear los vectores con Cyber Kill Chain: Organice los vectores 
de ataque identificados siguiendo las fases de Cyber Kill Chain. Relacione 
cada hallazgo con la fase que corresponda y construya una secuencia que 
permita visualizar cómo podría avanzar un atacante desde el 
reconocimiento inicial hasta el posible cumplimiento de su objetivo.
Paso 6. Mapear mínimo diez técnicas MITRE ATT&CK: Seleccione como 
mínimo diez técnicas o subtécnicas MITRE ATT&CK relacionadas con los 
hallazgos obtenidos. Para cada una registre su identificador, nombre, 
táctica asociada y evidencia o situación del caso que justifica su selección. 
Evite incluir técnicas que no puedan relacionarse razonablemente con el 
escenario analizado.
Paso 7. Construir hipótesis de ruta de compromiso: Integre los resultados 
anteriores y construya una posible secuencia de compromiso desde un 
punto inicial de acceso hasta uno o varios activos críticos. En cada etapa 
diferencie claramente la pista encontrada, la hipótesis formulada y la 
evidencia que sería necesario obtener para validarla. Si existen diferentes 
posibilidades, presente las rutas más probables y justifique su selección.
Paso 8. Preparar el video expositivo: Organice los resultados en una 
presentación que incluya introducción, descripción del caso, análisis 
preliminar,alternativas 
de 
análisis 
de 
vectores 
y 
validación, 
(vulnerabilidades, Cyber Kill Chain, MITRE ATT&CK, 
ruta 
probable 
de 
compromiso) 
propuesta 
preliminar(impactos), 
conclusiones, 
preguntas y referencias. Utilice tablas, esquemas y diagramas que 
faciliten la explicación y posteriormente exporte la presentación al 
formato de video solicitado.
Paso 9. Documentar el uso de IA: Si utilizó herramientas de inteligencia 
artificial, registre la herramienta empleada, propósito de uso y actividades 
en las que fue utilizada. Indique cómo verificó o contrastó la información

> [Imagen(es) en la pagina: 2 | xref53 2028x222px; xref10 2028x63px [recurrente: posible encabezado/pie/logo]]

---

### [p. 5]

obtenida antes de incorporarla al análisis. Si no utilizó IA, déjelo 
expresamente indicado en la declaración correspondiente.
Indicaciones e interacciones para el desarrollo de el Reto  
Las evidencias de aprendizaje son las acciones, productos o procesos 
observables que se realizan y/o entregan para manifestar las 
capacidades, habilidades, aptitudes y actitudes adquiridas.
Para el desarrollo de este Reto, el estudiante deberá realizar un proceso 
individual de análisis del caso AgroSmart del Sumapaz, apoyado en la 
revisión de referentes conceptuales, fuentes técnicas confiables y marcos 
de análisis ofensivo y defensivo. La actividad exige capacidad de síntesis, 
organización de la información, argumentación técnica y claridad 
comunicativa.
El uso de inteligencia artificial está permitido como recurso de apoyo para 
explorar ideas, organizar información, contrastar enfoques, mejorar la 
estructuración del guion o fortalecer la comprensión del caso; no 
obstante, dicho uso debe ser explícito, documentado y críticamente 
validado. El estudiante es responsable de verificar la calidad de la 
información obtenida, contrastarla con fuentes confiables y evitar el uso 
acrítico o la reproducción literal de respuestas generadas por sistemas de 
IA.
Las evidencias a desarrollar individualmente son:
Video expositivo de presentación del reto donde se analiza la situación de 
AgroSmart del Sumapaz S.A.S., en el que el estudiante diseña esquemas 
de detección e identificación de ataques cibernéticos aplicando 
pensamiento adversarial al mapeo de vectores, técnicas MITRE ATT&CK y 
rutas de compromiso en un ecosistema híbrido IT–IoT/OT, aportando 
insumos para la toma de decisiones tácticas y estratégicas.
Condiciones de elaboración y entrega del video expositivo
El video debe presentar de forma organizada y técnicamente sustentada 
los siguientes apartados:
1. Introducción: título del caso, contexto general, objetivo de la 
exposición y justificación del caso.
2. Descripción del caso: contexto específico, situación problemática, 
actores involucrados y datos relevantes.
3. Análisis 
preliminar 
del 
caso: 
problema 
principal, 
causas, 
consecuencias, perspectiva teórica y valoración crítica.
5

> [Imagen(es) en la pagina: 2 | xref10 2028x63px [recurrente: posible encabezado/pie/logo]; xref5 2028x222px [recurrente: posible encabezado/pie/logo]]

---

### [p. 6]

4. Conclusiones: síntesis del aprendizaje, reflexión académica y 
recomendaciones.
5. Preguntas para discusión: preguntas que promuevan continuidad 
analítica en los retos posteriores.
6. Referencias: fuentes bibliográficas, técnicas o documentales en 
normas APA.
Condiciones técnicas de entrega del video
• 
Archivo en formato MP4.
• 
Generado a partir de una presentación en PowerPoint exportada a 
video.
• 
Duración máxima: 10 minutos.
• 
Peso máximo: 200 MB.
• 
Las tablas o cuadros comparativos deben diseñarse e incrustarse 
directamente en el archivo editable y mostrarlos en el video.
• 
No se admite la inserción de tablas provenientes de hojas de cálculo 
externas, ni el uso de capturas de pantalla o imágenes para 
reemplazar contenido analítico.
• 
No se permite enlazar direcciones URL externas ni vínculos a 
repositorios en la nube como sustituto del contenido solicitado.
6

> [Imagen(es) en la pagina: 2 | xref10 2028x63px [recurrente: posible encabezado/pie/logo]; xref5 2028x222px [recurrente: posible encabezado/pie/logo]]
