def chat(st):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = (st.chat_input
              (key="chat_input",
               placeholder="Aquí puedes preguntarme cualquier cosa sobre mi creador ♥️",
               max_chars=300)
              )

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)

        response = "¡Gracias por tu mensaje! ¿En qué más puedo ayudarte hoy?"
        st.session_state.messages.append({"role": "ai", "content": response})
        st.chat_message("ai").info(response)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
