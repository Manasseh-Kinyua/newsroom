class Config:
    '''
    general configuration class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'

class ProdConfig(Config):
    '''
    production configurationchild class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True
