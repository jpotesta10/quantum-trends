from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv('API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': query,
        'sortBy': 'publishedAt',
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
