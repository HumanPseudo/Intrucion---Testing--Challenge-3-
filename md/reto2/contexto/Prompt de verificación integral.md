---
tags: [prompt, revision, verificacion, fuentes, reto-2]
---

# Prompt de verificación integral — Reto 2 AgroSmart

> Propósito: revisar el entregable completo (presentación + instrumentos) **relacionándolo con
> este mismo repositorio** (el vault de Obsidian) y **verificando cada fuente** —tanto externa
> (NVD, MITRE, ley colombiana, DOI académicos) como local (los archivos que el estudiante ya
> descargó en `05 - Fuentes/`)— antes de dar cualquier hallazgo por bueno o por malo.
>
> A diferencia de [[03 - Video/prompt-revision-adversarial|el prompt adversarial]] (que audita
> densidad visual y defectos de diseño ya conocidos, y que queda desactualizado en cuanto cambian
> los números de diapositiva), este prompt es para una pasada de **coherencia + trazabilidad de
> fuentes**, pensada para repetirse cada vez que el deck o los instrumentos cambien de forma
> significativa.
>
> **Uso:** copia desde `=== INICIO DEL PROMPT ===` hasta `=== FIN DEL PROMPT ===` y pégalo en una
> sesión con acceso de lectura a este directorio y, si es posible, a internet (WebSearch/WebFetch).

---

=== INICIO DEL PROMPT ===

## 0. Mapa del repositorio (léelo antes de nada)

Todo vive bajo la raíz del vault. Rutas relativas a esa raíz:

| Carpeta | Contenido |
|---|---|
| `00 - Contexto/` | Contexto y arquitectura, Glosario, Marco legal y ROE, qué exige la guía, y el checklist maestro `Review - verificación paso a paso.md` |
| `01 - Artefactos/` | Transcripciones/resúmenes de las secciones 3.x del Anexo 1 (activos, web/OSINT, IoT-OT/logs, recon, Windows/IT, tabla maestra de pistas) |
| `02 - Instrumentos Reto 2/` | Los instrumentos entregables: `1.1`, `1.B`, `1.C`, `2.1` a `2.9`, y `Declaracion uso de IA.md` — **esta es la fuente de verdad intermedia**: lo que el deck debe reflejar |
| `03 - Video/` | `build_deck.py` (genera el `.pptx`), `deck_kit.py` (sistema de diseño), `audit.py` (auditor de ajuste de texto), `Guion del video.md`, y el `.pptx` final |
| `04 - Referencias/` | Lectura de apoyo sobre referencias |
| `05 - Fuentes/` | **Los documentos descargados**: `Anexo 1 Caso AgroSmart del Sumapaz.pdf`, `Guía de aprendizaje - Reto 2....pdf`, `Lecturas/` (PDF de cada referencia académica obligatoria + `REFERENCIAS_APA7.txt`, la lista maestra ya corregida por el estudiante) y `OVA/` (los objetos virtuales de aprendizaje/información descargados, algunos de acceso restringido) |

La fuente de verdad tiene una jerarquía estricta:

1. **Anexo 1 y Guía de aprendizaje** (`05 - Fuentes/*.pdf`) — verdad del caso y de las reglas de entrega. Prevalece sobre todo lo demás.
2. **Fuentes primarias externas verificables**: NVD (`nvd.nist.gov`), MITRE ATT&CK (`attack.mitre.org`), catálogo KEV de CISA, Exploit-DB, texto oficial de las leyes colombianas citadas (1273/2009, 1581/2012, 1341/2009), DOI de cada referencia académica.
3. **Los archivos ya descargados en `05 - Fuentes/`** — antes de declarar una referencia "no verificable" o "fabricada" por no encontrarla en un buscador público, **comprueba primero si existe un PDF, video o paquete OVA correspondiente en esta carpeta**. Varias fuentes de este proyecto son de acceso restringido (repositorio institucional de UNAD con login) y devolverán 404 a cualquier fetch público aunque sean legítimas — el archivo local es la prueba, no el enlace.
4. **Los instrumentos de `02 - Instrumentos Reto 2/`** — lo que el estudiante afirmó. Se audita, no se da por cierto.
5. **El `.pptx` / `build_deck.py`** — debe ser un reflejo fiel de 1-4, nunca una fuente en sí mismo.
6. **Tu memoria del modelo** — no es fuente. Si la usas para completar un dato, dilo explícitamente y verifícalo contra 1-3 antes de escribirlo.

Regla dura: si dos niveles se contradicen, gana el de menor número. Repórtalo como conflicto, no elijas en silencio.

## 1. Qué debes producir

Para cada diapositiva/instrumento que revises, contesta tres preguntas, en este orden:

1. **¿Está bien citado?** Toda cifra, ID técnico, artículo de ley o afirmación debe rastrearse a una sección concreta del Anexo/Guía (`Sec. 3.x`) o a una fuente pública verificada con URL. Si no puedes rastrearlo, es un hallazgo.
2. **¿La abstracción es correcta?** ¿Los dominios/fronteras/arquitectura, los conteos (activos, vectores, tácticas, saltos, riesgos) y las relaciones causales que arma el deck son una simplificación fiel del Anexo, o inventan/generalizan de más?
3. **¿El vocabulario es preciso y profesional?** Tildes, calcos del inglés (p. ej. "explotado en la naturaleza" en vez de "explotación activa confirmada"), frases tipo eslogan con contraste dramático ("no es X: es Y") cuando no aportan precisión técnica, autorreferencias de la diapositiva a sí misma, gerundios o fragmentos sin verbo.

## 2. Procedimiento

### 2.1 Verificación cruzada deck ↔ instrumentos ↔ Anexo/Guía
Para cada dato numérico o afirmación factual en `build_deck.py` (tablas, pies de página, cajas de cierre, notas del orador incluidas):
- Búscalo primero en el instrumento correspondiente de `02 - Instrumentos Reto 2/`.
- Luego confirma el instrumento contra el Anexo/Guía (`05 - Fuentes/*.pdf`, o su extracto en `01 - Artefactos/`).
- Si el deck y el instrumento no coinciden, o el instrumento y el Anexo no coinciden, es un `ERROR DE DATO` — cita `archivo:línea` (o número de sección/página) en ambos lados.

### 2.2 Verificación de fuentes técnicas externas
Para cada CVE: confirma el puntaje CVSS v3.1 y el vector contra NVD; confirma el estado de explotación contra el catálogo KEV de CISA y Exploit-DB. Para cada ID `Txxxx`/`T0xxx` de MITRE ATT&CK: confirma nombre y táctica contra `attack.mitre.org` (o la matriz ICS para IDs `T0xxx`). Para cada artículo de ley citado: confirma número y contenido contra el texto oficial. Usa WebSearch/WebFetch y cita la URL consultada; si no tienes acceso, marca `NO CONSULTADO` explícitamente — no lo des por bueno de memoria.

### 2.3 Verificación de la bibliografía académica (APA 7)
Esta es la parte que con más facilidad falla en falso positivo — sigue el orden exacto:
1. Lee `05 - Fuentes/Lecturas/REFERENCIAS_APA7.txt`: es la lista maestra que el propio estudiante ya verificó y corrigió (incluye notas de qué corrigió respecto a la guía original). Trátala como semi-autoritativa, pero no infalible.
2. Para cada referencia del `.pptx` (`REFERENCES` en `build_deck.py`), confirma que exista el PDF correspondiente en `05 - Fuentes/Lecturas/` **antes** de intentar verificarla por web.
3. Solo si no hay archivo local, intenta verificar por DOI/título vía WebSearch. Un DOI que resuelve a un artículo con mismo título/autores/revista = verificado.
4. Para fuentes tipo OVI/OVA de repositorio institucional (UNAD): revisa `05 - Fuentes/OVA/` — el nombre de archivo o el título embebido en el paquete debe coincidir con el título citado. Un 404 en `repository.unad.edu.co` **no es evidencia de que la fuente sea falsa**: ese repositorio exige login. Documenta el archivo local que la respalda en vez de basarte solo en el enlace.
5. Nunca declares una referencia "fabricada" solo por no encontrarla en buscadores públicos. Fabricada = ni el archivo local existe, ni el DOI/título resuelve a nada, ni el autor real tiene constancia pública de haberla publicado.

### 2.4 Verificación de aritmética y conteos
Recalcula tú mismo, no confíes en el texto: sumas de tablas (P×I, C+I+D), conteos de filas/tácticas/vectores/saltos declarados en pies de página o cajas de síntesis, coincidencia entre "N de M" declarado y el conteo real. Cualquier discrepancia es un hallazgo, aunque sea de una sola unidad (ej. "8 tácticas" cuando son 7).

### 2.5 Verificación de redacción
Por cada diapositiva, señala (sin corregir todavía, primero repórtalo):
- Tildes faltantes o mal puestas (`esta`/`está`, `que`/`qué`, `ultima`/`última`, etc.).
- Calcos directos del inglés técnico (`explotado en la naturaleza`, `en el radar`, etc.).
- Frases con estructura "no es X: es Y" o "X, no Y" cuando funcionan como eslogan retórico y no como distinción técnica real — diferénciarlas: una distinción técnica real (p. ej. "T1606.001 no es una escalada del sistema operativo") se mantiene; una dramatización vacía se reformula.
- Autorreferencias tipo "esta diapositiva" (una diapositiva no debe hablar de sí misma).
- Consistencia tipográfica: flechas Unicode `→` vs. ASCII `->`, comillas, guiones.

### 2.6 Verificación de layout (obligatoria tras cualquier corrección de texto)
Antes de escribir un cambio en `build_deck.py`, prueba el ajuste de línea con `audit.py` (funciones `wrap_lines`/`text_width_pt`) para el nuevo texto contra el ancho real de la caja, comparando el número de líneas contra la versión anterior. Después de aplicar el cambio:
```
python3 build_deck.py
python3 audit.py "Reto2 - AgroSmart - Análisis de vectores de ataque (ciberpunk).pptx"
```
Objetivo: **0 errores**. Las advertencias de tamaño de fuente por debajo del mínimo recomendado son una decisión de diseño preexistente del deck (mono/caption pequeño) y no requieren corrección salvo que además desborden la caja.

## 3. Reglas de no-sumisión

1. Prohibido el halago sin evidencia numérica ("se ve bien", "está completo"). Si algo está bien, di **por qué** con la comparación que lo demuestra.
2. Toda afirmación lleva evidencia: `archivo:línea`, `diapositiva N`, o URL consultada.
3. Prohibido "parece" y "probablemente": confirma contra la fuente o marca `NO VERIFICABLE`/`NO CONSULTADO` y di qué falta para verificarlo.
4. Prohibido inventar un dato que no está en los archivos ni en una fuente consultada.
5. Si dos fuentes se contradicen, reporta el conflicto explícitamente; no seleccione una en silencio.
6. **Nunca agregues una nota de tipo "[!warning] Corregido (fecha)" ni ningún rastro de historial de edición al contenido.** Corrige directamente en el texto — el vault debe reflejar siempre el estado actual, no su historial. La única excepción es `00 - Contexto/Review - verificación paso a paso.md`, que es en sí mismo un checklist vivo.
7. No declares una fuente como fabricada sin haber revisado primero `05 - Fuentes/` (ver 2.3).

## 4. Contrato de salida

1. **Tabla de verificación de fuentes**: `Referencia/Dato · Tipo (interna/externa/académica) · Verificado contra · Resultado (OK/ERROR/NO VERIFICABLE) · Evidencia`.
2. **Hallazgos de coherencia deck↔instrumentos↔Anexo**: `ID · Severidad (P0/P1/P2) · Archivo(s) · Qué dice cada lado · Cuál prevalece y por qué`.
3. **Hallazgos de redacción**: lista corta, agrupada por diapositiva, con la frase original y la propuesta de corrección.
4. **Estado de build**: resultado de `audit.py` antes y después de aplicar correcciones (0 errores es el objetivo).
5. **Autocalibración**: qué no pudiste verificar (sin acceso a internet, archivo no leído, etc.) y qué asumiste.

=== FIN DEL PROMPT ===

---

## Notas para quien lo ejecute (no forman parte del prompt)

- Este prompt nació de una revisión real en la que se declaró erróneamente "fabricadas" dos
  referencias (Zambrano Hernández, 2025 y 2026) que en realidad eran materiales OVI/OVA reales
  del curso, descargados en `05 - Fuentes/OVA/`, pero de acceso restringido — de ahí que
  devolvieran 404 en una verificación pública. La sección 2.3 existe específicamente para no
  repetir ese falso positivo.
- Complementa, no sustituye, a [[03 - Video/prompt-revision-adversarial]] (densidad visual y
  defectos de diseño ya conocidos) y a [[00 - Contexto/Review - verificación paso a paso]]
  (checklist de avance sección por sección).

**Relaciona**: [[03 - Video/prompt-revision-adversarial]] · [[00 - Contexto/Review - verificación paso a paso]] · [[05 - Fuentes/Lecturas/REFERENCIAS_APA7.txt|REFERENCIAS_APA7.txt]]
