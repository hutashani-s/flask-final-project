"""Flask web server for running EmotionDetection on input text."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# pylint: disable=invalid-name
app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main web UI template."""
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze text passed via query string and return formatted emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    