from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    '''
    returns the index page and its data.
    '''

    news = get_news()
    print(news)
    title = 'Home - Welcome to the Quickest News for Busy People'
    return render_template('index.html', title = title, articles = news)

@app.route('/sources')
def source():
    title = 'Home - Welcome to the Quickest News for Busy People'
    # see = get_sources()
    return render_template('source.html',title=title)

    # @app.route('News')
    # def














#rewtewrw
