# Skill Profesional: AI Video Generation

**Origen:** 101 Skills  
**Modelos:** 40+ (Veo, Seedance, HappyHorse, Wan, Grok, etc.)  
**Implementación:** Integrada al proyecto

---

## 🎬 Qué Puedes Generar

### 1. Text-to-Video
```
Prompt: "Una presentación de producto con zoom dinámico"
         ↓
    Video 1080P de 10-15 segundos
```

**Mejores Modelos:**
- `Veo 3.1` - Mejor calidad
- `Seedance 2.0` - Con audio sincronizado
- `HappyHorse T2V` - Realismo físico

### 2. Image-to-Video
```
Imagen estática → Video con movimiento
```

**Mejores Modelos:**
- `Wan 2.5` - Animar cualquier imagen
- `Seedance 2.0` - Con audio y movimiento de cámara
- `HappyHorse I2V` - Alta calidad

### 3. AI Avatars (Talking Heads)
```
Foto + Audio → Video de persona hablando
```

**Mejores Modelos:**
- `OmniHuman 1.5` - Multi-personaje
- `Fabric 1.0` - Sincronización de labios realista
- `PixVerse Lipsync` - Alta calidad

### 4. Video Editing con IA
```
"Cambia el fondo a una montaña nevada"
         ↓
    Video editado automáticamente
```

---

## 💡 Casos de Uso para Tu Canal

### 1. Crear Intros/Outros Automáticamente
```
Prompt: "Intro de YouTube profesional con logo de canal
         y texto animado 'John Jairo AI'"

Resultado: Video 1080P de 5 segundos
```

### 2. Animar Screenshots de Herramientas
```
Input: Screenshot de Make.com
Prompt: "Zoom suave en la interfaz, mouse haciendo click"

Resultado: Video tutorial de 10 segundos
```

### 3. Crear Avatares Hablantes
```
Input: Tu foto + Audio (texto a voz)
Prompt: "Persona leyendo guion sobre automatización"

Resultado: Video personalizado de ti hablando
```

### 4. Generar Videos de Productos
```
Prompt: "Demo del producto GoHighLevel
         con transiciones suaves, UI destacada"

Resultado: Video marketing profesional
```

### 5. Editar Videos Existentes
```
Input: Video grabado
Prompt: "Quita los ums y ahs, acelera 1.5x,
         agrega efectos de zoom en puntos clave"

Resultado: Video editado automáticamente
```

---

## 🛠️ Setup Necesario

### Paso 1: Instalar CLI
```bash
npm install -g belt-sh/cli
belt login
```

### Paso 2: Eligir Modelo Según Necesidad

| Caso | Modelo | Costo |
|---|---|---|
| Intro/Outro rápido | P-Video | $$$ (más barato) |
| Mejor calidad | Veo 3.1 | $$$$ |
| Con audio | Seedance 2.0 | $$$$ |
| Avatar parlante | OmniHuman | $$$$$ |

### Paso 3: Integrar a Make.com

```
Make.com Flujo:
  Trigger → Claude genera prompt
         → Skill AI Video Gen
         → Descarga video
         → Upload a YouTube
         → Notificación
```

---

## 📝 Ejemplos de Prompts Efectivos

### Intro Profesional
```
"Intro de YouTube profesional en 3D.
Título: 'John Jairo AI'
Fondo: Código de programación animado
Transición fade en azul y blanco.
Duración: 5 segundos.
Estilo: Moderno, tech"
```

### Demo de Herramienta
```
"Demostración del dashboard de Make.com.
Pantalla mostrando un flujo de automatización.
Zoom suave en componentes importantes.
Cursor haciendo click en botones.
Subtítulos: 'Conecta apps', 'Automatiza tareas'
Duración: 15 segundos"
```

### Video Tutorial
```
"Tutorial animado sobre IA.
Persona sentada ante computadora.
Screen sharing del software.
Gestos naturales mientras habla.
Transiciones suaves entre pasos.
Duración: 2 minutos"
```

---

## 🚀 Integración con Nuestros Flujos

### Flujo: Generador de Ideas → Video Generation
```
Idea generada: "Agente WhatsApp que cierra ventas"
              ↓
        Crear guion (Claude)
              ↓
        Generar video demo (Seedance)
              ↓
        Agregar música (Foley)
              ↓
        Upload a YouTube (Skill YouTube)
```

### Pipeline Automático
```
Lunes 14:00
    ↓
[Make.com Trigger]
    ↓
[Generador de Ideas] - Crea 3 ideas
    ↓
[AI Video Generation] - Genera videos
    ↓
[YouTube Automation] - Publica y promociona
    ↓
[Email] - Notificación completada
```

---

## 💰 Costos Estimados

| Modelo | Costo por Video |
|---|---|
| P-Video (rápido) | $0.50-1.00 |
| Veo 3.1 (calidad) | $1.50-2.50 |
| Seedance 2.0 (audio) | $2.00-3.00 |
| OmniHuman (avatar) | $3.00-5.00 |

**Para 3 videos/semana:** ~$5-10 USD/semana

---

## ⚡ Casos Prácticos Tú

### Para Tus Videos sobre IA:
1. **Intro animada** → Veo 3.1 o P-Video
2. **Demo herramientas** → Seedance 2.0
3. **Avatar de ti hablando** → OmniHuman
4. **Editar grabaciones** → HappyHorse Edit

### Ejemplo Real:
```
Generar un video:
- Hook: "Agente WhatsApp que vende"
- Demo: Screenshot de Make.com animado
- Tu avatar: Explicando configuración
- Outro: Logo del canal

Tiempo total: 1 minuto
Costo: ~$3-5
Esfuerzo manual: 20 minutos
```

---

## 📋 Checklist

- [ ] Instalar belt CLI
- [ ] Configurar API keys
- [ ] Probar con un modelo
- [ ] Elegir modelos favoritos para casos
- [ ] Crear prompts template
- [ ] Integrar a Make.com
- [ ] Programar generación automática

---

**Próximo paso:** Ver cómo integrar con YouTube Automation y calendario

