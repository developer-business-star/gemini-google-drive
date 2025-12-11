"""
Google Gemini API connector for querying with document context.
"""
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_CONTEXT_LENGTH


class GeminiConnector:
    """Handles interaction with Google Gemini API."""
    
    def __init__(self):
        """Initialize Gemini connector."""
        if not GEMINI_API_KEY or GEMINI_API_KEY == 'YOUR_GEMINI_API_KEY_HERE':
            raise ValueError(
                "GEMINI_API_KEY not set. Please set it in .env file or config.py"
            )
        
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Try different model name variations
        model_names_to_try = [
            GEMINI_MODEL,  # Try configured model first
            'gemini-flash-latest',  # Latest flash model
            'gemini-pro-latest',    # Latest pro model
            'gemini-1.5-flash-latest',
            'gemini-1.5-pro-latest',
            'gemini-1.5-flash',
            'gemini-1.5-pro',
            'gemini-pro'
        ]
        
        model_found = False
        last_error = None
        
        for model_name in model_names_to_try:
            try:
                self.model = genai.GenerativeModel(model_name)
                if model_name != GEMINI_MODEL:
                    print(f"⚠️  Using model: {model_name} (configured model '{GEMINI_MODEL}' not available)")
                else:
                    print(f"✓ Using model: {model_name}")
                model_found = True
                break
            except Exception as e:
                last_error = str(e)
                continue
        
        if not model_found:
            # Last attempt: try to list and use first available model
            try:
                available_models = [m.name.replace('models/', '') for m in genai.list_models() 
                                   if 'generateContent' in m.supported_generation_methods]
                if available_models:
                    # Prefer flash or pro models
                    preferred = [m for m in available_models if 'flash' in m.lower() or 'pro' in m.lower()]
                    model_to_use = preferred[0] if preferred else available_models[0]
                    self.model = genai.GenerativeModel(model_to_use)
                    print(f"⚠️  Auto-selected model: {model_to_use}")
                    model_found = True
            except:
                pass
        
        if not model_found:
            raise ValueError(
                f"Could not initialize any Gemini model. "
                f"Last error: {last_error}. "
                f"Run 'py check_models.py' to see available models."
            )
    
    def query_with_context(self, user_query: str, context: str) -> str:
        """
        Query Gemini with user question and document context.
        
        Args:
            user_query: User's question or prompt
            context: Relevant document context to include
            
        Returns:
            Gemini's response
        """
        # Truncate context if too long
        if len(context) > MAX_CONTEXT_LENGTH:
            context = context[:MAX_CONTEXT_LENGTH] + "... [truncated]"
        
        # Construct prompt with context
        prompt = f"""You have access to the following documents from Google Drive:

{context}

---

User Question: {user_query}

Please provide a comprehensive answer based on the documents above. If the information is not available in the documents, please state that clearly."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            error_msg = str(e)
            # Check for rate limit/quota errors
            if '429' in error_msg or 'quota' in error_msg.lower() or 'rate' in error_msg.lower():
                if 'gemini-2.5-pro' in error_msg or 'gemini-2.0' in error_msg:
                    return f"Error: The model requires a paid plan. Please change GEMINI_MODEL in config.py to 'gemini-flash-latest' or 'gemini-pro-latest' for free tier access."
                else:
                    return f"Error: Rate limit exceeded. Please wait a moment and try again. Details: {error_msg[:300]}"
            # Check for 404 model not found errors
            if '404' in error_msg and 'not found' in error_msg.lower():
                return f"Error: Model not found. The configured model may not be available. Please check GEMINI_MODEL in config.py. Available free tier models: 'gemini-flash-latest' or 'gemini-pro-latest'. For premium models, a paid Google Cloud billing account is required. See CLIENT_PRICING_MESSAGE.md for details."
            return f"Error querying Gemini: {error_msg}"
    
    def query(self, prompt: str) -> str:
        """
        Query Gemini without additional context (for general queries).
        
        Args:
            prompt: User's prompt
            
        Returns:
            Gemini's response
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            error_msg = str(e)
            # Check for rate limit/quota errors
            if '429' in error_msg or 'quota' in error_msg.lower() or 'rate' in error_msg.lower():
                if 'gemini-2.5-pro' in error_msg or 'gemini-2.0' in error_msg:
                    return f"Error: The model requires a paid plan. Please change GEMINI_MODEL in config.py to 'gemini-flash-latest' or 'gemini-pro-latest' for free tier access."
                else:
                    return f"Error: Rate limit exceeded. Please wait a moment and try again. Details: {error_msg[:300]}"
            # Check for 404 model not found errors
            if '404' in error_msg and 'not found' in error_msg.lower():
                return f"Error: Model not found. The configured model may not be available. Please check GEMINI_MODEL in config.py. Available free tier models: 'gemini-flash-latest' or 'gemini-pro-latest'. For premium models, a paid Google Cloud billing account is required. See CLIENT_PRICING_MESSAGE.md for details."
            return f"Error querying Gemini: {error_msg}"

