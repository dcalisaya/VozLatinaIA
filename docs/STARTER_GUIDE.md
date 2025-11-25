# Starter Guide 🚀

Welcome to **VozLatina AI**! This guide will take you from "Zero" to generating your first hyper-realistic video in Spanish.

## 📋 Prerequisites

Before you begin, ensure you have:
*   **NVIDIA GPU**: RTX 3060 or better recommended (min 8GB VRAM).
*   **OS**: Windows 10/11 or Linux (Ubuntu 22.04+).
*   **Software**:
    *   [Python 3.10+](https://www.python.org/downloads/)
    *   [Git](https://git-scm.com/downloads)

---

## 🛠️ Installation ("Zero to Hero")

### Step 1: Install ComfyUI
If you don't have ComfyUI yet, the easiest way is to use the portable version (Windows) or clone it manually.

```bash
# Manual installation
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt
```

### Step 2: Install VozLatina Nodes
Navigate to the `custom_nodes` folder inside your ComfyUI installation and clone this repository.

```bash
cd custom_nodes
git clone https://github.com/dcalisaya/VozLatinaIA VozLatina
cd VozLatina
pip install -r requirements.txt
```

### Step 3: Download Models
You need specific models for the magic to happen. Place them in the `ComfyUI/models` directory structure.

| Model Type | File | Path | Link |
| :--- | :--- | :--- | :--- |
| **RVC** | `rmvpe.pt` | `models/rvc/` | [Download](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/rmvpe.pt) |
| **LivePortrait** | `liveportrait_animals.pth` (etc) | `models/liveportrait/` | [Download](https://huggingface.co/Kijai/LivePortrait_safetensors) |
| **DeepFilterNet** | `DeepFilterNet3` | (Auto-downloaded) | — |

> [!TIP]
> **VozLatina Pack**: We are working on a single `.zip` file that contains all necessary models optimized for LatAm accents. Stay tuned!

---

## 🏃‍♂️ Running Your First Generation

1.  Start ComfyUI: `python main.py`
2.  Open your browser at `http://127.0.0.1:8188`.
3.  Drag and drop the `comfyui_workflow_mvp.json` file (found in the `workflows` folder of this repo) into the window.
4.  **Load your inputs**:
    *   **Audio**: Upload a 10-15s clean audio clip of the voice you want to clone.
    *   **Source Image**: Upload a high-quality portrait photo.
5.  Click **Queue Prompt**.

---

## ❓ Troubleshooting

### "CUDA Out of Memory"
*   **Cause**: Your GPU ran out of VRAM.
*   **Fix**:
    1.  Ensure `fp8_enabled` is set to `True` in the VozLatina nodes.
    2.  Close other apps (Chrome, Photoshop).
    3.  Reduce the `LivePortrait` resolution if possible.

### "ModuleNotFoundError: No module named 'deepfilternet'"
*   **Cause**: Dependencies weren't installed.
*   **Fix**: Run `pip install -r requirements.txt` inside the `custom_nodes/VozLatina` folder again.

### "Voice sounds robotic"
*   **Cause**: Poor quality reference audio or wrong F0 method.
*   **Fix**:
    *   Use `rmvpe` as the f0_method.
    *   Ensure reference audio has no background music/noise.
    *   Try the **Audio Restore** node with intensity 0.6.
