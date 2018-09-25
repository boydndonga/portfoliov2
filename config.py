import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB')
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

