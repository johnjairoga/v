# 📋 Plan de Validación: Top 10 Videos

**Fecha:** 2026-07-29  
**Objetivo:** Validar el pipeline funciona correctamente antes de escalar a 50 videos  
**Status:** 🔄 En progreso

---

## ✅ Cambios Realizados

### 1. **Nombres de Archivos Consistentes**
- **Antes:** 
  - Audio: `u-RlV46QSJY.mp3`
  - Transcripción: `01_Crear_Landing_Page_con_IA.md`
  - ❌ No se pueden asociar fácilmente

- **Ahora:**
  - Audio: `01_Crear_Landing_Page_con_IA.mp3`
  - Transcripción: `01_Crear_Landing_Page_con_IA.md`
  - ✅ Fácil asociación por nombre

### 2. **Actualización del Script**
✅ Función `descargar_audio()` modificada para recibir `idx` y `titulo`  
✅ Nombres de archivo ahora incluyen numeración y título  
✅ Búsqueda de archivos existentes funciona con nuevo formato

---

## 🧹 Preparación (IMPORTANTE)

### Paso 1: Limpiar carpetas antiguas

```bash
cd "c:\Users\John\Desktop\John Jairo\Youtube\v\v"

# Borrar archivos con formato antiguo
rmdir /s /q "videos de youtube\audio_mp3"
rmdir /s /q "videos de youtube\transcripciones_top_videos"

# Recrear carpetas vacías (el script las crea automáticamente)
mkdir "videos de youtube\audio_mp3"
mkdir "videos de youtube\transcripciones_top_videos"
```

O simplemente:
```powershell
Remove-Item -Path "c:\Users\John\Desktop\John Jairo\Youtube\v\v\videos de youtube\audio_mp3" -Recurse -Force
Remove-Item -Path "c:\Users\John\Desktop\John Jairo\Youtube\v\v\videos de youtube\transcripciones_top_videos" -Recurse -Force
```

---

## 🎯 Fase 1: Validación con Top 10

### Paso 2: Ejecutar con los primeros 10 videos

```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --top 10
```

**Tiempo estimado:** 60-90 minutos  
**CPU:** Alto (es normal, transcripción en CPU)

### Paso 3: Validación Manual

Cuando termine, verificar:

#### ✅ Carpeta `audio_mp3/` 
Debe tener archivos nombrados así:
```
01_Crear_Landing_Page_con_IA.mp3
02_n8n_GRATIS.mp3
03_CLAUDE_reemplazó_agencias.mp3
04_No_pagues_API_GoHighLevel.mp3
...
```

**Checkpoints:**
- ✅ 8-9 archivos MP3 (algunos videos se saltan por anomalías)
- ✅ Nombres claros con número + título
- ✅ Tamaño razonable (~10-15 MB cada uno)

#### ✅ Carpeta `transcripciones_top_videos/`
Debe tener archivos nombrados así:
```
01_Crear_Landing_Page_con_IA.md
02_n8n_GRATIS.md
03_CLAUDE_reemplazó_agencias.md
...
```

**Checkpoints:**
- ✅ 8-9 archivos `.md` (mismo número que MP3s)
- ✅ Nombres coinciden exactamente con los MP3s (sin extensión)
- ✅ Contenido legible (abre uno en editor de texto)

#### ✅ Validar Contenido de Transcripción

Abre uno de los `.md` y verifica:
```markdown
# Transcripción: [Título del video]

**Video:** [URL]
**Video ID:** [ID] ← Debe estar presente
**Descargado:** [Fecha/Hora]
**Origen:** Transcripción local (faster-whisper, modelo "small")
...

## 📝 Transcripción Completa

[Texto transcrito, debe ser legible en español]

## 📊 Estadísticas
- **Palabras:** [número]
- **Caracteres:** [número]
- **Duración audio:** [minutos]
- **Párrafos:** [número]
```

**Checkpoints:**
- ✅ Título correcto
- ✅ Video ID presente
- ✅ Texto en español legible
- ✅ Disclaimer claro: "⚠️ ASR local, no official, puede contener errores"
- ✅ Estadísticas calculadas

#### ✅ Verificar Asociación Audio-Transcripción

Para cada par verificar:
```
01_Crear_Landing_Page_con_IA.mp3  ↔ 01_Crear_Landing_Page_con_IA.md
02_n8n_GRATIS.mp3                  ↔ 02_n8n_GRATIS.md
03_CLAUDE_reemplazó_agencias.mp3  ↔ 03_CLAUDE_reemplazó_agencias.md
```

✅ Nombres idénticos (facilita programación futura para análisis)

---

## 📊 Resumen Esperado

```
======================================================================
📊 RESUMEN FINAL
======================================================================
✅ Procesados: 8
⏭️  Saltados: 2
❌ Errores: 0

📋 Razones de salto:
   - Duración anómala: 1 (livestream)
   - Video demasiado corto: 1 (imagen/short)

⏱️  Tiempo total: ~2400s (40 min)
   Promedio por video: ~300s (5 min)

📁 Transcripciones guardadas en: transcripciones_top_videos/
🎵 MP3s guardados en: audio_mp3/

======================================================================
```

---

## 🔍 Posibles Problemas y Soluciones

### Problema 1: "No se creó el archivo MP3"
**Causa:** Fallo en descarga o conversión  
**Solución:** 
- Verificar conexión a internet
- Verificar que ffmpeg está funcionando
- Re-ejecutar (el script es idempotente)

### Problema 2: "Transcripción vacía"
**Causa:** Problemas con Whisper  
**Solución:**
- Video muy silencioso o con música de fondo
- Ejecutar con `--model tiny` (más rápido, menos preciso)

### Problema 3: "Archivo ya existe"
**Causa:** Video ya fue procesado  
**Solución:**
- Es normal (idempotencia)
- Borra el archivo manualmente si quieres re-procesar
- O usa un segundo `--top 11` para procesar videos adicionales

### Problema 4: "Nombres de archivo muy largos"
**Causa:** Títulos muy largos  
**Solución:**
- Automático (se truncan a 60 caracteres)
- Siempre asociables por video_id en el contenido `.md`

---

## ✅ Checklist de Validación

- [ ] Carpeta `audio_mp3` limpia y vacía
- [ ] Carpeta `transcripciones_top_videos` limpia y vacía
- [ ] Ejecutar: `python descargar_y_transcribir_audio.py --top 10`
- [ ] 8-9 archivos MP3 descargados
- [ ] 8-9 archivos `.md` generados
- [ ] Nombres coinciden (ej. `01_...mp3` + `01_...md`)
- [ ] Contenido de transcripción legible en español
- [ ] Disclaimer presente en cada `.md`
- [ ] Estadísticas calculadas correctamente
- [ ] Resumen final dice 0 errores

---

## 🚀 Fase 2: Escalar a 50 Videos

Una vez validado todo (✅ todos los checkpoints), ejecutar:

```bash
python descargar_y_transcribir_audio.py --top 50
```

**Tiempo estimado:** 5-7 horas  
**Recomendación:** Ejecutar de noche o en fin de semana

---

## 📝 Notas

- El script es **idempotente**: puede pausarse y reanudarse sin perder progreso
- Si necesitas borrar y empezar de cero:
  ```bash
  rmdir /s /q "videos de youtube\audio_mp3"
  rmdir /s /q "videos de youtube\transcripciones_top_videos"
  ```
- El modelo Whisper se descarga ~500 MB la primera vez y se cachea
- CPU va a estar al 100% durante la transcripción (es normal)

---

**Status:** Listos para validación con Top 10 ✅
