def chat(st):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = st.chat_input(key="chat_input",
                           placeholder="Aquí puedes preguntarme cualquier cosa sobre mi creador ♥️",
                           accept_file=True,
                           file_type=["jpg", "jpeg", "png"],
                           max_chars=1000)

    if prompt:
        if prompt.text:
            st.session_state.messages.append({"role": "user", "content": prompt.text})
            st.chat_message("user").markdown(prompt.text)

            response = "¡Gracias por tu mensaje! ¿En qué más puedo ayudarte hoy?"
            st.session_state.messages.append({"role": "ai", "content": response})
            st.chat_message("ai").info(response)

        if prompt["files"]:
            st.image(prompt["files"][0], caption="Imagen enviada por el usuario")
            response = "¡Imagen recibida! ¿Quieres hacer algo con ella?"
            st.session_state.messages.append({"role": "ai", "content": response})
            st.chat_message("ai").info(response)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
