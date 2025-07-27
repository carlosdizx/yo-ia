from google.generativeai import configure, GenerativeModel

from src.config.setting import get_gemini_config
from src.prompts.system_instruction import build_system_instruction


class GeminiService:
    _instance = None

    def __new__(cls, language="es"):
        if cls._instance is None:
            cls._instance = super(GeminiService, cls).__new__(cls)
            cls._instance._initialize(language)
        return cls._instance

    def _initialize(self, language):
        config = get_gemini_config()
        configure(api_key=config["api_key"])

        system_instruction = build_system_instruction(language)
        self.model = GenerativeModel(
            model_name=config["model_name"],
            system_instruction=system_instruction
        )

    def get_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error al generar respuesta: {str(e)}"
