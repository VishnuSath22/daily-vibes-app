import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")

client = Client(account_sid, auth_token)

def send_whatsapp_message(to_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"✅ Sent to {to_number}: {message.sid}")
    except Exception as e:
        print(f"❌ Error sending to {to_number}: {e}")
