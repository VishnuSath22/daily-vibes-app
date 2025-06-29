from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip().lower()
    sender = request.values.get("From", "").replace("whatsapp:", "")
    print(f"📩 Message from {sender}: {incoming_msg}", flush=True)

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "quote":
        msg.body("🌟 Here's your motivational quote: Keep pushing forward, you're doing great!")
    else:
        msg.body("Hi! Type 'quote' for motivation.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
