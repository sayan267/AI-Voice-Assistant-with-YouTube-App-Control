import webbrowser
import requests
import smtplib
import platform
import subprocess
import os
from typing import Optional
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

# ✅ Weather using wttr.in (no API key needed)
def get_weather(city: str) -> str:
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Couldn't get weather info for {city}."
    except Exception as e:
        return f"Error fetching weather: {e}"

# ✅ Web search using DuckDuckGo
def search_web(query: str) -> str:
    try:
        return f"You can check this link: https://duckduckgo.com/?q={query.replace(' ', '+')}"
    except Exception as e:
        return f"Error performing search: {e}"

# ✅ Send email using Gmail SMTP
def send_email(to_email: str, subject: str, message: str, cc_email: Optional[str] = None) -> str:
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")

        if not gmail_user or not gmail_password:
            return "Gmail credentials not set in .env."

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

# ✅ Open Chrome based on platform
def open_chrome() -> str:
    try:
        if platform.system() == "Windows":
            subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
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

# ✅ Play first YouTube video from search result
def play_youtube_video(query: str) -> str:
    try:
        search_query = query.replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={search_query}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return "Failed to search YouTube."

        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and "/watch?v=" in href:
                video_url = f"https://www.youtube.com{href}"
                webbrowser.open(video_url)
                return f"Now playing {query} on YouTube."

        return "Could not find a video to play."
    except Exception as e:
        return f"Error playing YouTube video: {e}"
