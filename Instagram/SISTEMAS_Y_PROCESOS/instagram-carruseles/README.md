# 📱 Instagram Carruseles - Sistema Reutilizable

**Ubicación centralizada:** `C:\Users\John\Desktop\John Jairo\Youtube\v\v\SISTEMAS_Y_PROCESOS\instagram-carruseles\`

Sistema completo para crear carruseles Instagram profesionales. Documentado, testeado y listo para reutilizar.

---

## 🎯 Resumen Ejecutivo

- **Estructura:** 7 slides (Hook + 5 Tips + CTA)
- **Storytelling:** Problema → Solución → Resultado
- **Diseño:** Centralizado, moderno, con identidad visual
- **Export:** PNG 1080x1350px automático
- **Tiempo:** 50-70 minutos por carrusel
- **Reutilizable:** Sí, por cualquier proyecto

---

## 📂 Contenidos de Esta Carpeta

```
instagram-carruseles/
├── README.md                           (Este archivo)
├── TEMPLATE_CAROUSEL.html              (HTML vacío, copiar y llenar)
├── PROCESO_PASO_A_PASO.md             (Guía detallada)
├── ejemplos/
│   └── 2026-07-31-5-dicas-claude-code/
│       ├── carousel.html               (Ejemplo exitoso)
│       └── NOTAS.md                    (Lo que funcionó)
└── recursos/
    ├── logo-jr-ai.svg                  (Logo para watermark)
    ├── export_script.py                (Script para exportar PNG)
    └── PALETA_COLORES.md              (Colores de identidad)
```

---

## 🚀 Inicio Rápido (3 Pasos)

### Paso 1: Copiar Template
```bash
cp TEMPLATE_CAROUSEL.html mi-carrusel.html
```

### Paso 2: Llenar Contenido
Abre `mi-carrusel.html` y reemplaza:
- `Tu Hook Aquí` → Tu problema específico
- `Primer Paso` → Tu tip 1
- `Tu Resultado Final` → Tu transformación
- `@tu_usuario` → Tu usuario

### Paso 3: Validar y Exportar
1. Abre en navegador: `file:///path/mi-carrusel.html`
2. Valida con checklist (abajo)
3. Exporta: `python export_script.py mi-carrusel.html ./slides/`

**Total: 50-70 minutos**

---

## 📋 Patrón: 7 Slides (Fijo)

| # | Tipo | Estructura | Copy Pattern |
|---|------|-----------|--------------|
| 1 | **Hook** | Logo + Heading Grande | "Pierdo X en [PAIN POINT]" |
| 2 | **Tip 1** | Número + Título + Descripción + Resultado | "Primero..." |
| 3 | **Tip 2** | Idem | "Luego..." |
| 4 | **Tip 3** | Idem | "Después..." |
| 5 | **Tip 4** | Idem | "Los..." |
| 6 | **Tip 5** | Idem | "Finalmente..." |
| 7 | **CTA** | Resultado + Call-to-action | "Recuperé X. Tú también." |

---

## 🎨 Paleta de Colores (Fija)

```
Teal Oscuro:    #1a5f5f   (Fondos principales)
Verde Lima:     #7DD3C0   (Acentos, números)
Verde Claro:    #C5E8E3   (Texto secundario)
Blanco:         #FFFFFF   (Texto principal)
```

**Colores por slide:**
- Slides 1, 3, 5: Dark backgrounds
- Slides 2, 4, 6: Light backgrounds
- Slide 7: Green gradient (CTA)

---

## 🔤 Tipografía (Fija)

```
Números:        text-7xl font-black
Títulos:        text-5xl font-bold (mb-8)
Descripción:    text-2xl leading-relaxed

CRÍTICO:        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
                (En: p, h1, h2, h3, span)
```

---

## ✅ Checklist Antes de Exportar

- [ ] **Slide 1:** Hook claro y específico
- [ ] **Slides 2-6:** Narrativa progresiva (Primero → Luego → Después...)
- [ ] **Slide 7:** Resultado + CTA claro
- [ ] **Contraste:** Todos los textos legibles
- [ ] **Centralización:** Todo contenido en el MEDIO
- [ ] **Colores:** Alineados a paleta
- [ ] **Logo:** Watermark en esquina inferior derecha
- [ ] **Spacing:** Consistente (p-20, gap-8, mb-8)
- [ ] **Sombras:** Text-shadow visible

---

## 📐 Medidas Exactas (Copy-Paste)

```
Slide:              1080x1350px
Padding:            p-20 (80px)
Área útil:          920px ancho
Max-width:          max-w-2xl (672px)

Números:            text-7xl (110px+)
Títulos:            text-5xl (48px)
Descripción:        text-2xl (24px)
Gap:                gap-8 (32px)

Logo:               w-32 h-32 (128px)
Opacidad:           opacity-10
Posición:           bottom-8 right-8
```

---

## 🎯 Fórmula de Storytelling (Copy)

### Slide 1 - Hook
```
"Pierdo 3h diarias 
escribiendo [PAIN POINT ESPECÍFICO]"

Subtítulo: Explica brevemente el problema
```

### Slides 2-6 - Transformación
```
Slide 2: "Primero, [acción] → [resultado]"
Slide 3: "Luego, [acción] → [resultado]"
Slide 4: "Después, [acción] → [resultado]"
Slide 5: "[Acción] [resultado]"
Slide 6: "Finalmente, [acción] → [resultado]"
```

### Slide 7 - CTA
```
"Recuperé [RESULTADO]
Ahora [BENEFICIO]

Tú también puedes.

[Botón CTA]"
```

---

## 🔄 Patrón HTML Centralizado (Copy-Paste Base)

```html
<div class="slide relative bg-gradient-to-br from-[#F8FFFE] to-[#E8F5F2] text-[#1a5f5f] flex flex-col items-center justify-center p-20 shadow-2xl rounded-3xl overflow-hidden">
    
    <!-- Decorativos -->
    <div class="blob-1 -top-32 -right-32 opacity-30"></div>
    <div class="blob-2 -bottom-20 -left-20 opacity-25"></div>
    <div class="grid-pattern opacity-40"></div>
    
    <!-- Logo watermark -->
    <div class="absolute bottom-8 right-8 w-32 h-32 opacity-10 pointer-events-none">
        <svg><!-- Logo SVG --></svg>
    </div>

    <!-- Contenido (SIEMPRE IGUAL) -->
    <div class="relative z-10 flex flex-col items-center justify-center gap-8 w-full max-w-2xl">
        
        <!-- Top: Número + Título + Descripción -->
        <div class="text-center">
            <div class="text-7xl font-black mb-6">01</div>
            <h2 class="text-5xl font-bold mb-8">Título</h2>
            <p class="text-2xl leading-relaxed">Descripción</p>
        </div>
        
        <!-- Bottom: Resultado -->
        <div class="bg-gradient-to-br from-[#1a5f5f] to-[#0f4d4d] p-6 rounded-2xl w-full">
            <!-- Contenido resultado -->
        </div>
    </div>
</div>
```

---

## 📊 Ejemplos Exitosos

**Carpeta:** `ejemplos/2026-07-31-5-dicas-claude-code/`

- ✅ `carousel.html` - HTML final exitoso
- ✅ `NOTAS.md` - Lo que funcionó y lecciones
- ✅ `slides/` - PNGs exportados (7 archivos)

**Úsalo como referencia cuando tengas dudas**

---

## 🔧 Scripts Disponibles

### Export a PNG
```bash
python export_script.py carousel.html ./slides/
```

Genera 7 PNG de 1080x1350px en carpeta `slides/`

---

## 📚 Documentación Detallada

Para entender cada aspecto en profundidad:
- `PROCESO_PASO_A_PASO.md` - Guía completa con screenshots
- `PALETA_COLORES.md` - Teoría de colores
- `ejemplos/*/NOTAS.md` - Aprendizaje práctico

---

## ⏱️ Timeline Estimado

```
Prep:       10 min (leer guía)
Copywriting: 15 min (escribir 7 slides)
HTML:       20 min (llenar template)
Validación: 15 min (checklist + navegador)
Export:      5 min (generar PNG)

TOTAL:      65 minutos por carrusel
```

---

## 🚨 Errores Comunes (Evitar)

❌ Usar `justify-between` en contenedor (elementos van a extremos)  
❌ Olvidar `text-shadow` (textos no se ven)  
❌ Hook muy vago (no resonará con audiencia)  
❌ No centrar contenido (se ve desorganizado)  
❌ Cambiar patrón entre slides (pierde cohesión)  
❌ No validar contraste (ilegible en algunos fondos)  

---

## 🎓 Aprendizaje (De Primer Carrusel)

1. **Storytelling específico:** "Pierdo 3h escribiendo X" > "Pierdo tiempo"
2. **Centralización:** Usar `items-center justify-center` + `gap-8`
3. **Alternancia:** Dark/Light/Dark/Light es más dinámico
4. **Watermark:** Logo opacity-10 agrega profesionalismo sin ruido
5. **Consistencia:** Todos los slides DEBEN seguir el mismo patrón

---

## 🔗 Archivos Clave

| Archivo | Usa Para |
|---------|----------|
| `TEMPLATE_CAROUSEL.html` | Copiar y llenar |
| `export_script.py` | Exportar PNG |
| `ejemplos/*/carousel.html` | Referencia |
| `PALETA_COLORES.md` | Entender colores |
| `PROCESO_PASO_A_PASO.md` | Detalle completo |

---

## 💡 Tips Pro

1. **Usa el template:** No empieces desde cero
2. **Valida en navegador:** Antes de exportar
3. **Sigue el checklist:** No te saltes ningún paso
4. **Usa ejemplos:** Como referencia visual
5. **Lee NOTAS.md:** Aprende del primer carrusel

---

**Última actualización:** 31 julio 2026  
**Versión:** 1.0 - Sistema probado y funcional  
**Ubicación:** `C:\Users\John\Desktop\John Jairo\Youtube\v\v\SISTEMAS_Y_PROCESOS\instagram-carruseles\`
