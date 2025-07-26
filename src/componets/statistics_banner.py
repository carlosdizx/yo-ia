def statistics_banner(st):
    messages = {
        "es": {
            "chats": {
                "title": "Estadísticas del chat",
                "subtitle": "Mensajes enviados",
                "subtitle2": "Cantidad de letras enviadas",
            }
        },
        "en": {
            "chats": {
                "title": "Chat Statistics",
                "subtitle": "Messages sent",
                "subtitle2": "Number of letters sent",
            }

        }
    }

    cha_messages = messages[st.session_state.language]["chats"]

    if "messages" in st.session_state:
        num_messages = len(st.session_state.messages)
        num_letters = sum(len(message["content"]) for message in st.session_state.messages)
        st.sidebar.markdown(f"### {cha_messages['title']}")
        st.sidebar.markdown(f"{cha_messages['subtitle']}: {num_messages}")
        st.sidebar.markdown(f"{cha_messages['subtitle2']}: {num_letters}")
