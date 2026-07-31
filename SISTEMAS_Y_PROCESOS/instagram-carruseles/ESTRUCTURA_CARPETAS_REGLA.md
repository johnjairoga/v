# 📋 REGLA: Estructura de Carpetas para Carruseles de YouTube

## Propósito
Mantener todos los carruseles creados desde transcripciones de videos de YouTube **organizados y rápidos de encontrar**.

---

## 🗂️ Estructura Obligatoria

**Cada carrusel creado desde un video de YouTube sigue esta estructura:**

```
SISTEMAS_Y_PROCESOS/instagram-carruseles/youtube-carruseles/
│
└── [NOMBRE_TRANSCRIPCION]/
    ├── 📁 carruseles/
    │   ├── CARRUSEL_1_[ANGULO].html
    │   ├── CARRUSEL_2_[ANGULO].html
    │   ├── CARRUSEL_3_[ANGULO].html
    │   ├── CARRUSEL_4_[ANGULO].html
    │   └── CARRUSEL_5_[ANGULO].html
    │
    ├── 📁 png_exportadas/
    │   ├── CARRUSEL_1/
    │   │   ├── slide_1.png
    │   │   ├── slide_2.png
    │   │   └── ...
    │   ├── CARRUSEL_2/
    │   ├── CARRUSEL_3/
    │   ├── CARRUSEL_4/
    │   └── CARRUSEL_5/
    │
    └── 📄 README.md
        (Información: video fuente, ángulos, status)
```

---

## 📝 Nomenclatura

### Nombre de Carpeta Principal
```
[NOMBRE_TRANSCRIPCION]

Ejemplo:
✅ 01_Crear una Landing Page con IA en Minutos sin saber programar
✅ 02_5 Dicas de Claude Code
✅ 03_Cómo Crear un Blog con IA en 30 Minutos
```

**Regla:** Exactamente el mismo nombre que el archivo de transcripción (sin la extensión .md)

### Archivos HTML
```
CARRUSEL_[NUMERO]_[ANGULO_EN_MAYUSCULAS].html

Ejemplo:
✅ CARRUSEL_1_GANA_1000.html
✅ CARRUSEL_2_VIDEO_A_LANDING.html
✅ CARRUSEL_3_MI_DESCUBRIMIENTO.html
✅ CARRUSEL_4_COMO_APRENDI.html
✅ CARRUSEL_5_AGENCIA_IA.html
```

### Carpeta PNG
```
png_exportadas/
  ├── CARRUSEL_1/
  ├── CARRUSEL_2/
  └── ...

Archivo PNG individual:
slide_1.png, slide_2.png, ..., slide_7.png
```

---

## 📂 Ejemplo Completo

```
youtube-carruseles/
│
├── 01_Crear una Landing Page con IA en Minutos sin saber programar/
│   ├── carruseles/
│   │   ├── CARRUSEL_1_GANA_1000.html
│   │   ├── CARRUSEL_2_VIDEO_A_LANDING.html
│   │   ├── CARRUSEL_3_MI_DESCUBRIMIENTO.html
│   │   ├── CARRUSEL_4_COMO_APRENDI.html
│   │   └── CARRUSEL_5_AGENCIA_IA.html
│   ├── png_exportadas/
│   │   ├── CARRUSEL_1/
│   │   │   ├── slide_1.png
│   │   │   ├── slide_2.png
│   │   │   ├── slide_3.png
│   │   │   ├── slide_4.png
│   │   │   ├── slide_5.png
│   │   │   ├── slide_6.png
│   │   │   └── slide_7.png
│   │   ├── CARRUSEL_2/
│   │   ├── CARRUSEL_3/
│   │   ├── CARRUSEL_4/
│   │   └── CARRUSEL_5/
│   └── README.md
│
├── 02_5 Dicas de Claude Code/
│   ├── carruseles/
│   ├── png_exportadas/
│   └── README.md
│
└── 03_Próximo Video/
    ├── carruseles/
    ├── png_exportadas/
    └── README.md
```

---

## 📋 README.md (Plantilla)

Cada carpeta de video tiene un README.md con:

```markdown
# [NOMBRE_VIDEO]

## 📹 Información del Video
- **Transcripción:** @Redes sociales/YouTube/...
- **Fecha creación:** 2026-07-31
- **Ángulos explorados:** 5

## 🎨 Carruseles Creados
- ✅ CARRUSEL_1: [Descripción corta]
- ✅ CARRUSEL_2: [Descripción corta]
- ✅ CARRUSEL_3: [Descripción corta] ⭐
- ✅ CARRUSEL_4: [Descripción corta]
- ✅ CARRUSEL_5: [Descripción corta]

## 📊 Status
- HTML: Listos ✅
- PNG: [Parcial/Completo]
- Publicados: [Número]

## 📝 Notas
[Información relevante, lecciones aprendidas, etc]
```

---

## 🚀 Proceso Paso a Paso

### Cuando pidas generar carruseles desde transcripción:

1. **Identificar transcripción de video**
   ```
   Ubicación: @Redes sociales/YouTube/videos de youtube/transcripciones_top_videos/
   Archivo: [NOMBRE_TRANSCRIPCION].md
   ```

2. **Crear estructura**
   ```
   youtube-carruseles/
   └── [NOMBRE_TRANSCRIPCION]/
       ├── carruseles/
       ├── png_exportadas/
       └── README.md
   ```

3. **Generar carruseles HTML**
   ```
   Guardar en: youtube-carruseles/[NOMBRE]/carruseles/
   Archivos: CARRUSEL_1_[ANGULO].html hasta CARRUSEL_5_[ANGULO].html
   ```

4. **Exportar PNG**
   ```
   Guardar en: youtube-carruseles/[NOMBRE]/png_exportadas/CARRUSEL_X/
   Estructura: slide_1.png ... slide_7.png
   ```

5. **Actualizar README.md**
   ```
   Documentar: video fuente, ángulos, status, notas
   ```

---

## ✅ Checklist de Organización

Antes de dar por completo un video:

- [ ] Carpeta principal con nombre exacto de transcripción
- [ ] Subcarpeta `carruseles/` con 5 HTML
- [ ] Subcarpeta `png_exportadas/` con carpetas por carrusel
- [ ] Cada carrusel tiene 7 PNG (slide_1.png a slide_7.png)
- [ ] README.md completado
- [ ] Nombres siguen patrón: CARRUSEL_X_[ANGULO].html
- [ ] Todos los archivos en la ruta correcta

---

## 🔗 Ubicación Final

```
c:\Users\John\Desktop\John Jairo\Youtube\v\v\SISTEMAS_Y_PROCESOS\instagram-carruseles\youtube-carruseles\
```

**Este es el lugar ÚNICO donde se guardan todos los carruseles de YouTube.**

---

## ⚠️ Reglas Importantes

1. **Una transcripción = Una carpeta**
   - No mezcles videos diferentes en la misma carpeta
   - No duplices carruseles en múltiples carpetas

2. **Nombres exactos**
   - El nombre de la carpeta DEBE coincidir con el nombre del archivo de transcripción
   - Sin cambios, sin abreviaturas

3. **Siempre HTML + PNG**
   - Los HTML son la fuente (editables)
   - Los PNG son los exportados (para Instagram)
   - Mantén ambos sincronizados

4. **README obligatorio**
   - Documenta qué hay en cada carpeta
   - Actualiza el status cuando publiques

---

## 📍 Acceso Rápido

**Para encontrar carruseles de un video:**
```
youtube-carruseles/[NOMBRE_VIDEO]/carruseles/
```

**Para encontrar PNG listos:**
```
youtube-carruseles/[NOMBRE_VIDEO]/png_exportadas/
```

---

**Última actualización:** 2026-07-31
**Status:** Regla oficial para nuevos carruseles
**Aplicable a:** Todos los videos de YouTube que transcribamos
