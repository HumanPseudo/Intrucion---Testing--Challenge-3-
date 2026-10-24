<!-- Archivo original: resources/ovi_2_iyt_203028113.mp4 -->
<!-- Duracion: 07:57.6; video H.264 1920x1080; audio AAC estereo -->
<!-- Metodo: OCR de fotogramas (tesseract) + transcripcion automatica del audio (faster-whisper, modelo small, es). Se corrigieron tildes y errores evidentes de reconocimiento; no se altero el contenido. -->

# Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT

> Video (objeto virtual de información, OVI) del curso Intrusión y Testing (203028113), Universidad Nacional Abierta y a Distancia (UNAD), Maestría en Ciberseguridad. Docente: Luis Fernando Zambrano Hernández. Año: 2026. Duración: 7:57.
>
> Conversión a Markdown del contenido del video: se transcribe la narración y se reproduce el texto de las diapositivas. La transcripción es automática y fue revisada solo para corregir tildes y errores evidentes de reconocimiento del habla. Las figuras del video son imágenes; se conservan sus títulos, notas y etiquetas legibles, no su representación gráfica.

## 1. Introducción

**Texto en pantalla**

Este recurso presenta los fundamentos para la detección, identificación y gestión de ataques cibernéticos en entornos de Tecnologías de Información (TI) e Internet de las Cosas (IoT), integrando el análisis de vectores de ataque y el pensamiento adversarial como soporte para la toma de decisiones en ciberseguridad.

Para ello, se abordarán conceptos asociados a marcos de referencia como MITRE ATT&CK y Cyber Kill Chain, así como principios para el diseño de estrategias de detección y arquitecturas seguras orientadas a comprender el comportamiento de las amenazas, fortalecer la capacidad de respuesta y mejorar la postura de ciberseguridad en ecosistemas digitales interconectados.

**Narración**

Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT. Introducción. Este recurso presenta los fundamentos para la detección, identificación y gestión de ataques cibernéticos en entornos de tecnologías de información TI e internet de las cosas IoT, integrando el análisis de vectores de ataque y el pensamiento adversarial como soporte para la toma de decisiones en ciberseguridad. Para ello se abordarán conceptos asociados a marcos de referencia como MITRE ATT&CK y Cyber Kill Chain, así como principios para el diseño de estrategias de detección y arquitecturas seguras orientadas a comprender el comportamiento de las amenazas, fortalecer la capacidad de respuesta y mejorar la postura de ciberseguridad en ecosistemas digitales interconectados.

## 2. Objetivo de aprendizaje

**Texto en pantalla**

Comprender estrategias de detección, identificación y gestión de ataques cibernéticos mediante el análisis de vectores de ataque, el pensamiento adversarial y el diseño de mecanismos de protección para entornos TI e IoT.

**Narración**

Objetivo de aprendizaje. Comprender estrategias de detección, identificación y gestión de ataques cibernéticos mediante el análisis de vectores de ataque, el pensamiento adversarial y el diseño de mecanismos de protección para entornos TI e IoT.

## 3. Introducción

**Texto en pantalla**

Con el presente recurso, se busca brindar al estudiante fundamentos para la detección, identificación y gestión de ataques cibernéticos en entornos de Tecnologías de Información (TI) e Internet de las Cosas (IoT), mediante el análisis de vectores de ataque y la comprensión del comportamiento de las amenazas digitales.

Para ello, se abordarán conceptos asociados a marcos de referencia como MITRE ATT&CK y Cyber Kill Chain, así como principios para el diseño de estrategias de detección y arquitecturas seguras, orientadas a fortalecer la capacidad de análisis, respuesta y toma de decisiones frente a escenarios de ciberseguridad en ecosistemas digitales interconectados.

**Narración**

Introducción. Con el presente recurso se busca brindar al estudiante fundamentos para la detección, identificación y gestión de ataques cibernéticos en entornos de tecnologías de información TI e internet de las cosas IoT, mediante el análisis de vectores de ataque y la comprensión del comportamiento de las amenazas digitales. Para ello se abordarán conceptos asociados a marcos de referencia como MITRE ATT&CK y Cyber Kill Chain, así como principios para el diseño de estrategias de detección y arquitecturas seguras orientadas a fortalecer la capacidad de análisis, respuesta y toma de decisiones frente a escenarios de ciberseguridad en ecosistemas digitales interconectados.

## 4. Contenido

### 4.1 Vectores de ataque y superficie de exposición

**Texto en pantalla**

Los entornos digitales actuales están compuestos por múltiples componentes interconectados que amplían continuamente la superficie de exposición frente a amenazas cibernéticas. Aplicaciones, usuarios, servicios en la nube, infraestructura tecnológica y dispositivos IoT generan nuevos escenarios que pueden convertirse en puntos potenciales de compromiso.

Comprender los vectores de ataque permite analizar cómo una amenaza podría ingresar, desplazarse y afectar procesos críticos dentro de una organización. Este análisis facilita reconocer relaciones entre activos, identificar dependencias y anticipar posibles impactos sobre la operación.

En entornos TI e IoT, la identificación temprana de superficies de exposición constituye un elemento fundamental para diseñar mecanismos de detección, fortalecer capacidades de respuesta y apoyar procesos de toma de decisiones orientados a mejorar la postura de ciberseguridad.

**Figura 1.** Superficie de exposición y vectores de ataque en entornos TI e IoT.

> Nota. En la figura se presenta la identificación de vectores de ataque, la cual permite priorizar mecanismos de detección y reducción del riesgo. Etiquetas visibles: redes; aplicaciones y servicios; infraestructura; sistemas y datos.

**Narración**

La figura 1 presenta la superficie de exposición y vectores de ataque en entornos TI e IoT. Los entornos digitales actuales están compuestos por múltiples componentes interconectados que amplían continuamente la superficie de exposición frente a amenazas cibernéticas. Aplicaciones, usuarios, servicios en la nube, infraestructura tecnológica y dispositivos IoT generan nuevos escenarios que pueden convertirse en puntos potenciales de compromiso. Comprender los vectores de ataque permite analizar cómo una amenaza podría ingresar, desplazarse y afectar procesos críticos dentro de una organización. Este análisis facilita reconocer relaciones entre activos, identificar dependencias y anticipar posibles impactos sobre la operación. En entornos TI e IoT, la identificación temprana de superficie de exposición constituye un elemento fundamental para diseñar mecanismos de detección, fortalecer capacidades de respuesta y apoyar procesos de toma de decisiones orientados a mejorar la postura de ciberseguridad.

### 4.2 Modelos de referencia

**Texto en pantalla**

Para comprender un ataque cibernético no basta con identificar una vulnerabilidad aislada. Es necesario analizar cómo actúa el adversario, qué fases sigue y qué técnicas utiliza para alcanzar su objetivo.

Cyber Kill Chain permite observar el ataque como una secuencia de siete etapas, desde el reconocimiento inicial hasta las acciones sobre los objetivos. Este modelo ayuda a ubicar en qué momento puede interrumpirse un intento de compromiso.

MITRE ATT&CK complementa este análisis al describir tácticas, técnicas y procedimientos utilizados por atacantes reales. Su valor está en conectar comportamientos observables con posibles acciones defensivas.

En entornos TI e IoT, estos modelos permiten mejorar la detección, orientar la investigación de incidentes y apoyar decisiones tácticas y estratégicas para fortalecer la ciberseguridad organizacional.

**Figura 2.** Modelos de referencia para análisis de ataques.

> Nota. En la figura se presenta cómo los modelos permiten interpretar fases y patrones comunes de compromiso. Relación complementaria: Cyber Kill Chain describe la secuencia del ataque desde la preparación hasta el logro del objetivo; MITRE ATT&CK detalla las tácticas y técnicas utilizadas en cada etapa. Componentes de ATT&CK visibles: tácticas, técnicas, subtécnicas, procedimientos y software. Aplicación en entornos TI e IoT.

**Narración**

La figura 2 presenta modelos de referencia para análisis de ataques. Para comprender un ataque cibernético no basta con identificar una vulnerabilidad aislada, es necesario analizar cómo actúa el adversario, qué fase sigue y qué técnica se utiliza para alcanzar su objetivo. Cyber Kill Chain permite observar el ataque como una secuencia de siete etapas, desde el conocimiento inicial hasta las acciones sobre los objetivos. Este modelo ayuda a ubicar en qué momento puede interrumpirse un intento de compromiso. MITRE ATT&CK complementa este análisis al describir tácticas, técnicas y procedimientos utilizados por atacantes reales. Su valor está en conectar comportamientos observables con posibles acciones defensivas. En entornos TI e IoT, estos modelos permiten mejorar la detección, orientar la investigación de incidentes y apoyar decisiones tácticas y estratégicas para fortalecer la ciberseguridad organizacional.

### 4.3 Estrategias para detectar ataques

**Texto en pantalla**

La detección de ataques cibernéticos consiste en identificar comportamientos anómalos y señales de alerta antes de que generen afectaciones sobre los activos digitales y los procesos organizacionales.

Para ello, las organizaciones integran información proveniente de registros de eventos, tráfico de red, monitoreo de dispositivos y mecanismos de correlación que permiten interpretar el contexto y reconocer posibles escenarios de compromiso.

La generación de alertas oportunas y el análisis de eventos facilitan la identificación temprana de amenazas, fortaleciendo los procesos de investigación y respuesta frente a incidentes.

En entornos TI e IoT, donde múltiples componentes operan de manera simultánea, la capacidad de detectar, correlacionar y priorizar eventos se convierte en un elemento clave para aumentar la visibilidad del entorno y apoyar la toma de decisiones en ciberseguridad.

**Figura 3.** Componentes para detectar eventos de ciberseguridad.

> Nota. Etiquetas visibles: SOC/monitoreo; logs y eventos; tráfico de red; SIEM/correlación; dispositivos IoT; alertas.

**Narración**

La figura 3 presenta componentes para detectar eventos de ciberseguridad. La detección de ataques cibernéticos consiste en identificar comportamientos anómalos y señales de alerta antes de que generen afectaciones sobre los activos digitales y los procesos organizacionales. Para ello, las organizaciones integran información proveniente de registros de eventos, tráfico de red, monitoreo de dispositivos y mecanismos de correlación que permiten interpretar el contexto y reconocer posibles escenarios de compromiso. La generación de alertas oportunas y el análisis de eventos facilitan la identificación temprana de amenazas, fortaleciendo los procesos de investigación y respuesta frente a incidentes. En entornos TI e IoT, donde múltiples componentes operan de manera simultánea, la capacidad de detectar, correlacionar y priorizar eventos se convierte en un elemento clave para aumentar la visibilidad del entorno y apoyar la toma de decisiones en ciberseguridad.

### 4.4 Gestión de respuesta ante incidentes

**Texto en pantalla**

La detección de un ataque representa únicamente el inicio del proceso de gestión de incidentes.

El verdadero valor para la organización está en responder de manera estructurada para contener el impacto y recuperar la operación de forma segura.

La gestión y respuesta ante incidentes integra actividades de identificación, contención, erradicación, recuperación y aprendizaje, permitiendo reducir la exposición al riesgo y fortalecer las capacidades de defensa frente a futuros eventos. Cada etapa aporta información que facilita la toma de decisiones basada en evidencia y mejora la coordinación entre equipos técnicos y organizacionales.

En entornos TI e IoT, donde la conectividad aumenta la velocidad de propagación de las amenazas, establecer procesos claros de respuesta contribuye al fortalecimiento de la resiliencia y a la mejora continua de la postura de ciberseguridad.

**Figura 4.** Etapas del proceso de gestión del riesgo y respuesta a incidentes.

> Nota. En la figura se presenta el proceso estructurado para reducir el impacto y mejorar la recuperación. Etapas visibles: identificación, contención, erradicación, recuperación y aprendizaje.

**Narración**

La figura 4 presenta etapas del proceso de gestión del riesgo y respuesta a incidentes. La detección de un ataque representa únicamente el inicio del proceso de gestión de incidentes. El verdadero valor para la organización está en responder de manera estructurada para contener el impacto y recuperar la operación de forma segura. La gestión y respuesta ante incidentes integra actividades de identificación, contención, erradicación, recuperación y aprendizaje, permitiendo reducir la exposición al riesgo y fortalecer las capacidades de defensa frente a futuros eventos. Cada etapa aporta información que facilita la toma de decisiones basada en evidencia y mejora la coordinación entre equipos técnicos y organizacionales. En entornos TI e IoT donde la conectividad aumenta la velocidad de propagación de las amenazas, establecer procesos claros de respuesta contribuye al fortalecimiento de la resiliencia y a la mejora continua de la postura de ciberseguridad.

### 4.5 Adopción de buenas prácticas para la reducción del riesgo

**Texto en pantalla**

Adoptar buenas prácticas reduce riesgos, fortalece la resiliencia y contribuye a proteger los activos digitales.

La ciberseguridad no depende únicamente de herramientas, sino de decisiones, procesos y comportamientos.

La figura 5 organiza las buenas prácticas en cinco bloques:

1. Gobernanza y políticas.
2. Gestión de riesgos.
3. Personas y cultura.
4. Tecnología y controles.
5. Monitoreo y mejora continua.

La combinación de personas, procesos y tecnología permite una defensa en profundidad sostenible. La mejora continua fortalece la resiliencia organizacional y aumenta la capacidad de respuesta frente a un entorno de amenazas dinámico.

**Figura 5.** Buenas prácticas para fortalecer la ciberseguridad.

> Nota. En la figura se presenta la adopción de buenas prácticas para la reducción del riesgo. El texto de los cinco bloques es parcialmente ilegible en el fotograma; se conservan los títulos y la secuencia que enuncia la narración.

**Narración**

La figura 5 presenta buenas prácticas para fortalecer la ciberseguridad. Consta de 5 pasos: gobernanza y políticas, gestión de riesgos, personas y cultura, tecnología y controles, monitoreo y mejora continua. Esto permite un enfoque integral donde la combinación de personas, procesos y tecnología permite una defensa en profundidad y sostenible.

## 5. Conclusiones

**Texto en pantalla**

- Comprender los vectores de ataque y el comportamiento del adversario permite fortalecer las capacidades de detección e identificación temprana de amenazas.
- Modelos como Cyber Kill Chain y MITRE ATT&CK aportan criterios estructurados para analizar escenarios de compromiso y apoyar procesos de investigación y respuesta.
- La gestión de incidentes requiere integrar detección, análisis y acciones coordinadas que reduzcan el impacto sobre los activos digitales.
- En entornos TI e IoT, la capacidad de correlacionar eventos y generar decisiones basadas en evidencia fortalece la resiliencia organizacional.
- La mejora continua y la aplicación de buenas prácticas permiten evolucionar la postura de ciberseguridad frente a amenazas dinámicas y entornos tecnológicos cambiantes.

**Narración**

Comprender los vectores de ataque y el comportamiento del adversario permite fortalecer las capacidades de detección e identificación temprana de amenazas. Modelos como Cyber Kill Chain y MITRE ATT&CK aportan criterios estructurados para analizar el escenario de compromiso y apoyar procesos de investigación y respuesta. La gestión de incidentes requiere integrar detección, análisis y acciones coordinadas que reduzcan el impacto sobre los activos digitales. En entornos TI e IoT, la capacidad de correlacionar eventos y generar decisiones basadas en evidencia fortalece la resiliencia organizacional. La mejora continua y la aplicación de buenas prácticas permite evolucionar la postura de ciberseguridad frente a amenazas dinámicas y entornos tecnológicos cambiantes.

## 6. Referencias bibliográficas

- Palomo Luna, D. F., Zambrano Hernández, L. F., Moreno Molano, S. X., & Peña Hidalgo, H. J. (2024). Una mirada a metodologías para pruebas de penetración en ciberseguridad. *Boletín Informativo CSIRT Académico UNAD*, (28). Universidad Nacional Abierta y a Distancia. https://selloeditorial.unad.edu.co/images/Documentos/ciberseguridad/Boletin/Octubre_2024.pdf
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018). *MITRE ATT&CK®: Design and philosophy*. MITRE Corporation. https://doi.org/10.13140/RG.2.2.13778.58565
- National Institute of Standards and Technology (NIST). (2012). *Computer Security Incident Handling Guide* (Special Publication 800-61 Revision 2). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-61r2

## 7. Créditos

Escuela de Ciencias Básicas, Tecnología e Ingeniería

Programa Maestría en Ciberseguridad

Nombre del docente: Luis Fernando Zambrano Hernández

Año: 2026

UNAD

Esta obra está protegida por derecho de autor bajo la titularidad de la UNAD. Cualquier reproducción o copia sin autorización constituye un delito conforme a la legislación nacional.

## Ficha de referencia sugerida (APA 7)

Zambrano Hernández, L. F. (2026). *Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT* [OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/83223

> Autor, año y título se verificaron en la portada y en los créditos del video. El handle del repositorio no resuelve sin sesión institucional; la copia local verificada es `resources/ovi_2_iyt_203028113.mp4`.
