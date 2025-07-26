def statistics_banner(st):
    messages = {
        "es": {
            "chats": {
                "title": "Estadísticas del chat",
                "subtitle": "Mensajes enviados"
            }
        },
        "en": {
            "chats": {
                "title": "Chat Statistics",
                "subtitle": "Messages sent"
            }

        }
    }

    cha_messages = messages[st.session_state.language]["chats"]

    if "messages" in st.session_state:
        num_messages = len(st.session_state.messages)
        st.sidebar.markdown(f"### {cha_messages['title']}")
        st.sidebar.markdown(f"{cha_messages['subtitle']}: {num_messages}")
