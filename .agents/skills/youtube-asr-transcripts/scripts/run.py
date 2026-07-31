#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube ASR Transcripts Skill - Orchestrator
Ejecuta el pipeline completo de transcripción de videos de YouTube sin subtítulos.

Este script orquesta:
1. youtube_channel/main.py - Extrae metadatos del canal
2. youtube_channel/descargar_y_transcribir_audio.py - Transcribe con Whisper ASR
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

# Detectar rutas
SKILL_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent.parent
YOUTUBE_CHANNEL_DIR = PROJECT_ROOT / "youtube_channel"
ENV_FILE = PROJECT_ROOT / ".env"

print(f"""
╔════════════════════════════════════════════════════════════════╗
║       🎬 YouTube ASR Transcripts - Skill Orchestrator         ║
║                                                                ║
║  Transcribe videos de YouTube sin depender de subtítulos     ║
║  Usando Whisper ASR (reconocimiento de voz automático)       ║
╚════════════════════════════════════════════════════════════════╝
""")


class YouTubeASRSkill:
    """Orquestador del pipeline de transcripción"""

    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.youtube_dir = YOUTUBE_CHANNEL_DIR
        self.env_file = ENV_FILE

    def check_dependencies(self) -> bool:
        """Verifica que todas las dependencias estén instaladas"""
        print("🔍 Verificando dependencias...")

        required_modules = [
            'yt_dlp',
            'faster_whisper',
            'google_auth_oauthlib',
            'googleapiclient',
            'youtube_transcript_api'
        ]

        missing = []
        for module in required_modules:
            try:
                __import__(module)
                print(f"  ✅ {module}")
            except ImportError:
                print(f"  ❌ {module}")
                missing.append(module)

        if missing:
            print(f"\n❌ Faltan dependencias: {', '.join(missing)}")
            print(f"\n📦 Instala con:")
            print(f"   pip install {' '.join(missing)}")
            return False

        print("✅ Todas las dependencias OK\n")
        return True

    def check_credentials(self) -> bool:
        """Verifica que existan credenciales válidas"""
        print("🔐 Verificando credenciales...")

        # Verificar .env
        if not self.env_file.exists():
            print(f"  ❌ No encontrado: {self.env_file}")
            print(f"\n     Necesitas configurar credenciales OAuth de Google.")
            print(f"     La skill te guiará paso a paso.\n")
            return False

        # Leer .env
        env_vars = {}
        with open(self.env_file, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value

        # Verificar variables críticas
        required_vars = ['GOOGLE_CLIENT_ID', 'GOOGLE_CLIENT_SECRET']
        missing_vars = [v for v in required_vars if v not in env_vars]

        if missing_vars:
            print(f"  ❌ Faltan variables en .env: {', '.join(missing_vars)}")
            return False

        print(f"  ✅ .env encontrado con credenciales")
        print("✅ Credenciales OK\n")
        return True

    def run_auth_only(self) -> bool:
        """Ejecuta solo autenticación (--auth-only)"""
        print("🔐 Ejecutando autenticación...")
        print("   Se abrirá tu navegador para hacer login.\n")

        try:
            result = subprocess.run(
                [sys.executable, str(self.youtube_dir / "main.py"), "--auth-only"],
                cwd=str(self.youtube_dir),
                check=True
            )
            print("\n✅ Autenticación exitosa\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error en autenticación: {e}\n")
            return False

    def run_test(self) -> bool:
        """Ejecuta test de conectividad (--test)"""
        print("🧪 Validando autenticación...")

        try:
            result = subprocess.run(
                [sys.executable, str(self.youtube_dir / "main.py"), "--test"],
                cwd=str(self.youtube_dir),
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
            print("✅ Validación exitosa\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Validación fallida")
            print(f"Error: {e.stderr}\n")
            return False

    def run_transcription(
        self,
        top: Optional[int] = 10,
        batch: Optional[str] = None,
        model: str = 'small',
        language: str = 'es',
        keep_audio: bool = True,
        all_videos: bool = False
    ) -> bool:
        """Ejecuta pipeline de transcripción"""

        print("🎬 Iniciando transcripción...\n")

        cmd = [
            sys.executable,
            str(self.youtube_dir / "descargar_y_transcribir_audio.py")
        ]

        # Agregar argumentos
        if all_videos:
            cmd.append('--all')
        elif batch:
            cmd.extend(['--batch', batch])
        else:
            cmd.extend(['--top', str(top)])

        cmd.extend(['--model', model])
        cmd.extend(['--idioma', language])

        if keep_audio:
            cmd.append('--keep-audio')
        else:
            cmd.append('--delete-audio')

        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.youtube_dir),
                check=True
            )
            print("\n✅ Transcripción completada\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error en transcripción: {e}\n")
            return False

    def run_metrics_extraction(self) -> bool:
        """Ejecuta extracción de metadatos (main.py)"""
        print("📊 Extrayendo metadatos del canal...")

        try:
            result = subprocess.run(
                [sys.executable, str(self.youtube_dir / "main.py")],
                cwd=str(self.youtube_dir),
                check=True
            )
            print("\n✅ Metadatos extraídos\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error extrayendo metadatos: {e}\n")
            return False

    def show_results(self):
        """Muestra dónde están los resultados"""
        transcripts_dir = self.project_root / "videos de youtube" / "transcripciones_top_videos"
        audio_dir = self.project_root / "videos de youtube" / "audio_mp3"

        print("📁 ARCHIVOS GENERADOS:\n")

        if transcripts_dir.exists():
            transcripts = list(transcripts_dir.glob("*.md"))
            if transcripts:
                print(f"  📄 Transcripciones ({len(transcripts)} archivos):")
                print(f"     {transcripts_dir}\n")
                for t in sorted(transcripts)[:5]:
                    print(f"     - {t.name}")
                if len(transcripts) > 5:
                    print(f"     ... y {len(transcripts) - 5} más\n")

        if audio_dir.exists():
            audio_files = list(audio_dir.glob("*.mp3"))
            if audio_files:
                print(f"  🎵 Audio MP3 ({len(audio_files)} archivos):")
                print(f"     {audio_dir}\n")

        print("\n🚀 PRÓXIMOS PASOS:")
        print("   1. Analizar transcripciones con Claude")
        print("   2. Crear blog posts")
        print("   3. Generar clips para redes sociales")
        print("   4. Crear Twitter threads\n")


def main():
    parser = argparse.ArgumentParser(
        description="YouTube ASR Transcripts - Descarga y transcribe videos sin subtítulos"
    )

    # Comandos principales
    subparsers = parser.add_subparsers(dest='command', help='Comando a ejecutar')

    # Comando: setup
    setup_parser = subparsers.add_parser('setup', help='Configurar autenticación (primera vez)')

    # Comando: test
    test_parser = subparsers.add_parser('test', help='Validar autenticación')

    # Comando: transcribe
    transcribe_parser = subparsers.add_parser('transcribe', help='Transcribir videos')
    transcribe_group = transcribe_parser.add_mutually_exclusive_group()
    transcribe_group.add_argument('--top', type=int, default=10, help='Top N videos (default: 10)')
    transcribe_group.add_argument('--batch', type=str, help='Rango específico (ej: "11-20")')
    transcribe_group.add_argument('--all', action='store_true', help='Todos los videos')

    transcribe_parser.add_argument('--model', choices=['tiny', 'base', 'small', 'medium'],
                                   default='small', help='Modelo Whisper (default: small)')
    transcribe_parser.add_argument('--language', default='es', help='Idioma (default: es)')
    transcribe_parser.add_argument('--keep-audio', action='store_true', default=True)
    transcribe_parser.add_argument('--delete-audio', action='store_false', dest='keep_audio')

    # Comando: full (completo: metadatos + transcripción)
    full_parser = subparsers.add_parser('full', help='Flujo completo (metadatos + transcripción)')
    full_parser.add_argument('--top', type=int, default=10, help='Top N videos (default: 10)')

    args = parser.parse_args()

    skill = YouTubeASRSkill()

    # Ejecutar según comando
    if not args.command:
        # Sin comando especifico: flujo interactivo
        print("¿Qué deseas hacer?\n")
        print("[1] Setup inicial (primera vez)")
        print("[2] Validar autenticación")
        print("[3] Transcribir videos")
        print("[4] Flujo completo (metadatos + transcripción)")
        choice = input("\nSelecciona [1-4]: ").strip()

        if choice == '1':
            args.command = 'setup'
        elif choice == '2':
            args.command = 'test'
        elif choice == '3':
            args.command = 'transcribe'
        elif choice == '4':
            args.command = 'full'
        else:
            print("❌ Opción inválida")
            return 1

    # Verificar dependencias siempre
    if not skill.check_dependencies():
        return 1

    if args.command == 'setup':
        if not skill.run_auth_only():
            return 1
        if not skill.run_test():
            print("⚠️  Autenticación completada, pero validación falló.")
            print("    Intenta de nuevo en unos minutos.\n")
            return 1

    elif args.command == 'test':
        if not skill.check_credentials():
            return 1
        if not skill.run_test():
            return 1

    elif args.command == 'transcribe':
        if not skill.check_credentials():
            return 1
        if not skill.run_test():
            return 1
        if not skill.run_transcription(
            top=args.top,
            batch=getattr(args, 'batch', None),
            model=args.model,
            language=args.language,
            keep_audio=args.keep_audio,
            all_videos=getattr(args, 'all', False)
        ):
            return 1
        skill.show_results()

    elif args.command == 'full':
        if not skill.check_credentials():
            return 1
        if not skill.run_metrics_extraction():
            return 1
        if not skill.run_transcription(top=args.top):
            return 1
        skill.show_results()

    print("\n✨ ¡Listo! Gracias por usar YouTube ASR Transcripts\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
