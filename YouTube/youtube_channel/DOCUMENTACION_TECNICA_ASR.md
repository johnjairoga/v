# 📚 Documentación Técnica: Pipeline ASR

**Para:** Desarrolladores / Mantenimiento futuro  
**Script:** `descargar_y_transcribir_audio.py`  
**Fecha:** 2026-07-29

---

## 📦 Estructura del Script

### Imports y Configuración Inicial

```python
import os, sys, re, json, time, argparse
from pathlib import Path
from typing import Optional, Tuple, List
from dataclasses import dataclass
from datetime import datetime

import yt_dlp
from faster_whisper import WhisperModel
import imageio_ffmpeg
```

**Variables globales constantes:**
- `BASE_DIR`: Ruta raíz del repo (`Path(__file__).parent.parent`)
- `AUDIO_DIR`: `videos de youtube/audio_mp3/`
- `TRANSCRIPTS_DIR`: `videos de youtube/transcripciones_top_videos/`
- `METRICS_FILE`: `youtube_channel/data/metrics.json`

**Fix de encoding (Windows):**
```python
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

---

## 🔧 Clases y Dataclasses

### `ValidacionVideo` (dataclass)

Resultado de la validación de un video usando yt-dlp metadata.

```python
@dataclass
class ValidacionVideo:
    ok: bool                          # True si pasa validación
    duracion_real_seg: Optional[int]  # Duración en segundos (o None si no se pudo determinar)
    motivo_skip: Optional[str]        # Razón por la que se saltó (o None si ok=True)
    live_status: Optional[str]        # 'is_live', 'was_live', 'not_live', o None
```

---

## 🔨 Funciones Principales

### `cargar_top_n_videos(n: int = 10) -> List[dict]`

**Propósito:** Lee `metrics.json` y retorna los top N videos ordenados por `view_count`.

**Entrada:**
- `n` (int, default 10): Cantidad de videos a retornar

**Salida:**
- List[dict]: Lista de hasta N dicts con claves `video_id`, `title`, `view_count`, `duration`, etc.

**Excepciones:**
- Si `metrics.json` no existe o no es JSON válido, imprime error y exit(1)

**Notas:**
- Ordena por `view_count` descendente
- No filtra anomalías aquí; eso lo hace `validar_video_ytdlp()`

---

### `validar_video_ytdlp(video_id: str, min_dur: int = 20, max_dur: int = 10800) -> ValidacionVideo`

**Propósito:** Valida que el video sea descargable usando yt-dlp en modo metadata-only.

**Entrada:**
- `video_id` (str): ID del video (ej. "u-RlV46QSJY")
- `min_dur` (int, default 20): Duración mínima en segundos (atrapa shorts/imágenes)
- `max_dur` (int, default 10800 = 3 horas): Duración máxima (atrapa livestreams mal parseados)

**Salida:**
- `ValidacionVideo` con `ok=True` si pasa todas las validaciones

**Reglas de validación:**

1. **Sin duración:** `duracion is None` → `ok=False`, skip "No se pudo determinar duración real"
2. **Livestream:** `live_status in ('is_live', 'was_live')` → `ok=False`, skip "Posible livestream"
3. **Duración anómala:** `duracion > max_dur` → `ok=False`, skip "Duración anómala: {dur}s (> {max_dur}s máximo)"
4. **Muy corto:** `duracion < min_dur` → `ok=False`, skip "Video demasiado corto / posible imagen/short"
5. **Otro error:** Excepción al validar → `ok=False`, skip "Error validando: {error_msg}"

**Notas:**
- Usa `yt_dlp.YoutubeDL({"quiet": True, "skip_download": True})` → no descarga nada, solo metadata
- Socket timeout: 30 segundos

---

### `descargar_audio(video_id: str, output_dir: Path = AUDIO_DIR) -> Optional[Path]`

**Propósito:** Descarga el audio del video y lo convierte a MP3.

**Entrada:**
- `video_id` (str): ID del video
- `output_dir` (Path, default `AUDIO_DIR`): Dónde guardar el MP3

**Salida:**
- `Path` al archivo MP3 creado
- `None` si falla

**Proceso:**
1. Si `output_dir/{video_id}.mp3` ya existe → retorna esa ruta (reutiliza)
2. Obtiene el path de ffmpeg vía `imageio_ffmpeg.get_ffmpeg_exe()`
3. Usa `yt_dlp` con opciones:
   - `format: 'bestaudio/best'` → descarga solo audio
   - `postprocessors: FFmpegExtractAudio` → convierte a MP3, 192 kbps
   - `outtmpl: '{video_id}.%(ext)s'`
4. Verifica que el archivo exista; retorna ruta o None

**Excepciones:**
- Si `yt_dlp` falla (descarga, conversión), atrapa la excepción, imprime error, retorna None

**Notas:**
- No sobrescribe MP3s existentes (para re-ejecutar sin perder trabajo)
- FFmpeg embebido en `imageio-ffmpeg` → no requiere PATH del sistema

---

### `transcribir_audio(mp3_path: Path, whisper_model: WhisperModel, idioma: str = 'es') -> Tuple[str, List[dict]]`

**Propósito:** Transcribe el MP3 usando faster-whisper.

**Entrada:**
- `mp3_path` (Path): Ruta al archivo MP3
- `whisper_model` (WhisperModel): Modelo cargado (pasado desde `procesar_pipeline`)
- `idioma` (str, default 'es'): Código de idioma

**Salida:**
- Tupla: `(texto_completo, segmentos_list)`
  - `texto_completo` (str): Texto limpio y concatenado
  - `segmentos_list` (List[dict]): Cada dict incluye `start`, `end`, `text`

**Proceso:**
1. Llama a `whisper_model.transcribe(mp3_path, language=idioma, beam_size=5, best_of=1)`
2. Convierte generador de segmentos a lista
3. Concatena todos los textos con espacios
4. Retorna (texto, segmentos)

**Excepciones:**
- Si la transcripción falla, atrapa excepción, imprime error, retorna ("", [])

**Notas:**
- `beam_size=5`: parámetro de búsqueda (balance entre precisión y velocidad)
- `best_of=1`: desactiva re-evaluación (acelera en CPU)
- El modelo debe ser cargado **una sola vez** fuera del loop (mejora performance)

---

### `generar_markdown_asr(...) -> str`

**Propósito:** Genera el contenido Markdown de la transcripción.

**Entrada:**
- `video` (dict): Video dict con keys `title`, `video_id`, etc.
- `video_id` (str): Video ID
- `transcripcion` (str): Texto completo transcrito
- `modelo_usado` (str): Nombre del modelo (ej. "small")
- `duracion_real_seg` (int): Duración en segundos
- `idioma` (str, default 'es'): Idioma

**Salida:**
- str: Contenido Markdown formateado

**Estructura del template:**
```markdown
# Transcripción: {titulo}

**Video:** [{titulo}](https://www.youtube.com/watch?v={video_id})
**Video ID:** {video_id}
**Descargado:** {timestamp}
**Origen:** Transcripción local (faster-whisper, modelo "{modelo_usado}") — ⚠️ NO son subtítulos oficiales...
**Duración real (validada vía yt-dlp):** {duracion_min}m {duracion_seg}s
**Idioma:** {idioma}

---

## 📝 Transcripción Completa

{transcripcion}

---

## 📊 Estadísticas

- **Palabras:** {num_palabras}
- **Caracteres:** {num_caracteres}
- **Duración audio:** {duracion_min}m {duracion_seg}s
- **Párrafos:** {num_parrafos}

---

## 🚀 Próximos Pasos

1. Analizar con Claude
2. Crear Blog Post
3. LinkedIn Article
4. Threads de Twitter
5. Clips Automáticos

---
```

**Notas:**
- Incluye disclaimer claro: ASR, no official, puede contener errores
- Metadatos incluyen duración real (validada vía yt-dlp), no la corrupta de metrics.json
- Calcula estadísticas: palabras, caracteres, párrafos

---

### `procesar_pipeline(...)`

**Propósito:** Orquesta el flujo completo.

**Parámetros:**
- `top_n` (int, default 10): Cantidad de videos a procesar
- `model_size` (str, default 'small'): Tamaño del modelo Whisper
- `keep_audio` (bool, default True): Guardar MP3s después de transcribir
- `skip_existing` (bool, default True): Saltar videos ya transcriptos
- `min_dur`, `max_dur` (int): Rangos de duración para validación
- `incluir_anomalias` (bool, default False): Procesar videos fuera de rango
- `idioma` (str, default 'es'): Idioma para transcripción

**Flujo:**

1. **Imprimir encabezado y config**
2. **Cargar top N videos** vía `cargar_top_n_videos()`
3. **Inicializar Whisper** una sola vez: `WhisperModel(model_size, device="cpu", compute_type="int8")`
4. **Loop por cada video:**
   - Imprimir: `[idx/N] 📺 Título (views)`
   - Chequear si ya existe transcripción: si yes y `skip_existing=True` → saltar
   - Validar con `validar_video_ytdlp()`
   - Si `not ok` y `not incluir_anomalias` → saltar con reporte
   - Descargar audio con `descargar_audio()`
   - Transcribir con `transcribir_audio()`
   - Generar Markdown con `generar_markdown_asr()`
   - Guardar `.md` file en `TRANSCRIPTS_DIR`
   - Opcionalmente eliminar MP3 si `not keep_audio`
   - Acumular stats (tiempo, contador de éxitos/saltos)
5. **Imprimir resumen final:**
   - Procesados, saltados, errores
   - Razones de salto con conteos
   - Tiempo total y promedio por video
   - Ubicaciones de output

---

### `main()`

**Propósito:** Entrada point. Parsea argumentos CLI y llama `procesar_pipeline()`.

**Argumentos CLI:**
```
--top N                    Cantidad de videos (default 10)
--model {tiny,base,small,medium}  Modelo Whisper (default small)
--keep-audio               Guardar MP3s (default True)
--delete-audio             Eliminar MP3s (action='store_false' dest='keep_audio')
--incluir-anomalias        Procesar videos fuera de rango (default False)
--idioma LANG              Idioma para transcripción (default 'es')
```

---

## 💡 Decisiones de Diseño

### 1. **Validación con yt-dlp, no metrics.json**

**Por qué:** `metrics.json` tiene bugs (duración de 42 días, 27 días para livestreams). yt-dlp es la verdad.

**Costo:** ~1 segundo adicional por video (metadata-only, sin descargar).

### 2. **MP3 guardados por defecto**

**Por qué:** 
- 100-150 MB es trivial en 372 GB libres
- Permite re-transcripción futura sin re-descargar
- Usuario puede `--delete-audio` si quiere

### 3. **Modelo `small` como default**

**Por qué:**
- 500 MB cachea localmente
- ~5 min/video en CPU (razonable)
- Muy buena precisión en español técnico
- `medium` sería mejor pero requiere ~5 GB RAM (riesgoso en 8 GB total)

### 4. **Descarga solo audio, no video**

**Por qué:** 
- Video completo ~50-200 MB por video = 500-2000 MB para 10 videos
- Audio solo ~10-15 MB por video = 100-150 MB para 10 videos
- 10x menos bandwidth, sin pérdida (Whisper solo necesita audio)

### 5. **Idempotencia (skip existentes)**

**Por qué:**
- Permite pausar/reanudar sin perder trabajo
- Permite cambiar configuración y re-ejecutar (solo recomputa nuevos)
- Usuario puede force-recompute borrando archivos `.md` específicos si lo necesita

### 6. **Disclaimer claro en cada transcripción**

**Por qué:** ASR no es perfecto (~95-99% en español). Usuarios deben saber que:
- No son subtítulos oficiales de YouTube
- Puede haber errores (sobre todo en nombres propios, anglicismos)
- Es mejor para análisis general que para citas verbatim

---

## 🧪 Testing / Verificación

### Test 1: Livestream Archivado
```bash
python descargar_y_transcribir_audio.py --top 1
```
Resultado esperado: Se salta `wizX-zWiWio` (livestream no disponible).

### Test 2: Post de Imagen
```bash
python descargar_y_transcribir_audio.py --top 10
```
Resultado esperado: Se salta `9M5utoPygFk` (5 segundos, muy corto).

### Test 3: Idempotencia
```bash
python descargar_y_transcribir_audio.py --top 5  # Primera vez
python descargar_y_transcribir_audio.py --top 5  # Segunda vez
```
Resultado esperado: Segunda ejecución saltea todos los 5 (ya existen transcripciones).

### Test 4: Forzar re-proceso
```bash
# Borra una transcripción específica
rm 'videos de youtube/transcripciones_top_videos/ASR_02_*.md'

# Re-ejecuta
python descargar_y_transcribir_audio.py --top 5
```
Resultado esperado: Solo procesa ese 1 video de nuevo, salta los otros 4.

---

## 📝 Futuras Mejoras (Ideas, no implementadas)

1. **Modelo configurable por video:** algunos videos podrían necesitar `tiny` (música), otros `medium` (técnico)
2. **Batch processing con multiprocessing:** transcribir 2-3 videos en paralelo (si suficiente RAM)
3. **Diarización:** detectar cambios de locutor (quién habla)
4. **Subtítulos SRT automáticos:** generar `.srt` además de `.md` para integrar en YouTube
5. **Web UI:** interfaz simple en Flask/Streamlit en lugar de CLI
6. **Caché de palabras clave:** extraer automáticamente keywords de cada transcripción
7. **Integración con Make.com/n8n:** triggerear descarga/transcripción automáticamente

---

## 🔗 Referencias

- **yt-dlp docs:** https://github.com/yt-dlp/yt-dlp
- **faster-whisper docs:** https://github.com/SYSTRAN/faster-whisper
- **imageio-ffmpeg:** https://pypi.org/project/imageio-ffmpeg/

---

**Documento generado:** 2026-07-29  
**Versión del script:** 1.0  
**Status:** Production-ready ✅
