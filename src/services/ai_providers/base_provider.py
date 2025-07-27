from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any


class BaseAIProvider(ABC):

    def __init__(self, api_key: str, model_name: str = None):
        self.api_key = api_key
        self.model_name = model_name
    
    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate a response from the AI provider
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            **kwargs: Additional provider-specific parameters
            
        Returns:
            Generated response as string
        """
        pass
    
    @abstractmethod
    def stream_response(self, messages: List[Dict[str, str]], **kwargs) -> Any:
        """
        Generate a streaming response from the AI provider
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            **kwargs: Additional provider-specific parameters
            
        Returns:
            Streaming response object
        """
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Return the name of the provider"""
        pass
    
    @abstractmethod
    def validate_connection(self) -> bool:
        """Validate if the provider connection is working"""
        pass
    
    def format_messages(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Format messages for the provider (can be overridden by specific providers)
        
        Args:
            messages: List of message dictionaries
            
        Returns:
            Formatted messages
        """
        return messages
