from transformers import pipeline
classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
print(classifier("I'm scared and don't know what to do"))
