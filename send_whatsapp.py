from twilio.rest import Client
import os

# Replace with your real Twilio credentials
account_sid = "your_account_sid"
auth_token = "your_auth_token"
from_number = "whatsapp:+14155238886"  # Twilio sandbox number

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
