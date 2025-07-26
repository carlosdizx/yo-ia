import pandas as pd


def statistics_banner(st):
    messages = {
        "es": {
            "chats": {
                "title": "Estadísticas del chat",
                "subtitle0": "Mensajes enviados",
                "subtitle1": "Cantidad de palabras enviadas",
                "subtitle2": "Cantidad de letras enviadas",
                "subtitle3": "Cantidad de letras enviadas por el usuario",
                "subtitle4": "Cantidad de letras enviadas por la IA",
            },
            "reset_session": "Reiniciar sesión"
        },
        "en": {
            "chats": {
                "title": "Chat Statistics",
                "subtitle0": "Messages sent",
                "subtitle1": "Number of words sent",
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

        df_grouped = df.groupby('role')['content'].apply(list)

        df_user = df_grouped.get('user', [])
        df_ai = df_grouped.get('ai', [])

        words_user = [str(msg).split() for msg in df_user]
        words_ai = [str(msg).split() for msg in df_ai]

        sum_words_user = sum([len(msg) for msg in words_user])
        sum_words_ai = sum([len(msg) for msg in words_ai])

        st.sidebar.markdown(
            f"{cha_messages['subtitle0']}: {df.shape[0]}<br>"
            f"User: {len(df_user)}<br>"
            f"AI: {len(df_ai)}",
            unsafe_allow_html=True
        )

        st.sidebar.markdown(
            f"{cha_messages['subtitle1']}: {sum_words_user + sum_words_ai}<br>"
            f"User: {sum_words_user}<br>"
            f"AI: {sum_words_ai}",
            unsafe_allow_html=True
        )

    reset_session_text = messages[st.session_state.language]["reset_session"]

    if st.sidebar.button(reset_session_text):
        st.session_state.messages = []
        st.sidebar.markdown(f"**Sesión reiniciada.**")

        st.rerun()
