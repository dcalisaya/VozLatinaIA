import sys
import os

# Add custom_nodes to path
sys.path.append(os.path.join(os.getcwd(), 'custom_nodes'))

# Mock folder_paths since we are not in ComfyUI environment
import types
folder_paths = types.ModuleType("folder_paths")
sys.modules["folder_paths"] = folder_paths

# Mock torch
torch = types.ModuleType("torch")
torch.cuda = types.ModuleType("torch.cuda")
torch.cuda.empty_cache = lambda: None
sys.modules["torch"] = torch

try:
    from vozlatina_nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    print("Successfully imported vozlatina_nodes")
except ImportError as e:
    print(f"Failed to import vozlatina_nodes: {e}")
    sys.exit(1)

def test_nodes():
    expected_nodes = [
        "VozLatinaRVC",
        "VozLatinaAudioRestore",
        "VozLatinaLivePortrait",
        "VozLatinaWatermark"
    ]

    for node_name in expected_nodes:
        if node_name not in NODE_CLASS_MAPPINGS:
            print(f"ERROR: {node_name} not found in NODE_CLASS_MAPPINGS")
            sys.exit(1)
        
        cls = NODE_CLASS_MAPPINGS[node_name]
        print(f"Verified {node_name}: {NODE_DISPLAY_NAME_MAPPINGS[node_name]}")
        
        # Check input types
        inputs = cls.INPUT_TYPES()
        print(f"  Inputs: {list(inputs['required'].keys())}")

    print("\nAll nodes verified successfully.")

if __name__ == "__main__":
    test_nodes()
