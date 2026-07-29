#!/usr/bin/env python3

import json
import os
from youtube_transcript_api import YouTubeTranscriptApi
from config import DATA_DIR, BASE_DIR

OUTPUT_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "videos de youtube", "transcripciones_top_videos")
)


def load_metrics():
    """Cargar métricas de videos"""
    filepath = os.path.join(DATA_DIR, 'metrics.json')
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_transcript(video_id):
    """Obtener transcripción de un video"""
    try:
        # Intentar en español primero
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=['es', 'en']
        )
        return ' '.join([item['text'] for item in transcript])
    except Exception as e:
        print(f"   ⚠️  No se pudo obtener transcript: {e}")
        return None


def save_transcript(video_title, video_id, views, transcript):
    """Guardar transcripción en markdown"""
    # Sanitizar nombre de archivo
    filename = f"{views:06d}_{video_title[:50].replace('/', '_').replace(':', '')}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    content = f"""# {video_title}

**Video ID:** {video_id}
**Views:** {views:,}
**Fecha:** {os.path.getmtime(filepath) if os.path.exists(filepath) else 'N/A'}

---

## Transcripción

{transcript}

---

*Generado automáticamente desde YouTube Analytics*
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def main():
    print("🎬 Extrayendo transcripciones de top videos...\n")

    # Cargar métricas
    metrics = load_metrics()

    # Ordenar por views y obtener top 10
    sorted_videos = sorted(metrics, key=lambda x: x['view_count'], reverse=True)[:10]

    print(f"📥 Extrayendo {len(sorted_videos)} videos principales:\n")

    for i, video in enumerate(sorted_videos, 1):
        title = video['title']
        video_id = video['video_id']
        views = video['view_count']

        print(f"[{i}/10] {title[:60]}...", end=" ", flush=True)

        # Obtener transcripción
        transcript = get_transcript(video_id)

        if transcript:
            filepath = save_transcript(title, video_id, views, transcript)
            print(f"✓")
        else:
            print(f"✗")

    print(f"\n✅ Transcripciones guardadas en:\n{OUTPUT_DIR}")


if __name__ == '__main__':
    main()
