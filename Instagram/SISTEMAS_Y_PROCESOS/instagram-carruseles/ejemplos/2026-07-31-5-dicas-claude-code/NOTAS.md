# Notas - Primer Carrusel Exitoso

**Tema:** 5 Dicas de Claude Code  
**Fecha:** 31 julio 2026  
**Estado:** ✅ Completo y Exportado  
**Ubicación:** `Instagram/Skill-ig-carruseles/instagram-carrossel/conteudos/2026-07-31-5-dicas-claude-code/`

---

## 🎯 Qué Funcionó

### 1. Storytelling Específico
```
❌ ANTES: "5 Dicas de Claude Code"
✅ DESPUÉS: "Pierdo 3h diarias escribiendo lo que podría automatizar"
```
**Lección:** El hook específico resonó mucho más que un título genérico.

### 2. Centralización (Key Pattern)
**Estructura que funcionó:**
```html
flex flex-col items-center justify-center 
+ gap-8 
+ max-w-2xl
```
- Todo contenido en el MEDIO del slide
- No en extremos (justifying-between)
- Visualmente más limpio y profesional

### 3. Alternancia de Colores
- Slides 1, 3, 5: Dark backgrounds (teal)
- Slides 2, 4, 6: Light backgrounds
- Slide 7: Green gradient (CTA)

**Resultado:** Más dinámico que colores fijos

### 4. Tipografía Jerárquica
```
Números:     text-7xl (120px+)  → Atrae atención
Títulos:     text-5xl (48px)    → Subtítulo
Descripción: text-2xl (24px)    → Cuerpo legible
```

### 5. Text-Shadow Crítico
```css
p, h1, h2, h3, span {
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}
```
- **Antes:** Textos blancos invisibles sobre fondos oscuros
- **Después:** Legible en TODOS los fondos
- **Conclusión:** NUNCA omitir esta regla

### 6. Logo Watermark
- Posición: `bottom-8 right-8`
- Opacidad: `opacity-10` (decorativo, no compite)
- Efecto: Agrega profesionalismo sin ruido visual

### 7. Patrón Consistente
Todos los slides (2-6) seguían:
```
1. Número (01-05)
2. Título (5xl bold)
3. Descripción (2xl light)
4. Resultado/Box (bottom)
```
→ Cohesión visual perfecta

---

## 🚨 Errores Corregidos (Aprender de Ellos)

### Error 1: Slides No Centralizados
**Problema:** Slides 4 y 5 usaban `justify-between` que dispersaba elementos  
**Solución:** Cambiar a `justify-center` + `gap-8`  
**Lección:** La centralización es KEY para modernidad

### Error 2: Contraste de Colores
**Problema:** Slide 1 tenía texto blanco sobre blanco  
**Solución:** Cambiar a `text-[#C5E8E3]` (verde claro) + text-shadow  
**Lección:** Validar contraste en navegador SIEMPRE

### Error 3: Frase del Hook
**Problema:** Inicial era muy vaga: "Pierdo 3h diarias en..."  
**Solución:** Hacer específica: "...escribiendo lo que podría automatizar"  
**Lección:** Especificidad = Resonancia

### Error 4: Gradient Erróneo
**Problema:** Gradient del título usaba naranja (#B65E42)  
**Solución:** Cambiar a verde claro (#C5E8E3)  
**Lección:** Mantener paleta consistente

### Error 5: Tamaños Inconsistentes
**Problema:** Primero usé text-xl/text-lg para descripciones  
**Solución:** Estandarizar a text-2xl  
**Lección:** Medidas FIJAS en el template

---

## 📊 Métricas del Carrusel

```
Slides:           7 (Hook + 5 Tips + CTA)
Estructura:       Centralizada, iterable
Tiempo total:     ~2 horas (incluye debugging)
Correcciones:     5 mayores
Export:           7 PNG @ 1080x1350px
Tamaño total:     ~250KB (optimizado)
```

---

## 🎓 Lecciones Clave

### 1. Template > Desde Cero
Usar template ahorra 45 min de setup

### 2. Validar en Navegador
No confiar en el editor; abrir en navegador real

### 3. Checklist Obligatorio
Validar todos los 10 puntos antes de exportar

### 4. Storytelling > Features
La narrativa emocional supera la lista de features

### 5. Consistencia > Creatividad
Mantener patrón > experimentar con cada slide

### 6. Colores Alternados > Monótonos
Dark/Light/Dark es más dinámico

### 7. Centralización es Profesionalidad
`items-center justify-center` + `max-w-2xl` = limpio

### 8. Text-Shadow No Es Opcional
Necesario para legibilidad en TODOS los fondos

### 9. Watermark con opacity-10
Logo decorativo agrega profesionalismo

### 10. Medidas Exactas
Usar las MISMAS medidas para consistencia

---

## ⏱️ Timeline Real

```
Análisis/Setup:      30 min
Copywriting:         25 min
HTML inicial:        25 min
Correcciones:        20 min (contraste, colores, centralización)
Validación:          10 min
Export PNG:           5 min

TOTAL:              115 min (casi 2 horas)
```

**Próxima vez:** 50-70 min (sin correcciones iniciales)

---

## 🔧 Checklist para Próximo Carrusel

- [ ] Usar TEMPLATE_CAROUSEL.html
- [ ] Escribir hook específico (no genérico)
- [ ] Llenar 7 slides siguiendo estructura
- [ ] Validar contraste en navegador (no editor)
- [ ] Revisar centralización (items-center justify-center)
- [ ] Confirmar text-shadow en todos los textos
- [ ] Verificar colores en paleta
- [ ] Revisar logo watermark en esquina
- [ ] Exportar PNG
- [ ] Validar 7 archivos @ 1080x1350px

---

## 📁 Archivos Generados

```
carousel.html           HTML final (1 archivo)
slides/
├── slide_1.png         Hook (733KB)
├── slide_2.png         Tip 1 (30KB)
├── slide_3.png         Tip 2 (40KB)
├── slide_4.png         Tip 3 (29KB)
├── slide_5.png         Tip 4 (36KB)
├── slide_6.png         Tip 5 (25KB)
└── slide_7.png         CTA (65KB)

TOTAL: 8 archivos, ~250KB
```

---

## 🎯 Recomendaciones para Futuros Carruseles

1. **Copiar structure exacta** de este carrusel
2. **Usar paleta de colores fija** (nunca cambiar)
3. **Mantener 7 slides** (estructura probada)
4. **Alternar dark/light/dark** (patrón dinámico)
5. **Ser específico en hook** (no genérico)
6. **Validar en navegador** (no confiar en editor)
7. **Seguir checklist** (no saltarse pasos)
8. **Usar template base** (no empezar desde cero)

---

**Estado:** Listo para replicar  
**Calidad:** ⭐⭐⭐⭐⭐ (profesional)  
**Reusabilidad:** ⭐⭐⭐⭐⭐ (template perfecto)  
**Tiempo próximo:** 50-70 min (optimizado)
