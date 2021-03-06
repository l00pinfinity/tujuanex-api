import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = "thisisverysecret"
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:////" + os.path.join(base_dir,"data-dev.sqlite")

class TestingConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    pass


config = {
        "default":DevelopmentConfig,
        "development":DevelopmentConfig,
        "testing":TestingConfig,
        "production":ProductionConfig
    }
