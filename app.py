from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Movie, Rating, Log
import requests
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

OMDB_API_KEY = "43dcb5aa"

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Film ekleme
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form.get('rating')  
        response = requests.get(f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}")
        if response.status_code == 200:
            data = response.json()
            if data.get('Response') == 'True':
                movie = Movie(
                    title=data['Title'],
                    year=data['Year'],
                    genre=data['Genre'],
                    description=data['Plot'],
                    poster_url=data['Poster']
                )
                db.session.add(movie)
                db.session.commit()
                
                log = Log(movie_id=movie.id, watched_date=datetime.utcnow())
                db.session.add(log)
                db.session.commit()
                
                if rating:
                    movie_rating = Rating(movie_id=movie.id, rating=int(rating))  
                    db.session.add(movie_rating)
                    db.session.commit()
        
                return redirect(url_for('list_movies'))
            else:
                return "Film bulunamadı!"
    return render_template('add_movie.html')


@app.route('/delete_movie/<int:movie_id>', methods=['GET', 'POST'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    ratings = Rating.query.filter_by(movie_id=movie_id).all()  
    logs = Log.query.filter_by(movie_id=movie_id).all()
    for log in logs:
        db.session.delete(log)
    for rating in ratings:
        db.session.delete(rating)  
    db.session.delete(movie)  
    db.session.commit()  
    return redirect(url_for('list_movies'))  


@app.route('/movies')
def list_movies():
    movies = Movie.query.all()
    return render_template('movie_list.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
    






