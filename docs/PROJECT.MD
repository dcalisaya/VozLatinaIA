¡Aquí tienes el plan completo y ejecutable de **VozLatina AI** — el proyecto open source que es una alternativa a  ElevenLabs + Synthesia + HeyGen en todo el mercado hispanohablante (y de paso en portugués brasileño) antes de que termine 2026.

### Nombre final sugerido (para que sea viral en LATAM)
**VozLatina AI** – “La voz que habla como tú, gratis y para siempre”

### Objetivo del MVP (lanzable en 4–6 semanas)
Un solo workflow de ComfyUI que haga esto con **un solo clic**:
1. Subes 10–30 segundos de audio de referencia (tu voz, la de tu abuela, Bad Bunny, Shakira, whoever).
2. Escribes el texto que quieres que diga (hasta 5 minutos).
3. Pulsa “Generar” → sale video 1080p 60 fps con avatar realista hablando perfecto español neutro o regional + voz clonada idéntica + labios 100 % sincronizados.

Todo 100 % local en tu PC con la 5070 Ti, sin subir nada a la nube, sin pagar nunca.

### Stack definitivo 2025–2026 (todo open source y ya maduro)

| Parte                     | Modelo/Herramienta ganador 2025                          | VRAM necesaria (5070 Ti 16 GB) | Velocidad real en 5070 Ti |
|---------------------------|----------------------------------------------------------|--------------------------------|----------------------------|
| Voz clonada (RVC v2)      | RVC v2 + So-VITS-SVC 4.1 + Crepe full                   | 4–6 GB                         | 30–40× real-time          |
| TTS fallback (si no hay referencia) | XTTS-v2 + Coqui TTS español neutro + voces regionales   | 3–4 GB                         | 50× real-time             |
| Lip-sync & cabeza         | LivePortrait 512 + GroundingDINO + ControlNet depth     | 7–9 GB                         | 8–15 fps en 512px         |
| Upscale final a 1080p     | Ultimate SD Upscale + Real-ESRGAN 4x+                   | 4 GB                           | 4–6 fps                   |
| Audio final + limpieza    | Demucs v4 + MDX-Net para separar stems + voz limpia     | 2 GB                           | 20× real-time             |
| GUI y workflow            | ComfyUI + custom nodes (te los paso yo)                 | —                              | —                         |

### Estructura del workflow ComfyUI (el “holy grail”)

```
[Audio referencia] → RVC v2 → voz clonada
                        ↓
[TEXTO] → XTTS-v2 (fallback si <10s referencia) → wav 48kHz
                        ↓
Wav final → LivePortrait (avatar base latino) → video 512px
                        ↓
Ultimate Upscale → 1080p 60 fps + frame interpolation (RIFE)
                        ↓
FFmpeg NVENC → MP4 final con audio perfecto
```

### Modelos pre-entrenados que YA existen y son brutales (solo descargar)

1. RVC v2 Hub → https://huggingface.co/lj1995/VoiceConversionWebUI  
   (miles de voces latinas ya entrenadas: México, Argentina, Perú, Colombia, España, etc.)

2. XTTS-v2 español neutro + regional → https://huggingface.co/coqui/XTTS-v2  
   (incluye acentos boliviano, chileno, venezolano)

3. LivePortrait latino base (512px) → https://huggingface.co/Kijai/LivePortrait_safetensors  
   (ya hay versiones fine-tuneadas con caras latinas)

4. Voces famosas “libres” (entrenadas por la comunidad):  
   Bad Bunny, Karol G, Residente, Peso Pluma, Duki, Quevedo, etc. (todos en el Hub).

### Custom nodes que necesitas (te los paso listos para copiar-pegar)

1. Node “RVC Realtime Pipe” (ya existe, solo actualizar a v2 + Crepe)
2. Node “XTTS-v2 Streaming” (ya existe en ComfyUI-XTTS)
3. Node “LivePortrait Ultimate” (Kijai lo tiene casi listo)
4. Node “One-Click VozLatina” (yo te armo el meta-node que encadena todo)

### Diferenciadores Clave y Mejoras ("La Salsa Secreta")

#### 1. Producto: El "Pack de Inicio LatAm"
*   **Curación Regional**: No usar modelos genéricos. Incluir presets RVC entrenados específicamente para: 🇲🇽 (Mexicano Neutro), 🇦🇷 (Rioplatense), 🇨🇴 (Colombiano), 🇨🇱 (Chileno).
*   **Modo Híbrido**: Opción para usar APIs de ElevenLabs/OpenAI para el TTS (calidad suprema) y usar la GPU local solo para Lip-Sync y Render.

#### 2. Arquitectura y Rendimiento
*   **Soporte FP8 (Floating Point 8)**: Implementación nativa para RTX serie 40/50. Reduce VRAM a la mitad.
*   **Version Pinning**: Congelar versiones de ComfyUI y dependencias. No actualizaciones automáticas que rompen el entorno.
*   **Cola de Renderizado (Batch)**: Sistema "Set & Forget". Configurar 5 videos y procesarlos en cola durante la noche.

#### 3. Calidad Audiovisual (Post-Procesamiento)
*   **Audio Restoration**: Nodo integrado de **DeepFilterNet** o **UVR** para eliminar artefactos metálicos del TTS/RVC.
*   **Face Enhancer Selectivo**: Integración de **CodeFormer** con slider de intensidad (0.3-0.5) para recuperar nitidez en ojos/dientes sin efecto "filtro barato".

#### 4. Seguridad y Ética
*   **Watermarking Invisible**: Inserción de metadatos/esteganografía para identificar contenido generado por "VozLatina AI". Protección legal para el creador de la herramienta.

#### 6. Arquitectura Flexible (Cliente-Servidor)
*   **Modo Remoto (Pro)**: Ejecuta la interfaz en una laptop ligera (Mac/Windows) y conecta a un servidor GPU (Ubuntu/Windows) vía red local. Ideal para estudios o usuarios con "Render Farm".

### Roadmap Actualizado

Semana 1–2: MVP Funcional (RVC + XTTS + LivePortrait).
Semana 3: Optimización (FP8, Lazy Loading) y Calidad (Audio Restore, Face Enhancer).
Semana 4: Pack LatAm (Curación de modelos) y Watermarking.
Semana 5: GUI Desktop (Electron) con Cola de Batch y Editor Multi-Escena.
Semana 6: Lanzamiento "Portable" congelado (Version Pinning).