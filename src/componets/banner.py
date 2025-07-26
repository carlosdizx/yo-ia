def banner(st):
    st.title("Chatbot Gemini - YO-IA")
    st.chat_message("ai").info("""
        ¡Hola! Soy **YO-IA**, asistente personal diseñado por **Carlos Ernesto Díaz Basante**.
        Estoy aquí para responder cualquier pregunta sobre mi creador y proporcionar detalles precisos sobre su vida.
    """)

    # Mostrar el mensaje de la IA con opciones como botones
    st.chat_message("ai").markdown("""
        Aquí tienes algunas cosas sobre las que puedes preguntarme:
        - ¿Quién es Carlos Ernesto Díaz Basante?
        - Su profesión y experiencia
        - Áreas de interés
        - Gustos y hobbies
        - Descargar su CV
        - Temas de interés: centros de la casa, proyectos, y más.
        
        Pídeme cualquier cosa que quieras saber sobre **Ernesto Díaz**.
    """)
