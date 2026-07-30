#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor de Transcripción - Video Único
Usa Skill Baoyu YouTube Transcript
"""

import os
import sys
import re
import time
from pathlib import Path
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from datetime import datetime

# Configurar encoding UTF-8 en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class ExtractorVideoUnico:
    """Extrae transcripción de un video específico"""

    def __init__(self, video_url: str):
        self.video_url = video_url
        self.video_id = self._extraer_video_id(video_url)
        self.output_dir = Path("videos de youtube/transcripciones_top_videos")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _extraer_video_id(self, url: str) -> Optional[str]:
        """Extrae video ID de URL de YouTube"""
        patterns = [
            r'youtube\.com/watch\?v=([^&\n?#]+)',
            r'youtu\.be/([^&\n?#]+)',
            r'v=([^&\n?#]+)'
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    def obtener_transcripcion(self) -> Optional[str]:
        """Obtiene transcripción del video con reintentos"""
        if not self.video_id:
            print("❌ No se pudo extraer video ID de la URL")
            return None

        # Reintentos con espera progresiva
        max_intentos = 3
        for intento in range(max_intentos):
            try:
                print(f"📥 Descargando transcripción... (intento {intento + 1}/{max_intentos})")
                print(f"📺 Video ID: {self.video_id}")

                # Esperamos un poco entre intentos para evitar rate limiting
                if intento > 0:
                    espera = 10 * intento
                    print(f"⏳ Esperando {espera} segundos...")
                    time.sleep(espera)

                # Intentar obtener transcripción
                transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)

                # Preferencia: Español > Inglés > Otros
                transcript = None

                try:
                    transcript = transcript_list.find_transcript(['es'])
                    print("✅ Encontrada en español")
                except:
                    try:
                        transcript = transcript_list.find_transcript(['en'])
                        print("✅ Encontrada en inglés")
                    except:
                        if transcript_list.manually_created_transcripts:
                            transcript = transcript_list.manually_created_transcripts[0]
                            print("✅ Encontrada (manual)")
                        elif transcript_list.generated_transcripts:
                            transcript = transcript_list.generated_transcripts[0]
                            print("✅ Encontrada (auto-generada)")

                if transcript:
                    print("📥 Descargando contenido...")
                    transcript_text = transcript.fetch()
                    texto_completo = ' '.join([item['text'] for item in transcript_text])
                    print("✅ Descarga completada")
                    return texto_completo

                print("❌ No hay transcripción disponible")
                return None

            except Exception as e:
                if intento < max_intentos - 1:
                    print(f"⚠️ Intento {intento + 1} falló: {str(e)[:100]}")
                    continue
                else:
                    error_str = str(e)
                    if "Too Many Requests" in error_str or "429" in error_str:
                        print("❌ Rate limit de YouTube. Intenta nuevamente en 5 minutos.")
                    elif "Transcripts" in error_str or "disabled" in error_str.lower():
                        print("❌ Transcripciones deshabilitadas en este video")
                    elif "No transcript" in error_str:
                        print("❌ Transcripción no encontrada")
                    else:
                        print(f"❌ Error: {error_str[:100]}")
                    return None

    def obtener_metadata_video(self) -> dict:
        """Obtiene información del video desde YouTube"""
        try:
            import requests
            url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={self.video_id}&format=json"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return {}

    def guardar_transcripcion(self, transcripcion: str, titulo: str = None):
        """Guarda la transcripción en un archivo"""
        if not titulo:
            titulo = f"video_{self.video_id}"

        # Limpiar título
        titulo_limpio = re.sub(r'[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ\s\-]', '', titulo)
        titulo_limpio = titulo_limpio.strip()[:50]

        filename = f"DESCARGA_{self.video_id}_{titulo_limpio}.md"
        filepath = self.output_dir / filename

        contenido = self._generar_contenido(titulo, transcripcion)

        try:
            filepath.write_text(contenido, encoding='utf-8')
            print(f"\n✅ Guardado en: {filepath.name}")
            return True
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
            return False

    def _generar_contenido(self, titulo: str, transcripcion: str) -> str:
        """Genera contenido del archivo markdown"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""# Transcripción: {titulo}

**Video:** https://www.youtube.com/watch?v={self.video_id}
**Video ID:** {self.video_id}
**Descargado:** {timestamp}
**Origen:** YouTube Transcript API (Skill Baoyu)

---

## 📝 Transcripción Completa

{transcripcion}

---

## 📊 Estadísticas

- **Palabras:** {len(transcripcion.split())}
- **Caracteres:** {len(transcripcion)}
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

    def extraer(self, titulo: str = None) -> bool:
        """Ejecuta la extracción completa"""
        print("\n" + "=" * 60)
        print("🎯 BAOYU YOUTUBE TRANSCRIPT - VIDEO ÚNICO")
        print("=" * 60)

        print(f"\n🔗 URL: {self.video_url}")

        # Obtener transcripción
        transcripcion = self.obtener_transcripcion()

        if not transcripcion:
            print("\n❌ No se pudo obtener transcripción")
            return False

        # Guardar
        if not titulo:
            titulo = f"Video {self.video_id}"

        self.guardar_transcripcion(transcripcion, titulo)

        print("\n" + "=" * 60)
        print("✨ ¡Listo!")
        print("=" * 60)

        return True


def main():
    """Función principal"""
    # URL del video
    video_url = "https://www.youtube.com/watch?v=quMX1eK9zHU"

    extractor = ExtractorVideoUnico(video_url)
    extractor.extraer(titulo="Mensajes Masivos WhatsApp")


if __name__ == "__main__":
    main()
