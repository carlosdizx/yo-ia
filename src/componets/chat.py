def chat(st):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    messages = {
        "es": {
            "placeholder": "Aquí puedes preguntarme cualquier cosa sobre mi creador ♥️",
            "response": "¡Gracias por tu mensaje! ¿En qué más puedo ayudarte hoy?"
        },
        "en": {
            "placeholder": "Here you can ask me anything about my creator ♥️",
            "response": "Thanks for your message! How else can I help you today?"
        }
    }

    current_language = st.session_state.language
    text = messages[current_language]

    prompt = st.chat_input(key="chat_input", placeholder=text["placeholder"], max_chars=300)

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = text["response"]
        st.session_state.messages.append({"role": "ai", "content": response})

    def message_generator():
        yield from st.session_state.messages

    for message in message_generator():
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
