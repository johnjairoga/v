#!/usr/bin/env python3

import json
import os
import pickle
import requests
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from config import (
    GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI,
    YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    DATA_DIR, OUTPUT_DIR, THUMBNAILS_DIR, BASE_DIR
)

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
TOKEN_FILE = os.path.join(BASE_DIR, 'token.pickle')
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials.json')


def authenticate():
    """Autenticarse con Google usando OAuth 2.0"""
    creds = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)

        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_youtube_service(creds):
    """Crear servicio de YouTube"""
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)


def get_channel_id(youtube):
    """Obtener el Channel ID del usuario autenticado"""
    request = youtube.channels().list(part='id', mine=True)
    response = request.execute()
    return response['items'][0]['id']


def get_videos(youtube, channel_id, max_results=50):
    """Obtener lista de videos del canal"""
    videos = []

    # Obtener la playlist de uploads del canal
    request = youtube.channels().list(part='contentDetails', id=channel_id)
    response = request.execute()

    if not response['items']:
        return videos

    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Obtener videos de la playlist de uploads
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=min(max_results, 50)
    )

    while request and len(videos) < max_results:
        response = request.execute()

        for item in response.get('items', []):
            videos.append({
                'video_id': item['snippet']['resourceId']['videoId'],
                'title': item['snippet']['title'],
                'published_at': item['snippet']['publishedAt'],
                'description': item['snippet']['description'],
                'thumbnail_url': item['snippet']['thumbnails']['high']['url']
            })

        if len(videos) >= max_results or 'nextPageToken' not in response:
            break

        request = youtube.playlistItems().list_next(request, response)

    return videos[:max_results]


def get_video_stats(youtube, video_id):
    """Obtener estadísticas de un video"""
    request = youtube.videos().list(
        part='statistics,contentDetails',
        id=video_id
    )
    response = request.execute()

    if response['items']:
        item = response['items'][0]
        return {
            'view_count': int(item['statistics'].get('viewCount', 0)),
            'like_count': int(item['statistics'].get('likeCount', 0)),
            'comment_count': int(item['statistics'].get('commentCount', 0)),
            'duration': item['contentDetails']['duration']
        }
    return {}


def get_transcript(video_id):
    """Obtener transcripción de un video"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en'])
        return ' '.join([item['text'] for item in transcript])
    except Exception as e:
        print(f"Error obteniendo transcript para {video_id}: {e}")
        return None


def download_thumbnail(video_id, thumbnail_url):
    """Descargar thumbnail de un video"""
    try:
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            filename = os.path.join(THUMBNAILS_DIR, f"{video_id}.jpg")
            with open(filename, 'wb') as f:
                f.write(response.content)
            return filename
    except Exception as e:
        print(f"Error descargando thumbnail para {video_id}: {e}")
    return None


def save_json(data, filename):
    """Guardar datos en JSON"""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ Guardado: {filepath}")


def generate_analysis(videos_data, metrics_data):
    """Generar análisis en Markdown"""
    analysis = "# Análisis de Canal YouTube\n\n"

    analysis += "## 📊 Resumen\n\n"
    total_views = sum(m['view_count'] for m in metrics_data)
    total_likes = sum(m['like_count'] for m in metrics_data)
    total_comments = sum(m['comment_count'] for m in metrics_data)

    analysis += f"- **Videos totales:** {len(videos_data)}\n"
    analysis += f"- **Total views:** {total_views:,}\n"
    analysis += f"- **Total likes:** {total_likes:,}\n"
    analysis += f"- **Total comentarios:** {total_comments:,}\n\n"

    analysis += "## 🏆 Videos con mejor desempeño\n\n"
    sorted_metrics = sorted(
        zip(videos_data, metrics_data),
        key=lambda x: x[1]['view_count'],
        reverse=True
    )[:5]

    for i, (video, metrics) in enumerate(sorted_metrics, 1):
        analysis += f"{i}. **{video['title']}**\n"
        analysis += f"   - Views: {metrics['view_count']:,}\n"
        analysis += f"   - Likes: {metrics['like_count']:,}\n"
        analysis += f"   - Comentarios: {metrics['comment_count']:,}\n\n"

    filepath = os.path.join(OUTPUT_DIR, 'analysis.md')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(analysis)
    print(f"✓ Guardado: {filepath}")


def main():
    print("🚀 Iniciando extracción de datos de YouTube...\n")

    try:
        print("1️⃣  Autenticando con Google...")
        creds = authenticate()
        print("✓ Autenticación exitosa\n")

        print("2️⃣  Conectando a YouTube API...")
        youtube = get_youtube_service(creds)
        channel_id = get_channel_id(youtube)
        print(f"✓ Canal ID: {channel_id}\n")

        print("3️⃣  Obteniendo videos del canal...")
        videos = get_videos(youtube, channel_id, max_results=50)
        print(f"✓ {len(videos)} videos encontrados\n")

        print("4️⃣  Extrayendo datos de cada video...")
        videos_data = []
        metrics_data = []

        for i, video in enumerate(videos, 1):
            print(f"   [{i}/{len(videos)}] {video['title'][:50]}...", end=" ")

            # Obtener estadísticas
            stats = get_video_stats(youtube, video['video_id'])
            metrics_data.append(stats)

            # Descargar thumbnail
            download_thumbnail(video['video_id'], video['thumbnail_url'])

            # Obtener transcripción (opcional, puede ser lento)
            # transcript = get_transcript(video['video_id'])
            # video['transcript'] = transcript

            videos_data.append(video)
            print("✓")

        print("\n5️⃣  Guardando datos...\n")

        # Guardar videos
        save_json(videos_data, 'videos.json')

        # Guardar métricas
        metrics_with_ids = [
            {**v, **m} for v, m in zip(videos_data, metrics_data)
        ]
        save_json(metrics_with_ids, 'metrics.json')

        # Generar análisis
        print("6️⃣  Generando análisis...\n")
        generate_analysis(videos_data, metrics_data)

        print("✅ Proceso completado exitosamente!")
        print(f"\n📁 Datos guardados en: {DATA_DIR}")
        print(f"📁 Análisis guardado en: {OUTPUT_DIR}")

    except Exception as e:
        print(f"❌ Error: {e}")
        raise


if __name__ == '__main__':
    main()
