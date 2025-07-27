from enum import Enum
from typing import Optional, Dict, Any
from .base_provider import BaseAIProvider
from .gemini_provider import GeminiProvider
from .deepseek_provider import DeepSeekProvider


class ProviderType(Enum):
    """Enumeration of available AI providers"""
    GEMINI = "gemini"
    DEEPSEEK = "deepseek"


class AIProviderFactory:
    """Factory class for creating AI provider instances"""
    
    _providers = {
        ProviderType.GEMINI: GeminiProvider,
        ProviderType.DEEPSEEK: DeepSeekProvider,
    }
    
    @classmethod
    def create_provider(
        self,
        provider_type: ProviderType,
        api_key: str,
        model_name: Optional[str] = None,
        **kwargs
    ) -> BaseAIProvider:
        """
        Create an AI provider instance
        
        Args:
            provider_type: Type of provider to create
            api_key: API key for the provider
            model_name: Optional model name (uses provider default if not specified)
            **kwargs: Additional provider-specific parameters
            
        Returns:
            Configured AI provider instance
            
        Raises:
            ValueError: If provider type is not supported
        """
        if provider_type not in self._providers:
            available_providers = [p.value for p in ProviderType]
            raise ValueError(
                f"Unsupported provider type: {provider_type}. "
                f"Available providers: {available_providers}"
            )
        
        provider_class = self._providers[provider_type]
        
        if model_name:
            return provider_class(api_key, model_name, **kwargs)
        else:
            return provider_class(api_key, **kwargs)
    
    @classmethod
    def get_available_providers(cls) -> list[str]:
        """Get list of available provider names"""
        return [provider.value for provider in ProviderType]
    
    @classmethod
    def from_string(cls, provider_name: str) -> ProviderType:
        """
        Convert string to ProviderType enum
        
        Args:
            provider_name: Name of the provider as string
            
        Returns:
            ProviderType enum value
            
        Raises:
            ValueError: If provider name is not recognized
        """
        provider_name = provider_name.lower().strip()
        
        for provider_type in ProviderType:
            if provider_type.value == provider_name:
                return provider_type
        
        available_providers = [p.value for p in ProviderType]
        raise ValueError(
            f"Unknown provider: {provider_name}. "
            f"Available providers: {available_providers}"
        )
