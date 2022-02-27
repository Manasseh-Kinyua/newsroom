from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    returns the index page and its data.
    '''
    word = 'Hellor World'
    return render_template('index.html', message = word)

    # @app.route('News')
    # def














#rewtewrw
