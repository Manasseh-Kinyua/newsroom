class Config:
    '''
    general configuration class
    '''
    pass

class ProdConfig(config):
    '''
    production configurationchild class
    '''
    pass

class DevConfig(config):
    '''
    development configuration child class
    '''
    DEBUG = True
