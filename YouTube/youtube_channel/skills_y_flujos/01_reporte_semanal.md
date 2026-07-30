# Skill 1: Reporte Semanal Automático

**Prioridad:** ⭐⭐⭐ ALTA  
**Tiempo estimado:** 2 horas  
**Complejidad:** ⭐⭐ (Baja)  
**ROI:** Alto

---

## 📊 Qué hace

Ejecuta automáticamente cada lunes y genera un reporte con:
- Cambios en views, likes, comentarios desde la semana anterior
- Videos que subieron o bajaron de posición
- Tendencias (qué está funcionando)
- Resumen ejecutivo en tabla HTML/Sheets

---

## 🔄 Flujo de Trabajo

```
Lunes 9:00 AM
    ↓
[Make.com Trigger]
    ↓
[YouTube API] → Obtener métricas actuales
    ↓
[Google Sheets] → Buscar datos de semana anterior
    ↓
[Claude API] → Generar análisis
    ↓
[Google Sheets] → Guardar reporte
    ↓
[Email/Telegram] → Notificar al usuario
```

---

## 🛠️ Herramientas Necesarias

### 1. Make.com
- **Plan:** Free ($0)
- **Necesidad:** Orquestación del flujo
- **Setup:** 30 min

### 2. YouTube Data API
- **Ya configurada:** ✅ (lo hicimos)
- **Necesidad:** Obtener métricas semanales

### 3. Google Sheets
- **Necesidad:** Base de datos + reporte
- **Setup:** 15 min (crear hoja)

### 4. Claude API
- **Plan:** Pay-as-you-go (~$0.01 por reporte)
- **Necesidad:** Análisis inteligente
- **Setup:** 10 min (obtener API key)

---

## 📝 Pasos de Implementación

### Paso 1: Crear Google Sheet (15 min)

**Nombre:** `YouTube Channel Weekly Report`

**Hojas necesarias:**
1. `Weekly Data` → Datos semanales
2. `Historical` → Datos históricos
3. `Report Template` → Plantilla del reporte

**Columnas en "Weekly Data":**
```
Fecha | Video ID | Título | Views | Likes | Comentarios | Cambio_Views | Posición
```

### Paso 2: Configurar Make.com (1 hora)

**Módulos del flujo:**
1. **Trigger:** Weekly Schedule (Lunes 9:00 AM)
2. **HTTP:** GET YouTube API (obtener videos)
3. **Google Sheets:** Agregar datos nuevos
4. **Google Sheets:** Buscar datos previos
5. **Claude API:** Generar análisis
6. **Google Sheets:** Guardar análisis
7. **Email/Telegram:** Enviar notificación

**Configuración básica:**
```
Trigger: Schedule (Recurrent)
  └─ Lunes, 9:00 AM
  
HTTP Module:
  └─ URL: https://www.googleapis.com/youtube/v3/channels?part=statistics
  └─ Auth: Bearer [TU_TOKEN]
  
Claude Module:
  └─ Prompt: "Analiza estos datos de YouTube..."
  └─ Model: claude-opus-5
  
Email Module:
  └─ To: tu_email@ejemplo.com
  └─ Subject: "Reporte Semanal YouTube"
```

### Paso 3: Crear Prompt para Claude (15 min)

```
Eres un analista de contenido YouTube. 
Recibiste estos datos de videos:

[DATOS ACTUALES]
- Total views: {views}
- Total likes: {likes}
- Cambio semana anterior: {cambio_views}%

[VIDEOS TOP 5]
{videos_top}

[CAMBIOS NOTABLES]
{cambios}

Genera un análisis ejecutivo en 3 puntos:
1. Lo que funcionó esta semana
2. Lo que bajó en desempeño
3. Recomendación para próxima semana

Sé conciso y accionable.
```

### Paso 4: Automatizar Google Sheets (30 min)

**Apps Script en Google Sheets:**
```javascript
function enviarReporte() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var datos = sheet.getRange("A2:H100").getValues();
  
  // Enviar a Make.com webhook
  var payload = {
    fecha: new Date(),
    datos: datos
  };
  
  UrlFetchApp.fetch("TU_MAKE_WEBHOOK_URL", {
    method: "post",
    payload: JSON.stringify(payload)
  });
}
```

---

## 📊 Ejemplo de Output

```
REPORTE SEMANAL - YouTube Channel
Semana: 29 Julio - 4 Agosto, 2026

RESUMEN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Views:     38,295 (+2,145 vs semana anterior)
Total Likes:        948 (+42)
Total Comentarios:  147 (-5)

TOP 3 VIDEOS ESTA SEMANA:
1. Un Agente IA Vendedor... (9,227 views) ↑ 500 views
2. Crear Landing Page... (3,963 views) ↑ 200 views
3. n8n GRATIS... (3,536 views) ↓ 50 views

ANÁLISIS:
✓ Lo que funcionó: Videos sobre "Agentes de IA" 
✓ Baja en comentarios: Investigar posible problema con comentarios
✓ Recomendación: Grabar 3 videos sobre "Automatización con IA"

PRÓXIMOS PASOS:
- Habilitar subtítulos en top 5 videos
- Crear playlist "Agentes de IA"
- Optimizar descripciones de videos bajo-rendimiento
```

---

## 💰 Costo

| Herramienta | Costo | Frecuencia |
|---|---|---|
| Make.com | Free | Semanal |
| YouTube API | Free | Semanal |
| Google Sheets | Free | Semanal |
| Claude API | ~$0.05 | Semanal |
| **TOTAL** | **~$0.20** | **Por semana** |

---

## ✅ Checklist de Setup

- [ ] Google Sheet creado y compartido
- [ ] Make.com cuenta creada
- [ ] YouTube API conectada a Make
- [ ] Google Sheets conectada a Make
- [ ] Claude API key generada
- [ ] Prompt de Claude personalizado
- [ ] Trigger de horario configurado
- [ ] Email/Telegram de notificación configurado
- [ ] Test del flujo realizado
- [ ] Datos guardados correctamente

---

## 🔧 Troubleshooting

**"No se obtienen datos de YouTube"**
- [ ] Verificar que el token de YouTube API es válido
- [ ] Revisar que el channel ID es correcto

**"Tabla de Google Sheets no se actualiza"**
- [ ] Revisar permisos de Make.com en Google Sheets
- [ ] Verificar que la hoja no tiene protección

**"Claude no genera análisis"**
- [ ] Verificar API key de Claude
- [ ] Revisar que el prompt no está vacío

---

## 📚 Recursos

- [Make.com - YouTube Integration](https://www.make.com/en/integrations/youtube)
- [Claude API Docs](https://docs.anthropic.com/)
- [Google Sheets API](https://developers.google.com/sheets)

---

**Siguiente:** Una vez este flujo esté funcionando, pasamos a [Generador de Ideas](./02_generador_ideas.md)
