import requests
from bs4 import BeautifulSoup
import json
import time
from twilio.rest import Client

# --------------------------
# Twilio Credentials
ACCOUNT_SID = "your_account_sid_here"
AUTH_TOKEN = "your_auth_token_here"
TO_NUMBER = "whatsapp:+91xxxxxxxxxx"  # your WhatsApp number
FROM_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox sender
# --------------------------

# Movie and city
CITY = "chennai"
TARGET_MOVIE = "Coolie"

# URLs to scrape
URL_NOW_SHOWING = f"https://in.bookmyshow.com/explore/movies-{CITY}?cat=MT"
URL_UPCOMING = f"https://in.bookmyshow.com/explore/upcoming-movies-{CITY}"

def fetch_movies(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        script_tag = soup.find("script", id="__NEXT_DATA__")
        data = json.loads(script_tag.string)
        events = data["props"]["pageProps"]["events"]
        return [event["eventName"].lower() for event in events]
    except Exception as e:
        print(f"[Error fetching {url}] {e}")
        return []

def send_whatsapp_alert(movie):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=f"🎬 '{movie}' is now showing in Chennai! Book now on BookMyShow!",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
    print(f"[✅ WhatsApp Sent] SID: {message.sid}")

def main():
    print(f"🔍 Tracking movie: {TARGET_MOVIE.title()} in Chennai...")

    was_upcoming = False

    while True:
        upcoming = fetch_movies(URL_UPCOMING)
        now_showing = fetch_movies(URL_NOW_SHOWING)

        if TARGET_MOVIE.lower() in upcoming:
            print(f"[📅 Still Upcoming] '{TARGET_MOVIE.title()}' not released yet.")
            was_upcoming = True

        elif TARGET_MOVIE.lower() in now_showing:
            print(f"[🎉 Released] '{TARGET_MOVIE.title()}' is now showing!")
            if was_upcoming:
                send_whatsapp_alert(TARGET_MOVIE.title())
            break

        else:
            print(f"[❓ Not Found] '{TARGET_MOVIE.title()}' not listed yet.")

        print("⏳ Checking again in 15 minutes...\n")
        time.sleep(900)  # Wait 15 minutes before checking again

if __name__ == "__main__":
    main()
