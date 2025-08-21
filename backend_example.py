# Example Flask Backend API for the Streamlit Dashboard
# This is a reference implementation - you'll need to implement actual ML models

from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    """
    Sentiment analysis endpoint
    Expected input: {"keyword": "your_keyword"}
    """
    try:
        data = request.get_json()
        keyword = data.get('keyword', '')
        
        # Simulate processing time
        time.sleep(1)
        
        # Mock sentiment analysis results
        # In a real implementation, you would:
        # 1. Fetch tweets/social media posts for the keyword
        # 2. Run them through a sentiment analysis model
        # 3. Aggregate the results
        
        total = random.randint(100, 500)
        positive = random.randint(20, total//2)
        negative = random.randint(10, total//3)
        neutral = total - positive - negative
        
        sample_tweets = [
            {"text": f"Great news about {keyword}! Very positive development.", "sentiment": "positive"},
            {"text": f"Not sure about this {keyword} situation. Seems concerning.", "sentiment": "negative"},
            {"text": f"Just heard about {keyword}. Need more information.", "sentiment": "neutral"},
            {"text": f"Amazing progress with {keyword}! Love to see it.", "sentiment": "positive"},
            {"text": f"The {keyword} issue is getting worse every day.", "sentiment": "negative"}
        ]
        
        response = {
            "total_tweets": total,
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "positive_pct": round((positive / total) * 100, 1),
            "negative_pct": round((negative / total) * 100, 1),
            "neutral_pct": round((neutral / total) * 100, 1),
            "sample_tweets": sample_tweets
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/fakenews', methods=['POST'])
def check_fake_news():
    """
    Fake news detection endpoint
    Expected input: {"text": "news text to analyze"}
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        # Simulate processing time
        time.sleep(1)
        
        # Mock fake news detection
        # In a real implementation, you would:
        # 1. Preprocess the text
        # 2. Run it through a trained fake news detection model
        # 3. Return prediction and confidence score
        
        # Simple mock logic based on certain keywords
        fake_indicators = ['shocking', 'unbelievable', 'doctors hate this', 'secret', 'conspiracy']
        real_indicators = ['according to', 'study shows', 'research indicates', 'official', 'confirmed']
        
        fake_score = sum(1 for indicator in fake_indicators if indicator.lower() in text.lower())
        real_score = sum(1 for indicator in real_indicators if indicator.lower() in text.lower())
        
        if fake_score > real_score:
            prediction = "fake"
            confidence = random.uniform(0.6, 0.9)
        else:
            prediction = "real" 
            confidence = random.uniform(0.6, 0.9)
        
        response = {
            "prediction": prediction,
            "confidence": confidence,
            "analysis": {
                "credibility": random.uniform(0.3, 0.9),
                "language_quality": random.uniform(0.4, 0.9),
                "source_reliability": random.uniform(0.3, 0.8)
            }
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "fake-news-sentiment-api"})

if __name__ == '__main__':
    print("Starting Flask API server...")
    print("Endpoints available:")
    print("- POST /sentiment - Sentiment analysis")
    print("- POST /fakenews - Fake news detection") 
    print("- GET /health - Health check")
    app.run(debug=True, host='127.0.0.1', port=5000)