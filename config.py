import os

class Config:
    BASE_URL = 'https://newsapi.org/v2/sources?apiKey=988fb23113204cfcb2cf79eb7ad99b76'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

