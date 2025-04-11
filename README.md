# 🚨 SOS Emergency Detection App

A full-stack real-time distress detection system using voice inputs and AI, built with **FastAPI (Python)** for the backend and **React Native (Expo)** for the mobile frontend. On SOS detection, the system automatically sends **calls and SMS with location** to emergency contacts using Twilio and other APIs.

---

## 📁 Project Structure

```
SPDEMERGENCY/
├── backend/
│   ├── detection/         # Real-time audio listener and SOS trigger logic
│   ├── model/             # ML models for distress detection (if any)
│   ├── tests/             # Test scripts
│   ├── main.py            # FastAPI backend entrypoint
│   ├── config.py          # Twilio / location configuration
│   ├── requirements.txt   # Python dependencies
│   └── ...
├── frontend/
│   ├── app/               # React Native app screens
│   ├── assets/            # Images & fonts
│   ├── App.js / index.tsx # App entry
│   ├── package.json       # JS dependencies
│   └── ...
```

---

## ⚙️ Setup Instructions

### 📌 Backend (FastAPI + Python)

#### 1. 🔧 Install dependencies

```bash
cd backend/
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### 2. 🏃‍♂️ Run the backend

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

> Make sure to update your IP in the frontend (`BASE_URL` in `Home.js` or `index.tsx`).

---

### 📱 Frontend (React Native + Expo)

#### 1. 📦 Install JS dependencies

```bash
cd frontend/
npm install
```

#### 2. 🚀 Run the app

```bash
npx expo start
```

> Scan the QR code using the **Expo Go** app on your phone.

---

## 📲 Features

- 🎙 Real-time voice-based SOS detection
- 📡 Automatic call and SMS on emergency
- 📍 Auto-fetches and sends current GPS location
- 🔊 Soundwave animation (optional)
- 📳 Haptic feedback on toggles
- 📇 Add/edit emergency contacts (via local storage or backend)
- 🌐 Cross-platform support (iOS & Android)

---

## 🔐 Tech Stack

| Layer     | Tech Used                           |
|-----------|-------------------------------------|
| Frontend  | React Native (Expo), AsyncStorage   |
| Backend   | FastAPI (Python), Uvicorn, Pyaudio  |
| APIs      | Twilio API, Geolocation API         |
| Extra     | Expo Haptics, Expo Location         |

---

## 🚀 Future Improvements

- 🧠 Better AI model for emotion/scream detection
- 🔒 Secure backend endpoints
- ☁️ Backend deployment on cloud (Render, Railway, etc.)
- 📦 Add Firestore or SQLite for persistent emergency contacts

---

## 👨‍💻 Developed By

> Built with 💙 as part of a smart emergency system project.