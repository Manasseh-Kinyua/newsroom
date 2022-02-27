from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

#getting the api key
api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config['NEWS_API_BASE_URL']








#dsff
