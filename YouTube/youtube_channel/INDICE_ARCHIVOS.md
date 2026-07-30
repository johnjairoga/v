# 📑 Índice de Archivos del Proyecto

**Fecha:** 2026-07-29  
**Proyecto:** Pipeline de Transcripción YouTube - 50 Videos

---

## 🚀 Scripts Principales

| Archivo | Ubicación | Propósito | Estado |
|---------|-----------|----------|--------|
| `descargar_y_transcribir_audio.py` | `youtube_channel/` | Script principal de descarga + transcripción | ✅ Activo |
| `requirements.txt` | `youtube_channel/` | Dependencias (yt-dlp, ffmpeg, whisper) | ✅ Actualizado |

---

## 📋 Documentos de Plan y Estado

| Documento | Ubicación | Propósito |
|-----------|-----------|----------|
| `PLAN_MAESTRO_PROYECTO.md` | `youtube_channel/` | Plan completo con fases, checklist, timeline |
| `ESTADO_PROCESAMIENTO_VIDEOS.md` | `youtube_channel/` | Listado detallado de 50 videos (qué falta, qué se hizo) |
| `VALIDACION_LISTA_VIDEOS.md` | `youtube_channel/` | Confirmación: todo sincronizado con lista maestra |
| `VIDEOS_PROCESADOS_CHECKLIST.txt` | `youtube_channel/` | Resumen rápido (6 hechos, 3 saltados, 1 error, 40 pendientes) |
| `PLAN_VALIDACION_TOP10.md` | `youtube_channel/` | Detalles de validación Fase 1 |
| `PLAN_ESCALADO_50_VIDEOS.md` | `youtube_channel/` | Instrucciones para Fase 2 |
| **INDICE_ARCHIVOS.md** | `youtube_channel/` | **Este archivo - índice de todo** |

---

## 📊 Documentos de Análisis (Anteriores)

| Documento | Ubicación | Propósito |
|-----------|-----------|----------|
| `DATOS_EXTRAIDOS_47_VIDEOS.md` | `youtube_channel/` | Análisis anterior de 47 videos (actualizado) |
| `RESUMEN_DESCARGA_TRANSCRIPCIONES.md` | `youtube_channel/` | Resumen de intento anterior con Baoyu |
| `USANDO_BAOYU_SKILL.md` | `youtube_channel/` | Documentación del intento con skill Baoyu |
| `CAPACIDADES_Y_LIMITACIONES.md` | `youtube_channel/` | Limitaciones conocidas (será actualizado) |

---

## 📁 Carpetas de Datos

| Carpeta | Ubicación | Contenido |
|---------|-----------|----------|
| `transcripciones_top_videos/` | `videos de youtube/` | 6 archivos `.md` (transcripciones ASR) |
| `audio_mp3/` | `videos de youtube/` | 6 archivos `.mp3` (audios descargados) |

---

## 📖 Listas Maestras

| Archivo | Ubicación | Contenido |
|---------|-----------|----------|
| `TODOS_LOS_VIDEOS_CON_LINKS.md` | Raíz (`/`) | Lista de 50 videos con links (fuente de verdad) |

---

## 🎯 Referencia Rápida

### Comando Próxima Fase
```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --all
```

### Documentos Por Tipo

**Para ver dónde estamos:**
- `PLAN_MAESTRO_PROYECTO.md` ← LEE ESTO PRIMERO

**Para ver qué falta:**
- `ESTADO_PROCESAMIENTO_VIDEOS.md` (detallado)
- `VIDEOS_PROCESADOS_CHECKLIST.txt` (rápido)

**Para validar que está sincronizado:**
- `VALIDACION_LISTA_VIDEOS.md`

**Para próximos pasos:**
- `PLAN_ESCALADO_50_VIDEOS.md`

---

## 📊 Resumen de Estado

```
✅ Completado: 6 videos (12%)
⏭️  Saltados: 3 videos
❌ Error: 1 video
⏳ Pendientes: 40 videos (88%)

Próximo paso: Ejecutar con --all (Fase 2)
Tiempo estimado: 5-7 horas
```

---

**¿Necesitas algo específico? Usa este índice como referencia.**
