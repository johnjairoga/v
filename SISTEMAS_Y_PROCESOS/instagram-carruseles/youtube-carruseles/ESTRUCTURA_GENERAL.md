# 🗂️ Estructura General: youtube-carruseles

## Propósito
Organizar todos los carruseles creados desde transcripciones de videos de YouTube en un único lugar, fácil de navegar y mantener.

---

## 📁 Estructura Actual

```
youtube-carruseles/
│
└── 01_Crear una Landing Page con IA en Minutos sin saber programar/
    ├── 📁 carruseles/
    │   ├── CARRUSEL_1_GANA_1000.html
    │   ├── CARRUSEL_2_VIDEO_A_LANDING.html
    │   ├── CARRUSEL_3_MI_DESCUBRIMIENTO.html ⭐
    │   ├── CARRUSEL_4_COMO_APRENDI.html
    │   └── CARRUSEL_5_AGENCIA_IA.html
    │
    ├── 📁 png_exportadas/
    │   ├── CARRUSEL_1/ (vacío - listo para PNG)
    │   ├── CARRUSEL_2/ (vacío - listo para PNG)
    │   ├── CARRUSEL_3/ (vacío - listo para PNG)
    │   ├── CARRUSEL_4/ (vacío - listo para PNG)
    │   └── CARRUSEL_5/ (vacío - listo para PNG)
    │
    └── 📄 README.md (info del video + status)
```

---

## 🚀 Próximas Carpetas (Próximos Videos)

Cuando creemos carruseles de otros videos de YouTube, seguiremos esta estructura:

```
youtube-carruseles/
├── 01_Crear una Landing Page con ía en Minutos sin saber programar/
│   ├── carruseles/
│   ├── png_exportadas/
│   └── README.md
│
├── 02_[PRÓXIMO VIDEO]/
│   ├── carruseles/
│   ├── png_exportadas/
│   └── README.md
│
├── 03_[OTRO VIDEO]/
│   ├── carruseles/
│   ├── png_exportadas/
│   └── README.md
│
└── ESTRUCTURA_GENERAL.md (este archivo)
```

---

## 📋 Cómo Encontrar Carruseles

### Buscar carruseles de un video específico:
```
youtube-carruseles/[NOMBRE_VIDEO]/carruseles/
```

**Ejemplo:**
```
youtube-carruseles/01_Crear una Landing Page con ía en Minutos sin saber programar/carruseles/
```

### Buscar PNG exportados:
```
youtube-carruseles/[NOMBRE_VIDEO]/png_exportadas/CARRUSEL_X/
```

**Ejemplo:**
```
youtube-carruseles/01_Crear una Landing Page con ía en Minutos sin saber programar/png_exportadas/CARRUSEL_3/
```

### Información del video:
```
youtube-carruseles/[NOMBRE_VIDEO]/README.md
```

---

## ✅ Ventajas de Esta Estructura

1. **Organizado por video:**
   - Todos los carruseles de un video en una carpeta
   - No se mezclan contenidos de videos diferentes

2. **Rápido de encontrar:**
   - Buscar por nombre de transcripción
   - Ubicación consistente siempre

3. **HTML + PNG juntos:**
   - Fuente HTML en carruseles/
   - Exportados PNG en png_exportadas/
   - Ambos en el mismo lugar

4. **Documentado:**
   - Cada carpeta tiene README.md
   - Info de video, ángulos, status

5. **Escalable:**
   - Para 5 videos, 10 videos, 100 videos
   - Misma estructura, mismo lugar

---

## 📍 Ubicación Completa

```
c:\Users\John\Desktop\John Jairo\Youtube\v\v\
  └── SISTEMAS_Y_PROCESOS\
      └── instagram-carruseles\
          └── youtube-carruseles\ ⬅️ AQUÍ ESTÁN TODOS LOS CARRUSELES
              └── [NOMBRE_VIDEO]/
                  ├── carruseles/
                  ├── png_exportadas/
                  └── README.md
```

---

## 🎯 Checklist: Agregar Nuevo Video

Cuando pidas crear carruseles desde un nuevo video:

- [ ] Identifica la transcripción (ubicación: @Redes sociales/YouTube/...)
- [ ] Copia el nombre exacto de la transcripción
- [ ] Crea carpeta: `youtube-carruseles/[NOMBRE]/`
- [ ] Dentro: crea `carruseles/` y `png_exportadas/`
- [ ] Dentro de `png_exportadas/`: crea `CARRUSEL_1/`, `CARRUSEL_2/`, etc.
- [ ] Crea `README.md` en la carpeta del video
- [ ] Genera 5 carruseles HTML (CARRUSEL_1 a CARRUSEL_5)
- [ ] Exporta PNG a `png_exportadas/CARRUSEL_X/`
- [ ] Actualiza README.md con status

---

## 📝 Nombres Consistentes

**Nombre de carpeta principal:**
```
EXACTAMENTE el nombre del archivo de transcripción (sin .md)

Ejemplo:
✅ 01_Crear una Landing Page con ía en Minutos sin saber programar
❌ 01_crear una landing page
❌ landing page video
❌ video 1
```

**Nombres de carruseles:**
```
CARRUSEL_[NUMBER]_[ANGULO_MAYUSCULAS].html

Ejemplo:
✅ CARRUSEL_1_GANA_1000.html
✅ CARRUSEL_3_MI_DESCUBRIMIENTO.html
❌ carrusel1.html
❌ video_carousel.html
```

---

## 🔗 Links Importantes

**Ubicación de esta carpeta:**
```
c:\Users\John\Desktop\John Jairo\Youtube\v\v\SISTEMAS_Y_PROCESOS\instagram-carruseles\youtube-carruseles\
```

**Ubicación de transcripciones:**
```
@Redes sociales\YouTube\videos de youtube\transcripciones_top_videos\
```

**Documentación de reglas:**
```
SISTEMAS_Y_PROCESOS/instagram-carruseles/ESTRUCTURA_CARPETAS_REGLA.md
```

---

## ⚠️ Importante

✅ **Carruseles nuevos:** Aquí en `youtube-carruseles/`
❌ **NO:** En `ejemplos/` (esa carpeta es de referencia, solo lectura)

Todos los carruseles de YouTube DEBEN estar en `youtube-carruseles/[NOMBRE_VIDEO]/`

---

**Última actualización:** 2026-07-31
**Status:** Sistema de carpetas activo
**Versión:** 1.0
