# Sentiment Analysis Tool

A web-based application that analyzes the emotional tone of text using natural language processing. Simply input any text and get instant sentiment classification with confidence scores and visual gauges.

## Live Demo

Try the app here: [https://huggingface.co/spaces/mohataseem/sentivibe](https://huggingface.co/spaces/mohataseem/sentivibe)

## Features

- **Real-time Sentiment Analysis**: Instantly classify text as Positive, Negative, or Neutral
- **Confidence Scoring**: Get numerical sentiment scores ranging from -1 (very negative) to +1 (very positive)
- **Visual Feedback**: Interactive gauge charts to visualize sentiment scores
- **Sample Data Analysis**: Pre-loaded examples with sentiment distribution visualization
- **Easy-to-Use Interface**: Clean, intuitive UI built with Gradio

## Technology Stack

- **Python**: Core programming language
- **TextBlob**: Natural language processing library for sentiment analysis
- **Gradio**: Web interface framework
- **Plotly**: Interactive data visualization
- **Pandas**: Data manipulation and analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sentiment-analysis-tool.git
cd sentiment-analysis-tool
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to the local URL provided (typically `http://127.0.0.1:7860`)

## Requirements

```
textblob==0.17.1
gradio
plotly
pandas
numpy
```

## Usage

1. Enter or paste your text in the input box
2. Click the "Analyze" button or press Enter
3. View the sentiment classification, score, and confidence level
4. Check the gauge chart for a visual representation of the sentiment score

### Example Use Cases

- Analyzing customer reviews and feedback
- Monitoring social media sentiment
- Evaluating survey responses
- Assessing email or message tone
- Content moderation

## How It Works

The application uses TextBlob's pre-trained sentiment analyzer, which:

1. **Polarity Score**: Ranges from -1 (most negative) to +1 (most positive)
2. **Classification Logic**:
   - Positive: polarity > 0.1
   - Negative: polarity < -0.1
   - Neutral: polarity between -0.1 and 0.1
3. **Confidence Levels**:
   - Very Confident: |score| ≥ 0.5
   - Confident: |score| ≥ 0.3
   - Somewhat Confident: |score| ≥ 0.1
   - Low Confidence: |score| < 0.1

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Author

**Mohataseem**

- Hugging Face: [@mohataseem](https://huggingface.co/mohataseem)

## Acknowledgments

- TextBlob for sentiment analysis capabilities
- Gradio for the amazing web interface framework
- Plotly for interactive visualizations