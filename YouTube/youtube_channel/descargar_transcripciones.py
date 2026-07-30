#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Descargador de Transcripciones YouTube - Skill Baoyu
Extrae transcripciones de todos los videos del canal
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import requests
from datetime import datetime

# Configurar encoding UTF-8 en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configuración
BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "videos de youtube" / "transcripciones_top_videos"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VIDEOS_FILE = BASE_DIR / "TODOS_LOS_VIDEOS_CON_LINKS.md"

class TranscripcionDescargador:
    """Descarga transcripciones de YouTube videos"""

    def __init__(self):
        self.stats = {
            "total": 0,
            "exitosas": 0,
            "fallidas": 0,
            "sin_transcripcion": 0
        }
        self.errores = []

    def extraer_video_id(self, url: str) -> Optional[str]:
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

    def obtener_transcripcion(self, video_id: str) -> Optional[str]:
        """Obtiene transcripción de un video específico"""
        try:
            # Intentar obtener transcripción en español primero
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            # Preferencia: Español > Otros idiomas > Auto-generadas
            transcript = None

            # Buscar en español
            try:
                transcript = transcript_list.find_transcript(['es'])
            except:
                # Buscar en inglés
                try:
                    transcript = transcript_list.find_transcript(['en'])
                except:
                    # Usar cualquier disponible
                    try:
                        transcript = transcript_list.find_transcript(transcript_list.available_transcripts[0].language_code)
                    except:
                        # Intentar auto-generadas
                        if transcript_list.manually_created_transcripts:
                            transcript = transcript_list.manually_created_transcripts[0]
                        elif transcript_list.generated_transcripts:
                            transcript = transcript_list.generated_transcripts[0]

            if transcript:
                # Obtener texto completo
                transcript_text = transcript.fetch()
                return self._formatear_transcripcion(transcript_text)

            return None

        except TranscriptsDisabled:
            return None
        except NoTranscriptFound:
            return None
        except Exception as e:
            self.errores.append(f"Video {video_id}: {str(e)}")
            return None

    def _formatear_transcripcion(self, transcript_list: List[Dict]) -> str:
        """Formatea la transcripción descargada"""
        texto = []
        for item in transcript_list:
            texto.append(item['text'])
        return ' '.join(texto)

    def obtener_metadata_video(self, video_id: str) -> Dict:
        """Obtiene metadatos del video (usar si necesitas YouTube API)"""
        # Por ahora retornamos un dict vacío
        # Se puede mejorar con YouTube API si es necesario
        return {}

    def descargar_video(self, url: str, titulo: str, orden: int) -> bool:
        """Descarga transcripción de un video individual"""
        video_id = self.extraer_video_id(url)

        if not video_id:
            self.errores.append(f"{titulo}: No se pudo extraer video ID de {url}")
            self.stats["fallidas"] += 1
            return False

        print(f"[{orden}] Descargando: {titulo[:50]}...", end=" ")

        # Obtener transcripción
        transcripcion = self.obtener_transcripcion(video_id)

        if transcripcion is None:
            print("❌ (sin transcripción)")
            self.stats["sin_transcripcion"] += 1
            return False

        # Guardar archivo
        filename = f"{orden:02d}_{titulo[:40].replace(' ', '_')}.md"
        filepath = OUTPUT_DIR / filename

        try:
            contenido = self._generar_archivo(titulo, url, video_id, transcripcion)
            filepath.write_text(contenido, encoding='utf-8')
            print("✅")
            self.stats["exitosas"] += 1
            return True
        except Exception as e:
            print(f"❌ (error al guardar: {e})")
            self.errores.append(f"{titulo}: {str(e)}")
            self.stats["fallidas"] += 1
            return False

    def _generar_archivo(self, titulo: str, url: str, video_id: str, transcripcion: str) -> str:
        """Genera contenido del archivo de transcripción"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""# Transcripción: {titulo}

**Video:** [{titulo}]({url})
**Video ID:** {video_id}
**Descargado:** {timestamp}
**Origen:** YouTube Transcript API (Skill Baoyu)

---

## Transcripción Completa

{transcripcion}

---

## Estadísticas

- **Largo:** {len(transcripcion.split())} palabras
- **Caracteres:** {len(transcripcion)}

---

## Uso

Esta transcripción puede usarse para:
- Crear blog posts
- SEO optimization
- Análisis de contenido
- Repurposing en diferentes formatos
- Búsqueda y referencias

"""

    def procesar_archivo_videos(self):
        """Lee el archivo de videos y procesa cada uno"""
        if not VIDEOS_FILE.exists():
            print(f"❌ Archivo no encontrado: {VIDEOS_FILE}")
            return

        contenido = VIDEOS_FILE.read_text(encoding='utf-8')

        # Extraer URLs del formato de tabla markdown
        # Formato: | titulo | views | [Ver](URL) |
        pattern = r'\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*[\d,]+\s*\|\s*\[Ver\]\((https://www\.youtube\.com/watch\?v=[^)]+)\)'
        matches = re.findall(pattern, contenido)

        if not matches:
            print("❌ No se encontraron videos en el archivo")
            return

        print(f"\n🎬 Encontrados {len(matches)} videos")
        print(f"📁 Guardando en: {OUTPUT_DIR.resolve()}\n")
        print("-" * 60)

        self.stats["total"] = len(matches)

        # Procesar cada video
        for orden, (titulo, url) in enumerate(matches, 1):
            titulo = titulo.strip()
            # Limpiar caracteres especiales y emojis del título
            titulo = re.sub(r'[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ\s\-]', '', titulo)
            self.descargar_video(url, titulo, orden)

        # Resumen
        self._mostrar_resumen()

    def _mostrar_resumen(self):
        """Muestra resumen de descargas"""
        print("-" * 60)
        print("\n📊 RESUMEN:")
        print(f"Total videos:        {self.stats['total']}")
        print(f"Transcripciones:     {self.stats['exitosas']} ✅")
        print(f"Sin transcripción:   {self.stats['sin_transcripcion']} ⏭️")
        print(f"Errores:             {self.stats['fallidas']} ❌")

        tasa_exito = (self.stats['exitosas'] / self.stats['total'] * 100) if self.stats['total'] > 0 else 0
        print(f"Tasa de éxito:       {tasa_exito:.1f}%")

        if self.errores:
            print("\n⚠️ Errores encontrados:")
            for error in self.errores[:5]:  # Mostrar primeros 5
                print(f"  - {error}")
            if len(self.errores) > 5:
                print(f"  ... y {len(self.errores) - 5} más")

        print("\n" + "=" * 60)
        print("✨ Descarga completada!")
        print(f"📁 Archivos guardados en: {OUTPUT_DIR.resolve()}")
        print("=" * 60)


def main():
    """Función principal"""
    print("\n" + "=" * 60)
    print("🎯 DESCARGADOR DE TRANSCRIPCIONES - SKILL BAOYU")
    print("=" * 60)

    descargador = TranscripcionDescargador()
    descargador.procesar_archivo_videos()


if __name__ == "__main__":
    main()
