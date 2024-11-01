import streamlit as st
from nltk.chat.util import Chat, reflections
from frases import pares

# Crear instancia del chatbot
chatbot = Chat(pares, reflections)

# Configuración de la aplicación con Streamlit
st.title("Chatbot con NLTK y Streamlit")
st.write("Grupo sin TACC pero con Tocs")

# Inicializar una lista para almacenar el historial de conversación
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Entrada de usuario
user_input = st.text_input("Tú:", "")

# Procesar entrada cuando se ingresa texto
if user_input:
    # Obtener la respuesta del chatbot
    response = chatbot.respond(user_input)
    
    # Guardar la conversación en el historial
    st.session_state.conversation_history.append(("Tú", user_input))
    st.session_state.conversation_history.append(("Chatbot", response))
    
    # Limpiar el campo de entrada
    st.session_state["user_input"] = ""  # Esto restablece la entrada de texto

# Mostrar el historial de conversación
for i, (sender, message) in enumerate(st.session_state.conversation_history):
    if sender == "Tú":
        st.text_area("Tú:", message, height=50, disabled=True, key=f"user_{i}")
    else:
        st.text_area("Chatbot:", message, height=50, disabled=True, key=f"bot_{i}")