# Sistema de Carruseles Instagram @johnjairo.ai

## 🎯 Propósito
Crear carruseles de Instagram profesionales y con alta tasa de engagement mediante storytelling personal.

## ⚡ Regla Cardinal
**TODOS los carruseles DEBEN ser storytelling en PRIMERA PERSONA**

Esto significa:
- Usar "Yo", "Descubrí", "Gané", "Aprendí", "Mi" en lugar de "La gente", "Se puede", "Es posible"
- Contar tu historia personal: problema → solución → transformación → invitación
- Conectar emocionalmente: mostrar vulnerabilidad, epifanía, resultados tangibles
- Estructura: Hook personal → Viaje (pasos/dicas) → Transformación → CTA invitando al audience a su propia jornada

**Ejemplo correcto:** "Lancé mi agencia IA" vs **Incorrecto:** "Cómo lanzar una agencia IA"

---

## 🎨 Especificaciones Técnicas

### Dimensiones
- **Por slide:** 1080px × 1350px
- **Total:** 7 slides por carrusel (1 hook + 5 pasos/dicas + 1 CTA)

### Paleta de Colores (Identidad Visual)
- **Teal Oscuro:** #1a5f5f (fondo principal, slides oscuros)
- **Verde Lima:** #7DD3C0 (acentos, botones)
- **Verde Claro:** #C5E8E3 (contraste de texto, detalles)
- **Blanco:** #FFFFFF (texto principal)

### Reglas de Contraste
- Texto principal: Blanco (#FFFFFF) o Verde Claro (#C5E8E3)
- Text-shadow global: `0 2px 8px rgba(0, 0, 0, 0.3)`
- En slides claros: usar Teal Oscuro (#1a5f5f) para heading
- En slides oscuros: usar gradientes (Verde Lima → Verde Claro)

### Tipografía
- **Headings (h1, h2):** Space Grotesk, 700 bold
- **Body text:** Poppins (regular para párrafos)
- **Código/detalles:** JetBrains Mono para datos técnicos

### Diseño Visual
- **Blur/Glow:** usar blob-1 y blob-2 para efectos de fondo
- **Grid pattern:** patrón sutil de grid en fondo (5% opacity)
- **Centralization:** flex flex-col items-center justify-center + gap-8 + max-w-2xl
- **Emojis:** mantener como visuales principales para segmentar temas
- **Iconografía:** Lucide icons para elementos adicionales

---

## 📋 Estructura de 7 Slides

### Slide 1 - Hook
- **Fondo:** Teal Oscuro + gradiente
- **Contenido:** Pregunta o afirmación fuerte en PRIMERA PERSONA
- **Emojis:** Opcional, si refuerza el tema
- **CTA:** "Desliza →" con indicadores de progreso

### Slides 2-6 - Narrativa Personal (5 pasos/momentos)
Patrón alternado (claro → oscuro → claro → oscuro → claro):
- **Slide par (2, 4, 6):** Fondo claro (#F8FFFE → #E8F5F2)
- **Slide impar (3, 5):** Fondo oscuro (teal)
- **Contenido:** 
  - Emoji grande (emojis que refuerzan emoción: 😕 problema, 💡 idea, 🎯 acción, 🚀 resultado, 💰 beneficio)
  - Heading de 2-3 palabras
  - Párrafo de 1-2 líneas en contexto personal
  - Visual adicional: grid, barras, líneas de progreso, etc.

### Slide 7 - CTA
- **Fondo:** Verde oscuro con gradiente (from-[#0D9488] via-[#1a5f5f] to-[#0f3d3d])
- **Contenido:**
  - Icono destacado en botón blurred
  - Heading: "Yo lo hice. Tú también." (invitación a su jornada)
  - CTA principal: Botón verde lima con flecha
  - CTAs secundarias: Me gustó, Guardar (grid 2 cols)
  - Footer: @johnjairo.ai + número del carrusel

---

## 📁 Estructura de Archivos

```
instagram-carruseles/
├── README.md (este archivo)
├── TEMPLATE_CAROUSEL.html (plantilla en blanco para copiar)
├── PROCESO_PASO_A_PASO.md (guía detallada de creación)
└── ejemplos/
    ├── 2026-07-31-5-dicas-claude-code/
    │   ├── carousel.html (carrusel final)
    │   └── NOTAS.md (lecciones aprendidas)
    ├── CARRUSEL_1_GANA_1000.html (ángulo: ingresos)
    ├── CARRUSEL_2_VIDEO_A_LANDING.html (ángulo: velocidad)
    ├── CARRUSEL_3_MI_DESCUBRIMIENTO.html ⭐ (ángulo: descubrimiento)
    ├── CARRUSEL_4_COMO_APRENDI.html (ángulo: aprendizaje)
    └── CARRUSEL_5_AGENCIA_IA.html (ángulo: emprendimiento)
```

---

## 🚀 Cómo Crear un Nuevo Carrusel

### Paso 1: Identifica el Ángulo Personal
- ¿Cuál es TU historia en relación al contenido?
- Problema personal → Solución → Transformación personal
- Ejemplos: "Descubrí", "Lancé", "Aprendí", "Gané", "Cambié"

### Paso 2: Estructura los 5 Pasos (Slides 2-6)
Cada paso debe ser TU viaje:
1. **Problema:** Emoción inicial (😕 o similar)
2. **Epifanía:** Momento "aha" (💡)
3. **Acción:** Qué hiciste TÚ (🎯)
4. **Resultado:** Lo que pasó (🚀)
5. **Transformación:** Cómo cambió tu vida (💰 o similar)

### Paso 3: Copia TEMPLATE_CAROUSEL.html
Usa como punto de partida.

### Paso 4: Personaliza
- Reemplaza contenido en cada slide
- Respeta paleta de colores y estructura
- Mantén emojis y estilos visuales
- Prueba en navegador (abre HTML)

### Paso 5: Exporta a PNG
Usa Playwright script o herramienta de screenshot:
```bash
# Abre HTML en navegador, posiciona cada slide, exporta como PNG
# 1080 × 1350px por imagen
```

---

## ✅ Checklist de Validación

Antes de exportar cada carrusel, verifica:

- [ ] **Primera persona:** Toda narrativa usa "Yo/Mi" (no "Se puede/Es posible")
- [ ] **Emojis claros:** Cada slide 2-6 tiene emoji que refleja emoción/acción
- [ ] **Colores correctos:** Teal, Verde Lima, Verde Claro, Blanco (sin azules/naranjas)
- [ ] **Contraste:** Texto visible en todos los fondos
- [ ] **Text-shadow:** CSS rule aplicada a p, h1, h2, h3, span
- [ ] **Centralización:** Contenido centrado (flex items-center justify-center)
- [ ] **Slide 1:** Hook fuerte, "Desliza →"
- [ ] **Slides 2-6:** Alternancia color, estructura emoji + heading + párrafo + visual
- [ ] **Slide 7:** CTA clara, "Yo lo hice. Tú también.", botón principal + secundarios
- [ ] **Branding:** Logo/watermark si aplica, @johnjairo.ai en footer

---

## 🎬 Ángulos de Carruseles Disponibles

Los 5 carruseles iniciales (del video "Crear Landing Page con IA en Minutos"):

1. **CARRUSEL_1_GANA_1000.html** — "Gana $1000+ creando landing pages"
2. **CARRUSEL_2_VIDEO_A_LANDING.html** — "De video a landing en 30 minutos"
3. **CARRUSEL_3_MI_DESCUBRIMIENTO.html** ⭐ — "Descubrí la fórmula"
4. **CARRUSEL_4_COMO_APRENDI.html** — "Así que aprendí a crear websites sin código"
5. **CARRUSEL_5_AGENCIA_IA.html** — "Lancé mi agencia IA"

**Recomendación:** Comienza con CARRUSEL_3 (mejor ejecución de storytelling en primera persona).

---

## 📚 Referencias
- Ver TEMPLATE_CAROUSEL.html para estructura HTML completa
- Ver PROCESO_PASO_A_PASO.md para detalles de diseño paso a paso
- Ver ejemplos/ para referencia visual de cada ángulo

**Pregunta guía para cada nuevo carrusel:** "¿Cuál es MI historia aquí?" — Si no puedes responderla en primera persona, reconceptualiza el ángulo.
