---
tags: [contexto, orientacion, guia, reto-2]
---

# Qué me piden y qué tengo que entregar

> Esta nota es el mapa de todo el reto. Lela **antes** de abrir cualquier otra.
> Fuentes: [[04 - Referencias/Referencias y lectura]] · Guía de aprendizaje (6 págs.) · Anexo 1 (48 págs.)

## TL;DR

Te dan un caso (AgroSmart) y una carpeta de **artefactos de reconocimiento** ya recolectados. Tu trabajo es **razonar como atacante sobre esos datos** y producir un análisis sustentado, cuyo entregable es **un video de máximo 10 minutos**.

No te piden escanear nada. No te piden una máquina. No hay laboratorio que romper. Todo el trabajo es documental y argumentativo.

> [!danger] Fecha límite
> Inicia **lunes 31 de agosto 2026** · Finaliza **domingo 27 de septiembre 2026**.
> **45 horas** de trabajo autónomo · **125 puntos**.

---

## 1. El encargo, en una frase

> *"Evaluar vulnerabilidades en infraestructuras digitales mediante la aplicación de metodologías de intrusión, pruebas de penetración e ingeniería social, interpretando críticamente los vectores de ataque para anticipar escenarios de compromiso y fortalecer la postura de seguridad de la organización."*

Eso es el **Resultado de aprendizaje 1**. Léelo despacio: dice *evaluar*, *interpretar*, *anticipar*. Ninguno de esos verbos es "escanear".

## 2. Dos documentos, dos funciones distintas

| | **Guía** (6 págs.) | **Anexo 1** (48 págs.) |
|---|---|---|
| Es el | **instructivo** | **el caso + los formularios** |
| Responde a | ¿Qué, cuánto, con qué reglas? | ¿Sobre qué? ¿Con qué datos? ¿Dónde entrego? |
| Cómo se lee | Completa, en orden (6 págs.) | Por secciones, **no entera** |
| Son 20% rastro / 80% tuyo | Reglas y plazos | El resto lo produzcas tú |

> [!important] La frase que lo explica todo (Anexo pág. 3)
> *"Los identificadores CVE, técnicas MITRE (Txxxx) y referencias son **pistas a investigar**: el documento no entrega la respuesta resuelta, **entrega el rastro**."*

El Anexo te da un banner de `Apache httpd 2.4.49`, un error SQL, un evento 7045. Eso es la pista. El hallazgo completo —con CVE, severidad, vector CVSS, mapeo MITRE y justificación— lo construyes tú.

Si entregaras solo lo que el Anexo ya tiene escrito en las tablas, estarías reprobando.

---

## 3. El punto más importante: hay DOS guiones y hay que fusionarlos

Esta es la trampa principal del reto. La guía pide un video con **6 apartados académicos**; el Anexo (pág. 30) propone un guion de **6 bloques analíticos**. **No son los mismos**, y el video final cumple ambos.

| Apartado que exige la **Guía** (págs. 5-6) | Qué metes ahí | Bloque del guion del **Anexo** (pág. 30) |
|---|---|---|
| **1. Introducción** — título del caso, contexto general, objetivo, justificación | El encuadre ético y el alcance | **1.** Presentación y encuadre ético (alcance, ROE, finalidad defensiva) |
| **2. Descripción del caso** — contexto específico, situación problemática, actores, datos relevantes | Caso AgroSmart, arquitectura de 3 dominios (Anexo 2.1-2.2) | — |
| **3. Análisis preliminar** — problema principal, causas, consecuencias, perspectiva teórica, valoración crítica | **Aquí va el 80% del video** | **2.** Activos críticos y superficie · **3.** Vulnerabilidades CVE/CVSS · **4.** Ingeniería social · **5.** Ruta CKC + MITRE ATT&CK |
| **4. Conclusiones** — síntesis del aprendizaje, reflexión, recomendaciones | Impacto, riesgo y qué debería preocupar a la gerencia | **6.** Impacto/riesgo y mensaje de cierre |
| **5. Preguntas para discusión** — que promuevan continuidad analítica en los retos siguientes | ⚠️ **Olvidado por casi todos.** Tienes que escribirlas tú | — |
| **6. Referencias** — fuentes en normas APA | Los 9 referentes + complementarias | — |

**Estructura real del video:** el bloque 3 de la guía es enorme (4 de los 6 bloques del guion del Anexo caben ahí). Reparte los 10 minutos con eso en mente.

### Las "preguntas para discusión"
La guía dice que deben *promover continuidad analítica en los retos posteriores*. Los retos siguientes son **Reto 3** (diseño de detección y defensa), **Reto 4** (planificación) y **Reto 5** (ejecución en Cyber Range). Ejemplos del tipo de pregunta que sí encajan:

- ¿Qué regla de detección en el segmento IoT/OT habría detectado el acceso al broker MQTT antes del movimiento al PLC?
- ¿Cuál de los vectores mapeados es el más costoso de remediar y por qué conviene priorizarlo?
- ¿Qué controles del Reto 3 no quedarían cubiertos si el adversario ya tiene acceso persistente al segmento IT?

---

## 4. Qué entregas exactamente

| # | Entregable | Dónde se diligencia | Peso |
|---|-----------|--------------------|------|
| 1 | **Video expositivo** (MP4, 10 min máx, desde PowerPoint) | [[03 - Video/Guion del video]] | Evidencia principal |
| 2 | **Instrumentos 2.1 → 2.9** (las tablas del Anexo) | `02 - Instrumentos Reto 2/` | Alimentan el video |
| 3 | **Instrumentos 1.1, 1.B, 1.C** (concepto, metodologías, glosario de 10) | `02 - Instrumentos Reto 2/` |idem |
| 4 | **Declaración de uso de IA** (si la usaste) | [[02 - Instrumentos Reto 2/Declaracion uso de IA]] | Obligatoria si aplica |
| 5 | **Referencias en APA 7** | [[04 - Referencias/Referencias y lectura]] | Requisito del Paso 9 |

> [!note] Aclaración sobre los 125 puntos
> La guía dice: *"Puntuación del cuestionario de evaluación de este Reto: 125"*. El Anexo dice *"Valor: 125 puntos"* para el Reto 2. **Confirma con el curso si además de la evidencia (video) hay un cuestionario que responder.**

## 5. Condiciones técnicas del video (texto literal de la guía)

| Condición | Detalle |
|-----------|---------|
| Formato | **MP4** |
| Origen | **Generado a partir de una presentación en PowerPoint exportada a video** |
| Duración | **Máximo 10 minutos** |
| Peso | **Máximo 200 MB** |
| Tablas | Deben **diseñarse e incrustarse directamente en el archivo editable** y mostrarse en el video |
| Prohibido | Tablas desde hojas de cálculo externas; **capturas de pantalla o imágenes** que reemplacen contenido analítico |
| Prohibido | **Enlazar URLs externas o vínculos a repositorios en la nube** como sustituto del contenido |

> [!warning] Implicación práctica
> No puedes grabar talking-heads. Tienes que hacer una **PowerPoint real** y exportarla. Las tablas van como **tablas nativas de PowerPoint**, no como imágenes de pantalla. Y los enlaces que hay en este vault sirven para que tú estudies, **no** para linkearlos en el video: el contenido va dentro.

## 6. Mapa: requisito → dónde está cada cosa

| Lo que te piden | Guía | Anexo | Tu nota |
|---|---|---|---|
| Contexto y arquitectura | — | pág. 9-10 | [[Contexto y arquitectura]] |
| Ley 1273, ROE, alcance | — | pág. 7-8 | [[Marco legal y ROE]] |
| Los 13 artefactos (datos) | pág. 2 | pág. 11-22 | `01 - Artefactos/` |
| Núcleo conceptual | — | pág. 23 | [[02 - Instrumentos Reto 2/1.1 Núcleo conceptual]] |
| Comparar metodologías | — | pág. 24 | [[02 - Instrumentos Reto 2/1.B Comparación de metodologías]] |
| Glosario de 10 definiciones | pág. 3 (Paso 2) | pág. 24 | [[02 - Instrumentos Reto 2/1.C Glosario operativo]] |
| Activos críticos C/I/D | pág. 3 (Paso 1) | pág. 26 | [[02 - Instrumentos Reto 2/2.1 Activos críticos C-I-D]] |
| Superficie de exposición | pág. 3 (Paso 1) | pág. 26 | [[02 - Instrumentos Reto 2/2.2 Superficie de exposición]] |
| Matriz CVE/CVSS | pág. 3 (Paso 2) | pág. 26-28 | [[02 - Instrumentos Reto 2/2.3 Matriz CVE-CVSS]] |
| Vectores de ataque | pág. 3 (Paso 2) | pág. 28 | [[02 - Instrumentos Reto 2/2.4 Vectores de ataque]] |
| Ingeniería social | pág. 3 (Paso 2) | pág. 28 | [[02 - Instrumentos Reto 2/2.5 Ingeniería social]] |
| Cyber Kill Chain | pág. 4 (Paso 5) | pág. 28-29 | [[02 - Instrumentos Reto 2/2.6 Cyber Kill Chain]] |
| MITRE ATT&CK | pág. 4 (Paso 5) | pág. 29 | [[02 - Instrumentos Reto 2/2.7 MITRE ATT&CK]] |
| Ruta probable de ataque | pág. 4 (Paso 6) | pág. 29 | [[02 - Instrumentos Reto 2/2.8 Ruta probable de ataque]] |
| Impacto y riesgo | pág. 4 (Paso 7) | pág. 29 | [[02 - Instrumentos Reto 2/2.9 Impacto y riesgo]] |
| Video (6 apartados) | pág. 5-6 | pág. 30 | [[03 - Video/Guion del video]] |
| Referencias APA | pág. 4 (Paso 9) | — | [[04 - Referencias/Referencias y lectura]] |
| Declaración de IA | pág. 5 | pág. 25 y 30 | [[02 - Instrumentos Reto 2/Declaracion uso de IA]] |

## 7. Cómo se lee el Anexo (mapa de páginas)

**No leas las 48 páginas.** Esto es lo que importa:

| Págs. | Qué es | ¿Lo lees? |
|---|---|---|
| 1-6 | Introducción, cómo usar el documento | Sí, una vez |
| 7-8 | Marco legal y ROE (+ Instrumento 1.A → **es del Reto 4**) | Sí, para el bloque 1 del video |
| 9-10 | El caso: contexto y arquitectura | Sí, para el bloque 2 del video |
| **11-22** | **Informe de insumos** — los 13 artefactos (3.1-3.13) | **Sí, es tu materia prima** |
| **23-31** | **RETO 2** — lo que diligencias | **Sí, es tu trabajo** |
| 32-45 | RETO 3 — diseño de detección y defensa | **No**, es otro reto |
| 46-48 | RETO 5 — ejecución en Cyber Range | **No**, es otro reto |

> [!tip] La distinción clave
> Págs. 11-22 son **datos** (te los dieron). Págs. 23-31 son **formularios en blanco** (los llenas tú). No se mezclan.

### Convenciones visuales del Anexo (pág. 2)
- 🟧 **Cajas naranjas** → Declaración de uso de IA (omite si no la usas)
- 📋 **Tablas con filas en blanco** → instrumentos para diligenciar
- ⬛ **Bloques negros** → salidas de consola / artefactos de reconocimiento
- 🟦 **Cajas azules** → contexto o reglas
- `Sec. X` → referencia cruzada a otra sección del mismo Anexo

## 8. Los 5 artefactos que te entrega el Anexo

La guía (pág. 2) los lista como el punto de partida. En el Anexo son la **Sec. 3**:

1. **Inventario de activos** (3.1) — 8 activos, A-01 a A-08, con dominio y servicio
2. **Reconocimiento de servicios** (3.2) — salida de Nmap con banners de versión
3. **OSINT e ingeniería social** (3.4) — correos, dominios, el correo sospechoso de Contabilidad
4. **Logs simulados** (3.6) — eventos Windows y de red para correlación
5. **Evidencias preliminares** (3.7-3.8) — `/backup/`, `config.php.bak`, `.git` expuesto, JWT

Los identificadores de activo (`A-01` … `A-08`) son el hilo conductor: aparecen en los artefactos y los debes reutilizar en **todas** las tablas de los instrumentos.

## 9. Sobre el uso de IA

Texto de la guía (pág. 5): el uso de IA **está permitido** como apoyo para explorar ideas, organizar información, contrastar enfoques, mejorar el guion o fortalecer la comprensión del caso. **Pero** debe ser explícito, documentado y críticamente validado, y tú eres responsable de verificar la calidad de la información, contrastarla con fuentes confiables y evitar el uso acrítico o la reproducción literal.

En concreto:
- La **declaración es obligatoria si la usaste**. Si no, la dejas expresamente indicada.
- **Verifica siempre contra fuentes primarias**: NVD para los CVE, MITRE para los IDs de técnica, el propio Anexo para los datos del caso.
- No copies salidas de forma literal: el evaluador lo nota.

## 10. Cómo se encadenan los 9 pasos

No son 9 tareas sueltas. Son una secuencia de razonamiento donde cada paso consume el anterior:

```
Paso 1  Activos y dominios          ──►  qué importa
Paso 2  Vectores, ing. social, CVEs ──►  por dónde se ataca
Paso 3  Reconocer los artefactos    ──►  la evidencia concreta
Paso 4  Analizar con los instrumentos► lo convierte en hallazgos
Paso 5  Mapear a CKC y MITRE        ──►  dónde encaja en el framework
Paso 6  Ruta probable de ataque     ──►  la secuencia completa
Paso 7  Impacto y riesgo            ──►  qué se pierde si ocurre
Paso 8  Grabar el video             ──►  la evidencia
Paso 9  Referencias APA             ──►  la sustentación
```

Los pasos 1, 2 y 3 se alimentan entre sí; el 4 al 7 son el cuerpo analítico; el 8 y 9 son la entrega.

---

Relaciona: [[index]] · [[Contexto y arquitectura]] · [[Marco legal y ROE]] · [[04 - Referencias/Referencias y lectura]]
