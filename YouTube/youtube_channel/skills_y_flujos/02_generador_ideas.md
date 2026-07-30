# Skill 2: Generador de Ideas Basado en Top Videos

**Prioridad:** ⭐⭐⭐ ALTA  
**Tiempo estimado:** 2-3 horas  
**Complejidad:** ⭐⭐⭐ (Media)  
**ROI:** Muy Alto

---

## 📝 Qué hace

Analiza tus TOP 10 videos de mejor desempeño y genera:
- **10 ideas nuevas** de videos relacionados
- **Títulos optimizados** con palabras clave
- **Guiones básicos** de 5 minutos
- **Estrategia de publicación** (timing, formato)
- **Hooks de apertura** que funcionan

---

## 🔄 Flujo de Trabajo

```
Entrada: Top 10 Videos del Canal
    ↓
[Analizar títulos, descripciones, temas]
    ↓
[Extraer palabras clave comunes]
    ↓
[Claude API: Generar 10 ideas nuevas]
    ↓
[Claude API: Crear títulos para cada idea]
    ↓
[Claude API: Escribir hooks de apertura]
    ↓
[Google Docs: Guardar como documento]
    ↓
[Salida: Documento con ideas + briefing]
```

---

## 🎯 Ejemplo de Output

```
GENERADOR DE IDEAS - YouTube Channel
Fecha: 29 Julio, 2026

ANÁLISIS DE TOP 10 VIDEOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Palabras clave comunes:
- Agentes de IA (3 videos)
- WhatsApp (5 videos)
- GoHighLevel (4 videos)
- Automatización (7 videos)
- Clínicas/Consultorios (6 videos)

Temas trending en tu canal:
1. Automatización con IA ⭐⭐⭐
2. WhatsApp + Bots ⭐⭐⭐
3. Vendedores IA ⭐⭐⭐
4. Herramientas (n8n, Make) ⭐⭐
5. Casos reales de clínicas ⭐⭐

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDEAS PARA GRABAR (10):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. "Agente WhatsApp que CIERRA VENTAS automático"
   Hook: "Sin tocar el teléfono, este bot cierra 5 ventas por día"
   Guion: [5 min briefing]
   Publicar: Lunes (alto engagement)

2. "GoHighLevel + Claude = Tu equipo de ventas IA"
   Hook: "Conecté 2 herramientas y se triplicaron mis leads"
   Guion: [5 min briefing]
   Publicar: Miércoles

... (8 ideas más)

ESTRUCTURA RECOMENDADA:
- Hook: 15 segundos (impactante)
- Introducción: 30 segundos
- Demostración: 2 minutos
- Caso real: 1.5 minutos
- CTA: 30 segundos
```

---

## 🛠️ Herramientas Necesarias

### 1. Claude API
- **Plan:** Pay-as-you-go (~$0.10 por generación)
- **Necesidad:** Análisis y generación de ideas
- **Setup:** 10 min

### 2. Google Docs API
- **Necesidad:** Guardar ideas como documento
- **Setup:** 15 min

### 3. Make.com
- **Necesidad:** Orquestar flujo
- **Setup:** 30 min

---

## 📝 Pasos de Implementación

### Paso 1: Crear Prompt Maestro (30 min)

```
Eres un experto en estrategia de contenido YouTube para negocios de IA y automatización.

Analiza estos 10 videos más populares del canal:

{TOP_10_VIDEOS}

TAREA 1: Identifica
- Palabras clave comunes
- Temas que funcionan
- Patrones en títulos

TAREA 2: Genera 10 ideas nuevas
Cada idea debe:
- Relacionarse con los temas top
- Ser diferente a los 10 videos actuales
- Tener potencial viral para tu audiencia
- Ser grabable en 1 sesión

TAREA 3: Para cada idea, crea:
- Título optimizado (60 caracteres max)
- Hook de apertura (15-30 segundos)
- Guion básico (5 puntos clave)
- Día recomendado de publicación
- Duración estimada

FORMATO DE SALIDA:
```
# Idea [Número]
**Título:** [Título optimizado]

**Hook:** [Hook que engancha]

**Guion:**
1. Punto 1
2. Punto 2
3. Punto 3
4. Punto 4
5. Punto 5

**Publicar:** [Día]
**Duración:** [Minutos]
**Similitud a:**[Video más similar]
```

Ahora, genera las 10 ideas:
```

### Paso 2: Configurar Make.com (1 hora)

**Flujo en Make.com:**

```
1. Trigger: Manual o Scheduled (Semanalmente)

2. HTTP: GET YouTube API
   └─ Obtener TOP 10 videos (data/metrics.json)

3. Text Aggregator
   └─ Formatear datos para Claude

4. Claude API: Análisis
   └─ Input: Datos de 10 videos
   └─ Output: Análisis de temas

5. Claude API: Generación de ideas
   └─ Input: Análisis + Prompt maestro
   └─ Output: 10 ideas con títulos y hooks

6. Google Docs: Crear documento
   └─ Guardar ideas en Drive

7. Email: Notificar
   └─ "10 ideas nuevas listas para grabar"
```

### Paso 3: Crear Documento Template (15 min)

**En Google Drive:**
- Crear documento: "Ideas de Videos - [FECHA]"
- Plantilla con secciones:
  - Análisis de top videos
  - Palabras clave trending
  - 10 Ideas (con formato arriba)
  - Calendario de publicación

### Paso 4: Integrar Make.com → Google Docs (30 min)

```javascript
// Esto lo configuras en Make.com
1. Crear Google Doc automáticamente
2. Llenar con template
3. Reemplazar {CONTENIDO} con output de Claude
4. Compartir documento
5. Enviar link por email
```

---

## 💡 Tips de Optimización

### Mejora el Prompt
```
Agregar context adicional:
- Industria específica (IA, Automatización)
- Público objetivo (Dueños de clínicas, agencias)
- Tiempo de duración preferido (15-20 min)
- Tipo de contenido (tutorial, caso real, opinión)
```

### Filtrar Ideas
```
De las 10 ideas, selecciona 5:
- Que tengan más views potencial
- Que sean distintas entre sí
- Que puedas grabar pronto
- Que se alineen con tu estrategia
```

### Reutilizar Ideas
```
De cada idea, puedes generar:
- 1 video de YouTube
- 3-5 clips para TikTok/Reels
- 5-7 posts para LinkedIn
- Email para tu lista
```

---

## 📊 Ejemplo de Tabla (Google Sheets)

| # | Idea | Título | Views Potencial | Dificultad | Prioridad |
|---|---|---|---|---|---|
| 1 | Agente WhatsApp | Hook impactante... | Alto | Baja | 🔴 |
| 2 | GoHighLevel Claude | Conexión 2 tools... | Muy Alto | Media | 🔴 |
| 3 | Automatización clínica | Caso real... | Medio | Baja | 🟡 |
| ... | ... | ... | ... | ... | ... |

---

## 💰 Costo

| Herramienta | Costo | Frecuencia |
|---|---|---|
| Claude API | ~$0.20 | Semanal |
| Google Docs API | Free | Semanal |
| Make.com | Free | Semanal |
| **TOTAL** | **~$0.20** | **Por semana** |

---

## ✅ Checklist

- [ ] Prompt maestro creado y testeado
- [ ] Make.com configurado
- [ ] Claude API key integrada
- [ ] Google Docs conectada
- [ ] Template de documento creado
- [ ] Test generando 10 ideas
- [ ] Revisar calidad de ideas
- [ ] Ajustar prompt si es necesario
- [ ] Programar ejecución semanal
- [ ] Documentar mejores ideas

---

## 🔧 Mejoras Futuras

**Fase 2:**
- [ ] Analizar transcripciones de videos top
- [ ] Extraer segmentos más populares
- [ ] Basarse en eso para generar ideas

**Fase 3:**
- [ ] Integrar con Analytics avanzado
- [ ] Predecir qué ideas tendrán más views
- [ ] Auto-publicar en calendarios

---

**Siguiente:** [Transcripción + Análisis](./03_transcripcion_analisis.md)

