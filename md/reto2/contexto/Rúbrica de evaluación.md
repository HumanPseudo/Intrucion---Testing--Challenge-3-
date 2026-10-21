---
tags: [rubrica, evaluacion, reto-2]
---

# Rúbrica de evaluación – Reto 2

> Fuente: rúbrica oficial de evaluación del Reto 2 (Análisis de vectores de ataque, ingeniería
> social y escenarios de compromiso). Nivel 1 de la jerarquía de fuentes (junto con el Anexo 1
> y la Guía de aprendizaje): define exactamente qué se califica y con cuántos puntos.

Apreciado estudiante, esta rúbrica presenta los criterios y los niveles con los que se
calificará su producto académico. Léala antes de elaborar el video, pues cada nivel describe
condiciones verificables en el archivo entregado.

## Indicaciones técnicas de entrega

1. Video académico/técnico en formato MP4, generado a partir de una presentación en
   PowerPoint exportada a video.
2. Duración máxima de 10 minutos, en velocidad normal, y peso máximo de 200 MB.
3. La presentación debe contener, con **título visible en la diapositiva**, las siguientes
   ocho (8) secciones estructurales:
   1. **Introducción**: título del caso, nombre del expositor, objetivo de la exposición y
      justificación del análisis.
   2. **Descripción del caso**: contexto de AgroSmart del Sumapaz S.A.S., dominios DMZ/Web,
      IT e IoT/OT, activos, actores y artefactos técnicos del Anexo 1.
   3. **Análisis preliminar**: activos críticos, superficies de exposición, vectores de
      ataque, ingeniería social, CVE/CVSS, Cyber Kill Chain y técnicas MITRE ATT&CK.
   4. **Alternativas de análisis y validación**: rutas de compromiso posibles, criterios de
      priorización (criticidad, exposición, madurez de explotación) y limitaciones.
   5. **Propuesta preliminar**: ruta probable de compromiso sustentada e impactos
      organizacionales (negocio, datos y OT/físico).
   6. **Conclusiones**: síntesis del aprendizaje y recomendaciones.
   7. **Preguntas para discusión**: preguntas técnicas que orienten los retos posteriores.
   8. **Referencias**: fuentes en normas APA, citadas verbalmente durante la exposición.
4. Estilo: lenguaje técnico, voz propia y encuadre ético-legal del ejercicio (Ley 1273 de
   2009 y reglas de compromiso del Anexo 1). El análisis es documental: no se ejecutan
   explotaciones.
5. Fuentes: es obligatoria la citación verbal. Deben usarse los recursos del curso y fuentes
   públicas de consulta técnica (NVD, Exploit-DB, MITRE ATT&CK, Lockheed Martin).
6. Nota aclaratoria: las tablas y cuadros comparativos deben estar diseñados dentro de la
   presentación. No se aceptan capturas de pantalla, imágenes ni enlaces a repositorios
   externos como sustituto del contenido analítico.

## Tabla 1. Rúbrica de evaluación

**Resultado de aprendizaje 1:** Evaluar vulnerabilidades en infraestructuras digitales
mediante la aplicación de metodologías de intrusión, pruebas de penetración e ingeniería
social, interpretando críticamente los vectores de ataque para anticipar escenarios de
compromiso y fortalecer la postura de seguridad.

**Tipo de actividad:** Independiente · **Puntaje:** 125 puntos

### Primer criterio (de forma) — 25 puntos, 20% del total

> El video cumple las condiciones técnicas de entrega y la presentación contiene, de forma
> explícita y rotulada, las ocho secciones estructurales exigidas.

- **Nivel alto (20-25 pts):** MP4 ≤10 min y ≤200 MB · texto extraído contiene las 8 secciones
  explícitamente · todas las tablas nativas, sin capturas ni URL externas · audio continuo y
  comprensible.
- **Nivel medio (15-19 pts):** MP4 correcto pero faltan 1-2 de las 8 secciones o alguna solo
  enunciada sin contenido · hasta 2 tablas como captura/imagen · audio con cortes puntuales.
- **Nivel bajo (1-14 pts):** faltan 3+ secciones · archivo no MP4 o excede duración/peso ·
  contenido analítico sustituido por capturas o enlaces externos · audio inaudible o ausente
  en parte.
- **No presentado:** 0 puntos.

### Segundo criterio (de contenido) — 50 puntos, 40% del total

> El video nombra los tres dominios del caso, clasifica los activos críticos y lista con
> identificador las vulnerabilidades y las técnicas adversarias, hasta construir una ruta
> probable de compromiso con sus impactos.

- **Nivel alto (40-50 pts):** menciona explícitamente "DMZ/Web", "IT" e "IoT/OT" y clasifica
  ≥6 activos · ≥4 vulnerabilidades con CVE + vector CVSS v3.1 + puntaje, asociadas a
  tecnologías del caso · ≥10 técnicas MITRE ATT&CK con ID Txxxx, nombre y táctica ·
  recorre las 7 fases CKC con acción, activo y pista · ≥2 técnicas de ingeniería social con
  rol, canal y pretexto · ruta de compromiso de ≥4 pasos con pista/hipótesis/evidencia
  pendiente en cada uno · ≥3 impactos organizacionales (negocio, datos, OT/físico) y ≥3
  preguntas técnicas.
- **Nivel medio (30-39 pts):** menciona los 3 dominios pero clasifica <6 activos o sin
  asociar dominio · 2-3 CVE, o CVE sin vector CVSS · 6-9 técnicas MITRE con ID · 4-6 fases
  CKC · 1 técnica de ingeniería social o sin pretexto/rol · ruta de 2-3 pasos o sin distinguir
  pista/hipótesis/evidencia en todos · 1-2 impactos y <3 preguntas.
- **Nivel bajo (1-29 pts):** no menciona los 3 dominios o no clasifica activos · <2 CVE o sin
  identificador/severidad · <6 técnicas MITRE o sin ID Txxxx · ≤3 fases CKC y sin ingeniería
  social · sin ruta trazable, impactos ni preguntas.
- **No presentado:** 0 puntos.

### Tercer criterio (de calidad académica) — 50 puntos, 40% del total

> El video sustenta cada afirmación en una pista del Anexo 1 y en una fuente pública
> verificable, e incluye referencias en normas APA, encuadre ético-legal y declaración de
> uso de inteligencia artificial.

- **Nivel alto (40-50 pts):** ≥5 referencias APA (mín. 2 del curso, mín. 2 de fuente técnica
  pública: NVD, Exploit-DB, MITRE ATT&CK o Lockheed Martin) + declaración de uso de IA ·
  la declaración de IA nombra herramienta, propósito y verificación (o indica explícitamente
  que no se usó) · cada CVE y cada técnica ATT&CK indica la sección/artefacto del Anexo 1
  que la respalda · enuncia el encuadre ético-legal (Ley 1273/2009 y ROE) y aclara que el
  análisis es documental, sin exploits · cita las fuentes verbalmente.
- **Nivel medio (30-39 pts):** 3-4 fuentes con errores de formato APA · declaración de IA
  presente pero sin propósito o verificación · solo parte de los CVE/técnicas indican su
  pista del Anexo 1 · encuadre ético mencionado en general, sin norma ni ROE.
- **Nivel bajo (1-29 pts):** <3 fuentes o sin norma APA · sin declaración de uso de IA ·
  afirmaciones sin pista del Anexo 1 ni fuente pública · sin mención del encuadre ético-legal.
- **No presentado:** 0 puntos.

---

Relaciona: [[Review - verificación paso a paso]] · [[05 - Fuentes/Guía de aprendizaje - Reto 2]]
