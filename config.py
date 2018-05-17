import os

class Config:
    """
    General configuration parent class
    """
    # pass
    MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}" 
    MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://marion:{os.environ.get("DATABASE_PASSWORD")}@localhost/watchlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    
class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """

    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://marion:{os.environ.get("DATABASE_PASSWORD")}@localhost/watchlist_test'

    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'test': TestConfig
}