# 🚨 SOS Emergency Detection App

A **real-time full-stack emergency distress detection system** using **voice input and AI**, built with **FastAPI** for the backend and **React Native (Expo)** for the mobile frontend. On detecting an SOS phrase or distress keyword, the system automatically sends **SMS and calls with GPS location** to configured emergency contacts using Twilio and other APIs.

---

## 📁 Project Structure

```

distress_sos_system/
├── backend/
│   ├── detection/         # Real-time audio listener and SOS trigger logic
│   ├── model/             # ML models for distress detection (if any)
│   ├── tests/             # Test scripts
│   ├── main.py            # FastAPI backend entrypoint
│   ├── config.py          # Twilio / location configuration
│   ├── .env               # 🔐 Credentials file (not tracked)
│   ├── requirements.txt   # Python dependencies
│   └── ...
├── frontend/
│   ├── app/               # React Native app screens
│   ├── assets/            # Images & fonts
│   ├── App.js / index.tsx # App entry
│   ├── package.json       # JS dependencies
│   └── ...

````

---

## ⚙️ Setup Instructions

### 📌 Backend (FastAPI + Python)

1. **Install dependencies**

```bash
cd backend/
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux

pip install -r requirements.txt
````

2. **Add your credentials**

Update the `.env` file inside the `backend/` folder with the following:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+xxxxxxx
```
Make sure your Twilio phone numbers are eligible for the type of calling you're opting for. For example- a purchased phone number that only has local calling capabilities will not be able to make international calls.
Also Important in `main.py`, make sure to replace any hardcoded numbers or API placeholders with your actual credentials same as env file.

3. **Run the backend server**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### 📱 Frontend (React Native + Expo)

1. **Install JavaScript dependencies**

```bash
cd frontend/
npm install
```

2. **To connect your frontend Operations with Backend**<br>
       a. **Inside Frontend Folder find index.tsx named file inside app folder**.<br>
       b. **Refer below**.<br>
   <img width="220" height="92" alt="image" src="https://github.com/user-attachments/assets/e9a4c6a1-db94-4150-9786-634c29051de7" />

**CHANGE THIS TO YOUR IP ADDRESS**
 ```bash
   const BASE_URL = "http://<YOUR-IP>:8000";
 ```
**After Changing the your url look like this**
```bash
 const BASE_URL = "http://192.xxx.x.xxx:8000";
```

**YOU CAN FIND YOUR LOCAL SYSTEM IP ADDRESS IN CMD**<br>
Simply type this command in CMD
```bash
ipconfig
```

**Find IPv4 ADDRESS**
```bash
IPv4 Address. . . . . . . . . . . : 192.xxx.x.xxx
```

4. **Run the app**

```bash
npx expo start
```

> Then scan the QR code with the **Expo Go** app on your phone.

---

## 📲 Features

* 🎙 Real-time **voice-based SOS detection**
* 📡 **Automatic call and SMS** on emergency trigger
* 📍 Sends **live GPS location**
* 🔊 Optional **soundwave animation**
* 📳 Haptic feedback when toggling detection
* 📇 Add/edit emergency contacts (via local or cloud)
* 🌐 Cross-platform support (iOS & Android)

---

## 🔐 Tech Stack

| Layer    | Tech Used                             |
| -------- | ------------------------------------- |
| Frontend | React Native (Expo), AsyncStorage     |
| Backend  | FastAPI (Python), Uvicorn, PyAudio    |
| APIs     | Twilio API, Expo Location API         |
| Extras   | Expo Haptics, React Native Animations |

---

## 🚀 Future Improvements

* 🧠 Enhanced AI model for scream/emotion detection
* 🔐 Add user authentication and secure endpoints
* ☁️ Deploy backend to cloud (Render, Railway, etc.)
* 📦 Add persistent contact storage (Firestore/SQLite)

---

## 📁 .env Example

Here is a sample `.env` file to guide users:

```env
# .env
TWILIO_ACCOUNT_SID=your_twilio_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE_NUMBER=+11234567890
```

> Copy this file and rename it to `.env` before running the backend.

---

## 👨‍💻 Developed By

Built with 💙 as part of a **Smart Emergency Response System** for real-time safety and automated alerting.

