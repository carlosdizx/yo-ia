import pandas as pd


def statistics_banner(st):
    messages = {
        "es": {
            "chats": {
                "title": "Estadísticas del chat",
                "table": {
                    "messages": "Mensajes",
                    "words": "Palabras",
                    "letters": "Letras"
                }
            },
            "reset_session": "Reiniciar sesión"
        },
        "en": {
            "chats": {
                "title": "Chat Statistics",
                "table": {
                    "messages": "Messages",
                    "words": "Words",
                    "letters": "Letters"
                }
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

        letters_user = sum(len(str(msg).replace(" ", "")) for msg in df_user)
        letters_ai = sum(len(str(msg).replace(" ", "")) for msg in df_ai)

        st.sidebar.header(cha_messages['title'])

        summary_df = pd.DataFrame({
            cha_messages['table']['messages']: [len(df_user), len(df_ai)],
            cha_messages['table']['words']: [sum_words_user, sum_words_ai],
            cha_messages['table']['letters']: [letters_user, letters_ai]
        }, index=['User', 'AI'])

        st.sidebar.table(summary_df.T)

    reset_session_text = messages[st.session_state.language]["reset_session"]

    if st.sidebar.button(reset_session_text):
        st.session_state.messages = []
        st.sidebar.markdown(f"**Sesión reiniciada.**")

        st.rerun()
