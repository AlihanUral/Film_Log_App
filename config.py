import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'movies.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'film_log_secret_key'
    OMDB_API_KEY = '43dcb5aa'
    MOVIES_PER_PAGE = 10  # Number of movies to show per page
    DEBUG = True
    