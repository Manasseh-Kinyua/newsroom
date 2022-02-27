class Config:
    '''
    general configuration class
    '''
    pass

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
