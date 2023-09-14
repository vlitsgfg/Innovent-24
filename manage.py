from flask import Flask, render_template, request

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(comment):
    sentiment_score = sia.polarity_scores(comment)
    if sentiment_score['compound'] >= 0.05:
        return 'positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'


def overall_rating(comments):
    score = 0
    for comment in comments:
        sentiment_score = sia.polarity_scores(comment)
        score += sentiment_score['compound']

    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comments = request.form.get('comments')
        comments = comments.split('\n')
        individual_results = [analyze_sentiment(comment) for comment in comments]
        overall_result = overall_rating(comments)
        return render_template('index.html', individual_results=individual_results, overall_result=overall_result)

    return render_template('index.html', individual_results=None, overall_result=None)


if __name__ == '__main__':
    app.run(debug=True)
