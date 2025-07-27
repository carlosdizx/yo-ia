from src.services import AIService


def chat(st):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "ai_service" not in st.session_state:
        st.session_state.ai_service = AIService(default_provider="gemini")

    messages = {
        "es": {
            "placeholder": "Aquí puedes preguntarme cualquier cosa sobre mi creador ♥️",
            "error": "Lo siento, hubo un error al procesar tu mensaje. Inténtalo de nuevo."
        },
        "en": {
            "placeholder": "Here you can ask me anything about my creator ♥️",
            "error": "Sorry, there was an error processing your message. Please try again."
        }
    }

    current_language = st.session_state.language
    text = messages[current_language]

    prompt = st.chat_input(key="chat_input", placeholder=text["placeholder"], max_chars=300)

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            ai_messages = []
            for msg in st.session_state.messages:
                ai_messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

            with st.spinner("Generando respuesta..."):
                response = st.session_state.ai_service.generate_response(
                    ai_messages,
                    temperature=0.7,
                    max_tokens=10000
                )

            st.session_state.messages.append({"role": "ai", "content": response})

        except Exception as e:
            error_message = text["error"]
            st.session_state.messages.append({"role": "ai", "content": error_message})
            st.error(f"Error: {str(e)}")

    def message_generator():
        yield from st.session_state.messages

    for message in message_generator():
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
