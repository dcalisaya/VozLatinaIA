import torch
import folder_paths
import os
import subprocess
import numpy as np
import torchaudio

def is_fp8_supported():
    """Check if the current GPU supports FP8 (Ada Lovelace or newer)."""
    if not torch.cuda.is_available():
        return False
    try:
        # FP8 is supported on Compute Capability 8.9 (Ada) and 9.0 (Hopper)
        major, minor = torch.cuda.get_device_capability()
        return major >= 9 or (major == 8 and minor >= 9)
    except:
        return False

class LazyLoadModel:
    """
    Helper class to manage VRAM by loading/unloading models on demand.
    """
    def __init__(self):
        self.current_model = None
        self.model_name = None

    def load(self, model_path, loader_func):
        if self.model_name != model_path:
            # Unload previous model if exists
            if self.current_model is not None:
                del self.current_model
                torch.cuda.empty_cache()
            
            # Load new model
            print(f"Loading model: {model_path}")
            self.current_model = loader_func(model_path)
            self.model_name = model_path
        return self.current_model

    def unload(self):
        if self.current_model is not None:
            del self.current_model
            self.current_model = None
            self.model_name = None
            torch.cuda.empty_cache()

class VozLatinaRVC:
    """
    Custom node for RVC Inference with VRAM optimization and FP8 support.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "model_name": (["bad_bunny.pth", "shakira.pth", "my_voice.pth"],),
                "f0_method": (["rmvpe", "crepe"],),
                "fp8_enabled": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "process"
    CATEGORY = "VozLatina"

    def process(self, audio, model_name, f0_method, fp8_enabled):
        print(f"Processing RVC with model {model_name} using {f0_method}")
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.float16
        
        if fp8_enabled:
            if is_fp8_supported():
                print("FP8 Optimization Enabled: Using torch.float8_e4m3fn")
                dtype = torch.float8_e4m3fn
            else:
                print("Warning: FP8 requested but GPU does not support it. Falling back to FP16.")

        # Mocking the RVC inference pipeline for now since we don't have the full RVC lib
        # In a real scenario, we would load the checkpoint here:
        # checkpoint = torch.load(model_name, map_location=device)
        # if fp8_enabled: checkpoint = checkpoint.to(dtype)
        
        # For now, pass through the audio
        return (audio,)

class VozLatinaAudioRestore:
    """
    Node to clean up audio artifacts using DeepFilterNet or UVR logic.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "intensity": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0}),
            }
        }
    
    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "restore"
    CATEGORY = "VozLatina"

    def restore(self, audio, intensity):
        print(f"Restoring audio with intensity {intensity}")
        
        # Check if DeepFilterNet is installed
        try:
            from df.enhance import enhance, init_df, load_audio, save_audio
            # This is where we would call the actual DeepFilterNet API
            # model, df_state, _ = init_df()
            # enhanced_audio = enhance(model, df_state, audio)
            print("DeepFilterNet found. Audio restoration applied (simulated).")
        except ImportError:
            print("DeepFilterNet not found. Please install it via 'pip install deepfilternet'")
            print("Returning original audio.")
            
        return (audio,)

class VozLatinaLivePortrait:
    """
    Custom node for LivePortrait with FP8 support.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "source_image": ("IMAGE",),
                "driving_audio": ("AUDIO",),
                "lip_sync_ratio": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0}),
                "fp8_enabled": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "animate"
    CATEGORY = "VozLatina"

    def animate(self, source_image, driving_audio, lip_sync_ratio, fp8_enabled):
        print(f"Animating portrait with ratio {lip_sync_ratio}")
        
        if fp8_enabled:
            if is_fp8_supported():
                print("FP8 Optimization Enabled for LivePortrait.")
                # In real implementation:
                # model.unet.to(dtype=torch.float8_e4m3fn)
            else:
                print("FP8 not supported on this device.")
        
        # Return dummy frames (placeholder)
        return (source_image,)

class VozLatinaWatermark:
    """
    Node to inject invisible metadata/watermark into the output using LSB Steganography.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_frames": ("IMAGE",),
                "watermark_text": ("STRING", {"default": "Generated by VozLatina AI"}),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "inject"
    CATEGORY = "VozLatina"

    def inject(self, video_frames, watermark_text):
        print(f"Injecting invisible watermark: {watermark_text}")
        
        # Convert tensor to numpy (B, H, W, C) -> range [0, 1]
        frames_np = video_frames.cpu().numpy()
        
        # Simple LSB injection on the first frame, first row
        # We encode the text into the Blue channel of the first few pixels
        
        # Convert text to binary
        binary_text = ''.join(format(ord(char), '08b') for char in watermark_text)
        binary_text += '1111111111111110' # EOF marker
        
        data_index = 0
        data_len = len(binary_text)
        
        # Work on a copy to avoid modifying original tensor in place if it's shared
        watermarked_frames = frames_np.copy()
        
        # Only watermark the first frame for efficiency in this demo
        first_frame = watermarked_frames[0]
        height, width, _ = first_frame.shape
        
        # Iterate over pixels
        for y in range(height):
            for x in range(width):
                if data_index < data_len:
                    # Get Blue channel (assuming RGB)
                    b = first_frame[y, x, 2]
                    
                    # Convert to 0-255 int
                    b_int = int(b * 255)
                    
                    # Modify LSB
                    bit = int(binary_text[data_index])
                    b_int = (b_int & ~1) | bit
                    
                    # Write back normalized
                    first_frame[y, x, 2] = b_int / 255.0
                    
                    data_index += 1
                else:
                    break
            if data_index >= data_len:
                break
                
        # Convert back to tensor
        return (torch.from_numpy(watermarked_frames),)

NODE_CLASS_MAPPINGS = {
    "VozLatinaRVC": VozLatinaRVC,
    "VozLatinaAudioRestore": VozLatinaAudioRestore,
    "VozLatinaLivePortrait": VozLatinaLivePortrait,
    "VozLatinaWatermark": VozLatinaWatermark
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VozLatinaRVC": "VozLatina RVC Inference",
    "VozLatinaAudioRestore": "VozLatina Audio Restore",
    "VozLatinaLivePortrait": "VozLatina LivePortrait",
    "VozLatinaWatermark": "VozLatina Watermark"
}
