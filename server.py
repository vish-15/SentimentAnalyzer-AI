"""
server.py - A Flask application for sentiment analysis using Watson NLP.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route("/sentimentAnalyzer", methods=['GET'])
def sent_analyzer():
    """Handles GET requests for sentiment analysis."""
    text_to_analyze = request.args.get('textToAnalyze')
    analysis_result = sentiment_analyzer(text_to_analyze)

    if analysis_result['label'] is None:  # Check for invalid input
        return "Invalid input! Try again."

    formatted_output = (
        f"The given text has been identified as {analysis_result['label']} "
        f"with a score of {analysis_result['score']:.5f}."
    )
    return formatted_output

@app.route("/")
def render_index_page():
    """Renders the index.html template."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000
