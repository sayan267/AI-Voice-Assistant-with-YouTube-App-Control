import wikipedia
from jarvis import play_youtube_video, open_chrome, open_youtube, send_whatsapp_message, detect_language_switch

# WhatsApp contact dictionary
whatsapp_contacts = {
    "pulak": "+9170001580172",
    "hritrab": "+917003286013",
    "priyo": "+917908452001",
    "sayak": "+917586935621",
    "koushik": "+916297917413",
    "shuvronil": "+918597011566",
    "arun": "+919679198587",
    "ma": "+918001404933",
    "baba": "+919874482162",
    "sanket": "+917363842308",
    "soumya": "+918345093331"
}

def run_assistant(command: str):
    command = command.lower()

    if "your name" in command or "tumhara naam" in command or "তোমার নাম" in command:
        return "I am Sai, your assistant.", "en"

    elif "how are you" in command or "kaisa hai" in command or "কেমন আছো" in command:
        return "I'm always ready to help you!", "en"

    elif "time" in command:
        from time import strftime
        return strftime("The time is %I:%M %p"), "en"

    elif "date" in command:
        from time import strftime
        return strftime("Today is %A, %d %B %Y"), "en"

    elif "open youtube" in command:
        return open_youtube(), "en"

    elif "open chrome" in command:
        return open_chrome(), "en"

    elif "play" in command and "youtube" in command:
        video_query = command.replace("play", "").replace("on youtube", "").strip()
        return play_youtube_video(video_query), "en"

    elif "tell me about" in command or "who is" in command:
        topic = command.replace("tell me about", "").replace("who is", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return summary, "en"
        except:
            return "Sorry, I couldn't find information on that.", "en"

    elif "send message" in command or "send a message" in command or "whatsapp" in command:
        return "whatsapp_flow", "en"  # signal for WhatsApp mode

    elif "exit" in command or "quit" in command or "stop" in command:
        return "Goodbye!", "en"

    # Language switching intent
    lang_code = detect_language_switch(command)
    if lang_code:
        lang_names = {"bn": "বাংলা", "hi": "हिंदी", "en": "English"}
        message = {
            "bn": "ভাষা বাংলায় পরিবর্তন করা হয়েছে।",
            "hi": "अब मैं हिंदी में बोलूंगा।",
            "en": "Language changed to English."
        }
        return message[lang_code], lang_code

    return "Sorry, I don't understand that command yet.", "en"
