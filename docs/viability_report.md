# Análisis de Viabilidad Técnica y Estratégica
**VozLatina AI** – Solución Local de Generación de Video con Clonación de Voz y Lip-Sync
*Noviembre 2025*

## Resumen Ejecutivo

**Veredicto final**: **TÉCNICAMENTE VIABLE** con hardware de gama alta (RTX 5070 Ti 16 GB o superior).
El mayor desafío no es la tecnología en sí, sino **la experiencia de usuario final** y **la mitigación de riesgos legales**.

| Aspecto | Nivel de Viabilidad | Riesgo Principal |
| :--- | :--- | :--- |
| Hardware requerido | Alta | Accesibilidad (solo PCs gaming) |
| Stack técnico | Muy Alta | Dependency hell y portabilidad |
| Calidad de salida | Alta | Uncanny valley en acentos fuertes |
| Riesgos legales | Medio-Alto | Deepfakes / derechos de voz |
| UX para usuario final | Baja (actual) | ComfyUI es hostil para novatos |

## 1. Validación Técnica

### Hardware objetivo
- **RTX 5070 Ti 16 GB** → Realista y suficiente para Noviembre 2025.
- Estimación real de consumo VRAM (inferencia concurrente optimizada):

| Modelo | VRAM pico (fp16) | Notas |
| :--- | :--- | :--- |
| RVC v2 | ~3.8 GB | |
| XTTS-v2 | ~2.5 GB | |
| LivePortrait | ~4.2 GB | |
| Upscaler (4x) | ~3.5 GB | Solo se carga al final |
| **Total simultáneo** | **~10–12 GB** | Viable con lazy loading |

**Conclusión**: 16 GB es cómodo, 12 GB (RTX 4060/5060) sería el mínimo realista.

### Stack de software elegido
| Componente | Tecnología elegida | Estado actual (2025) | Calificación |
| :--- | :--- | :--- | :--- |
| Orquestador | ComfyUI | Excelente, muy activo | 9.5/10 |
| Voice Cloning | RVC v2 | Estándar de facto | 9/10 |
| TTS | XTTS-v2 | Mejor soporte multilingüe | 9.5/10 |
| Lip-sync | LivePortrait | Mejor relación calidad/VRAM | 9/10 |

## 2. Riesgos Críticos y Estrategia Legal

### Posición legal recomendada (100% local = herramienta neutral)
> VozLatina AI es software **offline** → equivalente legal a Adobe Premiere, Blender o Audacity.

**Disclaimer obligatorio** (incluir en instalador, README y splash screen):

```text
VozLatina AI es una herramienta de procesamiento completamente local.
Los desarrolladores no alojan, distribuyen ni tienen acceso a ningún modelo de voz ni a los contenidos generados.
El usuario asume toda la responsabilidad legal y ética por el uso de la herramienta,
incluyendo el respeto a derechos de autor, derechos de imagen, voz y personalidad de terceros.
```

## 3. Desafíos Técnicos y Mejoras (Anexo)

### "Dependency Hell" y Portabilidad
*   **Desafío**: Python + PyTorch + CUDA + FFmpeg es frágil.
*   **Solución**: Usar un entorno embebido hermético (Pinokio / Stability Matrix).

### Gestión de VRAM
*   **Estrategia**: Implementar `Lazy Loading` estricto. Descargar modelos de audio antes de cargar LivePortrait/Upscaler.

### Mejoras Propuestas
1.  **Cuantización (fp16/int8)**: Vital para soportar tarjetas de 12GB.
2.  **Wrapper de Escritorio**: Electron/Tauri para ocultar ComfyUI.
