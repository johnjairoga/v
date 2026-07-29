#!/usr/bin/env python3

import json
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from config import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, BASE_DIR

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
TOKEN_FILE = os.path.join(BASE_DIR, 'token.pickle')
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials.json')


def authenticate():
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


def debug():
    print("🔍 Debug: Revisando canal de YouTube...\n")

    creds = authenticate()
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)

    # Obtener info del canal
    request = youtube.channels().list(part='snippet,statistics,contentDetails', mine=True)
    response = request.execute()

    print("📺 Información del Canal:")
    print(json.dumps(response, indent=2, ensure_ascii=False))

    if response['items']:
        channel = response['items'][0]
        print(f"\nNombre: {channel['snippet']['title']}")
        print(f"Suscriptores: {channel['statistics'].get('subscriberCount', 'privado')}")
        print(f"Videos: {channel['statistics'].get('videoCount', '?')}")

        uploads_playlist_id = channel['contentDetails']['relatedPlaylists']['uploads']
        print(f"\nPlaylist de uploads: {uploads_playlist_id}")

        # Listar videos
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=10
        )
        response = request.execute()

        print(f"\nVideos encontrados: {len(response.get('items', []))}")
        for item in response.get('items', []):
            print(f"  - {item['snippet']['title']}")


if __name__ == '__main__':
    debug()
