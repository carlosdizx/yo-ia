from typing import Dict, List, Optional, Any
from .ai_providers.provider_factory import AIProviderFactory, ProviderType
from .ai_providers.base_provider import BaseAIProvider
from ..utils.env_config import load_config


class AIService:
    """
    Main AI service that provides a unified interface for all AI providers.
    This service handles provider selection, configuration, and request routing.
    """

    def __init__(self, default_provider: str = "gemini"):
        """
        Initialize AI service
        
        Args:
            default_provider: Default provider to use if none specified
        """
        self.config = load_config()
        self.default_provider = default_provider
        self._providers: Dict[str, BaseAIProvider] = {}
        self._initialize_providers()

    def _initialize_providers(self):
        """Initialize all available providers based on environment configuration"""
        provider_configs = {
            "gemini": {
                "api_key": self.config.get("GEMINI_API_KEY"),
                "model_name": "gemini-2.5-flash"
            },
            "deepseek": {
                "api_key": self.config.get("DEEP_SEEK_API_KEY"),
                "model_name": "deepseek-chat"
            }
        }

        for provider_name, config in provider_configs.items():
            if config["api_key"]:
                try:
                    provider_type = AIProviderFactory.from_string(provider_name)
                    provider = AIProviderFactory.create_provider(
                        provider_type=provider_type,
                        api_key=config["api_key"],
                        model_name=config["model_name"]
                    )
                    self._providers[provider_name] = provider
                    print(f"{provider.get_provider_name()} provider initialized successfully")
                except Exception as e:
                    print(f"Failed to initialize {provider_name} provider: {str(e)}")
                    raise e

    def generate_response(
            self,
            messages: List[Dict[str, str]],
            provider: Optional[str] = None,
            **kwargs
    ) -> str:
        """
        Generate a response using the specified or default provider
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            provider: Optional provider name (uses default if not specified)
            **kwargs: Additional generation parameters
            
        Returns:
            Generated response as string
            
        Raises:
            ValueError: If provider is not available
            Exception: If generation fails
        """
        provider_name = provider or self.default_provider

        if provider_name not in self._providers:
            available = list(self._providers.keys())
            raise ValueError(
                f"Provider '{provider_name}' not available. "
                f"Available providers: {available}"
            )

        provider_instance = self._providers[provider_name]
        return provider_instance.generate_response(messages, **kwargs)

    def stream_response(
            self,
            messages: List[Dict[str, str]],
            provider: Optional[str] = None,
            **kwargs
    ) -> Any:
        """
        Generate a streaming response using the specified or default provider
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            provider: Optional provider name (uses default if not specified)
            **kwargs: Additional generation parameters
            
        Returns:
            Streaming response object
            
        Raises:
            ValueError: If provider is not available
            Exception: If streaming fails
        """
        provider_name = provider or self.default_provider

        if provider_name not in self._providers:
            available = list(self._providers.keys())
            raise ValueError(
                f"Provider '{provider_name}' not available. "
                f"Available providers: {available}"
            )

        provider_instance = self._providers[provider_name]
        return provider_instance.stream_response(messages, **kwargs)

    def get_available_providers(self) -> List[str]:
        """Get list of available and initialized providers"""
        return list(self._providers.keys())

    def get_provider_info(self, provider_name: str) -> Dict[str, Any]:
        """
        Get information about a specific provider
        
        Args:
            provider_name: Name of the provider
            
        Returns:
            Dictionary with provider information
        """
        if provider_name not in self._providers:
            return {"available": False, "error": "Provider not initialized"}

        provider = self._providers[provider_name]
        return {
            "available": True,
            "name": provider.get_provider_name(),
            "model": provider.model_name,
            "connection_valid": provider.validate_connection()
        }

    def set_default_provider(self, provider_name: str):
        """
        Set the default provider
        
        Args:
            provider_name: Name of the provider to set as default
            
        Raises:
            ValueError: If provider is not available
        """
        if provider_name not in self._providers:
            available = list(self._providers.keys())
            raise ValueError(
                f"Cannot set '{provider_name}' as default. "
                f"Available providers: {available}"
            )

        self.default_provider = provider_name

    def health_check(self) -> Dict[str, Any]:
        """
        Perform health check on all providers
        
        Returns:
            Dictionary with health status of all providers
        """
        health_status = {
            "total_providers": len(self._providers),
            "providers": {}
        }

        for name, provider in self._providers.items():
            try:
                is_healthy = provider.validate_connection()
                health_status["providers"][name] = {
                    "status": "healthy" if is_healthy else "unhealthy",
                    "provider_name": provider.get_provider_name(),
                    "model": provider.model_name
                }
            except Exception as e:
                health_status["providers"][name] = {
                    "status": "error",
                    "error": str(e)
                }

        return health_status
