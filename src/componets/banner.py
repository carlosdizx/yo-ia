import streamlit as stt


def banner(st):
    messages = {
        "es": {
            "title": "AI-Me",
            "info": "¡Hola! Soy **YO-IA**, asistente personal diseñado por **Carlos Ernesto Díaz Basante**. Estoy "
                    "aquí para responder cualquier pregunta sobre mi creador y proporcionar detalles precisos sobre "
                    "su vida. "
                    "Puedes cambiar el idioma en la barra lateral.",
            "questions": [
                "¿Quién es Carlos Ernesto Díaz Basante?",
                "Su profesión y experiencia",
                "Áreas de interés",
                "Gustos y hobbies",
                "Descargar su CV",
                "Temas de interés (centros de la casa, proyectos, y mucho más)"
            ],
            "ai_info": "Puedes hacerme preguntas sobre mi creador, su profesión y experiencia, temas de interés, "
                       "etc. También puedes preguntarme sobre sus gustos y hobbies, o descargar su CV en formato PDF."
        },
        "en": {
            "title": "AI-Me",
            "info": "Hello! I am **ME-IA**, a personal assistant designed by **Carlos Ernesto Díaz Basante**. I am "
                    "here to answer any questions about my creator and provide detailed information about his life. "
                    "You can change the language in the sidebar.",
            "questions": [
                "Who is Carlos Ernesto Díaz Basante?",
                "His profession and experience",
                "Areas of interest",
                "Likes and hobbies",
                "Download his CV",
                "Topics of interest (centers of the house, projects, and more)"
            ],
            "ai_info": "You can ask me about my creator, his profession and experience, areas of interest, etc. You "
                       "can also ask about his likes and hobbies, or download his CV in PDF format."
        }
    }

    current_language = st.session_state.language
    text = messages[current_language]

    st.title(text["title"])
    st.chat_message("ai").info(text["info"])

    for question in text["questions"]:
        if st.button(question):
            st.session_state.chat_input = question

    st.chat_message("ai").info(text["ai_info"])
