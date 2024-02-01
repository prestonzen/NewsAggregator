from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={query}&language=en&from=2023-12-31&sortBy=publishedAt&apiKey=7236ab677e7c41be82dfa8db654a56b1"
    )
    news = response.json()
    return render_template('news.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
