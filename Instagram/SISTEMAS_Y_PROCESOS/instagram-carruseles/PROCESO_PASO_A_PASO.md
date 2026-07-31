# Proceso de Creación de Carruseles Instagram - Guía Práctica

## 📋 Estructura Base (Reutilizable)

### Dimensiones
- **Tamaño por slide:** 1080x1350px
- **Total slides recomendado:** 7 (Hook + 5 Dicas + CTA)
- **Gap entre slides:** 32px
- **Border-radius:** 3xl (24px)
- **Padding:** p-20 (80px)

### Paleta de Colores (Tu Identidad)
```
Teal Oscuro:    #1a5f5f
Verde Lima:     #7DD3C0
Verde Claro:    #C5E8E3
Blanco:         #FFFFFF
```

### Tipografía
- **Fuentes:** Poppins (body), Space Grotesk (headings), JetBrains Mono (code)
- **Números:** text-7xl, font-black
- **Títulos:** text-5xl, font-bold
- **Descripción:** text-2xl, font-light
- **Regla CSS crítica:** `text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);` en todo el texto

---

## 🎬 Paso 1: STORYTELLING (Estructura Narrativa)

### Arc narrativo de 7 slides:

| Slide | Tipo | Patrón | Objetivo |
|-------|------|--------|----------|
| 1 | **Hook** | Top/Bottom con logo | Identificar el problema/pain point |
| 2-6 | **Dicas** | Centralizado | Presentar soluciones/pasos |
| 7 | **CTA** | Centralizado | Call-to-action + invitación |

### Fórmula de storytelling:
1. **Slide 1:** "Pierdo 3h diarias EN [PAIN POINT ESPECÍFICO]"
2. **Slides 2-6:** "Primero... Luego... Después... Los... Finalmente..."
3. **Slide 7:** "Recuperé [RESULTADO]. Tú también puedes."

---

## 🎨 Paso 2: DISEÑO (Estructura HTML)

### Patrón de Slide Centralizado (Slides 2-6):
```html
<div class="slide relative bg-gradient-to-br from-[#F8FFFE] to-[#E8F5F2] text-[#1a5f5f] flex flex-col items-center justify-center p-20 shadow-2xl rounded-3xl overflow-hidden">
    <!-- Elementos decorativos -->
    <div class="blob-1 -top-32 -right-32 opacity-30"></div>
    <div class="blob-2 -bottom-20 -left-20 opacity-25"></div>
    <div class="grid-pattern opacity-40"></div>
    
    <!-- Logo watermark -->
    <div class="absolute bottom-8 right-8 w-32 h-32 opacity-10 pointer-events-none">
        <!-- SVG del logo -->
    </div>

    <!-- Contenido centralizado -->
    <div class="relative z-10 flex flex-col items-center justify-center gap-8 w-full max-w-2xl">
        <!-- Top: Número + Título + Descripción -->
        <div class="text-center">
            <div class="text-7xl font-black mb-6">01</div>
            <h2 class="text-5xl font-bold mb-8">Título</h2>
            <p class="text-2xl leading-relaxed">Descripción</p>
        </div>
        
        <!-- Bottom: Resultado -->
        <div class="bg-gradient-to-br from-[#1a5f5f] to-[#0f4d4d] p-6 rounded-2xl w-full">
            <!-- Contenido de resultado -->
        </div>
    </div>
</div>
```

### Elementos decorativos CSS (Agregar a <style>):
```css
.blob-1 {
    position: absolute;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle at 30% 50%, rgba(125, 211, 192, 0.3), transparent 50%);
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    filter: blur(40px);
    pointer-events: none;
}

.grid-pattern {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: /* líneas sutiles */;
    opacity: 0.5;
    pointer-events: none;
}
```

### Colores por slide:
- **Slide 1 (Cover):** Dark teal bg-[#1a5f5f]
- **Slide 2:** Light bg-gradient-to-br from-[#F8FFFE] to-[#E8F5F2]
- **Slide 3:** Dark teal gradient
- **Slide 4:** Light gradient
- **Slide 5:** Dark teal gradient
- **Slide 6:** Light gradient
- **Slide 7:** CTA gradient from-[#0D9488] via-[#1a5f5f] to-[#0f3d3d]

---

## 🔄 Paso 3: FLUJO DE TRABAJO

### 3.1. Preparación
- [ ] Definir el tema/tópico del carrusel
- [ ] Identificar el público objetivo
- [ ] Crear la narrativa (pain point → solución → CTA)
- [ ] Escribir el copy para cada slide

### 3.2. Crear HTML
- [ ] Copiar template base de carousel.html
- [ ] Reemplazar copy en cada slide
- [ ] Mantener estructura centralizada
- [ ] Asegurar colores alineados

### 3.3. Validar Contraste
- [ ] Textos visibles en fondos claros/oscuros
- [ ] Verificar que text-shadow funciona
- [ ] Revisar en navegador (zoom 100%)

### 3.4. Centralización
- [ ] Todos los contenidos en el MEDIO del slide
- [ ] Usar `items-center justify-center` en contenedor principal
- [ ] Gap consistente entre elementos (gap-8)
- [ ] Max-width en contenedor de contenido (max-w-2xl)

### 3.5. Agregar Logo
- [ ] Posicionar en esquina inferior derecha (bottom-8 right-8)
- [ ] Opacidad 10% (opacity-10)
- [ ] SVG del logo jr-ai
- [ ] Color ajustado al slide

### 3.6. Export a PNG
```bash
python export_superdesign_carousel.py \
  Instagram/Skill-ig-carruseles/instagram-carrossel/conteudos/[FECHA]/carousel.html \
  Instagram/Skill-ig-carruseles/instagram-carrossel/conteudos/[FECHA]/slides/
```

---

## ✅ Checklist de Validación Final

- [ ] **Contenido:** 7 slides con narrativa clara
- [ ] **Storytelling:** Hook → Solución (5 steps) → CTA
- [ ] **Contraste:** Todos los textos legibles
- [ ] **Centralización:** Todo centrado en el medio
- [ ] **Tipografía:** Números grandes, títulos medianos, descripción legible
- [ ] **Colores:** Alineados a identidad visual (teal/verde)
- [ ] **Logo:** Watermark en esquina inferior derecha
- [ ] **Consistencia:** Todos los slides tienen el mismo patrón
- [ ] **Padding/Spacing:** Consistente (p-20, gap-8, mb-8)
- [ ] **Sombras:** Text-shadow en todos los textos

---

## 📐 Medidas y Espaciado (Referencia)

```
Slide completo:     1080x1350px
Padding:            p-20 (80px en cada lado)
Área de contenido:  1080 - 160 = 920px ancho
Max-width:          max-w-2xl (672px)

Números:            text-7xl
Títulos:            text-5xl (con mb-8 abajo)
Descripción:        text-2xl (con leading-relaxed)
Gap entre secciones: gap-8

Logo:               w-32 h-32 (128x128px)
Opacidad:           opacity-10
Posición:           bottom-8 right-8
```

---

## 🎯 Próxima Ejecución - Resumen Rápido

1. Copiar la estructura base de [carousel.html]
2. Reemplazar el copy (títulos + descripciones)
3. Mantener la estructura de divs
4. Validar contraste de colores
5. Verificar centralización
6. Agregar logo (SVG)
7. Exportar a PNG

**Tiempo estimado:** 30-45 minutos por carrusel nuevo

---

## 🔗 Archivos de Referencia

- **Template HTML:** `carousel.html`
- **Script de export:** `export_superdesign_carousel.py`
- **Logo SVG:** `Instagram/identidade visual/Elementos/logo-jr-ai.svg`
- **Paleta de colores:** `Instagram/identidade visual/BRAND_KIT_ACTUALIZADO.md`
