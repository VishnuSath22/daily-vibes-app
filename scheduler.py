import json
import datetime
from send_whatsapp import send_whatsapp_message  # your existing send function
import random

# Load user preferences
with open("user_data.json", "r") as f:
    user_data = json.load(f)

# Load content
with open("content/motivation.txt") as f:
    motivation_quotes = f.readlines()

with open("content/jokes.txt") as f:
    jokes = f.readlines()

with open("content/news.txt") as f:
    news_items = f.readlines()

with open("content/sleep.txt") as f:
    sleep_quotes = f.readlines()

# Get current time slot
now = datetime.datetime.now()
hour = now.hour

if 5 <= hour < 11:
    time_slot = "morning"
elif 11 <= hour < 17:
    time_slot = "afternoon"
else:
    time_slot = "night"

# Send messages based on preferences
for user, prefs in user_data.items():
    if time_slot in prefs.get("times", []):
        for category in prefs.get("preferences", []):
            if category == "motivation":
                quote = random.choice(motivation_quotes)
            elif category == "jokes":
                quote = random.choice(jokes)
            elif category == "news":
                quote = random.choice(news_items)
            elif category == "sleep":
                quote = random.choice(sleep_quotes)
            else:
                continue

            send_whatsapp_message(user, quote.strip())
