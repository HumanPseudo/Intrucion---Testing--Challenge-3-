---
tags: [video, entregable, reto-2]
---

# Guion del video — evidencia del Reto 2

> Fuente del guion: [Anexo 1 pág. 30](05%20-%20Fuentes/Anexo%201%20Caso%20AgroSmart%20del%20Sumapaz.pdf) · [Guía de aprendizaje](05%20-%20Fuentes/Gu%C3%ADa%20de%20aprendizaje%20-%20Reto%202%20-%20An%C3%A1lisis%20de%20vectores%20de%20ataque.pdf) · [[00 - Contexto/Rúbrica de evaluación|Rúbrica de evaluación]] (fija las 8 secciones y los 3 criterios)

## Entregable

- [Abrir la presentación](03%20-%20Video/Reto2%20-%20AgroSmart%20-%20An%C3%A1lisis%20de%20vectores%20de%20ataque%20%28ciberpunk%29.pptx) — 22 diapositivas, **14 tablas nativas editables**, 0 imágenes.
- Narración: **538 s (8:58)**. Con transiciones (11 s) y animaciones de entrada (14 s) nativas, la duración exportada es **563 s (9:23)** — determinista, porque cada transición lleva `advTm` con el segundo exacto de `TIMING` (no depende de que PowerPoint calcule bien las animaciones al exportar). Holgura: 37 s bajo el límite de 600 s.
- No se requiere aparecer en cámara: la rúbrica solo exige "video generado a partir de una presentación en PowerPoint exportada a video" con "audio continuo y comprensible". Al grabar en PowerPoint puedes desactivar la cámara y grabar solo audio + diapositivas.
- Fuentes declaradas en el XML: Arial Narrow, Calibri y Consolas (todas estándar de Office, sin sustituciones al abrir en PowerPoint).

## Estructura de la presentación (8 secciones de la rúbrica)

| Diapositiva | Título en pantalla                                                           | Sección (rúbrica)                         | Instrumento / apartado              |
| ----------- | ---------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------- |
| 1           | Análisis de vectores de ataque, ingeniería social y escenarios de compromiso | —                                         | Portada                             |
| 2           | El caso y por qué importa                                                    | 1 · Introducción                          | Apartado 1 de la guía               |
| 3           | Alcance y reglas de compromiso (ROE)                                         | 1 · Introducción                          | Apartado 1 de la guía               |
| 4           | Situación problemática y actores                                             | 2 · Descripción del caso                  | Apartado 2 de la guía               |
| 5           | Arquitectura: tres dominios, tres fronteras                                  | 2 · Descripción del caso                  | Apartado 2 de la guía               |
| 6           | Activos técnicos: A-01 a A-08                                                | 2 · Descripción del caso                  | Apartado 2 de la guía               |
| 7           | Fases del testing y lectura de la evidencia                                  | 3 · Análisis preliminar                   | Apartado 3 de la guía               |
| 8           | Identificación y valoración de activos críticos                              | 3 · Análisis preliminar                   | Instrumento 2.1                     |
| 9           | Superficie de exposición y fronteras de confianza                            | 3 · Análisis preliminar                   | Instrumento 2.2                     |
| 10          | Vectores de ataque identificados                                             | 3 · Análisis preliminar                   | Instrumento 2.4                     |
| 11          | Matriz de vulnerabilidades: CVE y severidad                                  | 3 · Análisis preliminar                   | Instrumento 2.3                     |
| 12          | Ingeniería social: por qué funcionaría el pretexto                           | 3 · Análisis preliminar                   | Instrumento 2.5                     |
| 13          | Cyber Kill Chain (Lockheed Martin)                                           | 3 · Análisis preliminar                   | Instrumento 2.6                     |
| 14          | MITRE ATT&CK: Enterprise + ICS                                               | 3 · Análisis preliminar                   | Instrumento 2.7                     |
| 15          | Ruta probable: pista, hipótesis y validación                                 | 4 · Alternativas de análisis y validación | Instrumento 2.8 · Paso 7 de la guía |
| 16          | Ruta probable de compromiso (attack path)                                    | 5 · Propuesta preliminar                  | Instrumento 2.8                     |
| 17          | Impacto, probabilidad y riesgo (P × I)                                       | 5 · Propuesta preliminar                  | Instrumento 2.9                     |
| 18          | Conclusiones y recomendaciones                                               | 6 · Conclusiones                          | Apartado 4 de la guía               |
| 19          | Preguntas para discusión                                                     | 7 · Preguntas para discusión              | Apartado 5 de la guía               |
| 20          | Referencias (APA 7) · 1 de 2                                                 | 8 · Referencias                           | Apartado 6 de la guía               |
| 21          | Referencias (APA 7) · 2 de 2                                                 | 8 · Referencias                           | Apartado 6 de la guía               |
| 22          | Declaración de uso de inteligencia artificial                                | —                                         | Paso 9 de la guía                   |

> Nota: la diapositiva 15 (tabla pista→hipótesis→validación) va **antes** que la 16 (diagrama de
> la ruta) a propósito — primero se enseña el criterio con el que se descarta la ruta
> alternativa, después se presenta la ruta que ya queda sustentada.

## Guion completo (para leer)

> Texto exacto de las notas del orador del `.pptx` generado — léelo palabra por palabra, en tu
> propio ritmo natural. El segundo junto a cada título es el tiempo asignado en `TIMING`; a
> algunos les sobrará o faltará un poco según tu velocidad de lectura, y está bien: son una
> guía de ritmo, no un cronómetro que debas perseguir sílaba por sílaba.

**01 · Portada** — 10 s
Presento el análisis de vectores de ataque, ingeniería social y escenarios de compromiso para el caso AgroSmart del Sumapaz. Es un análisis defensivo, no ofensivo.

**02 · El caso y por qué importa** — 24 s
AgroSmart del Sumapaz opera un portal de pedidos, un segmento corporativo Windows y un parque IoT/OT que controla el riego, sin segmentación entre los tres. Se identifican vectores de ataque, ingeniería social y escenarios de compromiso.

**03 · Alcance y reglas de compromiso (ROE)** — 24 s
AgroSmart autoriza el reconocimiento, la enumeración y la validación controlada de los ocho activos, únicamente dentro del Rango descrito. Quedan fuera cualquier objetivo real y la ingeniería social ejecutada contra personas: si no está explícito en el alcance, está fuera. La Ley 1273 de 2009, artículo 269A, tipifica el acceso abusivo a un sistema informático; aplican también la Ley 1581 de 2012 y la Ley 1341 de 2009.

**04 · Situación problemática y actores** — 19 s
El riego depende de un broker para el transporte de telemetria de cola de mensajes y un PLC sin autenticación; el portal de pedidos comparte dominio con el servidor de archivos, que acepta sesiones nulas. El usuario amunoz, de Contabilidad, aparece expuesto en el open source intelligence, en los logs y en la API.

**05 · Arquitectura: tres dominios, tres fronteras** — 28 s
La arquitectura tiene tres dominios y tres fronteras. La F1, entre Internet y la DMZ, expone el portal y phpMyAdmin. La F2, entre la DMZ y la red interna, no tiene control de flujo. La F3, entre el segmento IT y el segmento IoT/OT, es una frontera débil: comparten la misma red conmutada. Por eso un incidente en la TI puede convertirse en un incidente físico en el riego.

**06 · Activos técnicos: A-01 a A-08** — 19 s
Los ocho activos, de A-01 a A-08, se distribuyen en los tres dominios: DMZ/Web, IT e IoT/OT. A-07, el controlador de riego, y A-08, el broker de telemetría, son los vectores mas sensibles de ataque.

**07 · Fases del testing y lectura de la evidencia** — 18 s
El análisis se apoya en tres marcos: la normativa de ejecucion de pruebas de penetracion que ordena las fases, la guia de pruebas de seguridad web la publicacion especial NIST SP 800-115 fija el rigor de la evidencia. Este es un análisis documental

**08 · Identificación y valoración de activos críticos** — 32 s
se valora la confidencialidad, integridad y disponibilidad de uno a cinco, según el impacto sobre el negocio. El portal y phpMyAdmin comparten la máxima confidencialidad: son el único camino desde Internet hasta los pedidos y la base de datos. El controlador de riego, A-07, concentra la máxima disponibilidad e integridad: siendo esta sensible a comandos erronos afectando directamente el cultivo.

**09 · Superficie de exposición y fronteras de confianza** — 24 s
De once puntos de entrada, nueve no tienen autenticación en su frontera. El riesgo no está en Internet, que es visible y monitoreada, sino en las tres entradas internas: de comparticion de archivos y escritorio remoto remoto de aceso remoto y de comunicacion de dispositivos  SMB y RDP, sin embargo el Anexo no confirma su exposición más allá del propio host.

**10 · Vectores de ataque identificados** — 32 s
se identifican diez vectores de ataque. Los primeros cinco se apoyan en la aplicación web: explotación de Apache, inyección SQL, IDOR, falsificación del JWT y robo de credenciales expuestas. El sexto y el noveno afectan al segmento IoT/OT: credenciales por defecto en el gateway y manipulación de comandos. El séptimo y el octavo conectan la ingeniería social con el movimiento lateral. El décimo es del navegador: librerías desactualizadas y TLS débil.

**11 · Matriz de vulnerabilidades: CVE y severidad** — 36 s
Verifiqué cinco CVE contra el NVD. en Apache 2.4.49 y 2.4.50, puntúan 9.8 y tienen explotación activa confirmada en el catálogo KEV de CISA. CVE-2017-0143, la familia EternalBlue en SMBv1, puntúa 8.8 y también está en KEV. Para la cámara IP, CVE-2017-9833 figura como disputado en el NVD, y CVE-2022-45956, un bypass de autenticación, no está en KEV. Las cinco debilidades restantes son CWE sin CVE asignado, con severidad estimada.

**12 · Ingeniería social: por qué funcionaría el pretexto** — 28 s
El pretexto combina tres palancas que la organización ya dejó expuestas: la autoridad del proveedor de TI, la urgencia de una actualización de credenciales y datos reales, como el nombre de usuario y la ruta interna, publicados sin control. se Sigue la caracterización de Benavides Astudillo y su equipo sobre ataques de ingeniería social. La mitigación es procedimental, no tecnológica,

**13 · Cyber Kill Chain (Lockheed Martin)** — 32 s
se Organiza la intrusión en las siete fases de la Cyber Kill Chain  Las últimas cuatro quedan documentadas directamente en los registros: el evento 7045 define la instalación, Sysmon 3 define el canal de comando y control, y el PUBLISH en el tópico de riego define el objetivo. El punto de inflexión está en la fase de explotación: treinta y siete intentos de acceso contra el panel de administración, sin bloqueo.

**14 · MITRE ATT&CK: Enterprise + ICS** — 28 s
Mapeo trece técnicas de MITRE ATT&CK en siete tácticas, verificadas contra attack.mitre.org. T1606.001 es la falsificación de la credencial web del JWT, no una escalada del sistema operativo. T1210, la explotación de SMBv1, se marca como posible porque los logs no la muestran. T0855, de ATT&CK for ICS, es la orden no autorizada al proceso físico del riego.

**15 · Ruta probable: pista, hipótesis y validación** — 36 s
Para cada uno de los ocho saltos, separo lo que el Anexo 1 muestra, lo que infiero y la evidencia que haría falta para confirmarlo. Prioricé esta ruta, con phishing, porque los saltos tres, seis, siete y ocho tienen registro directo en los logs. Existe una ruta alternativa puramente técnica, sin ingeniería social, que entra por Apache: es más corta, pero de ella solo consta que es explotable, no que se haya explotado.

**16 · Ruta probable de compromiso (attack path)** — 28 s
Esta es la ruta que queda sustentada, en ocho saltos: desde el OSINT hasta la orden publicada en el broker MQTT. El punto de quiebre es el sexto: la sesión nula por SMB permite pasar de la credencial al recurso compartido, desde donde se instala persistencia y se publica el comando que abre la válvula de riego.

**17 · Impacto, probabilidad y riesgo (P × I)** — 28 s
Valoré seis escenarios de compromiso como probabilidad por impacto, en una escala de uno a veinticinco. Los dos escenarios de riesgo veinte no son intercambiables: el robo de pedidos se recupera con dinero; la apertura no autorizada del riego es un impacto físico irreversible. La probabilidad se deriva de la exposición observada en el Anexo, no de una estimación subjetiva.

**18 · Conclusiones y recomendaciones** — 36 s
AgroSmart no tiene un punto débil aislado: tiene una cadena, desde el banner obsoleto de Apache hasta el broker MQTT anónimo. Corregir un solo eslabón la rompe. Recomiendo segmentar la red entre la DMZ y el segmento IoT/OT, corregir la verificación de firma del JWT, deshabilitar SMBv1, actualizar Apache a la versión mas actual y eliminar los respaldos expuestos. El riesgo real no está en el SQL ni en el Apache obsoleto: está en que el portal de pedidos y el controlador de riego comparten segmento sin autenticación entre ellos.

**19 · Preguntas para discusión** — 24 s
Dejo cuatro preguntas para los retos siguientes: qué regla de detección habría alertado sobre la publicación anómala en el riego; qué vector es más costoso de remediar; qué controles quedarían sin cobertura si la persistencia ya está instalada; y qué vector nunca debería probarse, ni siquiera en el Cyber Range.

**20 · Referencias (APA 7) · 1 de 2** — 9 s
Las referencias combinan recursos del curso, como el Boletín 28 del CSIRT Académico de la UNAD, con fuentes técnicas públicas: NVD, Exploit-DB y el catálogo KEV de CISA.

**21 · Referencias (APA 7) · 2 de 2** — 9 s
La Cyber Kill Chain es el modelo de Lockheed Martin; la verificación técnica está en el NIST SP 800-115 y en MITRE ATT&CK, Enterprise e ICS.

**22 · Declaración de uso de inteligencia artificial** — 14 s
Declaro el uso de inteligencia artificial: qué hizo la herramienta, qué hice yo y cómo verifiqué cada dato, según el detalle de esta tabla.

## Checklist de grabación

- [x] Diagrama lógico de los 3 dominios visible — diapositiva 5
- [x] Diagrama de la ruta de ataque visible — diapositiva 16
- [x] Pista, hipótesis y evidencia para validar en cada salto, con la ruta alternativa justificada (Paso 7) — diapositiva 15
- [x] Cada CVE con su ID, severidad CVSS v3.1 y estado de verificación — diapositiva 11 (**5 CVE**, no 4: incluye `CVE-2022-45956`)
- [x] `CVE-2017-9833` marcado como **DISPUTED**, no como vulnerabilidad confirmada — diapositiva 11
- [x] 13 técnicas MITRE; T1606.001 (JWT forjado), T1210 (posible, no observada) y T0855 (ICS) justificadas frente al Anexo 3.13 — diapositiva 14
- [x] Explotación de cada CVE (CISA KEV y Exploit-DB) — diapositiva 11
- [x] Tablas nativas de PowerPoint (14), sin capturas de pantalla ni imágenes — todo el deck
- [x] Sin enlaces externos ni repositorios en la nube — todo el deck
- [x] Las 4 preguntas para discusión están escritas — diapositiva 19
- [x] Referencias APA 7 (**16**, en orden alfabético, con OVI, OVA y Lockheed Martin) — diapositivas 20 y 21
- [x] Declaración de uso de IA completa, incluido el % apoyado en IA — diapositiva 22
- [ ] Exportar a MP4 (máx. 200 MB) desde PowerPoint
- [ ] Verificar que el MP4 exportado dura ≈563 s (9:23), no más de 600 s
- [ ] Ver el MP4 completo una vez: audio continuo y comprensible, tablas legibles, sin cortes

> [!warning] Antes de exportar
> El único archivo vigente es el que termina en **(ciberpunk)**. Si lo tienes abierto en LibreOffice o PowerPoint mientras `build_deck.py` lo regenera, ciérralo sin guardar y vuelve a abrirlo antes de exportar, para no exportar una versión desactualizada en memoria.

Relaciona: [[00 - Contexto/Rúbrica de evaluación]] · [[00 - Contexto/Review - verificación paso a paso]]
