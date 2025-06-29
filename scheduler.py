from apscheduler.schedulers.background import BackgroundScheduler
from content.motivation import get_motivation
from content.humor import get_humor
from content.news import get_news
from utils import load_users
from datetime import datetime
import time

def send_messages():
    print(f"\n=== Sending Daily Vibes @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")

    users = load_users()
    if not users:
        print("⚠️ No users found.")
        return

    for uid, prefs in users.items():
        print(f"\n📤 Sending to user {uid}...")

        # Morning Motivation
        if prefs.get("motivation"):
            motivation = get_motivation(prefs["motivation"])
            print("☀️ Motivation:", motivation)

        # Midday Humor
        if prefs.get("humor"):
            humor = get_humor(prefs["humor"])
            print("😂 Humor:", humor)

        # News Updates
        if prefs.get("news"):
            news_items = get_news(prefs["news"])
            print("📰 News Headlines:")
            for headline in news_items:
                print("   -", headline)

        # Night Quote
        if prefs.get("night_quote"):
            print("🌙 Night Message: Sleep well champ. You’ve done enough today.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_messages, "cron", hour=7, minute=0)   # Morning 7:00 AM
    scheduler.add_job(send_messages, "cron", hour=13, minute=0)  # Midday 1:00 PM
    scheduler.add_job(send_messages, "cron", hour=22, minute=0)  # Night 10:00 PM
    scheduler.start()
    print("✅ Scheduler started...")

    # Keep the script running
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("🛑 Scheduler stopped.")

if __name__ == "__main__":
    start_scheduler()
