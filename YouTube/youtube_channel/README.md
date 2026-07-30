# YouTube Channel Analytics

Script para extraer datos de tu canal de YouTube: videos, transcripciones, thumbnails y métricas.

## Requisitos

- Python 3.8+
- Cuenta de Google (para autenticación)

## Setup

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar Google Cloud (veremos los pasos juntos)

Necesitarás credenciales de OAuth 2.0 para acceder a la YouTube Data API.

**Los pasos son:**
1. Crear un proyecto en Google Cloud Console
2. Habilitar YouTube Data API v3
3. Crear credenciales OAuth 2.0
4. Guardar el archivo JSON en `.env`

(Te guiaré por esto cuando estemos listos)

### 3. Ejecutar el script

```bash
python main.py
```

## Output

- `data/videos.json` - Lista de todos tus videos
- `data/metrics.json` - Métricas por video
- `data/thumbnails/` - Descargas de thumbnails
- `output/analysis.md` - Análisis y recomendaciones

## Estructura

```
youtube_channel/
├── main.py           # Script principal
├── config.py         # Configuración
├── requirements.txt  # Dependencias Python
├── .env             # Credenciales (no commitear)
├── data/            # Salida de datos
└── output/          # Análisis y reportes
```
