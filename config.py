
class Config:
    pass

class ProdConfig(Config):
    pass

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:moringa@localhost/portfolio_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:moringa@localhost/portfolio'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

