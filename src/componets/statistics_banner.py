import pandas as pd


def statistics_banner(st):
    messages = {
        "es": {
            "chats": {
                "title": "Estadísticas del chat",
                "subtitle": "Mensajes enviados",
                "subtitle2": "Cantidad de letras enviadas",
                "subtitle3": "Cantidad de letras enviadas por el usuario",
                "subtitle4": "Cantidad de letras enviadas por la IA",
            },
            "reset_session": "Reiniciar sesión"
        },
        "en": {
            "chats": {
                "title": "Chat Statistics",
                "subtitle": "Messages sent",
                "subtitle2": "Number of letters sent",
                "subtitle3": "Number of letters sent by the user",
                "subtitle4": "Number of letters sent by the AI",
            },
            "reset_session": "Reset Session"
        }
    }

    cha_messages = messages[st.session_state.language]["chats"]

    if "messages" in st.session_state:
        df = pd.DataFrame({
            "role": [message["role"] for message in st.session_state.messages],
            "content": [message["content"] for message in st.session_state.messages],
        })

        message_count_by_role = df['role'].value_counts().to_dict()

        st.sidebar.markdown(f"### {cha_messages['title']}")
        st.sidebar.markdown(
            f"{cha_messages['subtitle']}: {df.shape[0]}"
            f"(User: {message_count_by_role.get('user', 0)},"
            f" AI: {message_count_by_role.get('ai', 0)})")

        # st.sidebar.markdown(f"{cha_messages['subtitle2']}: {num_letters}")
        # st.sidebar.markdown(f"{cha_messages['subtitle3']}: {num_letters_user}")
        # st.sidebar.markdown(f"{cha_messages['subtitle4']}: {num_letters_ai}")

    reset_session_text = messages[st.session_state.language]["reset_session"]

    if st.sidebar.button(reset_session_text):
        st.session_state.messages = []
        st.sidebar.markdown(f"**Sesión reiniciada.**")

        st.rerun()
