"""
Helper script to check available Gemini models.
Run this to see what models are available with your API key.
"""
import google.generativeai as genai
from config import GEMINI_API_KEY

def list_available_models():
    """List all available Gemini models."""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        print("=" * 60)
        print("Available Gemini Models")
        print("=" * 60)
        
        models = genai.list_models()
        
        available = []
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                model_name = model.name.replace('models/', '')
                available.append(model_name)
                print(f"✓ {model_name}")
        
        print("\n" + "=" * 60)
        print(f"Total available models: {len(available)}")
        print("=" * 60)
        
        if available:
            print("\nRecommended models to use:")
            if 'gemini-1.5-flash-latest' in available:
                print("  - gemini-1.5-flash-latest (fast)")
            elif 'gemini-1.5-flash' in available:
                print("  - gemini-1.5-flash (fast)")
            
            if 'gemini-1.5-pro-latest' in available:
                print("  - gemini-1.5-pro-latest (more capable)")
            elif 'gemini-1.5-pro' in available:
                print("  - gemini-1.5-pro (more capable)")
        
        return available
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

if __name__ == '__main__':
    list_available_models()

