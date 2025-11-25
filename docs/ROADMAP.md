# VozLatina AI - Official Roadmap

This document outlines the strategic plan to build **VozLatina AI**, the open-source alternative to ElevenLabs/Synthesia for the Latin American market.

## 📅 Phases Overview

| Phase | Focus | Status |
| :--- | :--- | :--- |
| **Phase 1** | **MVP Core** (Workflow & Scaffolding) | ✅ Completed |
| **Phase 2** | **Logic & Optimization** (FP8, Audio Restore) | 🚧 In Progress |
| **Phase 3** | **The "LatAm Pack"** (Regional Models) | 📅 Planned |
| **Phase 4** | **Desktop Experience** (Electron App) | 📅 Planned |
| **Phase 5** | **"Product in a Box"** (Launch & Docs) | 📅 Planned |

---

## 🚀 Detailed Roadmap

### Phase 1: MVP Core (Completed)
*Goal: Establish the baseline workflow and project structure.*
- [x] **ComfyUI Workflow**: Single-click workflow for RVC + XTTS + LivePortrait.
- [x] **Custom Nodes Structure**: Python scaffolding for `vozlatina_nodes.py`.
- [x] **Project Docs**: Initial `PROJECT.MD` and `TECHNICAL_SPECS.md`.

### Phase 2: Logic & Optimization (Current Focus)
*Goal: Make it fast and high-quality on consumer hardware (RTX 3060/4060).*
- [ ] **FP8 Implementation**: Optimize RVC and LivePortrait to run on 8-bit precision (halves VRAM usage).
- [ ] **Audio Restoration**: Implement `DeepFilterNet` or `UVR` logic to clean up TTS artifacts.
- [ ] **Watermarking**: Implement invisible metadata injection for ethical usage.
- [ ] **Lazy Loading**: Ensure models only load when needed to save VRAM.

### Phase 3: The "LatAm Pack"
*Goal: Cultural relevance and "wow" factor.*
- [ ] **Regional RVC Models**: Curate/Train high-quality models for:
    - 🇲🇽 Mexican Neutral
    - 🇦🇷 Rioplatense
    - 🇨🇴 Colombian
    - 🇨🇱 Chilean
- [ ] **Hybrid Mode**: Add support for external APIs (ElevenLabs/OpenAI) for users who want cloud quality for TTS.

### Phase 4: Desktop Experience
*Goal: Move away from the "spaghetti nodes" UI for end-users.*
- [ ] **Electron App**: Build the `desktop_app` frontend.
- [ ] **Batch Queue**: "Set & Forget" system for rendering multiple videos overnight.
- [ ] **Multi-Scene Editor**: Simple timeline to stitch generated clips.
- [ ] **Backend Connection**: WebSocket bridge between Electron and ComfyUI.

### Phase 5: "Product in a Box" (Launch)
*Goal: A polished, installable product for non-technical users.*
- [ ] **One-Click Installer**: `.exe` / `.dmg` that bundles Python, ComfyUI, and Models.
- [ ] **Version Pinning**: Freeze all dependency versions to prevent updates from breaking the tool.
- [ ] **Update System**: OTA (Over-the-Air) updates for the custom nodes.

---

## 📚 Documentation Tracks

We are building documentation for three distinct audiences.

### 🛠 Track 1: Developer Guide
*For contributors and hackers who want to modify the core.*
- **Architecture Overview**: How `vozlatina_nodes.py` interacts with ComfyUI.
- **Custom Nodes API**: How to add new processors or models.
- **Contribution Guidelines**: Code style, testing, and PR process.

### 🚀 Track 2: Starter Guide
*For early adopters who know what "Python" is but want a quick start.*
- **"Zero to Hero" Setup**:
    1. Install ComfyUI Manager.
    2. `git clone` VozLatina.
    3. Download Models (links provided).
- **Troubleshooting**: Common errors (CUDA, VRAM issues).

### 📦 Track 3: User Manual ("Product in a Box")
*For the final user (Content Creator/Marketer) who just wants to make videos.*
- **Interface Tour**: Walkthrough of the Electron Desktop App.
- **Best Practices**: How to record good reference audio.
- **Prompt Engineering**: How to write text for better emotional expression.
- **Legal & Ethics**: Usage policy for cloned voices.
