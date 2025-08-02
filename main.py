import webbrowser
import time
import os
import re
import wikipedia
import pywhatkit
from jarvis import play_youtube_video, open_chrome, open_youtube, send_whatsapp_message
from utils import speak, listen
from agent import run_assistant


# Main assistant loop
def main():
    current_language = "en"  # Default language
    speak("Hi, I am Sai. How can I help you?", lang=current_language)

    while True:
        command, lang = listen()
        if command:
            # Language switching
            if "bengali" in command and "speak" in command:
                current_language = "bn"
                speak("ভাষা বাংলায় পরিবর্তন করা হয়েছে।", lang="bn")
                continue
            elif "hindi" in command and "speak" in command:
                current_language = "hi"
                speak("अब मैं हिंदी में बोलूंगा।", lang="hi")
                continue
            elif "english" in command and "speak" in command:
                current_language = "en"
                speak("Language changed to English.", lang="en")
                continue

            # Handle assistant command
            response, lang_used = run_assistant(command)
            speak(response, lang=current_language)

            if any(word in command for word in ["exit", "quit", "stop"]):
                break

if __name__ == "__main__":
    main()
