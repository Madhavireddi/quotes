from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# External API endpoint for random quotes
QUOTE_API_URL = 'https://api.quotable.io/random'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-quote')
def fetch_quote():
    try:
        response = requests.get(QUOTE_API_URL)
        quote_data = response.json()
        quote_text = quote_data.get('content', 'Failed to fetch quote.')
        quote_author = quote_data.get('author', '')
        return jsonify({'quote': quote_text, 'author': quote_author})
    except Exception as e:
        print('Error fetching quote:', e)
        return jsonify({'quote': 'Failed to fetch quote.', 'author': ''})

if __name__ == '__main__':
    app.run(debug=True)
