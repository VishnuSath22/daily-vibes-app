from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import os

app = Flask(__name__)

user_data_file = "user_data.json"
user_states = {}

# Load or initialize user data
if not os.path.exists(user_data_file):
    with open(user_data_file, 'w') as f:
        json.dump({}, f)

with open(user_data_file, 'r') as f:
    user_data = json.load(f)


@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get("Body", "").strip().lower()
    user_number = request.values.get("From", "")
    response = MessagingResponse()
    msg = response.message()

    # Command: start
    if incoming_msg == "start":
        user_states[user_number] = {"step": "awaiting_category"}
        msg.body(
            "Welcome to Daily Vibes 🌞\n\n"
            "What kind of messages do you want?\n"
            "1. Motivation\n"
            "2. Jokes\n"
            "3. Breaking News\n"
            "4. Sleep Quotes\n\n"
            "Reply like: 1,2,4"
        )
        return str(response)

    # Command: change preferences
    if incoming_msg == "change":
        user_states[user_number] = {"step": "awaiting_category"}
        msg.body(
            "Let's update your preferences! ✏️\n\n"
            "What kind of messages do you want?\n"
            "1. Motivation\n"
            "2. Jokes\n"
            "3. Breaking News\n"
            "4. Sleep Quotes\n\n"
            "Reply like: 1,2,4"
        )
        return str(response)

    # Step 2: Process category selection
    if user_number in user_states and user_states[user_number]["step"] == "awaiting_category":
        selected = incoming_msg.replace(" ", "").split(",")
        categories = {
            "1": "motivation",
            "2": "jokes",
            "3": "news",
            "4": "sleep"
        }
        selected_categories = [categories[i] for i in selected if i in categories]
        if not selected_categories:
            msg.body("Please reply with valid numbers like 1,2,4")
            return str(response)

        user_states[user_number]["preferences"] = selected_categories
        user_states[user_number]["step"] = "awaiting_time"
        msg.body(
            "Awesome! When do you want to receive them?\n\n"
            "A. Morning 🌅\nB. Afternoon 😄\nC. Night 🌙\n\nReply like: A,C"
        )
        return str(response)

    # Step 3: Process time selection
    if user_number in user_states and user_states[user_number]["step"] == "awaiting_time":
        selected = incoming_msg.replace(" ", "").split(",")
        times_map = {"a": "morning", "b": "afternoon", "c": "night"}
        selected_times = [times_map[t] for t in selected if t in times_map]
        if not selected_times:
            msg.body("Please reply with A, B, or C (like: A,C)")
            return str(response)

        # Save preferences
        user_data[user_number] = {
            "preferences": user_states[user_number]["preferences"],
            "times": selected_times
        }
        with open(user_data_file, 'w') as f:
            json.dump(user_data, f, indent=2)

        user_states.pop(user_number)
        msg.body("✅ Preferences saved! You'll now receive personalized Daily Vibes 😊")
        return str(response)

    # Fallback response
    msg.body("Hi! Send *start* to set up your preferences or *change* to update them anytime.")
    return str(response)


if __name__ == "__main__":
    app.run(port=5000)
