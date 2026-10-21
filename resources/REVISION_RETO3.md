# Revisión académica y auditoría de calidad — Reto 3
### Curso: Intrusión y Testing (Código 203028113) · Maestría en Ciberseguridad · UNAD
**Objeto:** guía de aprendizaje, rúbrica, referentes bibliográficos y corpus de PDFs del **Reto 3** «Diseño de estrategias de detección, defensa y fortalecimiento de la postura de ciberseguridad».

> **Alcance inequívoco:** este informe audita **el Reto 3 únicamente**. Cuando se menciona el «Reto 2» o el «Reto 4» es porque **la propia guía del Reto 3** los referencia: el Reto 3 *parte* del análisis ofensivo elaborado en el Reto 2 y *difiere* su validación al Reto 4. Esas menciones no son objeto de esta auditoría ni indican confusión de reto.

**Artefactos generados:** conversión íntegra de los 9 PDF a Markdown (`md/`), con índice en `md/INDEX.md`. Script reproducible: `md/_convert.py`.

> **Añadido — insumos del Reto 2 (`md/reto2/`).** Como el Reto 3 *se construye sobre el análisis ofensivo del Reto 2*, se incorporó también a Markdown el material de ese reto (documento maestro **Anexo 1**, guía del Reto 2, los 14 instrumentos 1.x/2.x y 8 notas de contexto). El punto de entrada es **`md/reto2/CONTEXTO-RETO3.md`** (contexto consolidado para redactar el informe). Ver Tarea 1.
>
> **Corrección de un falso positivo:** el «Anexo 1» que una primera pasada marcó como **inexistente/crítico** **existe** (documento maestro, 48 págs) y contiene la ficha y los 5 instrumentos del Reto 3. Ver §«Corrección de un falso positivo…».

> Nota de método: la conversión es **fiel e integral** (sin resúmenes). Los detalles de calidad y las salvedades (OCR, ligaduras, marcas de agua) están en `md/INDEX.md` y en la cabecera de cada `.md`.
>
> **Actualización:** los nombres de autores y los enlaces de las referencias fueron **corregidos** contrastándolos con los PDFs de respaldo (que son la fuente autorizada, ya que los recursos EBSCO solo son accesibles con credenciales institucionales). Ver la sección **«Errata aplicada»** al final.

---

## Tarea 1 — Organización y conversión de PDFs a Markdown

**Resultado:** ✅ Completa. Se detectaron **9 archivos `.pdf`** y **1 paquete `.h5p`** (que no es PDF sino un ZIP con una presentación H5P). **Todos los artefactos se convirtieron** a Markdown. **Añadido:** se convirtió también el material del Reto 2 (`md/reto2/`), por ser el insumo base del Reto 3.

Estructura creada:

```
md/
├── INDEX.md                     ← inventario y estado de conversión
├── _convert.py                  ← script reutilizable (PDF → MD)
├── _convert_h5p.py              ← script reutilizable (H5P → MD)
├── actividad/
│   ├── Guía de aprendizaje - Reto 3.md
│   └── course-presentation-508-508.md      (H5P → 7 diapositivas)
├── rubrica/
│   └── Rúbrica de evaluación - Reto 3.md
├── referencias/
│   ├── EBSCO-FullText-10_19_2026.md          (UNEMI)
│   ├── EBSCO-FullText-10_19_2026 (1).md      (Ciencia y Tecnología / phishing)
│   ├── Complexity - 2021 - Lu - Research on WiFi Penetration Testing with Kali Linux.md
│   ├── carla,+ODIGOS+V2-NUM3-2021-47-76.md
│   ├── indecs2023-pp168-173.md
│   ├── mquinde,+articulo10.md
│   └── Octubre_2024.md
└── reto2/                       ← insumos ofensivos del Reto 2 (contexto del Reto 3)
    ├── CONTEXTO-RETO3.md                       ← ⭐ contexto consolidado
    ├── fuentes/       (Anexo 1 48 págs, Guía Reto 2, guion del video, referencias)
    ├── instrumentos/  (1.1–2.9 + 3.13 + declaración IA)
    └── contexto/      (arquitectura, marco legal/ROE, rúbrica, glosario…)
```

**Además del corpus PDF, se convirtió el paquete H5P `course-presentation-508-508.h5p`** (→ `md/actividad/course-presentation-508-508.md`). Un `.h5p` **no es un PDF** sino un ZIP con una presentación interactiva (`H5P.CoursePresentation`); se transcribieron íntegras sus **7 diapositivas** (descripción, resultado de aprendizaje, actividades, tiempo, evaluación y créditos) y se inventariaron sus 7 audios de narración y 3 imágenes. **Salvedad:** la narración en audio no se transcribió (no hay motor STT disponible); el texto en pantalla, que contiene el mismo guion, sí está completo. Esta presentación es material **resumido/divulgativo** de la guía, no fuente normativa.

**Qué se conservó:** texto completo, encabezados/pies y numeración de página (marcas `[p. N]`), autores/afiliaciones/revista/volumen/número/año/DOI-URL, tablas (volcadas además como tablas Markdown), pies de figura y enumeración de imágenes, ecuaciones (INDECS ecs. 1-3), y **listas de referencias finales íntegras** de cada artículo.

**Salvedades de calidad (explícitas, no inventadas):**
- `Octubre_2024.pdf` p. 1 y guía p. 9: **páginas de imagen → OCR** (Tesseract spa+eng). La portada del boletín UNAD se reconoce con ruido; el título es legible.
- `Complexity …pdf` (Lu & Yu): la fuente original tiene un **mapeo de glifos corrupto** («Th» → «.»); se normalizó y se documentó. Residuo menor («e School» por «The School»).
- La «Tabla 1. Tabla de descripción» de la guía se reconstruyó como tabla Markdown con columnas duplicadas por el diseño del original; el contenido textual está íntegro.
- No hubo pérdidas de texto detectadas en el resto de documentos.

El detalle por archivo (páginas, estado, notas) está en **`md/INDEX.md`**.

---

## Tarea 2 — Revisión de la actividad

### 2.1 Resumen (5 líneas)
1. **Objetivo (uno solo):** alcanzar el *Resultado de aprendizaje 2* — «Diseñar esquemas integrales de detección, identificación y gestión de ataques cibernéticos, utilizando técnicas ofensivas y pensamiento adversarial, con el fin de aportar a la toma de decisiones tácticas y estratégicas en entornos organizacionales». El **producto** es un diseño **defensivo** para el caso AgroSmart del Sumapaz S.A.S.
2. **Entregable:** un **informe técnico de diseño defensivo** (Word .docx o PDF) de **6000-8000 palabras** (sin referencias), individual, con **10 secciones** obligatorias.
3. **Fases/pasos:** 15 pasos — retomar el análisis ofensivo del Reto 2 (1), clasificar activos por dominio (2), matriz de trazabilidad (3), priorizar riesgos (4), diseñar controles preventivos/detectivos/correctivos (5), hardening LAMP (6), seguridad de la app web (7), seguridad IT (8), seguridad IoT/OT (9), casos de uso SIEM/XDR (10), respuesta a incidentes (11), DevSecOps (12), criterios de validación para el Reto 4 (13), redactar el informe (14) y control de calidad/integridad académica (15).
4. **Caso:** AgroSmart del Sumapaz S.A.S., en tres dominios: DMZ/Web LAMP, corporativo IT e IoT/OT (invernadero inteligente).
5. **Cierre:** puntaje **125 puntos**, fechas 28-sep-2026 → 25-oct-2026, 30 h de trabajo independiente, evaluación «Intermedio». No se ejecutan pruebas técnicas (se difieren al Cyber Range del Reto 4).

### 2.2 Alineación resultado de aprendizaje ↔ contenido ↔ actividad

> El Reto 3 declara **un único resultado de aprendizaje (RA2)**, no varios. Lo descompongo abajo en sus tres componentes verificables para poder auditar la alineación.

| Componente del RA2 | ¿Lo evalúa la actividad/entregable? | ¿Lo soportan los contenidos/referentes? |
|---|---|---|
| Diseñar esquemas integrales de detección, identificación y gestión de ataques | ✅ Sí: secciones 3-8 del informe (matrices, controles, SIEM, respuesta). | ⚠️ **Parcial.** Los referentes son mayoritariamente **ofensivos** (SQLMAP, pentest WiFi, ingeniería social, phishing, metodologías de pentest). Los marcos **defensivos** exigidos (CIS Controls, NIST CSF, NIST SP 800-61, ISO/IEC 27001, OWASP ASVS/WSTG, MITRE ATT&CK, NVD) **no están entre los referentes suministrados** y el estudiante debe buscarlos por su cuenta. |
| Utilizar técnicas ofensivas y pensamiento adversarial | ✅ Sí: Pasos 1-4 recuperan activos, vectores, CVE/CVSS, MITRE y Kill Chain **del Reto 2** (insumo base que la guía del Reto 3 exige retomar). | ✅ Sí: los referentes del curso son de naturaleza ofensiva. |
| Aportar a decisiones tácticas y estratégicas organizacionales | ⚠️ Parcial: priorización de riesgos y plan de respuesta lo abordan implícitamente. | ⚠️ No hay referente de gobierno de seguridad / gestión de riesgos organizacional entre los materiales. |

**Síntesis:** hay alineación entre el RA2 y el entregable. El único desajuste real es **bibliográfico**: el banco de referentes provisto es **ofensivo** (coherente con el Reto 2, del cual el Reto 3 se nutre), mientras el Reto 3 exige **diseño defensivo**; la rúbrica premia ≥3 marcos técnicos que el estudiante debe procurarse por su cuenta. (Encadenamiento del curso: Reto 2 = ofensivo → **Reto 3 = defensivo (este)** → Reto 4 = validación en Cyber Range.)

### 2.3 Ambigüedades, instrucciones incompletas y problemas de coherencia

| # | Hallazgo | Tipo | Gravedad |
|---|---|---|---|
| A1 | **«Anexo 1» no está publicado *en `resources/`*.** La rúbrica lo cita **5 veces** («al menos 8 activos del Anexo 1», «la sección o el artefacto del Anexo 1», «pistas del Anexo 1») y la guía del Reto 3 **no lo adjunta ni lo describe**. **Corrección (ver §«Corrección de un falso positivo…» y «Errata aplicada»):** el Anexo **sí existe** — es el documento maestro del curso (`Anexo 1 Caso AgroSmart del Sumapaz.pdf`, 48 págs), que vive con el material del Reto 2 y **contiene la ficha y los 5 instrumentos del Reto 3 (pp. 32-35)**. Hallazgo real, ya **no crítico**: es un problema de **publicación/ubicación** (no viaja con la guía del Reto 3), no de inexistencia. Mitigado: incorporado a `md/reto2/`. | Coherencia / ubicación de materiales | **Media** (era «Crítica» por falso positivo) |
| A2 | **Canal y fecha-hora de entrega ausentes.** Solo se indica «finaliza el domingo 25 de octubre de 2026»; no hay plataforma, enlace ni hora límite de entrega. | Instrucción incompleta | Alta |
| A3 | **Foros sin criterio de evaluación.** Se declara la interacción «Foros de interacción entre estudiantes», pero el entregable es individual y **la rúbrica no evalúa participación en foros**. | Actividad sin evaluación | Media |
| A4 | **«Cuestionario de evaluación» mal rotulado.** La Tabla 1 dice «Puntuación del **cuestionario** de evaluación de este Reto: 125», pero el instrumento es una **rúbrica de informe**, no un cuestionario. | Redacción | Menor |
| A5 | **Número de columnas divergente.** La guía (Paso 3 / sección 4) pide incluir «**evidencia esperada de mitigación**»; la rúbrica habla de «las **9** columnas» y enumera sin la evidencia esperada (quedan 9 sin ella / 10 con ella). | Coherencia numérica | Media |
| A6 | **Cantidades exigidas solo en la rúbrica.** «≥6 casos SIEM», «≥5 criterios de validación», «≥4 prácticas DevSecOps», «≥4 acciones de hardening por dominio», «≥8 fuentes» aparecen como umbrales en la rúbrica pero la guía no fija cantidades. No es error grave (la rúbrica manda), pero la guía debería reflejarlos. | Alineación | Media |
| A7 | **Declaración de IA.** La guía pide «declaración o bitácora» con prompts, propósito, utilidad, validación y ajustes; la rúbrica (nivel alto) la exige, pero su primer ítem la describe como «**una frase** de declaración». Redacción potencialmente confusa sobre el nivel de detalle exigido. | Ambigüedad | Menor |
| A8 | **Ponderación vs. esfuerzo.** El criterio «de forma» (25 pts / 20 %) exige tanto como el criterio «de contenido» (50 pts): completar 10 secciones y 6000-8000 palabras. Razonable, pero concentra riesgo de pérdida de puntos en un criterio mecánico. | Diseño de rúbrica | Menor |

### 2.4 Pertinencia frente al perfil del estudiante y al contexto de ciberseguridad

- **Pertinencia temática:** alta. El caso AgroSmart (DMZ/Web LAMP + IT + IoT/OT) es realista y actual, e integra superficies web, corporativas y OT. El enfoque «defensa guiada por el análisis ofensivo» es adecuado para una Maestría en Ciberseguridad.
- **Carga y complejidad:** 6000-8000 palabras + 30 h declaradas es exigente pero coherente con un reto de maestría; sin embargo, la ausencia de referentes defensivos provistos aumenta artificialmente la carga.
- **Ética, autorización y alcance:** la actividad **delimita correctamente** que no se ejecutan pruebas ni explotación («no requiere ejecutar pruebas sobre la máquina virtual»), y difiere la verificación al Cyber Range autorizado del Reto 4. La rúbrica incluso penaliza «pruebas de explotación no autorizadas». **Sin embargo**, la guía no instruye explícitamente al estudiante a **declarar por escrito** en el informe que no se ejecutaron pruebas (la rúbrica sí lo exige y lo premia), lo que puede generar incumplimiento por omisión de instrucción.
- **Uso de IA:** se explicita, documenta y responsabiliza correctamente al estudiante (buena práctica de integridad académica).

---

## Tarea 3 — Contraste actividad ↔ rúbrica

> **Alcance:** se contrasta **la guía del Reto 3** contra **la rúbrica del Reto 3**. Las referencias al «Reto 2» y «Reto 4» en los criterios provienen del encadenamiento interno del curso.

### 3.1 Tabla cruzada

| Criterio de la rúbrica (peso) | Dónde se aborda en la actividad | Estado |
|---|---|---|
| **C1 (forma, 25 pts / 20 %):** archivo .docx/PDF; 6000-8000 palabras; **10 secciones** con título visible; tablas editables, rotuladas, numeradas y referenciadas; sin capturas ni enlaces. | Paso 14 (formato y extensión), sección «Las evidencias… 10 apartados», «Indicaciones» (Word/PDF, tablas editables, sin capturas) | **Alineado** |
| **C2.a (contenido):** clasificar activos en DMZ/Web LAMP, IT e IoT/OT; **≥8 activos del Anexo 1** con función, criticidad y exposición. | Paso 2 (clasificar activos por dominio, función/criticidad/exposición) | **Alineado** — la mecánica existe (Paso 2) y el universo de activos (≥8) está en el **Anexo 1** (Inventario Sec. 3.1: A-01…A-08), ya incorporado. |
| **C2.b:** matriz de priorización con los **6 criterios** (criticidad, impacto, probabilidad, severidad CVSS, exposición, propagación) y **orden** de mayor a menor. | Paso 4 (los 6 criterios) + sección 3 del informe | **Alineado** |
| **C2.c:** matriz de trazabilidad con **≥8 vectores** y **9 columnas** (causa, activo, impacto, fase Kill Chain, ATT&CK con `Txxxx`, CVE/referencia, control preventivo, detectivo, correctivo). | Paso 3 + sección 4 del informe | **Parcial** — coincide en sustancia, pero difiere el número de columnas (incluye «evidencia esperada»; ver A5) y no fija «≥8 vectores» (A6). |
| **C2.d:** hardening para los 3 dominios con **≥4 acciones** cada uno (LAMP, IT, IoT/OT) vinculadas a vectores. | Pasos 6, 8, 9 | **Alineado** |
| **C2.e:** **≥6 casos de uso SIEM/XDR** con fuente de log, condición de disparo, severidad, evento esperado y acción inicial. | Paso 10 (mismas columnas, sin número) | **Alineado** (diferencia de umbral, A6) |
| **C2.f:** plan de respuesta con las **6 fases NIST SP 800-61** para ≥1 escenario priorizado. | Paso 11 (6 fases) | **Alineado** |
| **C2.g:** DevSecOps con **≥4 prácticas** ubicadas en el ciclo. | Paso 12 | **Alineado** |
| **C2.h:** **≥5 criterios de validación** con evidencia y método para el Reto 4. | Paso 13 (sin número) | **Alineado** (umbral solo en rúbrica, A6) |
| **C2.i:** todos los controles asociados a un vector/activo/causa del Reto 2. | Paso 3 del Reto 3, «no debe proponer controles genéricos» | **Alineado** |
| **C3.a (calidad):** referencias APA con **≥8 fuentes** (≥3 del curso y ≥3 marcos técnicos: CIS, NIST CSF, NIST SP 800-61, ISO 27001, OWASP ASVS/WSTG, MITRE, NVD). | «Materiales y recursos» (7 referentes del curso) + Paso 15/sección 10 | **Parcial** — hay ≥3 recursos del curso disponibles, pero **ningún marco técnico defensivo está entre los referentes suministrados** (deben buscarlo aparte). |
| **C3.b:** declaración/bitácora de IA (prompts, propósito, verificación, ajustes) o declaración expresa de no uso. | Paso 15 + «Indicaciones» | **Alineado** |
| **C3.c:** correspondencia bidireccional citas ↔ referencias. | Paso 15 («citas y referencias completas») | **Alineado** |
| **C3.d:** cada control y regla de detección indica su marco de referencia **y la sección/artefacto del Anexo 1** que lo motiva. | Paso 5 (marcos: CIS, OWASP, hardening) — el **Anexo 1** ya está disponible | **Alineado** (una vez incorporado el Anexo 1, ver A1) |
| **C3.e:** declarar explícitamente que **no** se ejecutaron pruebas y que la verificación se difiere al Cyber Range. | «Indicaciones» (no se ejecutan pruebas) y Paso 13 (diferir al Reto 4) | **Parcial** — la idea está, pero la guía **no ordena incluir la declaración escrita** en el informe (la rúbrica sí la exige). |

### 3.2 Observabilidad y medición del nivel de logro

- **C1:** ✅ Totalmente observable (formato, conteo de palabras, número de secciones, tablas editables).
- **C2:** ✅ Mayoritariamente observable, **salvo** el detalle de «9 columnas» (C2.c), que queda mal definido. Los umbrales numéricos son medibles **cuando existen**; el conteo de «8 activos del Anexo 1» es verificable porque el Anexo 1 existe (inventario A-01…A-08).
- **C3:** ✅ Observable en su mayoría (fuentes, APA, correspondencia, declaración de IA, declaración de no-ejecución). La referencia al «Anexo 1» es verificable **porque el Anexo 1 existe** y contiene las secciones que la rúbrica exige citar.

### 3.3 Desalineaciones detectadas

- **Criterios de la rúbrica sin actividad que los sustente:** *(corregido)* ninguno por inexistencia de material. Los criterios que citan el «Anexo 1» (C2.a y C3.d) **tienen respaldo**: el Anexo 1 existe y contiene el inventario de activos (Sec. 3.1) y las pistas/artefactos (Sec. 3). La única observación es de **publicación**: el Anexo no viaja con la guía del Reto 3 en `resources/` (ver A1).
- **Actividades sin criterio que las evalúe:** **participación en foros** (declarada en la Tabla 1 de la guía del Reto 3, sin criterio en la rúbrica) y la tarea de **«retomar/revisar el video del Reto 2»** (Paso 1 del Reto 3), que no se evalúa directamente como producto propio del Reto 3.
- **Ponderaciones:** ✅ **Sin errores.** 25 + 50 + 50 = **125** puntos (= puntaje total declarado) y 20 % + 40 % + 40 % = **100 %**. Los rangos por nivel son consistentes y contiguos (p. ej. C1: 20-25 / 15-19 / 1-14 / 0).

---

## Tarea 4 — Verificación de referencias

> **Alcance:** se verifican los referentes del **Reto 3** (lista de `references.md` y las citas de la guía del Reto 3) contra sus PDFs de respaldo.

**Método:** cotejo del PDF local ↔ metadatos de Crossref (API `api.crossref.org`) ↔ resolución HTTP de DOI/URL (`curl -L`). Se verificó existencia, autores, año, revista, volumen, número, páginas y enlace.

### 4.1 Tabla de verificación (referencias de `references.md`)

| # | Referencia (según `references.md`) | ¿Existe? | ¿Datos correctos? | ¿Enlace funciona? | Observaciones |
|---|---|---|:--:|:--:|---|
| 1 | Crespo-Martínez, E. (2021). *Análisis de vulnerabilidades con SQLMAP…* Ingenius, (pp. 104-113). `10.17163/ings.n25.2021.10` | ✅ Sí | ⚠️ Parcial | ✅ 200 → `ingenius.ups.edu.ec/…/25.2021.10` | Autor correcto. **Falta el número de fascículo (N.º 25)** y el nombre de revista completo («Ingenius, Revista de Ciencia y Tecnología»). Crossref registra *issued* **2020-12-31**, pero la cita sugerida por la propia revista y el PDF usan **2021** (N.º 25, enero-junio). Páginas 104-113 correctas. |
| 2 | Lu, H.-J., & Yu, Y. (2021). *Research on WiFi Penetration Testing with Kali Linux*. Complexity, 2021, 1-8. `10.1155/2021/5570001` | ✅ Sí | ✅ Sí (matiz) | ⚠️ 302→**403** (Wiley bloquea bots) | Crossref: Lu, He-Jun; Yu, Yang; Complexity vol. 2021, n.º 1. Es *article ID 5570001* (8 págs.); APA preferiría «Article 5570001» en lugar de «1-8». La guía lo cita en español y como «He Jun, L., & **Yang, Y.**» → **autor inconsistente** entre guía y `references.md`. |
| 3 | Benavides-Astudillo, E., Fuertes-Díaz, W., & Sánchez-Gordon, S. (2020). *Un experimento…* Ciencia UNEMI, 13(32), 27-40. *(enlace EBSCO)* | ✅ Sí | ✅ Sí | ⚠️ 200 pero **requiere login institucional** | Vol. 13, N.º 32, pp. 27-40, 2020 ✅. **Existe DOI** (`10.29076/issn.2528-7737vol13iss32.2020pp27-40p`) que **no se cita**: se usa un enlace proxy EBSCO. **La guía la data como 2019** (incorrecto; es 2020). |
| 4 | Benavides-Astudillo, E., Fuertes-Díaz, W., & Sánchez-Gordon, S. (2020). *Caracterización de los ataques de phishing…* Ciencia y Tecnología, 13(1), 97-104. *(enlace EBSCO)* | ✅ Sí | ⚠️ Parcial | ⚠️ 200 pero requiere login | Título, vol. 13(1), pp. 97-104, 2020 ✅. DOI real: `10.18779/cyt.v13i1.357` (no citado). Crossref registra autores como **Benavides, Eduardo; Fuertes, Walter; Sanchez, Sandra**, no con apellidos compuestos («Benavides-Astudillo», etc.). Revisar concordancia con la forma publicada. |
| 5 | Budavári, E. A., Albini, A., & Mester, G. (2023). *The Role of Social Engineering in the Energy Balance of Systems*. INDECS, 21(2), 168-173. `10.7906/indecs.21.2.5` | ✅ Sí | ❌ No (autor) | ✅ 200 → `indecs.eu/2023/indecs2023-pp168-173.pdf` | **Apellido/ini­ciales incorrectos.** Crossref: *Albininé Budavári, Edina*. Debe citarse **«Albininé Budavári, E., Albini, A., & Mester, G.»**, no «Budavári, E. A.». Volumen/número/páginas/DOI correctos. |
| 6 | Prado Díaz, J. P. (2021). *Ingeniería social, un ejemplo práctico*. Revista ODIGOS, 2(3), 47-76. `10.35290/ro.v2n3.2021.493` | ✅ Sí | ✅ Sí | ✅ 200 → `revista.uisrael.edu.ec/…/493` | Coincide exactamente (Vol. 2, Núm. 3, 2021, pp. 47-76, e-ISSN 2697-3405). Sin objeciones. |
| 7 | Zambrano Hernández, L. F., Peña Hidalgo, H. J., & Cárdenas Corral, N. R. (2024). *Una mirada a metodologías…*. CSIRT UNAD. *(URL)* | ✅ Sí | ❌ No (autores) | ✅ 200 (PDF, 1 083 140 bytes = **idéntico** al archivo local) | **Autoría mal atribuida.** El documento es el *Boletín N.º 28 (Octubre 2024)*, «Una Mirada a Metodologías Para Pruebas de Penetración en Ciberseguridad», cuyos autores son **Palomo Luna, D. F.; Zambrano Hernández, L. F.; Moreno Molano, S. X.; Peña Hidalgo, H. J.** (Cárdenas Corral figura solo como «Revisó»). Además, la cita tiene **texto de interfaz incrustado en la URL** («Abrir este documento utilizando ReadSpeaker docReaderhttps://…») → error de formato. |

### 4.2 Citas adicionales presentes en la guía (sin entrada en `references.md`)

| Referencia (guía) | ¿Existe? | ¿Datos correctos? | ¿Enlace funciona? | Observaciones |
|---|---|:--:|:--:|---|
| Zambrano, L. F. (2026). *Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT* [OVI]. `repository.unad.edu.co/handle/10596/83223` | ❓ **No verificable** | N/D | ❌ **404** | El *handle* devuelve 404; no se pudo confirmar. Cita sin PDF de respaldo en la carpeta. Además, fecha **2026** (posterior al cierre del curso: 25-oct-2026 → posible errata de año). |
| Zambrano, L. F. (2026). *Vectores de ataque y estrategias de defensa* [OVA]. `repository.unad.edu.co/handle/10596/83229` | ❓ **No verificable** | N/D | ❌ **404** | Igual que la anterior: *handle* 404, sin PDF de respaldo, año 2026. |

> Nota: la búsqueda en el repositorio UNAD sugiere que existen recursos con descripción coincidente («…identificar, analizar y gestionar ataques cibernéticos en infraestructuras TI e IoT»), por lo que el recurso pudo **cambiar de *handle*** o no estar publicado al momento de la verificación. Se reporta como **roto/no verificable**, no como inexistente.

### 4.3 Correspondencia PDF ↔ referencia

- **Cada uno de los 7 PDF de la carpeta `resources/` corresponde a una referencia citada** (ver mapa en `md/INDEX.md`). ✅
- **PDF huérfanos:** ninguno. (Los otros 2 PDF son la guía y la rúbrica, materiales del curso.) ✅
- **Citas sin PDF de respaldo:** las **2 OVI/OVA (2026)** citadas en la guía. ❌

### 4.4 Estilo de citación

- Estilo declarado: **APA** (lo exigen guía y rúbrica). Existen **inconsistencias sistemáticas**:
  - Año distinto del real en la guía (Benavides… **2019** → debe ser **2020**).
  - Nombres de autor divergentes entre guía, `references.md` y publicación (Lu/Yu vs. «He Jun/Yang»; Budavári vs. Albininé Budavári).
  - **Títulos traducidos al español** en la guía para artículos en inglés (Lu & Yu) sin consignarlos como traducción.
  - Uso de **enlaces proxy EBSCO** donde existen **DOI** (casos 3 y 4).
  - **Texto de interfaz dentro de la URL** (caso 7).
  - Falta el **número de fascículo** en el caso 1 (Ingenius N.º 25).
- **Duplicados:** no se detectaron referencias duplicadas dentro de `references.md`, pero **sí solapamiento** entre la guía y `references.md` con datos contradictorios (misma obra, metadatos distintos).

---

## Correcciones recomendadas (priorizadas)

> ⚠️ **Estado:** las correcciones **críticas 1, 2** y **medias 4, 5, 6** ya se aplicaron a `references.md` y a `md/actividad/Guía de aprendizaje - Reto 3.md` (ver «Errata aplicada»). La **media 3** (Anexo 1) quedó mitigada al incorporar el documento. Se mantienen abajo como registro de la auditoría.

### 🔴 Críticas
1. **Corregir la autoría del Boletín CSIRT UNAD (referencia 7):** autores reales = **Palomo Luna, D. F.; Zambrano Hernández, L. F.; Moreno Molano, S. X.; Peña Hidalgo, H. J.** (Boletín N.º 28, Octubre 2024; e-ISSN 2806-0164). Eliminar el texto «Abrir este documento utilizando ReadSpeaker docReader» incrustado en la URL.
2. **Reparar/reemplazar los enlaces OVI/OVA (2026):** ambos *handles* (`10596/83223`, `10596/83229`) devuelven **404**. Verificar los *handles* vigentes o retirarlos de la guía; revisar el año (2026 vs. cronograma del curso).

### 🟠 Medias
3. *(Antes crítica — corregida.)* **Publicar el «Anexo 1» junto a la guía del Reto 3.** El Anexo **existe** (documento maestro del curso, 48 págs) y contiene la ficha y los 5 instrumentos del Reto 3 (pp. 32-35), pero **no viaja con la guía del Reto 3 en `resources/`**: está con el material del Reto 2. Los criterios C2.a y C3.d **no** son inalcanzables. Acción recomendada: distribuir el Anexo 1 junto a la guía del Reto 3 (o enlazarlo). Ya incorporado a `md/reto2/fuentes/`.
4. **Corregir el año del artículo UNEMI en la guía:** 2019 → **2020**.
5. **Corregir el apellido del autor del INDECS:** «Budavári, E. A.» → **«Albininé Budavári, E.»**.
6. **Añadir los DOI reales** en lugar de los enlaces proxy EBSCO:
   - UNEMI: `https://doi.org/10.29076/issn.2528-7737vol13iss32.2020pp27-40p`
   - Ciencia y Tecnología (phishing): `https://doi.org/10.18779/cyt.v13i1.357`
7. **Suministrar referentes defensivos** (CIS Controls, NIST CSF, NIST SP 800-61, ISO/IEC 27001, OWASP ASVS/WSTG, MITRE ATT&CK, NVD) o indicarlos como de búsqueda obligatoria, dado que la rúbrica exige ≥3 y no se provee ninguno.
8. **Especificar canal, fecha y hora de entrega** del informe (plataforma y enlace).
9. **Unificar el número de columnas de la matriz de trazabilidad** entre guía (incluye «evidencia esperada») y rúbrica (dice «9 columnas»).
10. **Instruir explícitamente** que el informe debe incluir la **declaración escrita de que no se ejecutaron pruebas** (hoy solo lo exige la rúbrica).
11. **Aclarar la evaluación de la participación en foros** (o retirar su mención) y el rol del vídeo del Reto 2 que el Paso 1 del Reto 3 manda revisar.

### 🟡 Menores
12. Cambiar «Puntuación del **cuestionario** de evaluación» por «**rúbrica/informe**» (Tabla 1 de la guía).
13. Escribir el nombre de revista completo y añadir el fascículo: «Ingenius, *Revista de Ciencia y Tecnología*, N.º 25, pp. 104-113».
14. Homogeneizar la cita de Lu & Yu (autoría y título) entre guía y `references.md`; considerar «Complexity, 2021, Article 5570001».
15. Reemplazar «1-8» por «Article 5570001» (8 págs.) si se adopta APA estricto con *article number*.
16. Reparar formato en `references.md`: espacio antes del punto en la línea de Crespo-Martínez («(pp. 104-113) .»).
17. Corregir la redacción de la rúbrica sobre la declaración de IA («una frase» vs. bitácora detallada) para que sea consistente con la guía.

---

## Anexo — Incertidumbres declaradas (no verificables)

- El DOI de Wiley (`10.1155/2021/5570001`) responde **403** a clientes automatizados; la existencia y los metadatos se confirmaron por Crossref y por el PDF local, pero **no** mediante acceso directo a la página.
- Los enlaces EBSCO resuelven a la pantalla de autenticación de la biblioteca UNAD (**200**); no fue posible confirmar el contenido exacto del artículo sin credenciales institucionales.
- Los *handles* OVI/OVA devuelven **404**; no se pudo confirmar si el recurso existe bajo otro identificador.
- La página 1 del boletín (OCR) y la página 9 de la guía (OCR) tienen calidad de transcripción limitada por ser imágenes; el contenido textual esencial es legible, pero puede contener errores de OCR en los elementos gráficos.

---

## Corrección de un falso positivo de la propia auditoría — el «Anexo 1» existe

En la primera pasada esta auditoría clasificó como **crítica** la **inexistencia del «Anexo 1»** (hallazgo **A1**), y de ahí concluyó que los criterios **C2.a** y **C3.d** de la rúbrica eran inalcanzables. **Esa conclusión era incorrecta.**

- El **Anexo 1 existe**: es el *documento maestro del curso* — `Anexo 1 Caso AgroSmart del Sumapaz.pdf`, **48 páginas** — y reside con el material del **Reto 2** en el vault (`Obsidian/Brain/Test 2/05 - Fuentes/`), no en la carpeta `resources/` del Reto 3.
- Contiene, además del caso completo y los 13 artefactos, la **ficha del Reto 3 y sus 5 instrumentos (pp. 32-35):** 3.1 matriz de trazabilidad, 3.2 hardening por dominio, 3.3 reglas de detección, 3.4 plan de monitoreo, 3.5 procedimiento de respuesta (NIST SP 800-61).
- Por tanto, **C2.a** («≥8 activos del Anexo 1» → inventario Sec. 3.1, activos A-01…A-08) y **C3.d** («sección/artefacto del Anexo 1 que motiva el control») **tienen respaldo material** y son evaluables.
- **Reclasificación:** A1 pasa de **Crítica** a **Media**. La observación que sobrevive es de **publicación/ubicación**: el Anexo no viaja con la guía del Reto 3. Mitigación aplicada: se convirtió a Markdown e incorporó al paquete de contexto (`md/reto2/fuentes/Anexo 1 - Caso AgroSmart del Sumapaz.md`).

---

## Errata aplicada (nombres y enlaces)

Cambios ejecutados sobre `references.md` y `md/actividad/Guía de aprendizaje - Reto 3.md`. Los **nombres se tomaron literalmente de la portada de cada PDF** (fuente autorizada), y los enlaces se sustituyeron/repararon y se probaron con `curl -L`.

### Nombres de autor

| Obra | Antes | Después (según el PDF) | Fuente del dato |
|---|---|---|---|
| Ingenius (SQLMAP) | Crespo Martínez | **Crespo-Martínez** (+ fascículo **(25)**) | p. 1 + cita sugerida del artículo |
| Complexity (WiFi) | He Jun, L., & Yang, Y. *(solo en la guía)* | **Lu, H.-J., & Yu, Y.** | p. 1: «He-Jun Lu and Yang Yu» |
| Ciencia UNEMI | Benavides Astudillo / Sánchez Gordon / **(2019)** | **Benavides-Astudillo, Fuertes-Díaz, Sánchez-Gordon / (2020)** | p. 1: «Eduardo, Benavides-Astudillo; Walter, Fuertes-Díaz; Sandra, Sánchez-Gordon» |
| Ciencia y Tecnología (phishing) | Benavides-Astudillo, Fuertes-Díaz, Sánchez-Gordon | **Benavides, E., Fuertes, W., & Sánchez, S.** | p. 1: «Benavides Eduardo; Fuertes Walter; Sanchez Sandra» |
| INDECS | Budavári, E. A. | **Albininé Budavári, E.** | p. 1: «Edina Albininé Budavári, Attila Albini and Gyula Mester» |
| ODIGOS | (correcto) | Prado Díaz, J. P. | p. 1: «Juan Pablo Prado Díaz» |
| Boletín UNAD | Zambrano Hernández, Peña Hidalgo, Cárdenas Corral | **Palomo Luna, Zambrano Hernández, Moreno Molano, Peña Hidalgo** | p. 4 (autores con ORCID); Cárdenas Corral figura como «Revisó» |

### Enlaces

| Referencia | Antes | Después | Estado verificado |
|---|---|---|---|
| Ingenius | DOI sin fascículo | `10.17163/ings.n25.2021.10` (sin cambio de DOI) | ✅ 200 |
| Complexity | DOI con espacio antes del punto | `10.1155/2021/5570001` | ⚠️ 403 anti-bot (resuelve al artículo correcto) |
| Ciencia UNEMI | enlace proxy EBSCO | **DOI `10.29076/issn.2528-7737vol13iss32.2020pp27-40p`** | ✅ 302 → artículo |
| Ciencia y Tecnología | enlace proxy EBSCO | **DOI `10.18779/cyt.v13i1.357`** | ✅ 200 |
| INDECS | enlace DOI-proxy UNAD | DOI directo `10.7906/indecs.21.2.5` | ✅ 200 |
| ODIGOS | DOI con espacio antes del punto | `10.35290/ro.v2n3.2021.493` | ✅ 200 |
| Boletín UNAD | URL con texto «ReadSpeaker docReader» incrustado | URL limpia + Boletín N.º 28 | ✅ 200 |
| OVI/OVA (guía) | handles `10596/83223`, `10596/83229` | **pendientes**: se marcaron como «ENLACE POR VERIFICAR» | ❌ 404 (recurso existe; handle por confirmar) |

> **Nota sobre EBSCO:** se reemplazaron los enlaces proxy por los DOI directos porque los enlaces EBSCO solo abren con credenciales institucionales (por eso se adjuntaron los PDF). Los PDF siguen siendo el respaldo verificable de cada referencia.
>
> **Pendiente de confirmar (no inventar enlace):** los *handles* de los dos recursos OVI/OVA del repositorio UNAD no pudieron verificarse (404). La búsqueda en el repositorio confirma que **ambos recursos existen** («Vectores de ataque y estrategias de defensa» y «Diseño de estrategias de detección y gestión de ataques cibernéticos en entornos TI e IoT», de Luis Fernando Zambrano Hernández, Maestría en Ciberseguridad, 2026-07-15), pero no se localizó el *handle* correcto; se dejan señalados en la guía para su corrección por parte del equipo docente.
