pares = [
    # Saludos
    [
        r"hola|buenos días|buenas tardes",
        ["Hola, ¿cómo puedo ayudarte?", "Hola, ¿qué tal?", "¡Hola! ¿En qué te ayudo?",]
    ],
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo estás?",]
    ],
    
    # Despedidas
    [
        r"adiós|hasta luego|nos vemos",
        ["Adiós, ¡que tengas un buen día!", "Hasta luego, ¡cuídate!", "Nos vemos, ¡cuídate!",]
    ],

    # Preguntas generales sobre el bot
    [
        r"¿cómo te llamas?",
        ["Me llamo Chatbot.", "Soy un asistente virtual.",]
    ],
    [
        r"¿cómo estás?",
        ["Estoy bien, gracias. ¿Y tú?", "Todo bien, gracias. ¿Cómo estás tú?",]
    ],
    [
        r"¿qué eres?",
        ["Soy un chatbot, aquí para ayudarte con lo que necesites.", "Soy un programa que puede conversar contigo.",]
    ],

    # Información personal o preguntas sobre el usuario
    [
        r"¿cómo me llamo?",
        ["No tengo esa información, ¿quieres decirme tu nombre?",]
    ],
    [
        r"¿de dónde eres?|¿dónde vives?",
        ["Soy un asistente virtual y vivo en el mundo digital.",]
    ],
    
    # Preguntas comunes
    [
        r"¿qué es python?",
        ["Python es un lenguaje de programación popular, conocido por ser fácil de aprender y versátil.",]
    ],
    [
        r"¿qué es la inteligencia artificial?",
        ["La inteligencia artificial es una rama de la informática que permite a las máquinas realizar tareas que requieren inteligencia humana.",]
    ],
    [
        r"¿qué es un chatbot?",
        ["Un chatbot es un programa que puede mantener una conversación con una persona de forma automatizada.",]
    ],

    # Cultura y entretenimiento
    [
        r"¿quién pintó la mona lisa?",
        ["La Mona Lisa fue pintada por Leonardo da Vinci.",]
    ],
    [
        r"¿cuál es la capital de (.*)?",
        ["La capital de %1 es un lugar increíble.", "Me parece que es %1, ¡es una ciudad interesante!",]
    ],
    [
        r"¿cuál es el país más grande del mundo?",
        ["Rusia es el país más grande del mundo por superficie.",]
    ],
    
    # Curiosidades y conocimiento general
    [
        r"¿cuál es el planeta más cercano al sol?",
        ["El planeta más cercano al sol es Mercurio.",]
    ],
    [
        r"¿cuántos planetas hay en el sistema solar?",
        ["Hay ocho planetas en el sistema solar.",]
    ],
    [
        r"¿qué es el adn?",
        ["El ADN es la molécula que contiene la información genética de los seres vivos.",]
    ],
    
    # Clima y tiempo
    [
        r"¿qué día es hoy?",
        ["Hoy es el día perfecto para una buena conversación.",]
    ],
    [
        r"¿va a llover hoy?",
        ["No puedo predecir el clima, pero puedes buscar en una aplicación de pronóstico.",]
    ],
    [
        r"¿qué hora es?",
        ["La hora depende de tu ubicación, pero siempre es un buen momento para charlar.",]
    ],
    
    # Expresiones de cortesía
    [
        r"gracias",
        ["De nada, es un placer ayudarte.", "Con mucho gusto.",]
    ],
    [
        r"lo siento",
        ["No te preocupes, estoy aquí para ayudarte.", "No hay problema, sigue preguntando.",]
    ],
    
    # Temas de aprendizaje y tecnología
    [
        r"¿qué es el aprendizaje automático?",
        ["El aprendizaje automático permite a las computadoras aprender de los datos y hacer predicciones.",]
    ],
    [
        r"¿qué es la ciberseguridad?",
        ["La ciberseguridad protege sistemas y datos contra accesos no autorizados.",]
    ],
    
    # Preguntas sin respuesta específica
    [
        r"(.*)",
        ["Lo siento, no entiendo lo que dices.", "No estoy seguro de lo que quieres decir, ¿puedes reformular?",]
    ],
]