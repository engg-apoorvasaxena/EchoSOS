from twilio.rest import Client

account_sid = "your credentials"
auth_token = "your credentials"
client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Testing Twilio SMS from debug file",
        from_="",  # Your Twilio number
        to=""     # Your verified number
    )
    print("[✅] Message sent successfully:", message.sid)
except Exception as e:
    print("[❌] Twilio Error:", e)


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import TWILIO_SID, TWILIO_AUTH, TWILIO_PHONE, EMERGENCY_CONTACT
