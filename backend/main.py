# main.py
from fastapi import FastAPI
from detection.listener import start_listening, stop_listening
from fastapi.middleware.cors import CORSMiddleware
from twilio.rest import Client
import requests

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TWILIO_SID = 'ACd8d88dae26ca39cb9ce717cbe067dd7c'
TWILIO_AUTH = 'be3699ccbc58473d8a496dd5bde638b3'
TWILIO_PHONE = '+19478885806'  # Your Twilio number
TO_PHONE = '+918691897799'    # Emergency contact


def get_location_link():
    try:
        res = requests.get("https://ipapi.co/json/").json()
        lat, lon = res.get('latitude'), res.get('longitude')
        return f"https://maps.google.com/?q={lat},{lon}"
    except:
        return "Location unavailable"


def send_sos_alert():
    location_link = get_location_link()
    message = f"🚨 SOS Alert!\nLocation: {location_link}"

    client = Client(TWILIO_SID, TWILIO_AUTH)

    # Send SMS
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=TO_PHONE
    )

    # Place Call
    client.calls.create(
        twiml='<Response><Say>SOS Alert. Please check immediately.</Say></Response>',
        from_=TWILIO_PHONE,
        to=TO_PHONE
    )


@app.get("/")
def read_root():
    return {"message": "Distress Detection API is live 🔥"}


@app.post("/start_detection")
def start():
    start_listening()
    return {"status": "Listening started"}


@app.post("/stop_detection")
def stop():
    stop_listening()
    return {"status": "Listening stopped"}


@app.get("/status")
def status():
    return {"status": "Idle"}


@app.post("/trigger_sos")
def trigger_sos():
    send_sos_alert()
    return {"status": "SOS sent with location"}
