import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Chatbot con Personalidad del Grupo", page_icon="🤖")

st.markdown("## 🤖 Chatbot con Personalidad del Grupo")
st.write("Este chatbot reúne las personalidades, gustos y fortalezas de Juan Manuel, Aylen, Kleiber, Johhan y Juan José.")

# Base de conocimientos basada en la entrevista a los 5 compañeros
knowledge_base = {
    "cancion": "Me gusta escuchar de todo un poco, desde 'QUE LIO' de Blessd, rap colombiano, 'Cam not' de Kino, hasta temas variados, rock y canciones románticas.",
    "pelicula": "Mis películas favoritas son variadas: desde 'La jungla', 'Zombieland', 'Jurassic Park (1993)', 'Gigantes de acero' hasta 'Rápidos y furiosos'.",
    "deporte": "Me encanta el deporte, especialmente el voleibol, el baloncesto, el golf y mantenerme activo.",
    "materia": "Mis materias favoritas son Educación Física, Informática, Física, Música y Matemáticas.",
    "comida": "Disfruto mucho comer arroz paisa, salchipapa, lasaña, cazuela de mariscos y pasta.",
    "fortaleza": "Considero que mis mayores fortalezas son el intelecto, la agilidad mental, el deporte y la creatividad.",
    "debilidad": "A veces flaqueo con el amor, ciertos momentos de distracción o pequeños tropiezos, ¡pero siempre se mejora!"
}

pregunta = st.text_input("Hazle una pregunta al chatbot:", "Canción favorita de Aylen")

if st.button("Enviar y Escuchar"):
    respuesta_texto = "No estoy seguro de eso, ¡pero mis amigos y yo amamos la tecnología y el deporte!"
    for clave, rta in knowledge_base.items():
        if clave in pregunta.lower():
            respuesta_texto = rta
            break
        
    st.markdown("### Respuesta:")
    st.write(respuesta_texto)
    
    # Generar audio con gTTS
    tts = gTTS(text=respuesta_texto, lang='es')
    audio_file = "temp_audio.mp3"
    tts.save(audio_file)
    
    st.audio(audio_file, format='audio/mp3')
