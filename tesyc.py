from twilio.rest import Client

account_sid = "ACd8d88dae26ca39cb9ce717cbe067dd7c"
auth_token = "dc0800e99c8fcc8a0cca87ab49ad6ea0"
client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Testing Twilio SMS from debug file",
        from_="+19478885806",  # Your Twilio number
        to="+918691897799"     # Your verified number
    )
    print("[✅] Message sent successfully:", message.sid)
except Exception as e:
    print("[❌] Twilio Error:", e)


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import TWILIO_SID, TWILIO_AUTH, TWILIO_PHONE, EMERGENCY_CONTACT
