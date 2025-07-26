def statistics_banner(st):
    messages = {
        "es": {
            "chats": {
                "title": "Estadísticas del chat",
                "subtitle": "Mensajes enviados",
                "subtitle2": "Cantidad de letras enviadas",
                "subtitle3": "Cantidad de letras enviadas por el usuario",
                "subtitle4": "Cantidad de letras enviadas por la IA",
            }
        },
        "en": {
            "chats": {
                "title": "Chat Statistics",
                "subtitle": "Messages sent",
                "subtitle2": "Number of letters sent",
                "subtitle3": "Number of letters sent by the user",
                "subtitle4": "Number of letters sent by the AI",
            }

        }
    }

    cha_messages = messages[st.session_state.language]["chats"]

    if "messages" in st.session_state:
        num_messages = len(st.session_state.messages)
        num_letters = sum(len(message["content"]) for message in st.session_state.messages)
        num_letters_user = sum(len(message["content"]) for message in st.session_state.messages if message["role"] == "user")
        num_letters_ai = sum(len(message["content"]) for message in st.session_state.messages if message["role"] == "ai")
        st.sidebar.markdown(f"### {cha_messages['title']}")
        st.sidebar.markdown(f"{cha_messages['subtitle']}: {num_messages}")
        st.sidebar.markdown(f"{cha_messages['subtitle2']}: {num_letters}")
        st.sidebar.markdown(f"{cha_messages['subtitle3']}: {num_letters_user}")
        st.sidebar.markdown(f"{cha_messages['subtitle4']}: {num_letters_ai}")
