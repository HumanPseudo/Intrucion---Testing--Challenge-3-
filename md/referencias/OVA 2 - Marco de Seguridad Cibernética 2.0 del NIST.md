<!-- Archivo original: resources/OVA2genially_203028113.zip -->
<!-- Fuente: exportación offline de Genially (https://view.genially.com/6a29fb634ab60d77b87d6b2c/presentation-ova-2-iyt-203028113) -->
<!-- Método: extracción del JSON embebido en index.html (window.dataBase64); texto conservado tal como aparece en las diapositivas -->

# OVA 2 IYT - 203028113

**Marco de Seguridad Cibernética 2.0 del NIST para gestión de los riesgos de seguridad cibernética**

> Recurso virtual de la Universidad Nacional Abierta y a Distancia (UNAD), Maestría en Ciberseguridad. Autor: Eduard Antonio Mantilla Torres. Año: 2025. Enlace público: https://view.genially.com/6a29fb634ab60d77b87d6b2c/presentation-ova-2-iyt-203028113
>
> Conversión a Markdown del contenido textual de las diapositivas. La narración en audio (22 pistas) no se transcribe aquí; el texto en pantalla se reproduce íntegro, incluidos los textos de relleno (*Lorem ipsum*) presentes en el original. Las respuestas correctas de las actividades se marcan con **(correcta)**.

> Nota de contenido: el cuerpo de este ejemplar desarrolla el Marco de Seguridad Cibernética (CSF) 2.0 del NIST. Las actividades de autoevaluación abordan vectores de ataque, ingeniería social, estrategias de detección y defensa, priorización de hallazgos y controles de mitigación. El mismo cuerpo de contenido aparece en los tres ejemplares OVA 1–OVA 3; cambian las actividades.

## Diapositiva 1 — Portada

Marco de Seguridad Cibernética 2.0 del NIST para gestión de los riesgos de seguridad

cibernética

## Diapositiva 2 — Introducción

El Marco de Seguridad Cibernética (CSF) 2.0 del NIST, publicado en febrero de 2024, un marco flexible y adaptable diseñado para ayudar a organizaciones de cualquier tamaño, sector o nivel de madurez a gestionar sus riesgos de seguridad cibernética mediante seis funciones interconectadas (Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar), destacando especialmente la nueva función "Gobernar" que posiciona la ciberseguridad como un componente estratégico alineado con los objetivos empresariales; el contenido explora la estructura jerárquica del marco (funciones, categorías y subcategorías), el uso de Perfiles Organizativos para evaluar la postura actual y deseada de seguridad, los Niveles de madurez (de Parcial a Adaptable) para caracterizar las prácticas de gestión de riesgos, y las innovaciones clave de esta versión como las Guías de Inicio Rápido para PYMES, el enfoque mejorado en gestión de riesgos de cadena de suministro y la introducción de métricas cuantificables para medir el progreso en la implementación de prácticas de ciberseguridad efectivas.

## Diapositiva 3 — Actividad previa

Comprender y aplicar los principios fundamentales del Marco de Seguridad Cibernética (CSF) 2.0 del NIST para gestionar eficazmente los riesgos de seguridad cibernética en organizaciones de cualquier tamaño, sector o nivel de madurez, integrando la gobernanza con las operaciones de seguridad.

## Diapositiva 4 — Actividad previa

A continuación, realizaremos la autoevaluación de conocimientos previos en este recurso. Consiste en responder 3 preguntas de selección múltiple con única respuesta.

**Actividad (QUIZ_ACTIVITY):** ¿Qué se entiende por vector de ataque en ciberseguridad?

- Una herramienta utilizada únicamente para cifrar información
- Una ruta o método que puede ser utilizado por una amenaza para comprometer un sistema **(correcta)**
- Un informe final de auditoría técnica
- Publicar fallas de seguridad sin informar al responsable del sistema
- Un mecanismo exclusivo para recuperar información después de un incidente

## Diapositiva 5 — Actividad previa

A continuación, realizaremos la autoevaluación de conocimientos previos en este recurso. Consiste en responder 3 preguntas de selección múltiple con única respuesta.

**Actividad (QUIZ_ACTIVITY):** ¿Cuál de las siguientes situaciones corresponde a una técnica de ingeniería social?

- Actualizar el sistema operativo de un servidor
- Manipular psicológicamente a un usuario para que entregue información confidencial **(correcta)**
- Configurar reglas de firewall para bloquear conexiones sospechosas
- Crear una copia de seguridad de una base de datos

## Diapositiva 6 — Actividad previa

A continuación, realizaremos la autoevaluación de conocimientos previos en este recurso. Consiste en responder 3 preguntas de selección múltiple con única respuesta.

**Actividad (QUIZ_ACTIVITY):** ¿Cuál es el propósito principal de diseñar estrategias de detección y defensa frente a un escenario de ataque?

- Aumentar la cantidad de vulnerabilidades presentes en el sistema
- Ocultar los incidentes para evitar su análisis
- Identificar señales de amenaza, reducir riesgos y fortalecer la postura de ciberseguridad **(correcta)**
- Permitir que todos los usuarios tengan privilegios administrativos

## Diapositiva 7 — Contenido

Introducción al Marco CSF 2.0

El Marco de Ciberseguridad del NIST (CSF) 2.0 representa una evolución estratégica respecto a su versión anterior (CSF 1.1). Diseñado como un marco flexible, escalable y aplicable a organizaciones de cualquier sector, tamaño o madurez, su objetivo es democratizar el acceso a prácticas robustas de ciberseguridad.

A diferencia del CSF 1.0 que se centraba en infraestructuras críticas como energía, salud o transporte, la versión 2.0 responde a la creciente interdependencia digital global, abordando riesgos emergentes como ataques de ransomware, cadenas de suministro vulnerables y brechas en entornos híbridos (presencial/remoto).

El CSF 2.0 no establece cómo deben lograrse los resultados de seguridad cibernética, sino que proporciona una taxonomía de resultados de alto nivel que cualquier organización puede utilizar para comprender, evaluar, priorizar y comunicar sus esfuerzos en esta materia.

## Diapositiva 8 — Contenido

Estructura Fundamental del CSF Core

El CSF Core organiza sus componentes en tres niveles jerárquicos que permiten una implementación modular según las necesidades específicas de cada organización:

Funciones (6 en total) - Son los objetivos estratégicos que guían la gestión de ciberseguridad:

Gobernar (GV): Establece la estrategia, expectativas y políticas de gestión de riesgos de seguridad cibernética. Define roles, responsabilidades y asegura alineación con objetivos empresariales.

Identificar (ID): Conoce los riesgos actuales de seguridad cibernética, mapeando activos críticos (datos, sistemas, personas), vulnerabilidades y dependencias tecnológicas.

Proteger (PR): Implementa salvaguardas técnicas y organizativas para limitar el impacto de amenazas (ej.: cifrado, controles de acceso, formación del personal).

Detectar (DE): Monitorea continuamente sistemas y redes para identificar incidentes en tiempo real.

Responder (RS): Actúa ante incidentes confirmados mediante planes predefinidos (contención, comunicación, análisis).

Recuperar (RC): Restaura operaciones afectadas y aprende de incidentes para mejorar la resiliencia.

100%

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

10

Lorem ipsum dolor sit amet, consectetur

## Diapositiva 9 — Contenido

Categorías (35 en total) - Cada función se desglosa en categorías, áreas temáticas concretas para priorizar acciones.

Por ejemplo:

En Gobernar: Contexto organizativo, Estrategia de gestión de riesgos, Gestión de riesgos de cadena de suministro.

En Identificar: Gestión de activos, Evaluación de riesgos, Mejora.

En Proteger: Gestión de identidades, Seguridad de datos, Resiliencia de infraestructura.

## Diapositiva 10 — Contenido

Subcategorías (108 en total) - Son actividades específicas y medibles que operacionalizan las categorías.

Por ejemplo:

"Implementar autenticación multifactor (MFA) en sistemas críticos" (Proteger).

"Establecer un programa continuo de concienciación en phishing" (Proteger).

"Monitorear las actividades y servicios de proveedores externos" (Detectar).

## Diapositiva 11 — Contenido

Perfiles y Niveles del CSF

Perfiles Organizativos: Un Perfil Organizativo describe la postura de seguridad cibernética actual u objetivo de una organización en términos de los resultados del CSF Core.

Incluye:

Perfil Actual: Especifica los resultados que una organización está logrando actualmente y cómo se están alcanzando.

Perfil Objetivo: Especifica los resultados deseados que una organización ha seleccionado para alcanzar sus objetivos de gestión de riesgos.

## Diapositiva 12 — Contenido

Niveles del CSF:Los Niveles caracterizan el rigor de las prácticas de gobernanza y gestión de riesgos de una organización:

Nivel 1: Parcial - Prácticas ad hoc, conciencia limitada de riesgos

Nivel 2: Conocimiento de riesgos - Prácticas aprobadas por gerencia, conciencia organizacional

Nivel 3: Repetible - Políticas formales, enfoque de toda la organización, métodos consistentes

Nivel 4: Adaptable - Enfoque basado en riesgos, prácticas avanzadas, adaptación continua

## Diapositiva 13 — Contenido

Innovaciones Clave del CSF 2.0

- Enfoque estratégico en gobernanza: La nueva función "Gobernar" exige que los líderes empresariales asuman responsabilidad activa sobre los riesgos cibernéticos, integrándolos en la toma de decisiones estratégicas y alineándolos con objetivos empresariales.

- Adaptabilidad para PYMES: Se incluyen "Guías de inicio rápido" (Quick Start Guides) con pasos prácticos y ejemplos concretos para organizaciones con recursos limitados, democratizando el acceso al marco.

- Gestión de riesgos en la cadena de suministro: Aborda amenazas como proveedores vulnerables o software comprometido, crítico en entornos globalizados. Incluye categorías específicas para gestionar riesgos de terceros.

## Diapositiva 14 — Contenido

Innovaciones Clave del CSF 2.0

4. Medición de resultados: Introduce métricas cuantificables (ej.: tiempo de detección de incidentes, reducción de exposición de datos) para evaluar el progreso y justificar inversiones en seguridad.

5. Recursos complementarios en línea: El NIST ofrece Referencias Informativas (mapeos a estándares existentes), Ejemplos de Implementación (acciones concretas) y Guías de Inicio Rápido para facilitar la adopción del marco.

6. Integración con gestión de riesgos empresariales (ERM): Facilita la comunicación entre equipos técnicos y directivos mediante un lenguaje común, permitiendo integrar los riesgos cibernéticos en la cartera general de riesgos de la organización.

## Diapositiva 15 — Contenido

Beneficios prácticos del CSF 2.0:

- Comunicación efectiva: Proporciona un lenguaje común para la comunicación interna y externa sobre riesgos de seguridad cibernética, capacidades, necesidades y expectativas.

- Priorización estratégica: Ayuda a identificar, organizar y priorizar acciones para gestionar riesgos que se alinean con la misión de la organización, requisitos legales y expectativas de gestión.

- Integración con otros marcos: Facilita la alineación con estándares como ISO 27001, CIS Controls, NIST SP 800-53 y regulaciones como GDPR, evitando esfuerzos duplicados.

- Mejora continua: Establece un ciclo de evaluación constante que permite a las organizaciones adaptarse a amenazas emergentes y cambios tecnológicos.

## Diapositiva 16 — Contenido

Casos de uso prácticos:

- PYMES: Utilizan las Guías de Inicio Rápido para implementar controles básicos de seguridad con recursos limitados.

- Sector financiero: Aplican perfiles específicos para cumplir con regulaciones y proteger datos sensibles de clientes.

- Salud: Implementan el marco para proteger historiales médicos y asegurar la disponibilidad de sistemas críticos.

- Gobierno: Utilizan el CSF para estandarizar la seguridad cibernética en múltiples agencias y mejorar la resiliencia nacional.

- Cadena de suministro: Organizaciones evalúan y gestionan riesgos de proveedores críticos mediante las categorías específicas de gestión de riesgos de cadena de suministro.

## Diapositiva 17 — Actividad de aprendizaje

A continuación, realizaremos la autoevaluación de conocimientos adquiridos en este recurso. Consiste en responder 3 preguntas de selección múltiple con única respuesta.

**Actividad (QUIZ_ACTIVITY):** Durante el análisis de un escenario de compromiso, se identifica que un atacante podría enviar un correo fraudulento para obtener credenciales de acceso y luego ingresar a una aplicación institucional. ¿Qué elementos se están relacionando principalmente?

- Copias de seguridad, recuperación y restauración.
- Ingeniería social, vector de ataque y acceso no autorizado. **(correcta)**
- Actualización de sistemas, monitoreo y cifrado.
- Segmentación de red, hardening y disponibilidad.

## Diapositiva 18 — Actividad de aprendizaje

A continuación, realizaremos la autoevaluación de conocimientos adquiridos en este recurso. Consiste en responder 3 preguntas de selección múltiple con única respuesta.

**Actividad (QUIZ_ACTIVITY):** Una organización identifica una vulnerabilidad en una aplicación web expuesta a internet. El sistema afectado almacena información sensible y la falla podría ser explotada fácilmente. ¿Qué criterio debe orientar la priorización de este hallazgo?

- El color de la interfaz de la aplicación
- La cantidad de usuarios que conocen la herramienta
- La exposición, facilidad de explotación, valor del activo e impacto potencial **(correcta)**
- El nombre comercial del software utilizado

## Diapositiva 19 — Actividad de aprendizaje

A continuación, realizaremos la autoevaluación de conocimientos adquiridos en este recurso. Consiste en responder 3 preguntas de selección múltiple con única respuesta.

**Actividad (QUIZ_ACTIVITY):** Después de analizar varios vectores de ataque, un equipo propone monitoreo de logs, segmentación de red, autenticación multifactor, cierre de puertos no utilizados y actualización de sistemas. ¿Cuál es el propósito principal de estas acciones?

- Aumentar la superficie de exposición del entorno
- Sustentar el hallazgo y orientar acciones de mejora **(correcta)**
- Permitir que todos los usuarios tengan privilegios administrativos
- Eliminar la necesidad de documentar los incidentes.

## Diapositiva 20 — Referencias bibliográficas

Referencias Bibliográficas

NIST. (2024). The NIST Cybersecurity Framework (CSF) 2.0 (pp 1-32). https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf

## Diapositiva 21 — Conclusiones

El Marco de Seguridad Cibernética (CSF) 2.0 del NIST representa un avance fundamental en la gestión de riesgos cibernéticos, ofreciendo una estructura flexible basada en seis funciones interconectadas -con la innovadora función "Gobernar" como eje central- que permite a organizaciones de cualquier tamaño y sector comprender, priorizar y comunicar eficazmente sus esfuerzos de seguridad, mientras que sus Perfiles Organizativos y Niveles proporcionan mecanismos prácticos para evaluar la madurez actual y diseñar hojas de ruta hacia una postura más robusta, democratizando el acceso a buenas prácticas de ciberseguridad mediante recursos como las Guías de Inicio Rápido para PYMES, el enfoque en gestión de riesgos de cadena de suministro y métricas cuantificables que, en conjunto, crean un lenguaje común para alinear la seguridad cibernética con los objetivos estratégicos empresariales y construir resiliencia organizacional a largo plazo en un entorno digital cada vez más complejo.

## Diapositiva 22 — Créditos

Escuela de Ciencias de Básicas Tecnología e Ingeniería

Maestría en Ciberseguridad

Eduard Antonio Mantilla Torres

2025

UNAD

Esta obra está protegida por derecho de autor bajo la titularidad de la UNAD. Cualquier reproducción o copia sin autorización constituye un delito conforme la legislación nacional.

## Ficha de referencia sugerida (APA 7)

Mantilla Torres, E. A. (2025). *Marco de seguridad cibernética 2.0 del NIST para gestión de los riesgos de seguridad cibernética* (OVA 2) [OVA]. Universidad Nacional Abierta y a Distancia. https://view.genially.com/6a29fb634ab60d77b87d6b2c/presentation-ova-2-iyt-203028113

> Autor, año y título se tomaron de la portada y de la diapositiva de créditos del recurso. El enlace público de Genially corresponde a la exportación consultada.
