def banner(st):
    st.title("Chatbot Gemini - YO-IA")
    st.chat_message("ai").info("""
        ¡Hola! Soy **YO-IA**, asistente personal diseñado por **Carlos Ernesto Díaz Basante**.
        Estoy aquí para responder cualquier pregunta sobre mi creador y proporcionar detalles precisos sobre su vida.
    """)

    if st.button("¿Quién es Carlos Ernesto Díaz Basante?"):
        st.session_state.chat_input = "¿Quién es Carlos Ernesto Díaz Basante?"

    if st.button("Su profesión y experiencia"):
        st.session_state.chat_input = "Su profesión y experiencia"
    if st.button("Áreas de interés"):
        st.session_state.chat_input = "Áreas de interés"
    if st.button("Gustos y hobbies"):
        st.session_state.chat_input = "Gustos y hobbies"
    if st.button("Descargar su CV"):
        st.session_state.chat_input = "Descargar su CV"
    if st.button("Temas de interés (centros de la casa, proyectos, y mucho más)"):
        st.session_state.chat_input = "Temas de interés (centros de la casa, proyectos, y mucho más)"

    (st.chat_message('ai')
     .info("""Puedes hacerme preguntas sobre mi creador, su profesión y experiencia, temas de interés, etc.
     También puedes preguntarme sobre sus gustos y hobbies, o descargar su CV en formato PDF.
     Puedes darme tu nombre y subir tu foto para saber quien eres.
     """))
