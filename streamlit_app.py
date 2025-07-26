import streamlit as st
import google.generativeai as genai
from src.utils.env_config import load_config

# Configura la clave API a partir de las variables de entorno
gemini_api_key = load_config().get("GEMINI_API_KEY")

# Si la clave no está configurada en el entorno, muestra un mensaje de error
if not gemini_api_key:
    st.error("No se encontró la clave API de Google Gemini. Por favor, asegúrate de configurarla en las variables de entorno.")

else:
    # Configurar el cliente de Google Generative AI con la clave API
    genai.configure(api_key=gemini_api_key)

    # Inicializa el modelo de Generative AI
    model = genai.GenerativeModel("models/gemini-2.5-flash-lite")  # Usamos el modelo más reciente disponible

    # Establece el título y la descripción de bienvenida
    st.title("Chatbot Gemini - YO-IA")
    st.write("""
    ¡Hola! Soy **YO-IA**, tu asistente personal diseñado por Carlos Ernesto Díaz Basante. Estoy aquí para responder cualquier 
    pregunta sobre mi creador y proporcionar detalles precisos sobre su vida. Si alguna vez mis sensores se desconectan, no te 
    preocupes, siempre estoy listo para adaptarme y seguir aprendiendo.
    """)

    # Crear una variable de estado para almacenar los mensajes del chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar los mensajes previos del chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de entrada de texto para que el usuario ingrese su mensaje
    if prompt := st.chat_input("¿Qué tienes en mente?"):
        # Almacenar y mostrar el mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Preparar el historial de mensajes para la API de Gemini
        gemini_messages = []
        for message in st.session_state.messages:
            if message["role"] == "user":
                gemini_messages.append({"role": "user", "parts": [message["content"]]})
            elif message["role"] == "assistant":  # Cambiar 'assistant' por 'model' para Gemini
                gemini_messages.append({"role": "model", "parts": [message["content"]]})

        try:
            # Iniciar la sesión de chat con el modelo de Gemini
            chat_session = model.start_chat(history=gemini_messages[:-1])

            # Enviar el mensaje más reciente del usuario
            response_stream = chat_session.send_message(gemini_messages[-1]["parts"][0], stream=True)

            # Mostrar la respuesta generada en el chat
            full_response = ""
            with st.chat_message("assistant"):
                # Muestra el texto a medida que se recibe
                for chunk in response_stream:
                    if chunk.text:  # Verificar que el chunk tiene texto
                        full_response += chunk.text
                        st.markdown(full_response + "▌")  # Agregar efecto de cursor intermitente
                st.markdown(full_response)  # Mostrar la respuesta final sin cursor

            # Guardar la respuesta del modelo en el historial de mensajes
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            # Manejo de errores
            st.error(f"Ocurrió un error al comunicarse con la API de Gemini: {e}")
            st.session_state.messages.pop()  # Eliminar el último mensaje del usuario si ocurre un error
