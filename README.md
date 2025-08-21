# 📰 Social Media Fake News & Sentiment Analyzer

A comprehensive Streamlit dashboard for analyzing social media content sentiment and detecting fake news using AI-powered APIs.

## Features

### 🎭 Sentiment Analysis
- Analyze sentiment from keywords or uploaded CSV files
- Interactive visualizations with Plotly charts
- Sample tweet analysis with sentiment tags
- Real-time API integration

### 🔍 Fake News Detection
- Text-based fake news detection
- Confidence scoring with gauge visualization
- Detailed analysis metrics
- Real/Fake classification with visual indicators

### ☁️ Word Cloud Generation
- Generate word clouds from uploaded text data
- Customizable color schemes and word limits
- Frequency analysis and top words visualization
- Support for various text column formats

## Installation

1. **Clone or download the project files**

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**
```bash
streamlit run app.py
```

## Backend API Requirements

The app expects a Flask backend API running on `http://127.0.0.1:5000` with the following endpoints:

### Sentiment Analysis Endpoint
```
POST /sentiment
Content-Type: application/json

{
  "keyword": "your_keyword_here"
}
```

Expected response:
```json
{
  "total_tweets": 150,
  "positive": 65,
  "negative": 35,
  "neutral": 50,
  "positive_pct": 43.3,
  "negative_pct": 23.3,
  "neutral_pct": 33.3,
  "sample_tweets": [
    {
      "text": "Sample tweet text",
      "sentiment": "positive"
    }
  ]
}
```

### Fake News Detection Endpoint
```
POST /fakenews
Content-Type: application/json

{
  "text": "News headline or article text"
}
```

Expected response:
```json
{
  "prediction": "real",
  "confidence": 0.85,
  "analysis": {
    "credibility": 0.8,
    "language_quality": 0.9,
    "source_reliability": 0.7
  }
}
```

## CSV File Format

For sentiment analysis and word cloud generation, upload CSV files with the following format:

```csv
tweet
"This is a sample tweet for analysis"
"Another tweet with different sentiment"
"More text content for processing"
```

Supported column names: `tweet`, `text`, `content`, `message`

## Usage

1. **Start the application:** `streamlit run app.py`
2. **Navigate through tabs:**
   - **Sentiment Analysis:** Enter keywords or upload CSV files
   - **Fake News Checker:** Paste news text for verification
   - **Word Cloud:** Upload text data for visualization

3. **Use the sidebar** for project information and quick help

## Demo Mode

If the backend API is unavailable, the app will show demo data to demonstrate functionality.

## Technologies Used

- **Streamlit** - Web app framework
- **Plotly** - Interactive visualizations
- **WordCloud** - Text visualization
- **Matplotlib** - Static plots
- **Pandas** - Data manipulation
- **Requests** - API communication

## Customization

The app includes:
- Custom CSS styling for modern appearance
- Responsive layout with columns and tabs
- Interactive charts and visualizations
- Progress indicators and loading states
- Error handling and fallback displays

## Contributing

1. Fork the repository
2. Create feature branches
3. Submit pull requests with detailed descriptions

## License

Open source project - feel free to modify and distribute.