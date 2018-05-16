import os

class Config:
    """
    General configuration parent class
    """
    # pass
    MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}" 
    MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marion:User Marion New Password@localhost/watchlist'
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


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}