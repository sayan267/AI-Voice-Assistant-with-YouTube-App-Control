# voice_utils.py

import speech_recognition as sr
from gtts import gTTS
from langdetect import detect
from deep_translator import GoogleTranslator
from playsound import playsound
import random
import os

def speak(text, lang="en"):
    try:
        print(f"Assistant ({lang.upper()}): {text}")
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = f"voice_{random.randint(1,99999)}.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"[Voice Error] {e}")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {query}")
        lang = detect(query)
        print(f"🌐 Detected Language: {lang}")
        translated = GoogleTranslator(source='auto', target='en').translate(query)
        print(f"📝 Translated: {translated}")
        return translated.lower(), lang
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.", lang="en")
    except sr.RequestError:
        speak("Speech service is unavailable.", lang="en")
    return None, "en"
