"""
sentiment_analysis.py - A module for performing sentiment analysis using Watson NLP.
"""

import requests  # Third-party import

def sentiment_analyzer(text_to_analyse):
    """Analyzes the sentiment of the given text using the Watson NLP API.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: A dictionary containing the sentiment label and score.
              Returns {'label': None, 'score': None} for invalid input.
    """
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/'
           'NlpService/SentimentPredict')
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Set a timeout for the POST request
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 200:
        formatted_response = response.json()  # Directly parse JSON response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {'label': label, 'score': score}

    # Return None for invalid input
    return {'label': None, 'score': None}
