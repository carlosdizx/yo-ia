from google.generativeai import configure, GenerativeModel

from src.config.setting import get_gemini_config
from src.prompts.system_instruction import build_system_instruction


class GeminiService:
    _instance = None
    _current_language = None

    def __new__(cls, language="es"):
        # Si el idioma cambió, forzar nueva instancia
        if cls._instance is None or cls._current_language != language:
            cls._instance = super(GeminiService, cls).__new__(cls)
            cls._instance._initialize(language)
            cls._current_language = language
        return cls._instance

    def _initialize(self, language):
        config = get_gemini_config()
        configure(api_key=config["api_key"])

        system_instruction = build_system_instruction(language)
        self.model = GenerativeModel(
            model_name=config["model_name"],
            system_instruction=system_instruction
        )
        self.language = language

    @classmethod
    def reset_instance(cls):
        """Fuerza el reset de la instancia singleton"""
        cls._instance = None
        cls._current_language = None

    def get_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error al generar respuesta: {str(e)}"
