import os

class Config(object):
    DEBUG = True
    TESTING = True
    TRAP_HTTP_EXCEPTIONS = True
    SESSION_COOKIE_SECURE = True
    CSRF_ENABLED = True
    SECRET_KEY = 'sdfsdf82347$$%$%$%$&fsdfs!!ASx+__WEBB$'
    
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/redspartan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
'''
