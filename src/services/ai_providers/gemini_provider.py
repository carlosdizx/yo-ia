import google.generativeai as genai
from typing import Dict, List, Any
from .base_provider import BaseAIProvider


class GeminiProvider(BaseAIProvider):
    """Gemini AI provider implementation"""
    
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        super().__init__(api_key, model_name)
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate response using Gemini"""
        try:
            formatted_messages = self._format_for_gemini(messages)
            response = self.model.generate_content(
                formatted_messages,
                generation_config=self._get_generation_config(**kwargs)
            )
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")
    
    def stream_response(self, messages: List[Dict[str, str]], **kwargs) -> Any:
        """Generate streaming response using Gemini"""
        try:
            formatted_messages = self._format_for_gemini(messages)
            response = self.model.generate_content(
                formatted_messages,
                generation_config=self._get_generation_config(**kwargs),
                stream=True
            )
            return response
        except Exception as e:
            raise Exception(f"Gemini streaming error: {str(e)}")
    
    def get_provider_name(self) -> str:
        """Return provider name"""
        return "Gemini"
    
    def validate_connection(self) -> bool:
        """Validate Gemini connection"""
        try:
            test_response = self.model.generate_content("Hello")
            return bool(test_response.text)
        except Exception:
            return False
    
    def _format_for_gemini(self, messages: List[Dict[str, str]]) -> str:
        """Format messages for Gemini API"""
        formatted_text = ""
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            
            if role == "user":
                formatted_text += f"User: {content}\n"
            elif role == "ai" or role == "assistant":
                formatted_text += f"Assistant: {content}\n"
            else:
                formatted_text += f"{role}: {content}\n"
        
        return formatted_text.strip()
    
    def _get_generation_config(self, **kwargs) -> genai.types.GenerationConfig:
        """Get generation configuration for Gemini"""
        config_params = {
            "temperature": kwargs.get("temperature", 0.7),
            "top_p": kwargs.get("top_p", 0.8),
            "top_k": kwargs.get("top_k", 40),
            "max_output_tokens": kwargs.get("max_tokens", 2048),
        }
        
        return genai.types.GenerationConfig(**config_params)
