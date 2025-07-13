from flask import Flask, request
import json
import os

app = Flask(__name__)

# Load or initialize user data
USER_DATA_FILE = "user_data.json"
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)

# Routes
@app.route("/", methods=["GET"])
def home():
    return "Daily Vibes WhatsApp Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    phone_number = data.get("phone_number")
    message = data.get("message", "").lower().strip()

    with open(USER_DATA_FILE) as f:
        user_data = json.load(f)

    if message == "start":
        user_data[phone_number] = {"preference": "motivational"}
        response = "✅ You're subscribed! Reply 'funny' or 'news' to change preference."
    elif message in ["motivational", "funny", "news"]:
        if phone_number in user_data:
            user_data[phone_number]["preference"] = message
            response = f"✅ Preference updated to {message}."
        else:
            response = "⚠️ Send 'start' first to subscribe."
    elif message == "stop":
        if phone_number in user_data:
            del user_data[phone_number]
            response = "🛑 You've been unsubscribed. Send 'start' to join again."
        else:
            response = "You're not subscribed."
    else:
        response = "🤖 Send 'start' to subscribe. Reply with 'motivational', 'funny' or 'news' to choose preference."

    with open(USER_DATA_FILE, "w") as f:
        json.dump(user_data, f, indent=2)

    return {"response": response}, 200

# Run with correct host and port for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
