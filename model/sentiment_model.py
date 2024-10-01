from transformers import pipeline

# Load pre-trained BERT model from Hugging Face
classifier = pipeline('sentiment-analysis')

def predict_sentiment(text):
    result = classifier(text)[0]
    sentiment = result['label']
    confidence = result['score']
    return sentiment, round(confidence, 2)
