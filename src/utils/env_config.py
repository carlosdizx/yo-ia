import os
from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv()

    required_env_vars = ["GEMINI_API_KEY"]

    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        error_message = f"ERROR: Faltan las siguientes variables de entorno: {', '.join(missing_vars)}"

        with open("missing_env_vars.txt", "w", encoding="utf-8") as file:
            file.write(error_message)

        raise EnvironmentError(error_message)
    return {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
    }
