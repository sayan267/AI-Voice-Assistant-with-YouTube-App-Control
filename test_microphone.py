# test_microphone.py
import speech_recognition as sr

mic_index = 1  # 🔁 Replace this with your correct mic index
r = sr.Recognizer()

with sr.Microphone(device_index=mic_index) as source:
    print("Say something:")
    audio = r.listen(source)
    print("Recognizing...")
    print(r.recognize_google(audio))
