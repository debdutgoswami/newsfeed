import os
from distutils.util import strtobool

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    #CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    # SERVER_NAME = os.getenv('SERVER_NAME',
    #                     'localhost:{0}'.format(os.getenv('DOCKER_WEB_PORT',
    #                                                      '8080')))
    SECRET_KEY = os.getenv('SECRET_KEY', 'yoursecret')
    # Flask-Mail.
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.getenv('MAIL_PORT', 465)
    MAIL_USE_TLS = bool(strtobool(os.getenv('MAIL_USE_TLS', 'false')))
    MAIL_USE_SSL = bool(strtobool(os.getenv('MAIL_USE_SSL', 'true')))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', None)
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', None)
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'smtp.gmail.com')

    # Celery.
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://localhost//')
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 5

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
