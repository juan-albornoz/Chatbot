import streamlit as st
from nltk.chat.util import Chat, reflections
from frases import pares

st.set_page_config(page_title="Chatbot con NLTK", page_icon="💬", layout="centered")

# Crear instancia del chatbot con NLTK
chatbot = Chat(pares, reflections)

# Configuración de la barra lateral
with st.sidebar:
    st.title("💬 Chatbot con NLTK")
    st.caption("🚀 Grupo sin TACC pero con Tocs")
    st.markdown(
    """
    [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juan-albornoz/Chatbot)
    """
)

# Título principal de la aplicación
st.title("💬 Chat")

# Inicializar el historial de mensajes en el estado de la sesión
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "¿En qué puedo ayudarte?"}]

# Mostrar mensajes previos
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Obtener respuesta del chatbot de NLTK
    response = chatbot.respond(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)