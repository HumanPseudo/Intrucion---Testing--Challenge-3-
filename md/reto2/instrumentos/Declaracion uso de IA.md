---
tags: [instrumento, ia, declaracion, reto-2]
---

# Declaracion uso de IA

> Anexo 1 págs. 25 y 30. **Obligatoria.** Sé honesto: la declaración se audita.

| Campo | Tu respuesta |
|-------|--------------|
| Herramienta de IA utilizada | Asistente de IA basado en modelos de lenguaje (Claude, de Anthropic, vía Claude Code). ⚠ *Confirmar/añadir cualquier otra herramienta usada (p. ej. la usada con `prompt-ciberpunk.md`).* |
| ¿Para qué la usé? (tarea concreta) | (1) Generar el código Python (`build_deck.py`, `deck_kit.py`, `audit.py`) que construye la presentación con tablas nativas y la verifica. (2) Maquetar y redactar el texto de las diapositivas y las notas del orador a partir de los instrumentos 2.1-2.9. (3) Auditoría adversarial del paquete (verificación de CVE, IDs MITRE, aritmética y consistencia) y aplicación de las correcciones. |
| Prompt(s) principal(es) — transcribir literalmente | Los prompts completos están en el vault: `03 - Video/prompt-ciberpunk.md` (generación del análisis y la presentación) y `03 - Video/prompt-revision-adversarial.md` (auditoría). Prompt de corrección: "aplica estos ajustes" sobre el informe de auditoría. |
| Resultado/salida que me arrojó | Presentación de 22 diapositivas generada por código, informe de auditoría con 12 hallazgos priorizados (P0-P2) y las correcciones aplicadas a la presentación y a los instrumentos 2.1, 2.3 y 2.7. |
| ¿Cómo verifiqué/validé esa salida? (NVD, ExploitDB, MITRE, curso, prueba propia) | CVE-2021-41773, CVE-2021-42013, CVE-2017-0143, CVE-2017-9833 y CVE-2022-45956 contrastados con la API de NVD (puntaje y vector); los 13 IDs ATT&CK contra attack.mitre.org; texto completo del Anexo 1 y de la Guía; `audit.py` sobre el .pptx (tablas, fuentes, tiempos de notas). ⚠ *Añadir la revisión personal que hiciste.* |
| Ajustes críticos que hice (qué corregí/descarté y por qué) | La IA había nombrado mal T1565.002 ("Stored" en vez de "Transmitted Data Manipulation"); sumado 13 como 14 en A-01; declarado 9 tablas en vez de 11; atribuido al Anexo una frase que es de NVD. Se corrigieron. Se añadió CVE-2022-45956 como alternativa para la cámara porque el Anexo pide un CVE de *bypass de autenticación*. |
| % aproximado del entregable apoyado en IA | ⚠ *Completar con tu estimación honesta.* |

> [!warning] Riesgo académico
> Declarar el uso de IA es **obligatorio** y no penaliza. Ocultarlo sí. Usa IA para entender, comparar y redactar; **verifica siempre contra NVD, Exploit-DB, MITRE y las fuentes del curso.**
