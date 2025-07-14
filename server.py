import os
import ollama
from PIL import Image
import io

def load_model(model_name: str = "granite3.2-vision:latest"):
    """Load the specified model into GPU memory"""
    try:
        # Check if model is available
        models = ollama.list()['models']
        installed_models = [m['name'] for m in models]
        
        if model_name not in installed_models:
            print(f"Model {model_name} not found. Pulling from Ollama...")
            ollama.pull(model_name)
            
        print(f"Model {model_name} is loaded and ready")
        return True
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return False

def analyze_schematic(image_path: str, prompt_text: str, model_name: str = "granite3.2-vision:latest"):
    """Analyze the schematic using the VLM"""
    try:
        # Load and prepare the image
        with Image.open(image_path) as img:
            byte_arr = io.BytesIO()
            img.save(byte_arr, format='PNG')
            image_bytes = byte_arr.getvalue()

        # Format prompt based on model
        if 'granite' in model_name.lower():
            formatted_prompt = (
                f"<|user|>\n"
                f"Analyze this technical schematic carefully and answer the following request:\n"
                f"{prompt_text}\n"
                f"Provide a detailed, structured response with clear sections.\n"
                f"<|assistant|>\n"
            )
        else:  # For LLaVA
            formatted_prompt = prompt_text

        # Create the message for the VLM
        messages = [
            {
                'role': 'user',
                'content': formatted_prompt,
                'images': [image_bytes]
            }
        ]

        # Model-specific options
        options = {}
        if 'granite' in model_name.lower():
            options = {'temperature': 0.3, 'num_ctx': 4096}

        # Call the Ollama model
        response = ollama.chat(
            model=model_name,
            messages=messages,
            options=options if options else None
        )

        return response['message']['content']

    except Exception as e:
        return f"Error analyzing schematic: {str(e)}"

if __name__ == "__main__":
    # Load the default model when server starts
    load_model()
