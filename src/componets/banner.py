from src.services.gemini_service import GeminiService

def banner(st, client: GeminiService):
    messages = {
        "es": {
            "title": "AI-Me",
            "info": "¡Hola! Soy **AI-Me**, asistente personal diseñado por **Carlos Ernesto Díaz Basante**. Estoy "
                    "aquí para responder cualquier pregunta sobre mi creador y proporcionar detalles precisos sobre "
                    "su vida. "
                    "Puedes cambiar el idioma en la barra lateral.",
            "questions": [
                "¿Quién es Carlos Ernesto Díaz Basante?",
                "Su profesión y experiencia",
                "Áreas de interés",
                "Gustos y hobbies",
                "Obtener su CV y redes sociales",
                "Proyectos, logros, educación y certificaciones"
            ],
            "ai_info": "Puedes hacerme preguntas sobre mi creador, su profesión y experiencia, temas de interés, "
                       "etc. También puedes preguntarme sobre sus gustos y hobbies, o descargar su CV en formato PDF.",
            "thinking": "Pensando..."
        },
        "en": {
            "title": "AI-Me",
            "info": "Hello! I am **AI-Me**, a personal assistant designed by **Carlos Ernesto Díaz Basante**. I am "
                    "here to answer any questions about my creator and provide detailed information about his life. "
                    "You can change the language in the sidebar.",
            "questions": [
                "Who is Carlos Ernesto Díaz Basante?",
                "His profession and experience",
                "Areas of interest",
                "Likes and hobbies",
                "Get his CV and social media",
                "Projects, achievements education and certifications"
            ],
            "ai_info": "You can ask me about my creator, his profession and experience, areas of interest, etc. You "
                       "can also ask about his likes and hobbies, or download his CV in PDF format.",
            "thinking": "Thinking..."
        }
    }

    current_language = st.session_state.language
    text = messages[current_language]

    st.title(text["title"])
    st.chat_message("ai").info(text["info"])

    for question in text["questions"]:
        if st.button(question):
            # Agregar la pregunta del usuario a los mensajes
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            st.session_state.messages.append({"role": "user", "content": question})
            
            # Mostrar spinner mientras se procesa la respuesta
            with st.spinner(text.get("thinking", "Pensando..." if current_language == "es" else "Thinking...")):
                response = client.get_response(question)
            
            # Agregar la respuesta del AI a los mensajes
            st.session_state.messages.append({"role": "ai", "content": response})
            
            # Rerun para actualizar la interfaz
            st.rerun()

    st.chat_message("ai").info(text["ai_info"])
