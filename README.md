# VozLatina AI 🎙️🎬
> **La voz que habla como tú, GRATIS y para siempre.**

![VozLatina Banner](https://via.placeholder.com/1200x400?text=VozLatina+AI+-+Local+Video+Generation)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue)](https://github.com/vozlatina/vozlatina)
[![GPU](https://img.shields.io/badge/GPU-NVIDIA%20RTX%203060%2B-green)](https://developer.nvidia.com/cuda-gpus)

**VozLatina AI** es una herramienta open-source para la generación de video con clonación de voz y sincronización labial (lip-sync), diseñada específicamente para el mercado hispanohablante.

🚀 **Características Principales:**
- **Clonación de Voz (RVC v2)**: Clona cualquier voz con solo 10 segundos de audio.
- **Lip-Sync Realista (LivePortrait)**: Anima avatares estáticos con precisión milimétrica.
- **100% Local**: Todo se ejecuta en tu GPU. Sin suscripciones, sin nubes, sin límites.
- **Pack LatAm**: Presets optimizados para acentos de México 🇲🇽, Argentina 🇦🇷, Colombia 🇨🇴, Chile 🇨🇱.
- **Modo Pro**: Arquitectura Cliente-Servidor para estudios.

---

## ⚠️ Disclaimer Legal (Puerto Seguro)

**VozLatina AI es una herramienta de procesamiento neutral.**
Los desarrolladores no alojan, distribuyen ni tienen acceso a ningún modelo de voz ni a los contenidos generados. El usuario asume toda la responsabilidad legal y ética por el uso de la herramienta.

---

## 🛠️ Instalación

### Requisitos Previos
*   **GPU**: NVIDIA RTX 3060 (12GB) o superior.
*   **OS**: Windows 10/11 o Ubuntu 22.04.
*   **Drivers**: NVIDIA Studio Driver 550+.

### Inicio Rápido (Desktop App)

1.  Clona el repositorio:
    ```bash
    git clone https://github.com/vozlatina/vozlatina.git
    cd vozlatina
    ```

2.  Instala las dependencias de la App:
    ```bash
    cd desktop_app
    npm install
    npm start
    ```

3.  Configura el Backend (ComfyUI):
    *   Sigue las instrucciones en [TECHNICAL_SPECS.md](docs/TECHNICAL_SPECS.md) para configurar el entorno Python.
    *   Carga el workflow `workflows/comfyui_workflow_mvp.json`.

## 📚 Documentación

*   [Especificaciones Técnicas](docs/TECHNICAL_SPECS.md)
*   [Reporte de Viabilidad](docs/viability_report.md)
*   [Plan de Proyecto](docs/PROJECT.MD)

## 🤝 Contribuir

¡Las Pull Requests son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de empezar.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
