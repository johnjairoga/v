# 📐 Especificaciones Técnicas - @johnjairo.ai

---

## 1. Dimensiones de Formato

### Carruseles (Posts principales)
```
Ancho: 1080px
Alto: 1350px
Proporción: 4:5 (Vertical)
Número máximo de slides: 10
Formato archivo: JPG (85-90% quality)
```

**Ideal para:**
- Tutoriales completos
- Procesos paso a paso
- Casos de éxito
- Argumentos de venta

---

### Reels (Videos cortos)
```
Ancho: 1080px
Alto: 1920px
Proporción: 9:16 (Full height)
Duración: 15-60 segundos
Formato archivo: MP4/WebM
```

**Ideal para:**
- Hooks impactantes
- Transformaciones visuales
- Demostraciones de herramientas
- Contenido viral

---

### Post Simple (Feed)
```
Ancho: 1080px
Alto: 1080px
Proporción: 1:1 (Cuadrado)
Formato archivo: JPG/PNG
```

**Ideal para:**
- Anuncios rápidos
- Números destacados
- Imágenes de impacto
- Teasers

---

### Story (Historias)
```
Ancho: 1080px
Alto: 1920px
Proporción: 9:16
Duración: 5-15 segundos (si es video)
Formato archivo: JPG/PNG/MP4
```

**Ideal para:**
- Teasers de posts
- Encuestas interactivas
- Behind-the-scenes
- Llamadas a acciones rápidas

---

## 2. Configuración de Color

### Perfil de Color
```
Espacio: sRGB
Gamma: 2.2
Modo: RGB (no CMYK)
```

### Compresión JPG
```
Calidad: 85-90%
Optimizar: Sí
Progressive: Sí
Tamaño máximo: 200KB (ideal 100-150KB)
```

### Compresión PNG
```
Nivel: 9 (máximo)
Entrelazado: Sí
Tamaño máximo: 150KB
```

---

## 3. Tipografía - Configuración Técnica

### Fuentes Google Fonts
```
Poppins:
  URL: https://fonts.google.com/specimen/Poppins
  Pesos: 400, 600, 700, 800
  Character set: Latin

Inter:
  URL: https://fonts.google.com/specimen/Inter
  Pesos: 400, 500, 600, 700
  Character set: Latin

Montserrat:
  URL: https://fonts.google.com/specimen/Montserrat
  Pesos: 400, 600, 700, 800
  Character set: Latin
```

### Renderizado de Texto
```
Anti-aliasing: Subpixel (Canva/Figma automático)
Ligaduras: Activadas
Kerning: Automático
Hinting: Activo
```

---

## 4. Márgenes y Espaciado

### Margen Exterior (Padding)
```
Bordes izq/der: Mínimo 40px
Borde superior: Mínimo 60px
Borde inferior: Mínimo 60px
```

### Espaciado Entre Elementos
```
Entre títulos y body: 16-24px
Entre puntos de lista: 8-12px
Entre secciones: 30-40px
Entre slides: N/A (nuevo slide)
```

### Línea Height (Interlineado)
```
Títulos (H1/H2): 1.2
Subtítulos (H3): 1.3
Body: 1.5-1.6
Números: N/A (un solo línea)
```

---

## 5. Efectos Visuales Permitidos

### Sombras
```
Permitidas: Sí (sutiles)
Color: Negro (30% opacidad)
Desenfoque: 8-12px
Offset: 0-2px vertical
Uso: Profundidad, separación de elementos
```

### Degradados
```
Permitidos: Sí (sutiles)
Tipo: Lineal (no radial)
Ángulo: 180° (vertical)
Colores: 2 máximo
Opacidad: 100% → 0% (desvanecer)
```

### Bordes
```
Ancho: 2-4px
Estilo: Sólido (no punteado)
Radio: 8-12px (redondeado)
Color: #3D5AFE, #FFB020, o #E8EBF0
```

### Transparencias
```
Permitidas: Sí (moderadas)
Fondos: 70-100% opacidad
Textos: 100% opacidad (nunca transparente)
Elementos decorativos: 30-70% opacidad
```

### Animaciones
```
En carruseles: No (son imágenes estáticas)
En reels: Sí (transiciones, efectos)
Velocidad recomendada: 0.3-0.8 segundos
Easing: Ease-in-out (suave)
```

---

## 6. Resolución & DPI

### Para Digital (Instagram)
```
Resolución: 72 DPI
Modo: RGB
Perfil: sRGB
```

### Para Impresión (Si aplica)
```
Resolución: 300 DPI
Modo: CMYK
Perfil: ISO Coated v2
```

---

## 7. Formato de Archivo - Exportación

### Carruseles & Post Simple
```
Formato: JPG
Compresión: 85-90%
Tamaño recomendado: 100-150KB por slide
Progresivo: Sí
```

### Reels & Videos
```
Formato: MP4
Códec video: H.264
Códec audio: AAC
Bitrate: 5-8 Mbps
Resolución: 1080p
Frame rate: 30fps
```

### Fuentes
```
Formato: Importar desde Google Fonts
No incrustar en imagen (usar Canva/Figma)
Si lo haces: Convertir texto a vectores
```

---

## 8. Checklist de Exportación

Antes de descargar/publicar:

- [ ] Dimensiones correctas (1080x1350 / 1080x1920)
- [ ] Formato JPG/MP4 correcto
- [ ] Calidad: 85-90% (JPG)
- [ ] Perfil de color: sRGB
- [ ] DPI: 72 (digital)
- [ ] Sin fuentes embedidas (si es JPG)
- [ ] Sin capas ocultas
- [ ] Sin elementos fuera del canvas
- [ ] Tamaño archivo: 100-200KB (ideal)
- [ ] Nombre descriptivo: PILAR_NUMERO_TITULO.jpg

---

## 9. Nombres de Archivo Recomendados

### Formato
```
[PILAR]_[NUMERO]_[TITULO_CORTO].jpg

Ejemplos:
AGENTES_001_GENERAR_LEADS.jpg
CLINICAS_002_RETENCION_PACIENTES.jpg
TUTORIALES_003_ZAPIER_BASICO.jpg
CASOS_004_$400K_90DIAS.jpg
```

### Estructura de Carpetas
```
Instagram/
├── identidade visual/
│   └── elementos/
├── carruseles/
│   ├── AGENTES_VENTA/
│   │   ├── 001_GENERAR_LEADS.jpg
│   │   ├── 002_CHATBOT_WHATSAPP.jpg
│   │   └── ...
│   ├── CLINICAS_SERVICIOS/
│   ├── TUTORIALES/
│   └── CASOS_EXITO/
└── CARRUSEL_PRUEBA_VIDEO_01.md
```

---

## 10. Guía de Publicación en Instagram

### Timing Recomendado
```
Días: Martes a viernes (mejor engagement)
Horas: 8am, 12pm, 6pm (timezone local)
Frecuencia: 1-2 posts/semana
```

### Caption Mínimo
```
Líneas: 3-5 líneas
Caracteres: 150-300
Hashtags: 8-12 (#IA, #AutomationIA, #Negocio)
CTA: Siempre presente (DM, Link bio, etc)
```

### Estructura Caption
```
Línea 1: Hook impactante
Línea 2: Beneficio o contexto
Línea 3-5: Detalles, llamada a acción
--- (separador)
#hashtags
```

### Configuración Post
```
Tipo: Carrusel (múltiples imágenes)
Descripción alternativa (alt text): Sí
Ubicación: Agrega si es relevante
Tags de personas: No (a menos que sea testimonio)
```

---

## 11. Herramientas Recomendadas

### Diseño
- **Canva Pro:** https://canva.com (templates, fuentes)
- **Figma:** https://figma.com (diseño profesional)
- **Adobe Express:** https://express.adobe.com (rápido)

### Optimización
- **TinyPNG:** https://tinypng.com (comprimir)
- **ImageOptim:** https://imageoptim.com (Mac)
- **Optimizilla:** https://optimizilla.com (web)

### Publicación
- **Buffer:** Programar posts
- **Later:** Planificar contenido
- **Meta Business Suite:** Publicar directo

---

## 12. Validación Final

Checklist antes de publicar:

- [ ] Paleta: #0B1220, #3D5AFE, #FFB020
- [ ] Tipografía: Poppins/Inter/Montserrat
- [ ] Ícono del pilar presente
- [ ] Números destacados en Ámbar
- [ ] CTA clara en último slide
- [ ] Margen 40px en laterales
- [ ] Contraste accesible (12:1+)
- [ ] Dimensiones 1080x1350
- [ ] Formato JPG, 85-90% quality
- [ ] Tamaño <200KB
- [ ] Nombre descriptivo
- [ ] Caption + hashtags listos
