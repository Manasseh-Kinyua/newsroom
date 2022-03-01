from app import app
import urllib.request,json
from .models import news
from .models import sources

News = news.News
Sources = sources.Sources

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

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            print(news_results_list)
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    function to transform the movie result into list objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        news_object = News(author,title,description,url,urlToImage,publishedAt,content)
        print(news_object)
        news_results.append(news_object)

    return news_results

def get_sources():
    get_sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_data(sources_results_list)
    return sources_results

def process_data(sources_list):
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(id,name,description,url,category,language,country)
        print(news_object)
        sources_results.append(sources_object)

    return sources_results















#dsff
