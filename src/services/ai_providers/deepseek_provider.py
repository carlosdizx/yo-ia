import requests
import json
from typing import Dict, List, Any
from .base_provider import BaseAIProvider


class DeepSeekProvider(BaseAIProvider):
    """DeepSeek AI provider implementation"""
    
    def __init__(self, api_key: str, model_name: str = "deepseek-chat"):
        super().__init__(api_key, model_name)
        self.base_url = "https://api.deepseek.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate response using DeepSeek"""
        try:
            formatted_messages = self._format_for_deepseek(messages)
            payload = {
                "model": self.model_name,
                "messages": formatted_messages,
                **self._get_generation_params(**kwargs)
            }
            
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"DeepSeek API request error: {str(e)}")
        except KeyError as e:
            raise Exception(f"DeepSeek API response format error: {str(e)}")
        except Exception as e:
            raise Exception(f"DeepSeek API error: {str(e)}")
    
    def stream_response(self, messages: List[Dict[str, str]], **kwargs) -> Any:
        """Generate streaming response using DeepSeek"""
        try:
            formatted_messages = self._format_for_deepseek(messages)
            payload = {
                "model": self.model_name,
                "messages": formatted_messages,
                "stream": True,
                **self._get_generation_params(**kwargs)
            }
            
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                stream=True,
                timeout=30
            )
            response.raise_for_status()
            
            return response
            
        except Exception as e:
            raise Exception(f"DeepSeek streaming error: {str(e)}")
    
    def get_provider_name(self) -> str:
        """Return provider name"""
        return "DeepSeek"
    
    def validate_connection(self) -> bool:
        """Validate DeepSeek connection"""
        try:
            test_messages = [{"role": "user", "content": "Hello"}]
            response = self.generate_response(test_messages)
            return bool(response)
        except Exception:
            return False
    
    def _format_for_deepseek(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Format messages for DeepSeek API"""
        formatted_messages = []
        
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            
            # Map roles to DeepSeek format
            if role == "ai":
                role = "assistant"
            elif role not in ["user", "assistant", "system"]:
                role = "user"
            
            formatted_messages.append({
                "role": role,
                "content": content
            })
        
        return formatted_messages
    
    def _get_generation_params(self, **kwargs) -> Dict[str, Any]:
        """Get generation parameters for DeepSeek"""
        params = {}
        
        if "temperature" in kwargs:
            params["temperature"] = kwargs["temperature"]
        if "max_tokens" in kwargs:
            params["max_tokens"] = kwargs["max_tokens"]
        if "top_p" in kwargs:
            params["top_p"] = kwargs["top_p"]
        if "frequency_penalty" in kwargs:
            params["frequency_penalty"] = kwargs["frequency_penalty"]
        if "presence_penalty" in kwargs:
            params["presence_penalty"] = kwargs["presence_penalty"]
        
        return params
