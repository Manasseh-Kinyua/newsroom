class Config:
    '''
    general configuration class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True
