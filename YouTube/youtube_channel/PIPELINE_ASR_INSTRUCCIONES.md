# 🎬 Pipeline Local: Transcripción ASR (Audio → Texto)

**Fecha:** 2026-07-29  
**Estado:** ✅ Implementado  
**Herramienta:** faster-whisper (local, gratuito, sin GPU)

---

## 📋 Resumen

Script que descarga los **Top 10 videos** del canal, los convierte a MP3, y **transcribe el audio localmente** usando un modelo de reconocimiento de voz (ASR) gratuito, sin depender de subtítulos de YouTube ni de APIs pagas.

---

## ⚡ Quick Start

### 1. Instalar dependencias (primera vez)

```bash
cd youtube_channel
pip install -r requirements.txt
```

Esto instala: `yt-dlp`, `imageio-ffmpeg`, `faster-whisper` (y sus dependencias previas).

### 2. Ejecutar el pipeline

**Opción A: Modo básico (Top 10, modelo small)**
```bash
python descargar_y_transcribir_audio.py
```

**Opción B: Ajustar número de videos**
```bash
python descargar_y_transcribir_audio.py --top 5
```

**Opción C: Modelo más rápido pero menos preciso**
```bash
python descargar_y_transcribir_audio.py --model base
```

**Opción D: Eliminar MP3s después de transcribir (para ahorrar espacio)**
```bash
python descargar_y_transcribir_audio.py --delete-audio
```

**Opción E: Incluir videos anómalos (livestreams, posts de imagen)**
```bash
python descargar_y_transcribir_audio.py --incluir-anomalias
```

---

## 🎯 Cómo Funciona

### Paso 1: Validación
Verifica que el video tenga duración real y no sea un livestream o post de imagen.

- ✅ Normal: 20s a 3 horas
- ⏭️ Se salta: livestream o duración > 3h (probable livestream archivado)
- ⏭️ Se salta: duración < 20s (probable imagen/short post)

**Nota:** El Top 10 real según `metrics.json` incluye 2 videos anómalos:
1. `wizX-zWiWio` (9,227 views) — Posible livestream (42 días de duración)
2. `9M5utoPygFk` (2,714 views) — Post de imagen (5 segundos)

Estos **se saltan automáticamente** para evitar descargar/procesar contenido que no tiene voz. Usa `--incluir-anomalias` si quieres procesarlos de todas formas.

### Paso 2: Descarga de Audio
Usa `yt-dlp` para descargar solo el audio (no el video completo), lo que ahorra bandwidth.

- Formato: mejor audio disponible
- Conversión: MP3 192 kbps
- Guardado: `videos de youtube/audio_mp3/{video_id}.mp3`

**Reutilización:** Si el MP3 ya existe, se reutiliza (no re-descarga).

### Paso 3: Transcripción
Usa **faster-whisper** (modelo local, CPU-only, sin GPU).

- Modelo por defecto: `small` (~500 MB, descargado una sola vez)
- Lenguaje: español por defecto
- Motores disponibles: `tiny` (rápido, menos preciso), `base`, `small` (recomendado), `medium` (lento, muy preciso)

### Paso 4: Guardado
Guarda la transcripción en formato Markdown:

```
videos de youtube/transcripciones_top_videos/
  ├─ ASR_01_u-RlV46QSJY_Crear_Landing_Page_con_IA.md
  ├─ ASR_02_pQo--gSE9e4_n8n_GRATIS.md
  └─ ...
```

Cada archivo incluye:
- Transcripción completa
- Metadatos (duración, modelo usado, timestamp)
- Nota: "⚠️ ASR local, no subtítulos oficiales, puede contener errores"
- Estadísticas (palabras, caracteres, duración)

---

## ⏱️ Tiempo Estimado

| Acción | Duración | Notas |
|--------|----------|-------|
| Instalación (primera vez) | ~2-5 min | `pip install` solo |
| Descarga modelo Whisper | ~10 min | Una sola vez, se cachea |
| Descarga + conversión audio | ~20-30 seg/video | Depende de conexión |
| Transcripción | ~3-6 min/video | CPU-only en este equipo |
| **Total (Top 10, modo basic)** | **~45-90 min** | Mayormente desatendido |

---

## 💻 Requisitos del Sistema

- Python 3.6+
- ~500 MB disco (modelo Whisper cachea, se descarga 1 sola vez)
- ~100-150 MB disco (MP3s de 10 videos, ~8-10 min cada uno)
- ~1-2 GB RAM disponible durante transcripción
- CPU: cualquiera (sin GPU necesaria)

**Nota:** El script usa CPU intensivamente durante ~45-90 min. La compu se notará más lenta mientras corre. Puedes dejarlo correr de noche.

---

## 🚀 Opciones de Línea de Comandos

```bash
python descargar_y_transcribir_audio.py [OPCIONES]
```

| Opción | Valor Default | Descripción |
|--------|-----------------|------------|
| `--top N` | 10 | Cantidad de videos a procesar |
| `--model {tiny,base,small,medium}` | small | Tamaño del modelo Whisper |
| `--keep-audio` | True | Guardar MP3s después de transcribir |
| `--delete-audio` | - | Eliminar MP3s (ahorra ~100 MB) |
| `--incluir-anomalias` | False | Procesar livestreams y vídeos cortos |
| `--idioma LANG` | es | Idioma para transcripción (ej. en, fr, etc.) |

---

## 📂 Estructura de Archivos

```
youtube_channel/
├─ descargar_y_transcribir_audio.py (NUEVO - este script)
├─ requirements.txt (ACTUALIZADO - con yt-dlp, imageio-ffmpeg, faster-whisper)
├─ data/
│  └─ metrics.json (fuente de ranking Top 10 por views)
│
videos de youtube/
├─ audio_mp3/ (NUEVA - MP3s descargados)
│  ├─ u-RlV46QSJY.mp3
│  ├─ pQo--gSE9e4.mp3
│  └─ ...
│
└─ transcripciones_top_videos/ (ACTUALIZADA - nuevas transcripciones ASR)
   ├─ ASR_01_u-RlV46QSJY_Crear_Landing_Page_con_IA.md
   ├─ ASR_02_pQo--gSE9e4_n8n_GRATIS.md
   ├─ ASR_03_dPIsXv0XhP4_CLAUDE_reemplazó_agencias.md
   └─ ...
```

**Nota:** Las transcripciones se prefijan con `ASR_` para distinguirlas de las basadas en captions (`DESCARGA_*`).

---

## 🔄 Idempotencia (Re-ejecutar sin problema)

- ✅ Si el MP3 ya existe → se reutiliza
- ✅ Si la transcripción ya existe → se salta el video
- ✅ Puedes pausar/reanudar el proceso sin perder progreso
- ✅ No descarga dos veces lo mismo

Ejemplo: si el script se detiene en video 5 de 10, la próxima vez saltará los 4 primeros y continuará del 5.

---

## ⚙️ Modelos Whisper: Comparativa

| Modelo | Tamaño | Velocidad | Precisión | RAM | Uso |
|--------|--------|-----------|-----------|-----|-----|
| `tiny` | 39 MB | ⚡⚡⚡ Muy rápido | 🎯 Básica | ~600 MB | Pruebas rápidas |
| `base` | 140 MB | ⚡⚡ Rápido | 🎯 Buena | ~900 MB | Balance |
| **`small`** | **500 MB** | **⚡ Moderado** | **🎯 Muy buena** | **~1.5 GB** | **RECOMENDADO** |
| `medium` | 1.5 GB | 🐢 Lento | 🎯 Excelente | **~3 GB** | Máx precisión (si tienes paciencia) |

**Recomendación:** `small` es el mejor balance para este equipo y contenido en español técnico.

---

## 🆘 Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'yt_dlp'`

```bash
pip install -r requirements.txt
```

### Error: `No module named 'faster_whisper'`

```bash
pip install faster-whisper
```

### Error: `Downloading model from Hugging Face...` (tarda mucho)

Es normal la primera vez. El modelo `small` (~500 MB) se descarga de Hugging Face y se cachea. Futuras ejecuciones reutilizarán la copia cacheada.

### El script es muy lento / usa mucho CPU

✅ Eso es normal. Transcripción de audio en CPU sin GPU es intrincadamente. Opciones:
1. Usa `--model base` (más rápido, menos preciso)
2. Usa `--model tiny` (muy rápido, precisión basic)
3. Corre de noche cuando no uses la compu

### YouTube bloqueó la descarga (403 / 429 error)

yt-dlp incluye reintentos automáticos. Si persiste:
1. Espera 5-10 minutos
2. Reinicia el script (reutilizará descargas existentes)
3. Prueba con `--model tiny` para iterar rápido mientras esperas

### El MP3 descargado es muy grande

Controla el bitrate en el script (línea ~150). Actualmente `preferredquality=192` (192 kbps). Bajarlo a 128 ahorra espacio pero reduce calidad.

---

## 📊 Ejemplo de Salida

```
======================================================================
🎬 PIPELINE: DESCARGA + TRANSCRIPCIÓN LOCAL (faster-whisper)
======================================================================

📋 Configuración:
  - Top N videos: 10
  - Modelo Whisper: small
  - Validación duración: 20s - 10800s (3h)
  - Incluir anomalías: False
  - Idioma: es
  - Guardar MP3s: True

📂 Cargando top 10 videos desde metrics.json...
✅ 10 videos cargados

🔧 Inicializando modelo Whisper 'small'...
✅ Modelo cargado

🎯 Procesando videos:
----------------------------------------------------------------------

[1/10] 📺 Crear Landing Page con IA... (3,963 views)
     ID: u-RlV46QSJY
  🔍 Validando...
  📥 Descargando audio de u-RlV46QSJY...
  ✅ Descargado: u-RlV46QSJY.mp3 (1.2 MB)
  🎤 Transcribiendo u-RlV46QSJY.mp3...
  ✅ Transcripción completada (4821 caracteres)
  ✅ Guardado: ASR_01_u-RlV46QSJY_Crear_Landing_Page_con_IA.md

[2/10] 📺 n8n GRATIS... (3,536 views)
     ID: pQo--gSE9e4
  🔍 Validando...
  ⏭️  Transcripción ya existe, omitido

[3/10] 📺 Un Agente IA Vendedor en WhatsApp... (9,227 views)
     ID: wizX-zWiWio
  🔍 Validando...
  ⏭️  Saltado: Duración anómala: 151211s (> 10800s máximo)

...

======================================================================
📊 RESUMEN FINAL
======================================================================
✅ Procesados: 7
⏭️  Saltados: 2
❌ Errores: 0

📋 Razones de salto:
   - Duración anómala: 2

⏱️  Tiempo total: 2145.3s (35.8 min)
   Promedio por video: 306.5s (5.1 min)

📁 Transcripciones guardadas en: transcripciones_top_videos/
🎵 MP3s guardados en: audio_mp3/

======================================================================
✨ ¡Listo!
======================================================================
```

---

## 🎯 Próximos Pasos Después de Transcribir

Una vez tengas las transcripciones en `.md`:

1. **Análisis con Claude** — Extrae palabras clave, resumen ejecutivo, tonalidad
2. **Generador de Ideas** — Identifica temas recurrentes para futuros videos
3. **Blog Posts** — Repurposea transcripciones en artículos
4. **SEO** — Extrae keywords de cada video para optimizar descripciones
5. **Clips Automáticos** — Segmenta el audio/video por tema y crea shorts

---

## ✨ Notes

- **No requiere GPU:** funciona en cualquier CPU moderna
- **Totalmente local:** no se sube nada a internet (excepto descargar modelo + videos de YouTube)
- **Gratuito:** sin APIs pagas, sin límites de transcripción
- **Configurable:** tamaño de modelo, idioma, número de videos

---

**¡Lista para ejecutar! 🚀**

```bash
python descargar_y_transcribir_audio.py
```
