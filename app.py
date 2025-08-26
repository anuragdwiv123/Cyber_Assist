from flask import Flask, render_template
from data.content import get_home_content, get_news_content, get_resources_content

app = Flask(__name__)

@app.route('/')
def home():
    content = get_home_content()
    return render_template('home.html', **content)

@app.route('/news')
def news():
    articles = get_news_content()
    return render_template('news.html', articles=articles)

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/resources')
def resources():
    content = get_resources_content()
    return render_template('resources.html', **content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)