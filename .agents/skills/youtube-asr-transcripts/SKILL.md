---
name: youtube-asr-transcripts
description: Transcribe videos de YouTube sin depender de subtítulos usando ASR (Whisper). Guía completa de autenticación, configuración y ejecución.
type: python
triggers:
  - "transcribe youtube"
  - "youtube asr"
  - "get youtube transcript"
  - "youtube transcripción"
  - "transcribir canal youtube"
---

# 🎬 YouTube ASR Transcripts Skill

Transcribe videos de tu canal YouTube **incluso sin subtítulos**, usando reconocimiento de voz automático (ASR) con Whisper.

## ✨ Características

- ✅ Funciona **SIN subtítulos** de YouTube
- ✅ Guía interactiva de autenticación OAuth
- ✅ Descarga audio automáticamente con yt-dlp
- ✅ Transcripción local con Whisper (más privado)
- ✅ Genera Markdown con contexto completo
- ✅ Validación inteligente de videos
- ✅ Soporte para múltiples idiomas
- ✅ Configuración flexible (Top N, rangos, todos)

## 🚀 Cómo Usarla

### Invocación Simple
```
/youtube-asr-transcripts
```

Luego sigue los pasos interactivos:
1. Configura autenticación Google (primera vez)
2. Selecciona cuántos videos transcribir
3. Elige configuración de Whisper
4. Espera a que termine
5. Revisa transcripciones en `videos de youtube/transcripciones_top_videos/`

### Parámetros (Avanzado)
```
/youtube-asr-transcripts --top 10 --model small --language es
/youtube-asr-transcripts --batch 11-20 --model medium
/youtube-asr-transcripts --all --delete-audio
```

## 📋 Requisitos

### Necesarios
- Python 3.8+
- Cuenta Google (para OAuth)
- Canal YouTube asociado a esa cuenta
- ~2GB disco para modelo Whisper (primera ejecución)

### Dependencias Python
```bash
pip install yt-dlp faster-whisper google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## 🔐 Autenticación (Primera Vez)

La skill te guía paso a paso, pero aquí está el resumen:

### Paso 1: Crear Google Cloud Project
1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Haz login con el email de tu canal YouTube
3. Crea nuevo proyecto: "YouTube ASR Transcripts"
4. Ve a APIs & Services → Enable APIs
5. Busca "YouTube Data API v3" → ENABLE

### Paso 2: Crear Credenciales OAuth
1. En Google Cloud Console → Credentials
2. Create Credentials → OAuth 2.0 Client ID
3. Elige "Desktop application"
4. Completa formulario
5. Descarga JSON como `credentials.json`

### Paso 3: Cargar en Skill
La skill te pedirá que subas `credentials.json`
- Se guarda de forma segura en `.env`
- **NO** se commitea a Git (git-ignored)
- Se valida automáticamente

## 📁 Estructura de Proyecto

```
tu-proyecto/
├── .agents/
│   └── skills/
│       └── youtube-asr-transcripts/  ← Esta skill
├── .env                             ← Credenciales (privadas)
├── .gitignore                       ← Incluye .env
├── videos de youtube/
│   ├── audio_mp3/                   ← MP3 descargados
│   └── transcripciones_top_videos/  ← Markdown generados
└── youtube_channel/
    └── data/
        └── metrics.json             ← Metadatos de videos
```

## ⚙️ Variables de Entorno

Crear archivo `.env` en raíz del proyecto:

```bash
# Google OAuth Credentials
GOOGLE_CLIENT_ID=tu_client_id_aqui
GOOGLE_CLIENT_SECRET=tu_client_secret_aqui
GOOGLE_REDIRECT_URI=http://localhost:8080/

# Configuración Whisper (opcional)
WHISPER_MODEL_SIZE=small
WHISPER_DEVICE=cpu
WHISPER_COMPUTE_TYPE=int8

# Configuración de salida
KEEP_AUDIO_AFTER_TRANSCRIPT=true
OUTPUT_LANGUAGE=es
```

## 📊 Flujo de Ejecución

```
1. Iniciar skill
   ↓
2. Detectar si hay credenciales
   ├─ NO: Guiar obtención de OAuth
   └─ SÍ: Validar token
   ↓
3. Obtener lista de videos del canal
   ↓
4. Seleccionar cantidad (Top N, rango, todos)
   ↓
5. Elegir configuración Whisper
   ├─ Tamaño modelo (tiny/base/small/medium)
   ├─ Idioma (es/en/etc)
   └─ Guardar MP3s (yes/no)
   ↓
6. Procesar cada video
   ├─ Validar duración
   ├─ Descargar audio
   ├─ Transcribir con Whisper
   └─ Generar Markdown
   ↓
7. Mostrar resultados y próximos pasos
```

## 📝 Salida Generada

Para cada video, genera un archivo Markdown:

```markdown
# Transcripción: Titulo del Video

**Video:** [URL]
**Video ID:** [ID]
**Descargado:** [Timestamp]
**Origen:** Transcripción local (faster-whisper ASR)
**Duración:** HH:MM:SS
**Idioma:** es

---

## 📝 Transcripción Completa

[Texto transcrito por Whisper]

---

## 📊 Estadísticas

- **Palabras:** XXX
- **Caracteres:** XXX
- **Duración:** HH:MM:SS
- **Párrafos:** X

---

## 🚀 Próximos Pasos

1. Analizar con Claude (palabras clave, resumen)
2. Crear Blog Post
3. LinkedIn Article
4. Threads de Twitter
5. Clips Automáticos
```

## 🔧 Opciones Avanzadas

### Modelos Whisper Disponibles
- **tiny** (39M) - Más rápido, menos preciso
- **base** (74M) - Rápido, buena precisión
- **small** (244M) - Recomendado, balance perfecto
- **medium** (769M) - Muy preciso, más lento

### Idiomas Soportados
- es (Español)
- en (English)
- fr (Français)
- de (Deutsch)
- pt (Português)
- Y más...

### Rangos de Video
```bash
# Top 10
--top 10

# Top 50
--top 50

# Todos los videos
--all

# Rango específico (videos #11 a #20)
--batch 11-20
```

## ❌ Troubleshooting

### Error: "No se encontraron credenciales"
→ Ejecuta de nuevo y sigue el paso de autenticación

### Error: "Token expirado"
→ La skill detecta y te pide re-login automáticamente

### Error: "Video demasiado corto"
→ Saltado automáticamente (< 20 segundos)

### Error: "Video es livestream"
→ Saltado automáticamente (no se puede transcribir en vivo)

### Transcripción lenta
→ Usa modelo `tiny` o `base` en lugar de `medium`

### Falta de espacio en disco
→ Usa `--delete-audio` para eliminar MP3s después

## 📚 Próximos Pasos Después de Transcribir

Una vez tengas las transcripciones:

1. **Análisis con Claude**
   ```
   Analiza estas transcripciones y extrae:
   - 5 palabras clave por video
   - 1 resumen de 2 párrafos
   - 3 tweets principales
   ```

2. **Crear Blog Posts**
   ```
   Convierte transcripción en artículo de blog
   ```

3. **Generar Clips**
   ```
   Identifica momentos clave para clips de 30-60s
   ```

## 🔐 Seguridad & Privacy

- ✅ OAuth seguro (no pide contraseña)
- ✅ Token guardado localmente (`.env` git-ignored)
- ✅ Credenciales **nunca** se suben a Git
- ✅ Transcripción local (no se envía a terceros)
- ✅ Archivo `credentials.json` borrado tras setup

## 📞 Soporte

Si hay problemas:
1. Revisa la sección Troubleshooting
2. Verifica que `.env` existe y tiene credenciales válidas
3. Ejecuta con `--debug` para más información

## 📄 Licencia

Esta skill está disponible para reutilización en otros proyectos.
Ver instrucciones de instalación en otras máquinas.

---

**Versión:** 1.0  
**Última actualización:** 2026-07-30  
**Estado:** ✅ Producción
