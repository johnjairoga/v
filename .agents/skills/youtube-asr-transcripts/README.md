# 🎬 YouTube ASR Transcripts Skill

Transcribe videos de YouTube **sin depender de subtítulos**, usando Whisper ASR (reconocimiento de voz automático).

## 🚀 Inicio Rápido

### En el Proyecto Actual
```bash
/youtube-asr-transcripts
```

Sigue los pasos guiados.

### En Otro Proyecto

#### Opción B: Clonar desde GitHub

```bash
# En tu nuevo proyecto:
cd /ruta/nuevo-proyecto

# Clonar la skill
git clone https://github.com/tu-usuario/v.git /tmp/youtube-asr-repo

# Copiar solo la skill
cp -r /tmp/youtube-asr-repo/.agents/skills/youtube-asr-transcripts/ \
      ./.agents/skills/

# Limpiar
rm -rf /tmp/youtube-asr-repo

# Ahora funciona:
/youtube-asr-transcripts
```

## 📋 Requisitos

- Python 3.8+
- Cuenta Google (para OAuth)
- Canal YouTube asociado
- ~2GB disco para modelo Whisper

## 🔧 Instalación de Dependencias

```bash
pip install yt-dlp faster-whisper google-auth-oauthlib google-auth-httplib2 google-api-python-client youtube-transcript-api
```

O:
```bash
pip install -r requirements.txt  # Si existe en el proyecto
```

## 🔐 Configuración (Primera Vez)

La skill te guía paso a paso, pero aquí está el resumen:

### 1. Crear Google Cloud Project
- Ve a https://console.cloud.google.com/
- Login con el email del canal YouTube
- Crea nuevo proyecto
- Habilita YouTube Data API v3

### 2. Crear Credenciales OAuth
- En Google Cloud: Credentials → Create Credentials
- Tipo: Desktop application
- Descarga archivo JSON

### 3. Cargar en Skill
La skill te pide subir `credentials.json`
- Se guarda en `.env` (privado, git-ignored)
- Se valida automáticamente

## 📖 Uso

### Flujo Interactivo (Recomendado)
```bash
/youtube-asr-transcripts
```

Sigue los pasos:
1. Verifica credenciales
2. Selecciona cantidad de videos
3. Elige configuración
4. Espera resultados

### CLI Directo

```bash
# Top 10 videos
python .agents/skills/youtube-asr-transcripts/scripts/run.py transcribe --top 10

# Top 50 con modelo medium
python .agents/skills/youtube-asr-transcripts/scripts/run.py transcribe --top 50 --model medium

# Rango específico (videos #11-20)
python .agents/skills/youtube-asr-transcripts/scripts/run.py transcribe --batch 11-20

# Todos los videos
python .agents/skills/youtube-asr-transcripts/scripts/run.py transcribe --all

# Setup inicial
python .agents/skills/youtube-asr-transcripts/scripts/run.py setup

# Validar autenticación
python .agents/skills/youtube-asr-transcripts/scripts/run.py test
```

## 📁 Estructura de Archivos

```
tu-proyecto/
├── .agents/
│   └── skills/
│       └── youtube-asr-transcripts/  ← Esta skill
│           ├── SKILL.md
│           ├── README.md
│           ├── scripts/
│           │   └── run.py
│           └── prompts/
│               └── guide.md
│
├── .env                             ← Credenciales (git-ignored)
├── .gitignore                       ← Incluye: .env, token.pickle
└── videos de youtube/
    ├── audio_mp3/                   ← MP3 descargados
    └── transcripciones_top_videos/  ← Markdown generados
```

## 🔒 Seguridad

- ✅ OAuth (no pide contraseña Gmail)
- ✅ Credenciales en `.env` (git-ignored)
- ✅ Token guardado localmente
- ✅ Nunca se sube a repositorio público
- ✅ Transcripción local (no se envía a terceros)

## 📊 Salida

Para cada video, genera Markdown con:
- Transcripción completa
- Estadísticas (palabras, caracteres, duración)
- Metadata (Video ID, fecha, idioma)
- Próximos pasos sugeridos

Ejemplo:
```
📁 videos de youtube/transcripciones_top_videos/
├── 01_Video_Titulo_1.md
├── 02_Video_Titulo_2.md
└── 03_Video_Titulo_3.md
```

## ⚙️ Configuración (.env)

Crear `.env` en raíz del proyecto:

```bash
# Google OAuth (obtén en Google Cloud Console)
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:8080/

# Whisper (opcional)
WHISPER_MODEL_SIZE=small
WHISPER_DEVICE=cpu
WHISPER_COMPUTE_TYPE=int8

# Salida
KEEP_AUDIO_AFTER_TRANSCRIPT=true
OUTPUT_LANGUAGE=es
```

## 🛠️ Troubleshooting

### "No se encontraron credenciales"
→ Ejecuta setup: `python scripts/run.py setup`

### "Token expirado"
→ La skill lo detecta automáticamente y pide re-login

### "Video demasiado corto"
→ Saltado automáticamente (< 20 segundos)

### "Transcripción lenta"
→ Usa modelo `tiny` o `base` en lugar de `medium`

### "Falta espacio en disco"
→ Usa `--delete-audio` para eliminar MP3s después

## 📝 Próximos Pasos

Una vez tengas las transcripciones:

1. **Analizar con Claude**
   ```
   Analiza estas transcripciones y extrae palabras clave, resúmenes
   ```

2. **Crear contenido**
   - Blog posts
   - LinkedIn articles
   - Twitter threads

3. **Generar clips**
   - Identificar momentos clave
   - Crear videos cortos para redes

## 📚 Documentación Completa

Ver `SKILL.md` para:
- Explicación detallada del flujo
- Requisitos completospaso
- Variables de entorno
- Opciones avanzadas
- Modelos Whisper disponibles

Ver `prompts/guide.md` para:
- Instrucciones completas para Claude
- Flujos de interacción
- Manejo de errores
- Ejemplos de diálogos

## 💡 Tips & Tricks

### Para máxima precisión
```bash
python scripts/run.py transcribe --top 10 --model medium
```

### Para máxima velocidad
```bash
python scripts/run.py transcribe --top 10 --model tiny --delete-audio
```

### Para análisis completo
```bash
python scripts/run.py full --top 50
```

## 📞 Soporte

Si tienes problemas:
1. Revisa la sección Troubleshooting
2. Verifica que `.env` existe y tiene credenciales válidas
3. Ejecuta con `--debug` para más información

## 📄 Licencia

Disponible para reutilización en otros proyectos.

---

**Versión:** 1.0  
**Última actualización:** 2026-07-30  
**Estado:** ✅ Producción
