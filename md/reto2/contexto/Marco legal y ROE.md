---
tags: [etica, roe, legal]
---

# Marco legal y ROE

> Fuente: Anexo 1, Sec. 1.1 y 1.2 (págs. 7-8).

## Leyes aplicables (Colombia)

| Norma | Qué regula | Por qué importa |
|-------|-----------|-----------------|
| **Ley 1273 de 2009** | Delitos informáticos: art. 269A acceso abusivo, interceptación, damage, software malicioso, violación de datos | Acceso o afectación **sin** autorización es delito. La autorización escrita y el alcance acotado separan el pentest de la conducta delictiva |
| **Ley 1581 de 2012** | Protección de datos personales (habeas data) | Los datos hallados (correos, credenciales, PII) exigen confidencialidad y minimización |
| **Ley 1341 de 2009** | Marco de las TIC | Encuadre sectorial de servicios y operadores |
| **Contrato / autorización** | Mandato y consentimiento informado | Define activos, ventanas, técnicas permitidas y exclusiones |

## ROE del caso

**Autorización simulada:** AgroSmart del Sumapaz S.A.S. autoriza reconocimiento,
enumeración, identificación y validación **controlada** de vulnerabilidades sobre los
activos del Anexo 1, **únicamente dentro del Cyber Range del curso**.

- **In-scope:** segmento DMZ (portal LAMP), segmento corporativo IT, segmento IoT/OT del laboratorio.
- **Out-of-scope:** cualquier IP, dominio, persona o servicio real ajeno al laboratorio; DoS destructivos; exfiltración real; ingeniería social **ejecutada** sobre personas reales (solo se analiza y simula).
- **Técnicas permitidas:** escaneo, enumeración, fuzzing controlado, validación con Nmap, Nikto, Burp Suite, SQLMap y Metasploit en módulos autorizados.
- **Regla de oro:** si no está explícitamente en el alcance, está fuera. Ante la duda, no se ejecuta.

> [!warning] OJO — el Instrumento 1.A (Acta de ROE) es del **Reto 4**, no de este reto.
