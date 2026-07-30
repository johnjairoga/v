# 🎯 Flujo de Procesamiento en Lotes - Fase 2

**Objetivo:** Procesar los 40 videos restantes en 4 lotes de 10 videos cada uno  
**Tiempo total:** ~3-4 horas (4 lotes × ~45-60 min)  
**Estrategia:** Secuencial (un lote a la vez) + validación entre lotes

---

## 📋 Checklist de Lotes

### ✅ Lote 0 (COMPLETADO)
```bash
# Videos #1-10 (Top 10)
# Estado: 6 transcritos ✅, 3 saltados ⏭️, 1 error ❌
```

---

### ⏳ LOTE 1: Videos #11-20

**Comando:**
```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --batch 11-20
```

**Duración estimada:** 45-60 minutos

**Después de completarse:**
- [ ] Revisar 2-3 transcripciones nuevas en `videos de youtube/transcripciones_top_videos/`
- [ ] Contar archivos `.md` para confirmar cantidad
- [ ] Anotar si hay errores o videos saltados
- [ ] Pasar a LOTE 2

**Comando para monitorear (en otra terminal):**
```powershell
# Contar archivos .md conforme se generan
Watch-Object { (Get-ChildItem "videos de youtube\transcripciones_top_videos\*.md").Count }
```

---

### ⏳ LOTE 2: Videos #21-30

**Comando:**
```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --batch 21-30
```

**Duración estimada:** 45-60 minutos

**Después de completarse:**
- [ ] Revisar 2-3 transcripciones nuevas
- [ ] Contar archivos `.md` 
- [ ] Anotar si hay errores o videos saltados
- [ ] Pasar a LOTE 3

---

### ⏳ LOTE 3: Videos #31-40

**Comando:**
```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --batch 31-40
```

**Duración estimada:** 45-60 minutos

**Después de completarse:**
- [ ] Revisar 2-3 transcripciones nuevas
- [ ] Contar archivos `.md` 
- [ ] Anotar si hay errores o videos saltados
- [ ] Pasar a LOTE 4

---

### ⏳ LOTE 4: Videos #41-50

**Comando:**
```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --batch 41-50
```

**Duración estimada:** 45-60 minutos

**Después de completarse:**
- [ ] Revisar 2-3 transcripciones nuevas
- [ ] Contar archivos `.md` (deberías tener ~45-50 totales)
- [ ] Anotar si hay errores o videos saltados
- [ ] ✅ **FASE 2 COMPLETADA**

---

## 📊 Validación Final (Después de todos los lotes)

```bash
# Contar transcripciones totales
(Get-ChildItem "videos de youtube\transcripciones_top_videos\*.md").Count
# Deberías ver: 45-50 (algunos videos se saltan por ser anómalos)

# Contar MP3s descargados
(Get-ChildItem "videos de youtube\audio_mp3\*.mp3").Count
# Deberías ver: 45-50
```

---

## 🚨 Si algo falla en un lote

**Opción 1: Re-ejecutar el mismo lote**
```bash
python descargar_y_transcribir_audio.py --batch 11-20
# El script es idempotente, no procesará duplicados
```

**Opción 2: Continuar con el siguiente lote (sin perder progreso)**
```bash
python descargar_y_transcribir_audio.py --batch 21-30
# Los videos anteriores ya están guardados
```

---

## ✨ Resumen de Progreso

| Lote | Rango | Estado | Transcritos | Nota |
|------|-------|--------|------------|------|
| 0 | #1-10 | ✅ | 6 | Top 10 ya completado |
| 1 | #11-20 | ⏳ | - | Próximo |
| 2 | #21-30 | ⏳ | - | Después del 1 |
| 3 | #31-40 | ⏳ | - | Después del 2 |
| 4 | #41-50 | ⏳ | - | Después del 3 |
| **TOTAL** | **#1-50** | **⏳** | **~45-50** | Al terminar todos |

---

## 🎯 Próximo paso

**Ejecuta Lote 1 cuando estés listo:**
```bash
cd youtube_channel
python descargar_y_transcribir_audio.py --batch 11-20
```

---

**¿Listo para empezar?**
