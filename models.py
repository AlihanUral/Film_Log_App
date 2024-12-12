from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(200))    
    logs = db.relationship('Log', backref='movie', lazy=True)  # Log ilişkisi

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    movie = db.relationship('Movie', backref=db.backref('ratings', lazy=True))

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    watched_date = db.Column(db.Date)
