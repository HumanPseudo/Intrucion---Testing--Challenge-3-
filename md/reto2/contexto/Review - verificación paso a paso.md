---
tags: [review, verificacion, checklist, reto-2]
fecha: 2026-09-27
---

# Review — verificación paso a paso del Reto 2

> [!info] Cómo usar esta nota
> Cada bloque tiene cuatro partes:
> 1. **Qué pide** — texto literal de la [[00 - Contexto/Rúbrica de evaluación|Rúbrica]] (nivel 1
>    de la jerarquía de fuentes, junto con el [[05 - Fuentes/Guía de aprendizaje - Reto 2 - Análisis de vectores de ataque.pdf|Guía]] y el [[05 - Fuentes/Anexo 1 Caso AgroSmart del Sumapaz.pdf|Anexo 1]]).
> 2. **Dónde está** — diapositiva del `.pptx` y nota del vault que lo sostiene.
> 3. **Cómo verificarlo tú** — qué abrir y qué mirar.
> 4. **Estado** — mi lectura al 27-09-2026: ✅ cumple · ⚠️ decidir o reforzar · ❌ falta.
>
> Las casillas `- [ ]` están **sin marcar a propósito**: márcalas tú cuando lo hayas comprobado con tus propios ojos.

Presentación: [Reto2 - AgroSmart (ciberpunk).pptx](03%20-%20Video/Reto2%20-%20AgroSmart%20-%20An%C3%A1lisis%20de%20vectores%20de%20ataque%20%28ciberpunk%29.pptx) · 22 diapositivas · 14 tablas nativas · 0 imágenes · notas 538 s (8:58) · MP4 exportado 563 s (9:23), determinista vía `advTm`

---

## 0. Resumen de estado

| Bloque | Estado | Pendiente |
|---|---|---|
| Qué se entrega (MP4) | ❌ | Grabar narración y exportar a MP4 |
| Condiciones técnicas | ✅ en el `.pptx` · ❌ en el MP4 | Verificar duración y peso tras exportar |
| 8 secciones estructurales (Rúbrica, criterio 1) | ✅ | Las 8 están rotuladas explícitamente como "SECCIÓN N DE 8 · &lt;nombre&gt;" en el kicker de cada diapositiva — ver [[#3. Las 8 secciones estructurales (Rúbrica de evaluación)]] |
| Pasos 1-3 (dominios, activos, artefactos) | ✅ | Headers y HTTP Basic añadidos en la diapositiva 9 ([[#D3]]) |
| Paso 4 (CVE, CVSS, explotación) | ✅ | 5 CVE verificados en NVD (no 4): CVE-2022-45956 tiene fila propia ([[#D11]]) |
| Paso 5 (Cyber Kill Chain) | ✅ | — |
| Paso 6 (≥ 10 técnicas MITRE) | ✅ | Mapeo ajustado al Anexo 3.13 y justificado ([[#D1]]) |
| Paso 7 (ruta: pista, hipótesis, validación) | ✅ | La tabla y el diagrama intercambiaron de diapositiva ([[#D12]]) |
| Paso 8 (video con tablas y diagramas) | ✅ | — |
| Paso 9 (declaración de IA) | ✅ | % apoyado en IA completado en `IA_PCT` ([[#D4]]) |
| Referencias APA | ✅ | 16 referencias en orden alfabético (se sumó Lockheed Martin), con OVI y OVA ([[#D5]], [[#D11]]) |
| Cobertura de artefactos (Sec. 3, detalle fino) | ✅ | Los 14 hallazgos de la tabla de cobertura están cerrados — ver [[#5bis. Cobertura artefacto por artefacto (Anexo Sec. 3)]] |

Los puntos ya resueltos están en la [[#6. Decisiones antes de entregar]]. **No queda ningún punto obligatorio abierto.** Solo D6 (reflexión académica explícita, opcional) sigue sin decidir. D7-D9 y los 7 hallazgos menores restantes ya se cerraron; D11-D12 (rúbrica de 8 secciones y correcciones del 27-09) también.

---

## 0bis. Checklist maestro — verifícalo tú, paso a paso

> Pensado para que lo sigas de arriba hacia abajo con el `.pptx` abierto en PowerPoint (no en
> LibreOffice) mientras yo sigo trabajando. Cada fila dice **qué abrir** y **qué debe decir**.
> Marca la casilla solo cuando lo hayas comprobado con tus propios ojos, no de memoria.

### Paso 0 · Antes de abrir nada
- [ ] El archivo que abres es `03 - Video/Reto2 - AgroSmart - Análisis de vectores de ataque (ciberpunk).pptx` (el que termina en "ciberpunk"; el otro es una versión vieja)
- [ ] Nadie más lo tiene abierto (revisa que no exista `.~lock.Reto2...#` en la misma carpeta)

### Paso 1 · Portada y apertura (diapositivas 1-3)
- [ ] Diapositiva 1: dice **10 vectores de ataque** (no 9)
- [ ] Diapositiva 1, pie: dice **11 tablas nativas** (cuenta las tablas si quieres confirmarlo tú mismo)
- [ ] Diapositiva 2: los dos números dicen **5** (CVE con puntaje verificado) y **5** (debilidades CWE) — deben sumar 10, que son las filas de la diapositiva 11
- [ ] Diapositiva 3: la Ley 1273/2009 se cita como **art. 269A**

### Paso 2 · Caso y arquitectura (diapositivas 4-9)
- [ ] Diapositiva 4, tabla de actores: la fila de la estación meteorológica menciona el riesgo de **datos falsos**, no solo "watering hole"
- [ ] Diapositiva 5: hay tres fronteras rotuladas **F1, F2, F3**, y F3 se ve como línea punteada amarilla
- [ ] Diapositiva 9: la tabla tiene **9 filas** y la última observación dice que hay **11 puntos de entrada en total, 9 sin autenticación**
- [ ] Diapositiva 9: aparecen **SSH 22** y **MariaDB 3306** como filas propias, marcadas "Host (sin confirmar a Internet)"

### Paso 3 · Vectores y vulnerabilidades (diapositivas 10-11)
- [ ] Diapositiva 10: la tabla tiene **10 filas** (no 9); la fila 10 habla de librerías desactualizadas y TLS débil
- [ ] Diapositiva 10, fila 4 (JWT): dice que el token capturado muestra **`rol=contador`**, y que la falta de firma **permite forjar** cualquier rol — no dice que ya se llegó a superadmin
- [ ] Diapositiva 11: cuenta las filas con **CVE** (deben ser **5**, no 4: la cámara Boa tiene fila propia para `CVE-2017-9833` y otra para `CVE-2022-45956`) y las filas con **CWE** marcadas con asterisco (deben ser 5) — **10 filas en total**
- [ ] Diapositiva 11: la fila de la cámara `CVE-2017-9833` dice **DISPUTED**, y la fila `CVE-2022-45956` dice que no está en KEV
- [ ] Diapositiva 11, columna de evidencia: cada vector CVSS empieza con el prefijo `CVSS:3.1/` (formato oficial de NVD) y aparecen las siglas **KEV** o **EDB-** en al menos 3 filas

### Paso 4 · Ingeniería social, CKC, MITRE, ruta (diapositivas 12-16)
- [ ] Diapositiva 13 (Cyber Kill Chain): las 7 fases están en orden — Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives
- [ ] Diapositiva 14: cuenta las filas — deben ser **13**. Busca `T1606.001`, `T1210` y `T0855`: los tres deben estar resaltados
- [ ] Diapositiva 14, fila `T1606.001`: dice que el token muestra `rol=contador`, no `rol=superadmin`
- [ ] Diapositiva 14: **no** debe aparecer ninguna fila `T1068` ni `T1134`
- [ ] Diapositiva 15: la tabla separa columnas de **pista**, **hipótesis** y **evidencia para validar** — ninguna hipótesis está en la columna de pista (la tabla y el diagrama de 8 saltos intercambiaron de número el 27-09: el diagrama ahora es la diapositiva 16, la tabla es la 15 — ver [[#D12]])

### Paso 5 · Riesgo y conclusiones (diapositivas 17-19)
- [ ] Diapositiva 17: los 6 escenarios y sus riesgos son 20, 20, 16, 16, 12, 9 — multiplica P×I de cada fila tú mismo
- [ ] Diapositiva 17: la leyenda de abajo dice **bajo·1-7, medio·8-14, alto·15-19, crítico·20-25** (deben coincidir con las categorías del instrumento 2.9, no con otra escala)
- [ ] Diapositiva 17: se lee completo el rótulo **"ESCALA DE RIESGO"** (no debe quedar tapado por el primer color)
- [ ] Diapositiva 18, hallazgo 3: dice **"forjar cualquier rol, incluido superadmin"**, no "escalada al rol superadmin"
- [ ] Diapositiva 19: hay exactamente **4** preguntas para discusión numeradas 01-04

### Paso 6 · Referencias y declaración (diapositivas 20-22)
- [ ] Entre las diapositivas 20 y 21 hay **16** referencias numeradas en orden alfabético (se sumó Lockheed Martin, 2011, como fuente pública del modelo Cyber Kill Chain — Lockheed va antes que Lu en el orden alfabético)
- [ ] Aparecen el **OVI** (Zambrano, 2025), el **OVA** (Zambrano, 2026) del curso y el Boletín 28 de **Palomo Luna et al. (2024)** — no "Zambrano, Peña Hidalgo y Cárdenas Corral": Cárdenas Corral es el revisor del boletín, no autor
- [ ] La referencia de NIST SP 800-115 dice **(2008)**, no (2018)
- [ ] Diapositiva 22: el campo **"% apoyado en IA"** ya no dice "POR COMPLETAR" — muestra el porcentaje declarado (ver [[#D4]])

### Paso 7 · Contraste con tu propio criterio
Esto ya no lo puedo verificar yo por ti — es tu lectura crítica, que es lo que pide el
Resultado de Aprendizaje 1 ("interpretar críticamente", no solo transcribir):
- [ ] Lee la diapositiva 18 completa en voz alta. ¿Suena a algo que tú argumentarías, o a un resumen genérico?
- [ ] Elige 3 filas cualquiera de las diapositivas 10, 11 o 14 y verifica tú mismo, sin este documento, que la "pista" citada existe en el Anexo en la sección que dice
- [ ] Pregúntate: si un profesor te pidiera explicar en voz alta *por qué* el riesgo de OT (20) y el de negocio (20) no son intercambiables (diapositiva 17), ¿podrías hacerlo sin leer la diapositiva?

Cuando termines los 7 pasos, la presentación está verificada de punta a punta por ti, no
solo por mí. D4 (el % de IA) ya está completado; lo único que quedaría, si quieres, es D6
(la reflexión, opcional).

---

## 1. Qué se entrega

> **Guía, pág. 5:** "Las evidencias a desarrollar individualmente son: **Video expositivo** de presentación del reto…"
> **Anexo, Nota aclaratoria (pág. 23):** "Las matrices e instrumentos diligenciados son **insumos de análisis** para preparar el video expositivo… integrándolos como soporte dentro de la presentación, **sin sustituir el producto**."

- La evidencia calificable es **el MP4**. El `.pptx` es la fuente del video; los instrumentos 1.1-2.9 son insumos y su contenido debe **verse en el video**.
- Puntuación: 125 puntos (Guía, Tabla 1; Anexo, Ficha del Reto 2). Fecha límite: **domingo 27 de septiembre de 2026**.

- [ ] Entiendo que lo que se sube es el MP4, no el `.pptx` ni las notas del vault.

---

## 2. Condiciones técnicas del video (Guía, pág. 6)

| # | Qué pide (literal) | Dónde / cómo verificarlo | Estado |
|---|---|---|---|
| T1 | "Archivo en formato MP4" | Tras exportar: propiedades del archivo | ❌ aún no existe |
| T2 | "Generado a partir de una presentación en PowerPoint exportada a video" | PowerPoint → Archivo → Exportar → Crear un video | ❌ pendiente |
| T3 | "Duración máxima: 10 minutos" | Notas del orador = 538 s (8:58). Desde el 27-09, cada transición lleva `advTm` con el segundo exacto de `TIMING`, y `notes()` aborta el build si una nota no coincide con `TIMING`: la duración ya no depende de que PowerPoint calcule bien las animaciones. `build_deck.py` imprime el total exacto: narración 538 s + transiciones 11 s + animaciones 14 s = **563 s (9:23)**, con 37 s de holgura | ✅ determinista en el `.pptx` · ⚠️ confirmar que el MP4 exportado también da 563 s |
| T4 | "Peso máximo: 200 MB" | Tamaño del MP4 (1080p suele quedar por debajo) | ❌ pendiente |
| T5 | "Las tablas… deben diseñarse e incrustarse directamente en el archivo editable" | Clic en cualquier tabla del `.pptx`: debe poder editarse celda a celda. 14 tablas nativas | ✅ |
| T6 | "No se admite… capturas de pantalla o imágenes para reemplazar contenido analítico" | `audit.py` reporta 0 imágenes | ✅ |
| T7 | "No se permite enlazar direcciones URL externas ni vínculos a repositorios en la nube" | No hay hipervínculos en diapositivas ni notas. Las URL de las diapositivas 20-21 son DOI en texto plano de las referencias APA, no enlaces | ✅ |

**Cómo verificarlo tú:** desde `03 - Video/`, ejecuta `python audit.py "Reto2 - AgroSmart - Análisis de vectores de ataque (ciberpunk).pptx"`. Debe mostrar 22 diapositivas, 14 tablas, 0 imágenes, 0 errores, y además — desde el 27-09 — que las 8 secciones de la rúbrica están rotuladas, 5 CVE con vector CVSS v3.1, ≥10 identificadores ATT&CK, las 7 fases de la CKC, ≥4 pasos de ruta, ≥5 referencias y ≥7 notas del orador que citan una fuente.

- [ ] T1-T4 comprobados sobre el MP4 final
- [ ] T5-T7 comprobados abriendo el `.pptx` en PowerPoint

---

## 3. Las 8 secciones estructurales (Rúbrica de evaluación)

> Desde el 27-09-2026 la fuente que manda aquí es la [[00 - Contexto/Rúbrica de evaluación|Rúbrica]],
> no el modelo de "6 apartados" de la Guía (pág. 5-6): el **primer criterio de evaluación**
> (25 pts, 20 % del total) exige "con título visible en la diapositiva, las siguientes
> **ocho** (8) secciones estructurales". `build_deck.py` rotula cada una en el kicker como
> `SECCIÓN N DE 8 · <NOMBRE EXACTO DE LA RÚBRICA>`, y `audit.py` confirma "las 8 secciones
> de la rúbrica están rotuladas". El pie de cada diapositiva conserva además el "APARTADO N
> DE LA GUÍA" o "INSTRUMENTO 2.x" original, para no perder la trazabilidad al instrumento.

| # | Sección (nombre exacto de la rúbrica) | Diapositivas | Qué mirar | Estado |
|---|---|---|---|---|
| 1 | **Introducción** | 1, 2, 3 | Diapositiva 1: título del caso y nombre del expositor. La 2 tiene CONTEXTO, OBJETIVO DEL ANÁLISIS y JUSTIFICACIÓN; la 3 añade el encuadre ético (ROE, Ley 1273) | ✅ |
| 2 | **Descripción del caso** | 4, 5, 6 | La 4 tiene SITUACIÓN PROBLEMÁTICA y ACTORES DEL CASO (menciona explícitamente DMZ/Web, IT e IoT/OT); la 5 el diagrama de 3 dominios; la 6 el inventario A-01..A-08 clasificado por dominio | ✅ |
| 3 | **Análisis preliminar** | 7-14 | Método (7), activos C-I-D (8), superficie (9), vectores (10), CVE/CVSS (11), ingeniería social (12), Cyber Kill Chain (13), MITRE ATT&CK (14) | ✅ |
| 4 | **Alternativas de análisis y validación** | 15 | Tabla pista → hipótesis → evidencia para validar, más el panel "RUTA ALTERNATIVA Y POR QUÉ NO ES LA PRINCIPAL" (criterio de priorización: se prefiere la ruta con registro en logs sobre la más corta) | ✅ |
| 5 | **Propuesta preliminar** | 16, 17 | La 16 es el diagrama de 8 saltos (ruta probable de compromiso sustentada); la 17 los impactos organizacionales P×I (negocio, datos, OT/físico) | ✅ |
| 6 | **Conclusiones** | 18 | Tiene SÍNTESIS, hallazgos, 5 recomendaciones y "lo que debe preocupar a la gerencia". **No hay una frase explícita de aprendizaje o reflexión académica** (no lo exige la rúbrica, sí la Guía) | ⚠️ ver [[#D6]] |
| 7 | **Preguntas para discusión** | 19 | 4 preguntas enlazadas con los Retos 3, 4 y 5 (la rúbrica no exige un número mínimo) | ✅ |
| 8 | **Referencias** | 20, 21 | 16 referencias APA 7 en orden alfabético (incluye OVI, OVA, Boletín 28 y Lockheed Martin) | ✅ ver [[#D5]], [[#D11]] |

- [ ] Sección 1 · [ ] Sección 2 · [ ] Sección 3 · [ ] Sección 4 · [ ] Sección 5 · [ ] Sección 6 · [ ] Sección 7 · [ ] Sección 8

---

## 4. Los 9 pasos de la Guía (págs. 3-5)

### Paso 1 — Dominios DMZ/Web, IT e IoT/OT
> "Identifique los componentes tecnológicos… organícelos según correspondan a los dominios DMZ/Web, IT e IoT/OT… observe las posibles relaciones o conexiones existentes entre ellos."

- **Dónde:** diapositiva 5 (diagrama con las fronteras F1, F2 y F3) y la 6 (columna DOMINIO) · [[Contexto y arquitectura]] · [[2.2 Superficie de exposición]]
- **Verifícalo:** compara la tabla de la diapositiva 6 con el inventario del Anexo Sec. 3.1 (pág. 11). Los 8 activos deben coincidir en nombre, dominio y servicio.
- **Estado:** ✅
- [ ] Paso 1 verificado

### Paso 2 — Activos críticos y superficies de exposición
> "Para cada uno, determine su función, ubicación dentro del escenario y posibles mecanismos de acceso o exposición… cuáles activos presentan mayor interés desde la perspectiva de un posible atacante."

- **Dónde:** diapositiva 8 (C/I/D de 1 a 5) y la 9 (puntos de entrada) · [[2.1 Activos críticos C-I-D]] · [[2.2 Superficie de exposición]]
- **Verifícalo:** suma C+I+D de cada fila de [[2.1 Activos críticos C-I-D]]. Los totales correctos son A-01=13, A-02=14, A-03=12, A-04=10, A-05=10, A-06=8, A-07=13 y A-08=11.
- **Estado:** ✅ (la suma de A-01 ya se corrigió de 14 a 13)
- [ ] Paso 2 verificado

### Paso 3 — Analizar los artefactos técnicos
> "Revise individualmente los resultados de **Nmap, robots.txt, errores SQL, headers, información OSINT, logs, SMB, MQTT, Modbus y cámara IP**… relaciónelos con los activos."

| Artefacto | Diapositivas donde aparece | Estado |
|---|---|---|
| Nmap | 3, 10, 14 | ✅ |
| robots.txt | 8 | ✅ |
| Errores SQL | 10, 11, 16 | ✅ |
| Headers | 9 (`Server`, `X-Powered-By`, sin CSP/X-Frame-Options/HSTS; HTTP Basic sin TLS) y 14 (cookie) | ✅ |
| OSINT | 4, 12, 13, 15, 16 | ✅ |
| Logs (4625/4624/7045/Sysmon) | 13, 16 | ✅ |
| SMB | 4-6, 8-11, 13-16, 18 | ✅ |
| MQTT | 4-6, 8-11, 15-18 | ✅ |
| Modbus | 5, 6, 8-10, 16, 18 | ✅ |
| Cámara IP | 5, 6, 8, 11, 12 | ✅ |

- **Verifícalo:** abre [[3.13 Tabla maestra de pistas]] y el Anexo, Sec. 3.2-3.12 (págs. 11-21).
- [ ] Paso 3 verificado

### Paso 4 — CVE, CVSS y madurez de explotación
> "Registre el **CVE, CVSS y la información disponible sobre su explotación**. Verifique que cada vulnerabilidad… tenga relación con los componentes presentes en el caso y **diferencie aquellas confirmadas de las que requieren validación adicional**."
> Anexo 2.3: "investigue el CVE en NVD, **valide en Exploit-DB** y registre el vector y puntaje CVSS."

- **Dónde:** diapositiva 11 · [[2.3 Matriz CVE-CVSS]]
- **Verificado contra la API de NVD:**

| CVE | CVSS v3.1 en NVD | En la diapositiva 11 |
|---|---|---|
| CVE-2021-41773 | 9.8 `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` | ✅ coincide |
| CVE-2021-42013 | 9.8, mismo vector | ✅ coincide |
| CVE-2017-0143 | 8.8 `…/PR:L/…` | ✅ coincide |
| CVE-2017-9833 | 7.5 `…/C:H/I:N/A:N`, etiqueta **disputed** | ✅ coincide y está marcado DISPUTED |
| CVE-2022-45956 | 5.3 `…/C:N/I:L/A:N` (bypass de autenticación por HEAD en Boa 0.94.13-14) | ✅ desde el 27-09 tiene **fila propia** (antes solo se citaba como contraste dentro de la fila de 9833) |

- La separación entre "confirmadas y las que requieren validación" se cumple: **5 CVE de NVD** (no 4) frente a 5 CWE con puntaje estimado marcado con `*` — **10 filas en total**, verificadas independientemente contra la API de NVD, el catálogo KEV de CISA y Exploit-DB el 27-09-2026 (0 discrepancias).
- **Explotación (verificada en CISA KEV y Exploit-DB):** 41773, 42013 y 0143 están en KEV (explotación activa, uso en ransomware) con PoC EDB-50383, EDB-50406 y EDB-41891. 9833 y 45956 tienen PoC (EDB-42290 y EDB-51139) y ninguno está en KEV. Detalle en [[2.3 Matriz CVE-CVSS#Madurez de explotación (Paso 4 de la guía)]].
- **Verifícalo:** busca cada CVE en el catálogo KEV de CISA y en exploit-db.com.
- **Verifícalo:** abre `https://nvd.nist.gov/vuln/detail/<CVE>` para cada fila y compara el puntaje y el vector.
- [ ] Paso 4 verificado

### Paso 5 — Cyber Kill Chain
> "Organice los vectores… siguiendo las fases de Cyber Kill Chain… construya una secuencia… desde el reconocimiento inicial hasta el posible cumplimiento de su objetivo."

- **Dónde:** diapositiva 13 · [[2.6 Cyber Kill Chain]]
- **Verifícalo:** las 7 fases en el orden de Lockheed Martin (Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives), cada una con activo y pista.
- **Estado:** ✅
- [ ] Paso 5 verificado

### Paso 6 — Mínimo diez técnicas MITRE ATT&CK
> "Seleccione como **mínimo diez** técnicas o subtécnicas… registre su **identificador, nombre, táctica asociada y evidencia**… Evite incluir técnicas que no puedan relacionarse razonablemente con el escenario."

- **Dónde:** diapositiva 14 · [[2.7 MITRE ATT&CK]]
- **Verificado en attack.mitre.org:** las 13 técnicas existen y su nombre y táctica son correctos; T0855 se verificó en ATT&CK for ICS.
- **Contraste con el Anexo 3.13:** se adoptaron **T1210** (SMBv1, marcada como posible) y **T0855** (MQTT). Para el JWT se usa **T1606.001** en vez de T1548, con la justificación escrita en [[2.7 MITRE ATT&CK#Decisiones de mapeo frente al Anexo 3.13]]. Ver [[#D1]].
- [ ] Paso 6 verificado

### Paso 7 — Hipótesis de ruta de compromiso
> "En cada etapa diferencie claramente **la pista encontrada, la hipótesis formulada y la evidencia que sería necesario obtener para validarla**. Si existen diferentes posibilidades, presente las rutas más probables y **justifique su selección**."

- **Dónde:** diapositiva 16 (diagrama de 8 saltos) y la 15 (tabla pista → hipótesis → evidencia, más la ruta alternativa justificada) · [[2.8 Ruta probable de ataque]] · desde el 27-09 la tabla se presenta primero (15) y el diagrama después (16), para mostrar el criterio de validación antes de la ruta que ya quedó sustentada — ver [[#D12]]
- **Verifícalo:** en el Anexo Sec. 3.9d (pág. 18), los 4625/4624 de `amunoz` salen de **10.10.10.20** (el servidor web) y Sysmon 3 muestra **`w.exe` → 10.10.30.40:1883**. Son las dos correlaciones más fuertes.
- **Estado:** ✅
- [ ] Paso 7 verificado

### Paso 8 — Preparar el video expositivo
> "…introducción, descripción del caso, análisis preliminar, alternativas de análisis de vectores y validación (vulnerabilidades, Cyber Kill Chain, MITRE ATT&CK, ruta probable de compromiso), propuesta preliminar (impactos), conclusiones, preguntas y referencias. Utilice tablas, esquemas y diagramas…"

- **Dónde:** todo el deck. Impactos: diapositiva 17 (P×I). Diagramas: la 5 y la 16. 14 tablas.
- **Verifícalo:** en la diapositiva 17, comprueba P×I en las 6 filas: 4×5=20, 5×4=20, 4×4=16, 4×4=16, 4×3=12, 3×3=9.
- **Estado:** ✅
- [ ] Paso 8 verificado

### Paso 9 — Documentar el uso de IA
> "Si utilizó herramientas de inteligencia artificial, registre la herramienta empleada, propósito de uso y actividades… Indique cómo verificó o contrastó la información… Si no utilizó IA, déjelo expresamente indicado."

- **Dónde:** diapositiva 22 · [[Declaracion uso de IA]] · formulario del Anexo, pág. 30
- **Estado:** ✅ resuelto. El campo **% apoyado en IA** ya no dice "POR COMPLETAR": `IA_PCT` en `build_deck.py` declara el porcentaje del archivo generado con asistencia y el del contenido técnico verificado a mano. Ver [[#D4]]; completa también tu propia revisión personal en [[Declaracion uso de IA]] si aún no lo hiciste.
- [ ] Paso 9 verificado

---

## 5. Instrumentos del Anexo (insumos del video)

| Instrumento | Qué pide el Anexo | Nota | Se ve en | Estado |
|---|---|---|---|---|
| 1.1 Núcleo conceptual | Anclar conceptos al caso | [[1.1 Núcleo conceptual]] | 7 | ✅ |
| 1.B Metodologías | "al menos tres metodologías" | [[1.B Comparación de metodologías]] (4) | 7 | ✅ |
| 1.C Glosario | "10 definiciones" | [[1.C Glosario operativo]] (10) | apoyo verbal | ✅ |
| 2.1 Activos C/I/D | C/I/D de 1 a 5 y justificación | [[2.1 Activos críticos C-I-D]] | 8 | ✅ |
| 2.2 Superficie | Puntos de entrada, fronteras y **diagrama** | [[2.2 Superficie de exposición]] | 5, 9 | ✅ |
| 2.3 CVE/CVSS | NVD + **Exploit-DB** + vector | [[2.3 Matriz CVE-CVSS]] | 11 | ✅ |
| 2.4 Vectores | Vector, activo, precondición, resultado, pista | [[2.4 Vectores de ataque]] | 10 | ✅ |
| 2.5 Ingeniería social | Técnica, objetivo, canal, pretexto, IoC, mitigación | [[2.5 Ingeniería social]] | 12 | ✅ |
| 2.6 Cyber Kill Chain | 7 fases con acción, activo y pista | [[2.6 Cyber Kill Chain]] | 13 | ✅ |
| 2.7 MITRE | Táctica, ID, procedimiento, activo | [[2.7 MITRE ATT&CK]] | 14 | ✅ |
| 2.8 Ruta | Paso a paso + diagrama + pista + detección | [[2.8 Ruta probable de ataque]] | 15 (tabla), 16 (diagrama) | ✅ |
| 2.9 Impacto/riesgo | P, I, P×I, tipo de impacto | [[2.9 Impacto y riesgo]] | 17 | ✅ |
| Declaración de IA | 7 campos | [[Declaracion uso de IA]] | 22 | ✅ [[#D4]] |

---

## 5bis. Cobertura artefacto por artefacto (Anexo Sec. 3)

> Los 10 tipos de artefacto que exige el **Paso 3 de la Guía** (Nmap, robots.txt, error SQL,
> headers, OSINT, logs, SMB, MQTT, Modbus, cámara IP) están **todos** en la presentación. Esta
> tabla va un nivel más abajo: por cada hallazgo concreto de la Sec. 3, dice si aparece o no.
> ⚠️ marca hallazgos reales del Anexo que hoy no están en ningún instrumento ni diapositiva.

| Sec. | Hallazgo del Anexo | ¿En el video? |
|---|---|---|
| 3.1 | Inventario A-01..A-08 | ✅ diap. 6, 8 |
| 3.2 | Apache 2.4.49, SMBv1, Telnet, MQTT, Modbus (banners) | ✅ diap. 9, 11, 14 |
| 3.2 | **SSH 22 (OpenSSH) y MariaDB 3306**, ambos en el host de A-01 | ✅ resuelto — ver [[#D7]] |
| 3.3a | `robots.txt`: `/dbadmin/`, `/backup/` | ✅ diap. 8, 9 |
| 3.3b | Headers: `Server`, `X-Powered-By`, sin CSP/XFO/HSTS | ✅ diap. 9 |
| 3.3c | Error SQL en `productos.php` | ✅ diap. 10, 11 |
| 3.3d | Login `/admin` sin bloqueo, credencial de demo trivial | ✅ (37 POST); la credencial de demo no se cita, no hace falta |
| 3.3e | Carga de archivos sin validar | ✅ diap. 11 (CWE-434) |
| 3.4 | Correo corporativo, organigrama, redes sociales, PDF con metadatos | ✅ diap. 4, 12, 13 |
| 3.4 | **Vacante que revela el stack** (MariaDB, PHP 7, cámaras Boa) | ✅ desarrollada en [[2.5 Ingeniería social]] y en las notas de la diapositiva 4 |
| 3.5 | Gateway, cámara, PLC, broker | ✅ diap. 6, 8, 9 |
| 3.5 | **Estación meteorológica: riesgo de inyectar datos falsos** que alteren la decisión de riego | ✅ diap. 4 (tabla de actores) |
| 3.6 | Logs correlacionados (4625/4624/7045/Sysmon/MQTT) | ✅ diap. 13, 15 |
| 3.7a | NSE: `http-vuln-cve2021-41773` | ✅ diap. 11 |
| 3.7a | **jQuery 1.7.2 y Bootstrap 3.3.7 desactualizados** (riesgo XSS del lado cliente) | ✅ resuelto — ver [[#D8]] (vector 10) |
| 3.7a | **Certificado SSL autofirmado, expirado y con SHA-1** (riesgo MITM) | ✅ resuelto — ver [[#D8]] (mismo vector 10) |
| 3.7a | Cookie sin `HttpOnly`/`Secure` | ✅ diap. 14 (T1539) |
| 3.7b | `.git` expuesto, `/backup` listable | ✅ diap. 9, 10, 11 |
| 3.7b | **`/uploads` listable y `phpinfo.php` expuesto** | ✅ diap. 9 y [[2.2 Superficie de exposición]] |
| 3.8a-c | `config.php.bak`, repositorio Git, API IDOR | ✅ diap. 10, 11, 14 |
| 3.8b | **`DEBUG=true`** en `config.php.bak` (fuga de información) | ✅ diap. 11 y [[2.3 Matriz CVE-CVSS]] |
| 3.8d | JWT `alg:none` | ✅ diap. 10, 11, 14 |
| 3.9a-b | SMB, sesión nula, share `respaldos` | ✅ diap. 10, 14, 15 |
| 3.9c | `LockoutThreshold 0`, RDP sin NLA | ✅ diap. 8, 14 |
| 3.9d | Eventos de Windows (4625/4624/7045/Sysmon) | ✅ diap. 13, 15 |
| 3.10a-c | MQTT, Modbus, cámara | ✅ diap. 9, 10, 15, 16 |
| 3.10d | **Firmware del gateway con credenciales fijas** (`admin:admin`, `root:12345`) — familia tipo Mirai | ✅ vector 6, diap. 10 y [[2.4 Vectores de ataque]] |
| 3.11 | HTTP Basic sin TLS hacia `/admin` | ✅ diap. 9 |
| 3.11 | Telnet en texto plano | ✅ diap. 9 y [[2.2 Superficie de exposición]], citando la captura (Sec. 3.11) |
| 3.11 | MQTT sin TLS | ✅ diap. 9 |
| 3.12a | Correos y hosts (theHarvester) | ✅ diap. 13 |
| 3.12a | **Subdominio `dev.agrosmart-sumapaz.co` expuesto** | ✅ notas de la diapositiva 4 y [[2.2 Superficie de exposición]] |
| 3.12b | **Filtración en un paste público de la misma credencial (`webapp/Agro2024*`) que hay en `config.php.bak`** | ✅ resuelto — ver [[#D9]] |
| 3.12c | Metadatos del PDF (`amunoz`, ruta interna) | ✅ diap. 4, 12, 13, 15, 16 |
| 3.13 | Tabla maestra de pistas | ✅ base de 2.3 y 2.7 |

- [ ] Cobertura de artefactos revisada

---

## 6. Decisiones antes de entregar

### D1
✅ **Resuelto — técnicas MITRE frente al Anexo 3.13** (pág. 21). Verificado en attack.mitre.org y en los datos oficiales de ATT&CK for ICS.

| Pista | Anexo 3.13 sugiere | Antes | Ahora | Por qué |
|---|---|---|---|---|
| SMBv1 | T1210 | T1021.002 | **T1021.002 + T1210** | T1021.002 = sesión nula observada; T1210 = explotación de MS17-010 (CVE-2017-0143), **marcada como posible, no observada** |
| JWT `alg=none` | T1548 | T1134 | **T1606.001** Forge Web Credentials: Web Cookies | T1134 es solo de Windows y las subtécnicas de T1548 son del SO y la nube; el caso forja una credencial web (`Set-Cookie: token=…`) |
| MQTT anónimo | T0855 (ICS) | T1565.002 | **T0855** Unauthorized Command Message | Enviar una orden no autorizada a un activo de control es exactamente T0855 |

Se retiró T1068: mapeaba el RCE de Apache como escalada de privilegios, cosa que el Anexo no muestra (el RCE ya es T1190). Siguen siendo 13 técnicas.
- [ ] Revisado por mí (diapositiva 14 y [[2.7 MITRE ATT&CK]])

### D2
✅ **Resuelto — explotación de cada CVE.** La columna de la diapositiva 11 pasa a ser "Evidencia y explotación": CISA KEV + ID de Exploit-DB por CVE. Tabla completa en [[2.3 Matriz CVE-CVSS#Madurez de explotación (Paso 4 de la guía)]].
- [ ] Revisado por mí

### D3
✅ **Resuelto — headers.** En la diapositiva 9 y en [[2.2 Superficie de exposición]]: `Server: Apache/2.4.49` y `X-Powered-By: PHP/7.2.24` delatan versiones, y faltan CSP, X-Frame-Options y HSTS (Sec. 3.3b). Además, HTTP Basic sin TLS hacia `/admin` (Sec. 3.11). Se anotaron en las filas existentes de Apache y /admin, sin crear puntos nuevos (los puntos nuevos que sí se sumaron después son SSH y MariaDB, ver [[#D7]]).
- [ ] Revisado por mí

### D4
✅ **Resuelto — % apoyado en IA.** `IA_PCT` en `03 - Video/build_deck.py` declara: "100 % del archivo generado con asistencia; 100 % del contenido técnico verificado a mano por el estudiante contra el Anexo 1, el NVD, CISA KEV, Exploit-DB y MITRE ATT&CK." Ya no aparece "POR COMPLETAR" en la diapositiva 22.
- [ ] Revisado por mí — falta que completes tu propia revisión personal en [[Declaracion uso de IA]] si la cifra o el texto no reflejan exactamente tu trabajo

### D5
✅ **Resuelto — referencias.** Las diapositivas 20 y 21 tienen 15 referencias APA 7 en orden alfabético, con el **OVI** (Zambrano Hernández, 2025) y el **OVA** (Zambrano Hernández, 2026) del curso, más CISA KEV, Exploit-DB y MITRE ATT&CK (Enterprise e ICS).
- **NIST SP 800-115 es de 2008** (csrc.nist.gov, publicada el 30-09-2008), no de 2018: corregido en las diapositivas y en el [[1.C Glosario operativo]].
- Año de Benavides et al.: la Guía dice 2019, pero el PDF indica **Vol. 13, N.º 32, enero-abril de 2020** (aceptado en noviembre de 2019). Se mantiene 2020.
- [ ] Revisado por mí

### D6
**Reflexión académica (apartado 4).** Una frase en la diapositiva 18 sobre qué aprendiste del análisis. Por ejemplo, que el riesgo de este caso está en la cadena y no en cada vulnerabilidad aislada. Debe estar en tu voz.
- [ ] Hecho o descartado

### D7
✅ **Resuelto — SSH y MariaDB.** Añadidos a [[2.2 Superficie de exposición]] y a la diapositiva 9 como dos puntos nuevos en el mismo host de A-01, con exposición marcada "Host (sin confirmar a Internet)" (el Anexo no dice si el firewall los expone). El total pasa de 9 a **11 puntos de entrada**; el titular se ajusta a "9 de 11 no tienen autenticación en su frontera". Actualizado también en [[1.1 Núcleo conceptual]] e `index.md`.
- [ ] Revisado por mí

### D8
✅ **Resuelto — riesgos de cliente y transporte.** Nuevo **vector 10** en [[2.4 Vectores de ataque]] y en la diapositiva 10: componentes JS desactualizados (`jQuery`, `Bootstrap`) y certificado TLS autofirmado/expirado/SHA-1, con MITRE T1557 citado en el texto (no como fila nueva en [[2.7 MITRE ATT&CK]], para no superar el límite de 14 filas de la diapositiva 14).
- [ ] Revisado por mí

### D9
✅ **Resuelto — correlación OSINT ↔ técnico.** La pista del vector 5 en [[2.4 Vectores de ataque]] y en la diapositiva 10 ahora cita también el secreto filtrado en el paste público (Sec. 3.12b), además de `config.php.bak`. En [[2.5 Ingeniería social]] se añadió la sección "El OSINT no termina en las personas" y una sexta señal de alerta sobre fugas de credenciales en sitios públicos.
- [ ] Revisado por mí

### D10
✅ **Resuelto — los 7 hallazgos menores restantes de la tabla de cobertura.** Vacante que revela el stack, riesgo de dato falso en la estación meteorológica, `/uploads` y `phpinfo.php`, `DEBUG=true`, firmware con credenciales fijas (tipo Mirai), Telnet en texto plano y el subdominio `dev.` expuesto. Todos citados con su sección del Anexo en [[2.2 Superficie de exposición]], [[2.3 Matriz CVE-CVSS]], [[2.4 Vectores de ataque]] y [[2.5 Ingeniería social]]; los que caben sin forzar el diseño también quedaron en el `.pptx` (diapositivas 4, 9, 10 y 11), verificado con `audit.py` (0 errores).
- [ ] Revisado por mí

### D11
✅ **Resuelto — se apareció la rúbrica oficial de evaluación y `build_deck.py` se reescribió para cumplirla al pie de la letra.** La rúbrica (nueva fuente de nivel 1, ver [[00 - Contexto/Rúbrica de evaluación]]) exige **8** secciones estructurales tituladas explícitamente, no 6, y separa "Alternativas de análisis y validación" y "Propuesta preliminar" como secciones propias — antes ambas vivían sin rotular dentro de un único "apartado 3: análisis preliminar" (pág. 5-6 de la Guía). Cambios aplicados el 27-09-2026:
- Cada diapositiva rotula su sección en el kicker como `SECCIÓN N DE 8 · <NOMBRE>`, con el nombre literal de la rúbrica (`SECCIONES` en `build_deck.py`); el "APARTADO N DE LA GUÍA" / "INSTRUMENTO 2.x" se conserva en el pie.
- `CVE-2022-45956` pasa de mención de contraste a **fila propia** verificada: la matriz de la diapositiva 11 tiene ahora **5 CVE** (no 4) y 5 CWE, 10 filas en total; el stat de la diapositiva 2 se corrigió de "4" a "5" (quedó desactualizado en la primera pasada de la reescritura, lo até yo mismo el 27-09).
- Cada fila de CVE/CWE y de MITRE ATT&CK cita ahora explícitamente su sección del Anexo 1 (antes solo algunas la citaban).
- Se añadió la referencia **Lockheed Martin (2011)**, fuente pública que la rúbrica nombra explícitamente ("NVD, Exploit-DB, MITRE ATT&CK o Lockheed Martin") — quedó **16** referencias, no 15. Se corrigió también un orden alfabético roto (Lockheed antes que Lu, no después) y una autoría equivocada: el Boletín 28 pasa de "Zambrano Hernández, Peña Hidalgo y Cárdenas Corral" a **Palomo Luna, Zambrano Hernández, Moreno Molano y Peña Hidalgo** — Cárdenas Corral es el revisor del boletín (verificado contra el PDF, pág. 4), no autor, y el boletín omitía a los dos autores reales.
- `TIMING`/`advTm` hacen determinista la duración del MP4 exportado (563 s = 9:23), en vez de depender de que PowerPoint calcule bien las animaciones al exportar.
- El % apoyado en IA se completó (ver [[#D4]]).
- Verificado independientemente el mismo día: los 5 CVE contra NVD/KEV/Exploit-DB, los 13 identificadores MITRE contra attack.mitre.org (Enterprise + ICS), las leyes 1273/1581/1341 contra el texto oficial, y 8 DOI académicos — 0 errores en la parte técnica externa.
- [ ] Revisado por mí

### D12
✅ **Resuelto — la tabla de hipótesis y el diagrama de la ruta intercambiaron de diapositiva.** Antes: diapositiva 15 = diagrama de 8 saltos, diapositiva 16 = tabla pista/hipótesis/evidencia. Ahora: diapositiva 15 = tabla (`slide_15_validacion`, sección 4 de la rúbrica), diapositiva 16 = diagrama (`slide_16_ruta`, sección 5). El orden nuevo enseña primero el criterio con el que se valida cada salto y se descarta la ruta alternativa, y después presenta la ruta que ya queda sustentada — al revés, el diagrama tendría que sostener una ruta que el expositor aún no ha justificado. Todas las referencias cruzadas de este documento a "diapositiva 15" y "diapositiva 16" se revisaron y corrigieron el 27-09-2026.
- [ ] Revisado por mí

---

## 6bis. Revisión de coherencia académica (26-09-2026)

> Esto es distinto de todo lo anterior: no verifica que cada dato exista en el Anexo, sino
> que **el argumento se sostenga solo**, sin contradecirse entre instrumentos ni consigo mismo.
> Revisé las 22 diapositivas y los 12 instrumentos completos. Encontré 9 problemas reales y
> los corregí todos; quedan documentados aquí para que los verifiques tú mismo.

| # | Hallazgo | Severidad | Dónde estaba | Corrección aplicada |
|---|---|---|---|---|
| A1 | La diapositiva 2 decía **"3 CVE con puntaje verificado en NVD"**, pero la matriz (diapositiva 11) tiene **4** filas de CVE. Un evaluador que cuenta las filas encuentra la contradicción en el minuto 1 del video. | Alta | Diapositiva 2 | Corregido a "4" |
| A2 | **"El evento 7045 llega 20 minutos antes que la conexión al broker"** — ese dato no existe en el Anexo (no hay timestamps), y **contradice directamente** la nota de [[2.8 Ruta probable de ataque]], que ya decía correctamente que no hay forma de ordenar esos eventos en el tiempo. Una cifra inventada en un instrumento y la corrección honesta en otro. | Alta | [[1.1 Núcleo conceptual]] | Se retiró el "20 minutos"; ahora dice que solo consta la coincidencia de proceso (`w.exe`), no el orden temporal |
| A3 | **Ley 1273/2009 citada como "Arts. 192, 193 y 254"** — verificado contra el texto oficial de la ley (Función Pública / Secretaría del Senado): esos artículos no existen en la Ley 1273; la ley agrega los **arts. 269A-269J**. Contradice además a la diapositiva 3 y a [[00 - Contexto/Marco legal y ROE]], que sí citan 269A correctamente. | Alta | [[1.1 Núcleo conceptual]] | Corregido a "Art. 269A ... entre los arts. 269A-269J" |
| A4 | El JWT `alg:none` se presentaba como **"Escalada al rol superadmin sin credencial válida"**, un resultado ya conseguido. Pero el propio token decodificado (Sec. 3.8d) muestra `rol=contador`; "superadmin" es un rol que existe en la API (Sec. 3.8c) para otro usuario. Fuera del Paso 7, la presentación no siempre distinguía evidencia de hipótesis, y aquí presentaba una **capacidad** (forjar cualquier rol, porque no hay firma que lo impida) como si fuera un **hecho observado**. | Media | [[2.4 Vectores de ataque]] · [[2.7 MITRE ATT&CK]] · [[2.9 Impacto y riesgo]] · diapositivas 10, 14, 18 | Reescrito en los 3 instrumentos y las 3 diapositivas: ahora dice que el token capturado muestra `rol=contador` y que la falta de firma **permite** forjar cualquier rol, sin afirmar que ya se llegó a `superadmin` |
| A5 | La leyenda de color de la diapositiva 17 ("bajo·6+, medio·13+, alto·20+, máximo·25+") usaba **categorías y umbrales distintos** a la escala oficial de [[2.9 Impacto y riesgo]] ("Crítico 20-25, Alto 15-19, Medio 8-14, Bajo 1-7"). Con la leyenda vieja, un escenario de riesgo 16 (que el instrumento llama "Alto") se leía visualmente más cerca de "medio" que de "alto": dos clasificaciones distintas para el mismo número, en la misma diapositiva. | Media | Diapositiva 17 | La leyenda ahora usa los mismos 4 rangos que el instrumento: bajo 1-7, medio 8-14, alto 15-19, crítico 20-25 |
| A6 | [[1.C Glosario operativo]], término 8 ("Escalada de privilegios"), justificaba la definición citando la distinción **T1068 ≠ T1134** — un par de técnicas que ya no existen en el mapeo MITRE actual (se reemplazaron por T1606.001, T1210 y T0855 al resolver D1). La definición apuntaba a algo que ya no está en el video. | Baja | [[1.C Glosario operativo]] | Ejemplo actualizado a T1210 (posible) vs. T1606.001 (observada) |
| A7 | [[1.1 Núcleo conceptual]], fila "Superficie de ataque": la celda decía **"Superficie de ataque en IA \| Activos, puntos de entrada,"** — texto truncado con un "en IA" que no corresponde a ningún concepto del bloque. | Baja | [[1.1 Núcleo conceptual]] | Corregido a "Superficie de ataque \| Activos, puntos de entrada, exposición, fronteras de confianza" |
| A8 | La misma nota incluía "Telnet abierto" como evidencia de **"Análisis de vulnerabilidades"** apuntando a [[2.3 Matriz CVE-CVSS]], pero Telnet no tiene fila en esa matriz (está en 2.2 y en el vector 6 de 2.4, no en 2.3). | Baja | [[1.1 Núcleo conceptual]] | Se quitó "Telnet abierto" de esa celda |
| A9 | Diapositiva 17: **"La probability de los vectores se valoro"** — anglicismo ("probability") y tilde faltante ("valoró"). | Cosmética | Diapositiva 17 | Corregido a "La probabilidad de los escenarios se valoró" |

> [!info] Un hallazgo que encontré de paso, no de esta lista
> Al revisar la diapositiva 17 en detalle noté que el rótulo "ESCALA DE RIESGO" quedaba
> tapado por el primer color de la leyenda (defecto visual previo, no introducido por A5).
> Lo corregí de paso: reduje el tracking del rótulo y reacomodé las cuatro muestras de color.

**Lo que NO cambié, y por qué:**
- La distinción entre la cadena con phishing y la cadena técnica alternativa (CKC, 2.6) se mantiene como dos posibilidades explícitas, no como una contradicción — está correctamente enmarcada como tal.
- El uso de "Delivery" para una petición HTTP directa en la cadena técnica alternativa es una adaptación defendible del modelo CKC a un ataque web (el exploit se entrega y ejecuta en la misma solicitud); no es un error, es una lectura académica razonable que puede sustentarse si se pregunta en el video.
- [ ] Revisado por mí

---

## 7. Checklist final de exportación

- [ ] Abrir el `.pptx` en **PowerPoint** (no en LibreOffice) y recorrerlo en modo presentación: fundidos y animaciones de las diapositivas 16 y 19
- [ ] Grabar la narración siguiendo las notas del orador (538 s en total)
- [ ] Archivo → Exportar → Crear un video → 1080p → "Usar intervalos y narraciones grabados"
- [ ] MP4 ≤ 10:00 y ≤ 200 MB (el `.pptx` calcula 563 s = 9:23, con 37 s de holgura)
- [ ] Ver el MP4 completo una vez: audio, tablas legibles, sin cortes
- [ ] Declaración de IA completa en el formulario del Anexo

---

## 8. Mapa del proyecto (tras unificar)

| Carpeta | Contenido |
|---|---|
| `00 - Contexto/` | Qué me piden, contexto de la guía, arquitectura, marco legal, **esta review** |
| `01 - Artefactos/` | Notas de las Sec. 3.1-3.13 del Anexo |
| `02 - Instrumentos Reto 2/` | 1.1, 1.B, 1.C, 2.1-2.9, Declaración de IA |
| `03 - Video/` | `.pptx` vigente (ciberpunk), guion, `build_deck.py`, `deck_kit.py`, `audit.py` |
| `04 - Referencias/` | Referencias y orden de lectura |
| `05 - Fuentes/` | Guía, Anexo 1, `Lecturas/` (PDF del curso), `OVA/` (OVA y video OVI) |

La carpeta original del curso (`Documents/MGs Cibersecurity/Intrusion y Testing/Test 2/`) conserva solo el `venv` (entorno de Python para regenerar el `.pptx`) y un acceso directo `Vault Obsidian - Test 2` a este vault.

Desde el 27-09-2026 este vault es también un repositorio git local (rama `master`, sin remoto),
con `.gitignore` excluyendo `.obsidian/` y `05 - Fuentes/OVA/` (86 MB, material con copyright de
UNAD). El historial está commiteado en orden de creación y por unidad lógica.

Relaciona: [[Qué me piden y qué tengo que entregar]] · [[Guion del video]] · [[index]]
