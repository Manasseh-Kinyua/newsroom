from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

#getting the api key
api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    '''
    function to get the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)









#dsff
