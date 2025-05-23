"""
This module provides a function analyzes customer feedback/reviews text
to detect and classify the emotions expressed,
enabling data-driven insights for improving products & services.

This system uses the Emotion Predict function of the Watson NLP Library
to classify the emotions expressed in the text.
The function sends the text to be analyzed via an HTTP POST request.

Dependencies:
    - requests: Required to send HTTP requests to the Watson NLP API.
"""

import json

import requests


def emotion_detector(text_to_analyse: str) -> str:
    """
    Analyze the emotion expressed from a given text.

    Args:
        text_to_analyse (str): The input text to be analyzed.

    Returns:
        dict: Dictionary containing scores for anger, disgust, fear,
        joy, and sadness,plus the dominant emotion.
        Returns None for each value if input is blank or API returns 400.
    """

    # Check for blank or whitespace-only input
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    try:
        url = (
            "https://sn-watson-emotion.labs.skills.network/v1/"
            "watson.runtime.nlp.v1/NlpService/EmotionPredict"
        )
        myobj = {"raw_document": {"text": text_to_analyse}}
        header = {
            "grpc-metadata-mm-model-id": ("emotion_aggregated-workflow_lang_en_stock"),
        }

        response = requests.post(url, json=myobj, headers=header, timeout=10)
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
        response.raise_for_status()

        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        result = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion,
        }

        return result

    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.RequestException as e:
        return f"Network error during emotion analysis: {e}"
    except ValueError as e:
        return f"Error parsing response: {e}"
