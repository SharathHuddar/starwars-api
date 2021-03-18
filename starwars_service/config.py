import os


class Config(object):
    DEBUG = False
    SW_API_BASE_URL = 'https://swapi.dev/api'

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
