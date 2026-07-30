#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipeline local: Descarga de video → MP3 → Transcripción con Whisper local
Procesa Top N videos del canal sin depender de subtítulos de YouTube.
"""

import os
import sys
import re
import json
import time
import argparse
from pathlib import Path
from typing import Optional, Tuple, List
from dataclasses import dataclass
from datetime import datetime

# Configurar encoding UTF-8 en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    import yt_dlp
    from faster_whisper import WhisperModel
    import imageio_ffmpeg
except ImportError as e:
    print(f"❌ Falta instalar dependencias: pip install yt-dlp imageio-ffmpeg faster-whisper")
    sys.exit(1)

BASE_DIR = Path(__file__).resolve().parent.parent
AUDIO_DIR = BASE_DIR / "videos de youtube" / "audio_mp3"
TRANSCRIPTS_DIR = BASE_DIR / "videos de youtube" / "transcripciones_top_videos"
METRICS_FILE = Path(__file__).resolve().parent / "data" / "metrics.json"

# Crear directorios si no existen
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class ValidacionVideo:
    ok: bool
    duracion_real_seg: Optional[int] = None
    motivo_skip: Optional[str] = None
    live_status: Optional[str] = None


def cargar_top_n_videos(n: Optional[int] = 10) -> List[dict]:
    """Lee metrics.json, ordena por view_count descendente, retorna top N o todos si n=None."""
    try:
        with open(METRICS_FILE, 'r', encoding='utf-8') as f:
            videos = json.load(f)

        # Ordenar por view_count descendente
        videos_sorted = sorted(videos, key=lambda v: v.get('view_count', 0), reverse=True)

        if n is None:
            return videos_sorted  # Retorna todos
        return videos_sorted[:n]
    except Exception as e:
        print(f"❌ Error cargando metrics.json: {e}")
        sys.exit(1)


def validar_video_ytdlp(video_id: str, min_dur: int = 20, max_dur: int = 10800) -> ValidacionVideo:
    """
    Valida el video usando yt-dlp sin descargar.
    Retorna duración real, live_status, y motivo de skip si aplica.
    """
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        duracion = info.get('duration')
        live_status = info.get('live_status')

        # Validaciones
        if duracion is None:
            return ValidacionVideo(
                ok=False,
                motivo_skip="No se pudo determinar duración real",
                live_status=live_status
            )

        if live_status in ('is_live', 'was_live'):
            return ValidacionVideo(
                ok=False,
                duracion_real_seg=duracion,
                motivo_skip=f"Posible livestream (live_status: {live_status})",
                live_status=live_status
            )

        if duracion > max_dur:
            return ValidacionVideo(
                ok=False,
                duracion_real_seg=duracion,
                motivo_skip=f"Duración anómala: {duracion}s (> {max_dur}s máximo)",
                live_status=live_status
            )

        if duracion < min_dur:
            return ValidacionVideo(
                ok=False,
                duracion_real_seg=duracion,
                motivo_skip=f"Video demasiado corto: {duracion}s (< {min_dur}s mínimo, posible imagen/short)",
                live_status=live_status
            )

        return ValidacionVideo(ok=True, duracion_real_seg=duracion, live_status=live_status)

    except Exception as e:
        return ValidacionVideo(
            ok=False,
            motivo_skip=f"Error validando: {str(e)[:80]}"
        )


def descargar_audio(video_id: str, idx: int, titulo: str, output_dir: Path = AUDIO_DIR) -> Optional[Path]:
    """
    Descarga audio del video y lo convierte a MP3.
    Retorna la ruta del archivo MP3, o None si falla.
    """
    # Limpiar título para usar en nombre de archivo
    titulo_limpio = re.sub(r'[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ\s\-]', '', titulo)
    titulo_limpio = titulo_limpio.strip()[:60]

    output_path = output_dir / f"{idx:02d}_{titulo_limpio}.mp3"

    # Si ya existe, reutilizar
    if output_path.exists():
        print(f"  📦 Usando MP3 existente: {output_path.name}")
        return output_path

    try:
        print(f"  📥 Descargando audio de {video_id}...")

        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': str(output_dir / f"{idx:02d}_{titulo_limpio}.%(ext)s"),
            'quiet': False,
            'no_warnings': False,
            'ffmpeg_location': ffmpeg_path,
            'socket_timeout': 30,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

        if output_path.exists():
            tamaño_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"  ✅ Descargado: {output_path.name} ({tamaño_mb:.1f} MB)")
            return output_path
        else:
            print(f"  ❌ No se creó el archivo MP3")
            return None

    except Exception as e:
        print(f"  ❌ Error descargando: {str(e)[:100]}")
        return None


def transcribir_audio(mp3_path: Path, whisper_model: WhisperModel, idioma: str = 'es') -> Tuple[str, List[dict]]:
    """
    Transcribe el MP3 usando faster-whisper.
    Retorna (texto_completo, segmentos).
    """
    try:
        print(f"  🎤 Transcribiendo {mp3_path.name}...")

        segments, info = whisper_model.transcribe(
            str(mp3_path),
            language=idioma,
            beam_size=5,
            best_of=1,
        )

        # Convertir a lista para reutilización
        segments_list = list(segments)
        texto_completo = ' '.join([seg.text.strip() for seg in segments_list])

        print(f"  ✅ Transcripción completada ({len(texto_completo)} caracteres)")

        return texto_completo, segments_list

    except Exception as e:
        print(f"  ❌ Error transcribiendo: {str(e)[:100]}")
        return "", []


def generar_markdown_asr(
    video: dict,
    video_id: str,
    transcripcion: str,
    modelo_usado: str,
    duracion_real_seg: int,
    idioma: str = 'es'
) -> str:
    """Genera el contenido markdown con la transcripción ASR."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    titulo = video.get('title', f'Video {video_id}')

    # Limpiar título para filename
    titulo_limpio = re.sub(r'[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ\s\-]', '', titulo)
    titulo_limpio = titulo_limpio.strip()[:60]

    num_palabras = len(transcripcion.split())
    num_caracteres = len(transcripcion)
    duracion_min = duracion_real_seg // 60
    duracion_seg_resto = duracion_real_seg % 60

    return f"""# Transcripción: {titulo}

**Video:** [{titulo}](https://www.youtube.com/watch?v={video_id})
**Video ID:** {video_id}
**Descargado:** {timestamp}
**Origen:** Transcripción local (faster-whisper, modelo "{modelo_usado}") — ⚠️ NO son subtítulos oficiales de YouTube; generada por reconocimiento de voz automático (ASR); puede contener errores.
**Duración real (validada vía yt-dlp):** {duracion_min}m {duracion_seg_resto}s
**Idioma:** {idioma}

---

## 📝 Transcripción Completa

{transcripcion}

---

## 📊 Estadísticas

- **Palabras:** {num_palabras}
- **Caracteres:** {num_caracteres}
- **Duración audio:** {duracion_min}m {duracion_seg_resto}s
- **Párrafos:** {len([p for p in transcripcion.split('.') if p.strip()])}

---

## 🚀 Próximos Pasos

1. **Analizar con Claude** - Extrae palabras clave, resumen
2. **Crear Blog Post** - Contenido para blog
3. **LinkedIn Article** - Formato para LinkedIn
4. **Threads de Twitter** - Fragmentos principales
5. **Clips Automáticos** - Segmentos clave en video

---

"""


def procesar_pipeline(
    top_n: int = 10,
    batch_range: Optional[Tuple[int, int]] = None,
    model_size: str = 'small',
    keep_audio: bool = True,
    skip_existing: bool = True,
    min_dur: int = 20,
    max_dur: int = 10800,
    incluir_anomalias: bool = False,
    idioma: str = 'es'
):
    """Orquesta el pipeline completo: load → validate → download → transcribe → save."""

    print("\n" + "=" * 70)
    print("🎬 PIPELINE: DESCARGA + TRANSCRIPCIÓN LOCAL (faster-whisper)")
    print("=" * 70)

    print(f"\n📋 Configuración:")
    if batch_range:
        videos_label = f"Lote (videos #{batch_range[0]}-{batch_range[1]})"
    else:
        videos_label = "TODOS los videos" if top_n is None else f"Top {top_n} videos"
    print(f"  - {videos_label}")
    print(f"  - Modelo Whisper: {model_size}")
    print(f"  - Validación duración: {min_dur}s - {max_dur}s")
    print(f"  - Incluir anomalías: {incluir_anomalias}")
    print(f"  - Idioma: {idioma}")
    print(f"  - Guardar MP3s: {keep_audio}")

    # Cargar videos
    print(f"\n📂 Cargando videos desde metrics.json...")
    todos_videos = cargar_top_n_videos(None)  # Cargar todos para poder filtrar por rango

    # Filtrar por batch si se especifica
    if batch_range:
        start_idx, end_idx = batch_range
        # Los índices en batch_range son 1-based (video #1, #2, etc.)
        videos_top = todos_videos[start_idx - 1:end_idx]
        print(f"✅ {len(videos_top)} videos cargados (videos #{start_idx}-{end_idx})")
    else:
        videos_top = todos_videos[:top_n] if top_n else todos_videos
        print(f"✅ {len(videos_top)} videos cargados")

    # Inicializar Whisper (una sola vez)
    print(f"\n🔧 Inicializando modelo Whisper '{model_size}'...")
    try:
        whisper_model = WhisperModel(model_size, device="cpu", compute_type="int8")
        print(f"✅ Modelo cargado")
    except Exception as e:
        print(f"❌ Error cargando modelo: {e}")
        sys.exit(1)

    # Procesamiento
    print(f"\n🎯 Procesando videos:")
    print("-" * 70)

    stats = {
        'procesados': 0,
        'saltados': 0,
        'errores': 0,
        'motivos_skip': {},
        'tiempos': []
    }

    for idx, video in enumerate(videos_top, 1):
        video_id = video.get('video_id')
        titulo = video.get('title', video_id)
        views = video.get('view_count', 0)

        print(f"\n[{idx}/{len(videos_top)}] 📺 {titulo[:50]}... ({views:,} views)")
        print(f"     ID: {video_id}")

        # Chequear si ya existe transcripción (busca video_id en contenido)
        transcripts_existentes = []
        if skip_existing:
            for md_file in TRANSCRIPTS_DIR.glob("*.md"):
                try:
                    contenido = md_file.read_text(encoding='utf-8')
                    if f"**Video ID:** {video_id}" in contenido:
                        transcripts_existentes.append(md_file)
                        break
                except:
                    pass

        if skip_existing and transcripts_existentes:
            print(f"  ⏭️  Transcripción ya existe, omitido")
            stats['saltados'] += 1
            continue

        # Validar video
        print(f"  🔍 Validando...")
        validacion = validar_video_ytdlp(video_id, min_dur=min_dur, max_dur=max_dur)

        if not validacion.ok:
            motivo = validacion.motivo_skip or "Razón desconocida"
            print(f"  ⏭️  Saltado: {motivo}")
            stats['saltados'] += 1
            stats['motivos_skip'][motivo] = stats['motivos_skip'].get(motivo, 0) + 1

            if not incluir_anomalias:
                continue
            else:
                print(f"     (forzado con --incluir-anomalias)")

        # Descargar
        inicio = time.time()
        audio_path = descargar_audio(video_id, idx, titulo)

        if not audio_path:
            print(f"  ❌ Fallo en descarga")
            stats['errores'] += 1
            continue

        # Transcribir
        transcripcion, segmentos = transcribir_audio(audio_path, whisper_model, idioma=idioma)

        if not transcripcion:
            print(f"  ❌ Fallo en transcripción")
            stats['errores'] += 1
            # Limpiar MP3 si fallo la transcripción
            if not keep_audio and audio_path.exists():
                audio_path.unlink()
            continue

        # Guardar markdown
        duracion_real = validacion.duracion_real_seg or 0
        contenido_md = generar_markdown_asr(
            video,
            video_id,
            transcripcion,
            model_size,
            duracion_real,
            idioma=idioma
        )

        # Generar filename para transcripción
        titulo_limpio = re.sub(r'[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ\s\-]', '', titulo)
        titulo_limpio = titulo_limpio.strip()[:60]
        filename_transcript = f"{idx:02d}_{titulo_limpio}.md"
        filepath_transcript = TRANSCRIPTS_DIR / filename_transcript

        try:
            filepath_transcript.write_text(contenido_md, encoding='utf-8')
            print(f"  ✅ Guardado: {filename_transcript}")
            stats['procesados'] += 1
        except Exception as e:
            print(f"  ❌ Error guardando: {e}")
            stats['errores'] += 1

        # Limpiar MP3 si se configura
        if not keep_audio and audio_path.exists():
            audio_path.unlink()
            print(f"  🗑️  MP3 eliminado")

        tiempo_transcripcion = time.time() - inicio
        stats['tiempos'].append(tiempo_transcripcion)

    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN FINAL")
    print("=" * 70)
    print(f"✅ Procesados: {stats['procesados']}")
    print(f"⏭️  Saltados: {stats['saltados']}")
    print(f"❌ Errores: {stats['errores']}")

    if stats['motivos_skip']:
        print(f"\n📋 Razones de salto:")
        for motivo, count in stats['motivos_skip'].items():
            print(f"   - {motivo}: {count}")

    if stats['tiempos']:
        tiempo_total = sum(stats['tiempos'])
        tiempo_promedio = tiempo_total / len(stats['tiempos'])
        print(f"\n⏱️  Tiempo total: {tiempo_total:.1f}s ({tiempo_total/60:.1f} min)")
        print(f"   Promedio por video: {tiempo_promedio:.1f}s")

    print(f"\n📁 Transcripciones guardadas en: {TRANSCRIPTS_DIR.name}/")
    if keep_audio:
        print(f"🎵 MP3s guardados en: {AUDIO_DIR.name}/")

    print("\n" + "=" * 70)
    print("✨ ¡Listo!")
    print("=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Descarga y transcribe videos del canal usando ASR local (faster-whisper)"
    )

    # Grupo mutualmente excluyente: --top, --all o --batch
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--top',
        type=int,
        default=10,
        help='Cantidad de videos a procesar (default: 10)'
    )
    group.add_argument(
        '--all',
        action='store_true',
        help='Procesar TODOS los videos del canal (en lugar de solo top N)'
    )
    group.add_argument(
        '--batch',
        type=str,
        help='Procesar un lote específico. Formato: "11-20" para videos #11 a #20 (inclusive)'
    )

    parser.add_argument(
        '--model',
        choices=['tiny', 'base', 'small', 'medium'],
        default='small',
        help='Tamaño del modelo Whisper (default: small). Larger = más preciso pero más lento.'
    )
    parser.add_argument(
        '--keep-audio',
        action='store_true',
        default=True,
        help='Guardar MP3s descargados (default: True)'
    )
    parser.add_argument(
        '--delete-audio',
        action='store_false',
        dest='keep_audio',
        help='Eliminar MP3s después de transcribir'
    )
    parser.add_argument(
        '--incluir-anomalias',
        action='store_true',
        default=False,
        help='Procesar videos con duración anómala o status de livestream'
    )
    parser.add_argument(
        '--idioma',
        default='es',
        help='Idioma para transcripción (default: es para español)'
    )

    args = parser.parse_args()

    # Determinar cantidad de videos y batch
    top_n = None if args.all else args.top
    batch_range = None

    if args.batch:
        try:
            parts = args.batch.split('-')
            if len(parts) != 2:
                print(f"❌ Formato de batch inválido: '{args.batch}'. Usa formato: '11-20'")
                sys.exit(1)
            start, end = int(parts[0]), int(parts[1])
            if start < 1 or end < start or end > 50:
                print(f"❌ Rango inválido: videos deben estar entre #1-50")
                sys.exit(1)
            batch_range = (start, end)
            top_n = None  # Ignorar --top cuando se usa --batch
        except ValueError:
            print(f"❌ Formato de batch inválido: '{args.batch}'. Usa números: '11-20'")
            sys.exit(1)

    procesar_pipeline(
        top_n=top_n,
        batch_range=batch_range,
        model_size=args.model,
        keep_audio=args.keep_audio,
        incluir_anomalias=args.incluir_anomalias,
        idioma=args.idioma
    )


if __name__ == "__main__":
    main()
