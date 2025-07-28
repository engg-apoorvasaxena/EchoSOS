# detection/classifier.py

from transformers import pipeline

# Load sentiment/emotion model from HuggingFace
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def classify_text(text):
    result = classifier(text)[0]
    emotion = result['label']
    score = result['score']
    return f"{emotion} ({score:.2f})"
