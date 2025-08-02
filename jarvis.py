import webbrowser
import time
import os
import re
import wikipedia
import pywhatkit
import requests
from bs4 import BeautifulSoup
import smtplib
import platform
import subprocess
from typing import Optional
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yt_dlp

# ✅ Get weather using wttr.in

def get_weather(city: str) -> str:
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Couldn't get weather info for {city}."
    except Exception as e:
        return f"Error fetching weather: {e}"

# ✅ Search the web using DuckDuckGo
def search_web(query: str) -> str:
    try:
        return f"Here are the search results: https://duckduckgo.com/?q={query.replace(' ', '+')}"
    except Exception as e:
        return f"Error performing search: {e}"

# ✅ Send email using SMTP
def send_email(to_email: str, subject: str, message: str, cc_email: Optional[str] = None) -> str:
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")

        if not gmail_user or not gmail_password:
            return "Gmail credentials not set in .env file."

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject

        recipients = [to_email]
        if cc_email:
            msg['Cc'] = cc_email
            recipients.append(cc_email)

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipients, msg.as_string())
        server.quit()

        return f"Email successfully sent to {to_email}."
    except Exception as e:
        return f"Failed to send email: {e}"

# ✅ Open Chrome browser
def open_chrome() -> str:
    try:
        if platform.system() == "Windows":
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chrome_path):
                subprocess.Popen(chrome_path)
            else:
                return "Chrome is not installed at the default path."
        else:
            webbrowser.open("https://www.google.com")
        return "Opening Google Chrome."
    except Exception as e:
        return f"Error opening Chrome: {e}"

# ✅ Open YouTube homepage
def open_youtube() -> str:
    try:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube homepage."
    except Exception as e:
        return f"Error opening YouTube: {e}"

# ✅ Play YouTube video by query
def play_youtube_video(query: str) -> str:
    try:
        if not query.strip():
            return "Please tell me the video you want to play."

        search_url = f"ytsearch1:{query}"
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(search_url, download=False)
            if 'entries' in info and len(info['entries']) > 0:
                video_url = info['entries'][0]['webpage_url']
                webbrowser.open(video_url)
                return f"Now playing {query} on YouTube."
            else:
                return "No video results found."
    except Exception as e:
        return f"Error playing video: {e}"

# ✅ Send WhatsApp message
def send_whatsapp_message(phone_number: str, message: str) -> str:
    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
        return f"Message sent to {phone_number}."
    except Exception as e:
        return f"Failed to send WhatsApp message: {e}"

# ✅ Detect language switch intent and return target code
def detect_language_switch(command: str) -> Optional[str]:
    command = command.lower()
    if "bengali" in command or "বাংলা" in command:
        return "bn"
    elif "hindi" in command or "हिंदी" in command:
        return "hi"
    elif "english" in command or "ইংরেজি" in command or "अंग्रेजी" in command:
        return "en"
    return None
