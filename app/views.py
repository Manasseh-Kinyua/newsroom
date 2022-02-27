from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    returns the index page and its data.
    '''
    title = 'Home - Welcome to the Quickest News for Busy People'
    return render_template('index.html', title = title)

    # @app.route('News')
    # def














#rewtewrw
