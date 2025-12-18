import pandas as pd
import numpy as np
from textblob import TextBlob
import gradio as gr
import plotly.express as px
import plotly.graph_objects as go

# Sample data
sample_texts = ["I love this movie! It's amazing!", "This product is terrible and disappointing.",
               "The weather is okay today.", "Best purchase ever! Highly recommend!",
               "Worst experience of my life.", "It's an average product, nothing special.",
               "Absolutely fantastic! Five stars!", "Not good, not bad, just normal."]
df = pd.DataFrame({'text': sample_texts})

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    return 'Positive' if polarity > 0.1 else 'Negative' if polarity < -0.1 else 'Neutral'

def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def get_confidence_level(score):
    abs_score = abs(score)
    return "Very Confident" if abs_score >= 0.5 else "Confident" if abs_score >= 0.3 else "Somewhat Confident" if abs_score >= 0.1 else "Low Confidence"

# Apply sentiment analysis
df['sentiment'] = df['text'].apply(analyze_sentiment)
df['score'] = df['text'].apply(get_sentiment_score)

def create_sentiment_visualization():
    sentiment_counts = df['sentiment'].value_counts()
    return px.pie(values=sentiment_counts.values, names=sentiment_counts.index,
                 title="Sample Data Sentiment Distribution",
                 color_discrete_map={'Positive': '#2ecc71', 'Negative': '#e74c3c', 'Neutral': '#95a5a6'})

def analyze_text_ui(text):
    if not text.strip():
        return "Please enter some text to analyze", "", None

    sentiment = analyze_sentiment(text)
    score = get_sentiment_score(text)
    confidence = get_confidence_level(score)

    result_text = f"**Sentiment:** {sentiment}\n\n**Score:** {score:.3f}\n\n**Confidence:** {confidence}"

    # Create gauge chart
    color = "#2ecc71" if sentiment == 'Positive' else "#e74c3c" if sentiment == 'Negative' else "#95a5a6"
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Sentiment Score"},
        gauge={
            'axis': {'range': [-1, 1]},
            'bar': {'color': color},
            'steps': [
                {'range': [-1, -0.1], 'color': "#ffebee"},
                {'range': [-0.1, 0.1], 'color': "#f5f5f5"},
                {'range': [0.1, 1], 'color': "#e8f5e8"}
            ]
        }
    ))
    fig.update_layout(height=300)

    return result_text, text, fig

# Create Gradio interface
with gr.Blocks(title="Sentiment Analysis Tool") as demo:
    gr.Markdown("# Sentiment Analysis Tool")
    gr.Markdown("Analyze the emotional tone of text using AI-powered sentiment detection")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Enter Text")
            text_input = gr.Textbox(
                placeholder="Type or paste your text here...", 
                lines=5, 
                label="Input Text"
            )
            
            with gr.Row():
                analyze_btn = gr.Button("Analyze", variant="primary")
                clear_btn = gr.Button("Clear")
            
            gr.Markdown("**Example texts:**")
            with gr.Row():
                example1_btn = gr.Button("Positive Example", size="sm")
                example2_btn = gr.Button("Negative Example", size="sm")
                example3_btn = gr.Button("Neutral Example", size="sm")

        with gr.Column():
            gr.Markdown("### Results")
            result_display = gr.Markdown()
            analyzed_text = gr.Textbox(label="Analyzed Text", interactive=False)
            score_chart = gr.Plot(label="Sentiment Score Gauge")

    gr.Markdown("---")
    gr.Markdown("### Sample Data Analysis")
    
    with gr.Row():
        with gr.Column():
            gr.Dataframe(
                value=df[['text', 'sentiment', 'score']], 
                headers=['Text', 'Sentiment', 'Score'],
                label="Sample Dataset"
            )
        with gr.Column():
            gr.Plot(value=create_sentiment_visualization())

    # Event handlers
    analyze_btn.click(
        analyze_text_ui, 
        inputs=text_input, 
        outputs=[result_display, analyzed_text, score_chart]
    )
    
    clear_btn.click(
        lambda: ("", "", "", None), 
        outputs=[text_input, result_display, analyzed_text, score_chart]
    )
    
    text_input.submit(
        analyze_text_ui, 
        inputs=text_input, 
        outputs=[result_display, analyzed_text, score_chart]
    )
    
    # Example buttons
    example1_btn.click(
        lambda: "I absolutely love this! It's the best thing ever!", 
        outputs=text_input
    )
    example2_btn.click(
        lambda: "This is terrible and completely disappointing.", 
        outputs=text_input
    )
    example3_btn.click(
        lambda: "It's okay, nothing special about it.", 
        outputs=text_input
    )

    gr.Markdown("---")
    gr.Markdown("*Built with Python, TextBlob, and Gradio*")

if __name__ == "__main__":
    demo.launch(share=True, show_error=True)