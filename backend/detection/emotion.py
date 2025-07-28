 # detection/emotion.py
from transformers import pipeline

# Load Hugging Face pipeline for emotion detection
emotion_classifier = pipeline("text-classification", 
                              model="bhadresh-savani/distilbert-base-uncased-emotion", 
                              return_all_scores=False)

def analyze_emotion(text: str) -> str:
    try:
        result = emotion_classifier(text)
        if result and len(result) > 0:
            label = result[0]['label'].lower()
            print(f"[Emotion] {label} (confidence: {result[0]['score']:.2f})")
            return label
        return "neutral"
    except Exception as e:
        print("[!] Emotion analysis failed:", e)
        return "error"

