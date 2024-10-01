from flask import Flask, render_template, request, jsonify
from model.sentiment_model import predict_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    sentiment, confidence = predict_sentiment(text)
    return jsonify({'sentiment': sentiment, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)
