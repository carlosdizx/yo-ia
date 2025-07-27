import streamlit as sst
from src.services.gemini_service import GeminiService


def chat(st: sst, client: GeminiService):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    messages = {
        "es": {
            "placeholder": "Aquí puedes preguntarme cualquier cosa sobre mi creador ♥️",
            "thinking": "Pensando...",
            "error": "Ocurrió un error al generar la respuesta."
        },
        "en": {
            "placeholder": "Here you can ask me anything about my creator ♥️",
            "thinking": "Thinking...",
            "error": "An error occurred while generating the response."
        }
    }

    current_language = st.session_state.language
    text = messages[current_language]

    prompt = st.chat_input(key="chat_input", placeholder=text["placeholder"], max_chars=300)

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner(text["thinking"]):
            response = client.get_response(prompt)

        st.session_state.messages.append({"role": "ai", "content": response})

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
