import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="📰 Social Media Fake News & Sentiment Analyzer",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    .fake-news-real {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .fake-news-fake {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .landing-hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .start-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 25px;
        border: none;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        text-align: center;
        display: block;
        margin: 2rem auto;
        min-width: 200px;
    }
    .quick-start-step {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #2196f3;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Navigation
def show_landing_page():
    """Display the landing/welcome page with project information"""
    
    # Hero Section
    st.markdown("""
    <div class="landing-hero">
        <h1 style="font-size: 3rem; margin-bottom: 1rem;">📰 Social Media Fake News & Sentiment Analyzer</h1>
        <p style="font-size: 1.3rem; margin-bottom: 0;">Advanced AI-powered analysis for social media content and news verification</p>
    </div>
    """, unsafe_allow_html=True)
    
    # About Section
    st.markdown("## 🎯 About This Application")
    st.markdown("""
    **Social Media Fake News & Sentiment Analyzer** is a comprehensive dashboard that leverages artificial intelligence 
    to analyze social media content and detect potentially misleading information. This tool is designed for researchers, 
    journalists, social media managers, and anyone interested in understanding the sentiment and credibility of online content.
    """)
    
    # How It Works Section
    st.markdown("## ⚙️ How It Works")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎭 Sentiment Analysis</h4>
            <p>Uses natural language processing to analyze emotions and opinions in social media posts, categorizing them as positive, negative, or neutral.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 Fake News Detection</h4>
            <p>Employs machine learning algorithms to identify potentially misleading or false information with confidence scoring.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>☁️ Text Visualization</h4>
            <p>Generates interactive word clouds and frequency analysis to visualize the most common terms in your data.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("## 🚀 Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Analytics & Visualization
        - **Interactive Charts**: Plotly-powered pie charts, bar graphs, and gauges
        - **Real-time Metrics**: Live sentiment distribution and confidence scores
        - **Word Frequency Analysis**: Top words and trending terms visualization
        - **Sample Data Display**: View analyzed tweets with sentiment tags
        
        ### 🔧 Data Input Options
        - **Keyword Analysis**: Enter topics for real-time social media analysis
        - **CSV Upload**: Bulk analyze your own tweet datasets
        - **Text Input**: Direct paste for news article verification
        - **Multiple Formats**: Support for various text column formats
        """)
    
    with col2:
        st.markdown("""
        ### 🛡️ AI-Powered Detection
        - **Sentiment Classification**: Positive, negative, neutral categorization
        - **Fake News Scoring**: Confidence-based credibility assessment
        - **Language Quality Analysis**: Text coherence and reliability metrics
        - **Source Reliability**: Credibility scoring for news sources
        
        ### 🎨 User Experience
        - **Modern Interface**: Clean, responsive design
        - **Error Handling**: Graceful fallbacks and demo data
        - **Progress Indicators**: Real-time processing feedback
        - **Mobile Friendly**: Works across all device sizes
        """)
    
    # Quick Start Guide
    st.markdown("## 🚀 Quick Start Guide")
    
    st.markdown("""
    <div class="quick-start-step">
        <strong>Step 1: Sentiment Analysis</strong><br>
        Enter a keyword (e.g., "elections", "climate change", "AI") or upload a CSV file with tweet data, then click "Analyze Sentiment" to see emotional distribution and sample tweets.
    </div>
    
    <div class="quick-start-step">
        <strong>Step 2: Fake News Detection</strong><br>
        Paste any news headline or article text into the checker, click "Check Fake News" to get a credibility assessment with confidence scoring.
    </div>
    
    <div class="quick-start-step">
        <strong>Step 3: Word Cloud Generation</strong><br>
        Upload a CSV file with text data to automatically generate beautiful word clouds and frequency analysis of the most common terms.
    </div>
    """, unsafe_allow_html=True)
    
    # How to Use Section
    st.markdown("## 📖 How to Use")
    
    with st.expander("📁 Data Format Requirements", expanded=False):
        st.markdown("""
        **For CSV uploads, ensure your file contains:**
        - A column named `tweet`, `text`, `content`, or `message`
        - One text entry per row
        - UTF-8 encoding for special characters
        
        **Example CSV format:**
        ```
        tweet
        "This is a sample tweet for analysis"
        "Another tweet with different sentiment"
        "More text content for processing"
        ```
        """)
    
    with st.expander("🔧 API Configuration", expanded=False):
        st.markdown("""
        **Backend Requirements:**
        - Flask API running on `http://127.0.0.1:5000`
        - Endpoints: `/sentiment` and `/fakenews`
        - If API is unavailable, demo data will be displayed
        
        **API Response Format:**
        - Sentiment: JSON with counts and percentages
        - Fake News: Prediction with confidence score
        """)
    
    with st.expander("💡 Tips for Best Results", expanded=False):
        st.markdown("""
        **Sentiment Analysis:**
        - Use specific, trending keywords for better results
        - Ensure CSV files have sufficient data (50+ entries recommended)
        - Check for proper text encoding in uploaded files
        
        **Fake News Detection:**
        - Paste complete headlines or article excerpts
        - Longer text generally provides more accurate results
        - Consider context and source when interpreting results
        """)
    
    # Team & Technology Section
    st.markdown("## 👥 Development Team & Technology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 👨‍💻 Development Team
        - **Data Science Team**: ML model development and training
        - **Backend Engineers**: API development and integration
        - **Frontend Developers**: Streamlit dashboard and UX design
        - **QA Engineers**: Testing and quality assurance
        """)
    
    with col2:
        st.markdown("""
        ### 🛠️ Technology Stack
        - **Frontend**: Streamlit, Plotly, Matplotlib
        - **Backend**: Flask, Python ML APIs
        - **Data Processing**: Pandas, NumPy, WordCloud
        - **Visualization**: Interactive charts and graphs
        """)
    
    # Call to Action
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h3>Ready to start analyzing?</h3>
            <p>Click the button below to access the full dashboard and begin your social media content analysis.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Start Application", key="start_app", help="Launch the main dashboard"):
            st.session_state.page = 'dashboard'
            st.rerun()

def show_dashboard():
    """Display the main dashboard with all analysis tools"""
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📊 Navigation")
        
        if st.button("🏠 Back to Home", key="back_home"):
            st.session_state.page = 'landing'
            st.rerun()
        
        st.markdown("---")
        
        with st.expander("📖 Quick Help"):
            st.markdown("""
            **Sentiment Analysis:**
            - Enter keyword or upload CSV
            - Click 'Analyze Sentiment'
            
            **Fake News Check:**
            - Paste news text
            - Click 'Check Fake News'
            
            **Word Cloud:**
            - Upload CSV with text data
            - Customize appearance
            """)
        
        with st.expander("ℹ️ About"):
            st.markdown("""
            AI-powered tool for analyzing social media sentiment and detecting fake news.
            
            Built with Streamlit, Plotly, and ML APIs.
            """)
    
    # Main header
    st.markdown('<div class="main-header">📰 Social Media Fake News & Sentiment Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Advanced AI-powered analysis for social media content and news verification</div>', unsafe_allow_html=True)
    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["🎭 Sentiment Analysis", "🔍 Fake News Checker", "☁️ Word Cloud Generator"])

    with tab1:
        st.subheader("🎭 Sentiment Analysis Dashboard")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Input Options")
            
            # Input method selection
            input_method = st.radio(
                "Choose input method:",
                ["Keyword Analysis", "CSV Upload"],
                horizontal=True
            )
            
            if input_method == "Keyword Analysis":
                keyword = st.text_input(
                    "Enter keyword to analyze:",
                    placeholder="e.g., elections, climate change, AI",
                    help="Enter a topic to analyze recent social media sentiment"
                )
            else:
                uploaded_file = st.file_uploader(
                    "Upload CSV file with tweets",
                    type=['csv'],
                    help="CSV should contain a 'tweet' column"
                )
                keyword = None
                if uploaded_file:
                    try:
                        df = pd.read_csv(uploaded_file)
                        st.success(f"✅ Loaded {len(df)} tweets from CSV")
                        if 'tweet' not in df.columns:
                            st.error("❌ CSV must contain a 'tweet' column")
                        else:
                            st.write("Preview of uploaded data:")
                            st.dataframe(df.head(3))
                    except Exception as e:
                        st.error(f"❌ Error loading CSV: {str(e)}")
        
        with col2:
            st.markdown("### Analysis Controls")
            analyze_btn = st.button(
                "🚀 Analyze Sentiment",
                type="primary",
                help="Start sentiment analysis"
            )
        
        # Sentiment Analysis Results
        if analyze_btn:
            if input_method == "Keyword Analysis" and keyword:
                with st.spinner("🔄 Analyzing sentiment data..."):
                    try:
                        # API call to backend
                        response = requests.post(
                            "http://127.0.0.1:5000/sentiment",
                            json={"keyword": keyword},
                            timeout=30
                        )
                        
                        if response.status_code == 200:
                            data = response.json()
                            
                            # Display results
                            st.success("✅ Analysis completed successfully!")
                            
                            # Metrics row
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.metric("Total Analyzed", data.get('total_tweets', 0))
                            with col2:
                                st.metric("Positive", data.get('positive', 0), f"{data.get('positive_pct', 0):.1f}%")
                            with col3:
                                st.metric("Negative", data.get('negative', 0), f"{data.get('negative_pct', 0):.1f}%")
                            with col4:
                                st.metric("Neutral", data.get('neutral', 0), f"{data.get('neutral_pct', 0):.1f}%")
                            
                            # Charts
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                # Pie chart
                                labels = ['Positive', 'Negative', 'Neutral']
                                values = [data.get('positive', 0), data.get('negative', 0), data.get('neutral', 0)]
                                colors = ['#2ecc71', '#e74c3c', '#95a5a6']
                                
                                fig_pie = go.Figure(data=[go.Pie(
                                    labels=labels, 
                                    values=values,
                                    marker_colors=colors,
                                    hole=0.4
                                )])
                                fig_pie.update_layout(title="Sentiment Distribution")
                                st.plotly_chart(fig_pie, use_container_width=True)
                            
                            with col2:
                                # Bar chart
                                fig_bar = px.bar(
                                    x=labels,
                                    y=values,
                                    color=labels,
                                    color_discrete_map={
                                        'Positive': '#2ecc71',
                                        'Negative': '#e74c3c',
                                        'Neutral': '#95a5a6'
                                    },
                                    title="Sentiment Comparison"
                                )
                                fig_bar.update_layout(showlegend=False)
                                st.plotly_chart(fig_bar, use_container_width=True)
                            
                            # Sample tweets
                            if 'sample_tweets' in data:
                                st.markdown("### 📝 Sample Tweets Analysis")
                                for i, tweet in enumerate(data['sample_tweets'][:5]):
                                    sentiment = tweet['sentiment']
                                    emoji = "😊" if sentiment == 'positive' else "😢" if sentiment == 'negative' else "😐"
                                    color = "#d4edda" if sentiment == 'positive' else "#f8d7da" if sentiment == 'negative' else "#e2e3e5"
                                    
                                    st.markdown(f"""
                                    <div style="background-color: {color}; padding: 10px; margin: 5px 0; border-radius: 8px;">
                                        <strong>{emoji} {sentiment.capitalize()}</strong><br>
                                        {tweet['text']}
                                    </div>
                                    """, unsafe_allow_html=True)
                        
                        else:
                            st.error(f"❌ API Error: {response.status_code}")
                    
                    except requests.exceptions.RequestException as e:
                        st.error(f"❌ Connection Error: {str(e)}")
                        # Show mock data for demo purposes
                        st.info("📊 Showing demo data (API unavailable)")
                        
                        # Mock data
                        mock_data = {
                            'total_tweets': 150,
                            'positive': 65,
                            'negative': 35,
                            'neutral': 50,
                            'positive_pct': 43.3,
                            'negative_pct': 23.3,
                            'neutral_pct': 33.3
                        }
                        
                        # Display mock results
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Total Analyzed", mock_data['total_tweets'])
                        with col2:
                            st.metric("Positive", mock_data['positive'], f"{mock_data['positive_pct']:.1f}%")
                        with col3:
                            st.metric("Negative", mock_data['negative'], f"{mock_data['negative_pct']:.1f}%")
                        with col4:
                            st.metric("Neutral", mock_data['neutral'], f"{mock_data['neutral_pct']:.1f}%")
            
            elif input_method == "CSV Upload" and uploaded_file:
                st.info("📊 Processing uploaded CSV data...")
                # Process uploaded CSV here
            else:
                st.warning("⚠️ Please provide input data before analyzing")

    # Tab 2: Fake News Checker
    with tab2:
        st.subheader("🔍 Fake News Detection System")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("### News Text Input")
            news_text = st.text_area(
                "Paste news headline or article text:",
                placeholder="Enter the news content you want to verify...",
                height=150,
                help="Paste any news headline or article text for fake news detection"
            )
        
        with col2:
            st.markdown("### Detection Controls")
            check_btn = st.button(
                "🔍 Check Fake News",
                type="primary",
                help="Analyze text for fake news indicators"
            )
        
        if check_btn and news_text:
            with st.spinner("🔄 Analyzing news content..."):
                try:
                    # API call to backend
                    response = requests.post(
                        "http://127.0.0.1:5000/fakenews",
                        json={"text": news_text},
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        # Display results
                        prediction = result.get('prediction', 'real')
                        confidence = result.get('confidence', 0.5)
                        
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            if prediction.lower() == 'real':
                                st.markdown(f'''
                                <div class="fake-news-real">
                                    ✅ REAL NEWS DETECTED
                                </div>
                                ''', unsafe_allow_html=True)
                            else:
                                st.markdown(f'''
                                <div class="fake-news-fake">
                                    ❌ FAKE NEWS DETECTED
                                </div>
                                ''', unsafe_allow_html=True)
                        
                        with col2:
                            # Confidence gauge
                            fig_gauge = go.Figure(go.Indicator(
                                mode = "gauge+number",
                                value = confidence * 100,
                                domain = {'x': [0, 1], 'y': [0, 1]},
                                title = {'text': "Confidence"},
                                gauge = {
                                    'axis': {'range': [None, 100]},
                                    'bar': {'color': "#2ecc71" if prediction.lower() == 'real' else "#e74c3c"},
                                    'steps': [
                                        {'range': [0, 50], 'color': "lightgray"},
                                        {'range': [50, 100], 'color': "gray"}
                                    ],
                                    'threshold': {
                                        'line': {'color': "red", 'width': 4},
                                        'thickness': 0.75,
                                        'value': 90
                                    }
                                }
                            ))
                            fig_gauge.update_layout(height=200)
                            st.plotly_chart(fig_gauge, use_container_width=True)
                        
                        # Additional analysis
                        if 'analysis' in result:
                            st.markdown("### 📊 Detailed Analysis")
                            analysis = result['analysis']
                            
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Credibility Score", f"{analysis.get('credibility', 0.5):.2f}")
                            with col2:
                                st.metric("Language Quality", f"{analysis.get('language_quality', 0.5):.2f}")
                            with col3:
                                st.metric("Source Reliability", f"{analysis.get('source_reliability', 0.5):.2f}")
                    
                    else:
                        st.error(f"❌ API Error: {response.status_code}")
                
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Connection Error: {str(e)}")
                    # Show mock result for demo
                    st.info("📊 Showing demo result (API unavailable)")
                    
                    # Mock result
                    import random
                    mock_prediction = random.choice(['real', 'fake'])
                    mock_confidence = random.uniform(0.6, 0.95)
                    
                    if mock_prediction == 'real':
                        st.markdown(f'''
                        <div class="fake-news-real">
                            ✅ REAL NEWS DETECTED
                        </div>
                        ''', unsafe_allow_html=True)
                    else:
                        st.markdown(f'''
                        <div class="fake-news-fake">
                            ❌ FAKE NEWS DETECTED
                        </div>
                        ''', unsafe_allow_html=True)
                    
                    st.progress(mock_confidence)
                    st.write(f"Confidence: {mock_confidence:.1%}")
        
        elif check_btn and not news_text:
            st.warning("⚠️ Please enter news text to analyze")

    # Tab 3: Word Cloud Generator
    with tab3:
        st.subheader("☁️ Word Cloud Visualization")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Upload Data for Word Cloud")
            wordcloud_file = st.file_uploader(
                "Upload CSV file for word cloud generation",
                type=['csv'],
                help="CSV should contain text data in a 'tweet' or 'text' column",
                key="wordcloud_upload"
            )
        
        with col2:
            st.markdown("### Customization")
            max_words = st.slider("Maximum words", 50, 200, 100)
            colormap = st.selectbox(
                "Color scheme",
                ["viridis", "plasma", "inferno", "magma", "cool", "hot"]
            )
        
        if wordcloud_file:
            try:
                df_wc = pd.read_csv(wordcloud_file)
                
                # Find text column
                text_column = None
                for col in ['tweet', 'text', 'content', 'message']:
                    if col in df_wc.columns:
                        text_column = col
                        break
                
                if text_column:
                    st.success(f"✅ Found text data in '{text_column}' column")
                    
                    # Generate word cloud
                    with st.spinner("🎨 Generating word cloud..."):
                        try:
                            # Combine all text
                            text_data = ' '.join(df_wc[text_column].astype(str).tolist())
                            
                            # Create word cloud
                            wordcloud = WordCloud(
                                width=800, 
                                height=400, 
                                max_words=max_words,
                                colormap=colormap,
                                background_color='white',
                                relative_scaling=0.5
                            ).generate(text_data)
                            
                            # Display word cloud
                            fig, ax = plt.subplots(figsize=(12, 6))
                            ax.imshow(wordcloud, interpolation='bilinear')
                            ax.axis('off')
                            plt.title(f'Word Cloud - Top {max_words} Words', fontsize=16, fontweight='bold')
                            
                            st.pyplot(fig)
                            
                            # Word frequency table
                            st.markdown("### 📊 Top Words")
                            word_freq = wordcloud.words_
                            freq_df = pd.DataFrame(
                                list(word_freq.items()), 
                                columns=['Word', 'Frequency']
                            ).head(20)
                            
                            col1, col2 = st.columns([1, 2])
                            
                            with col1:
                                st.dataframe(freq_df)
                            
                            with col2:
                                # Bar chart of top words
                                fig_words = px.bar(
                                    freq_df.head(10), 
                                    x='Frequency', 
                                    y='Word',
                                    orientation='h',
                                    title='Top 10 Most Frequent Words'
                                )
                                fig_words.update_layout(height=400)
                                st.plotly_chart(fig_words, use_container_width=True)
                            
                        except Exception as e:
                            st.error(f"❌ Error generating word cloud: {str(e)}")
                            
                else:
                    st.error("❌ No suitable text column found. Please ensure your CSV has a 'tweet', 'text', 'content', or 'message' column")
                    st.write("Available columns:", list(df_wc.columns))
            
            except Exception as e:
                st.error(f"❌ Error loading file: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #666; padding: 20px;">
            <p>📰 Social Media Fake News & Sentiment Analyzer | Built with ❤️ using Streamlit</p>
            <p>Last updated: {}</p>
        </div>
        """.format(datetime.now().strftime("%Y-%m-%d %H:%M")),
        unsafe_allow_html=True
    )

# Main app logic
if st.session_state.page == 'landing':
    show_landing_page()
else:
    show_dashboard()