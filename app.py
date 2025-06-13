from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['OMDB_API_KEY'] = '7b50a261'  # Kullanıcının OMDB API anahtarı

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(4))
    genre = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(500))
    imdb_id = db.Column(db.String(20), unique=True)
    rating = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Movie {self.title}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        if not title:
            flash('Lütfen bir film adı girin.', 'error')
            return redirect(url_for('add_movie'))

        # OMDB API'den film araması yap
        search_url = f'http://www.omdbapi.com/?apikey={app.config["OMDB_API_KEY"]}&s={title}'
        try:
            response = requests.get(search_url)
            data = response.json()
            
            # API yanıtını kontrol et
            if data.get('Response') == 'True':
                return render_template('search_results.html', movies=data['Search'])
            else:
                error_message = data.get('Error', 'Film bulunamadı.')
                flash(f'Film araması başarısız: {error_message}', 'error')
                return redirect(url_for('add_movie'))
        except Exception as e:
            app.logger.error(f'API Hatası: {str(e)}')
            flash('Film araması sırasında bir hata oluştu. Lütfen tekrar deneyin.', 'error')
            return redirect(url_for('add_movie'))

    return render_template('add_movie.html')

@app.route('/movie_details/<imdb_id>')
def movie_details(imdb_id):
    # OMDB API'den film detaylarını getir
    url = f'http://www.omdbapi.com/?apikey={app.config["OMDB_API_KEY"]}&i={imdb_id}&plot=full'
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get('Response') == 'True':
            return jsonify(data)
        else:
            error_message = data.get('Error', 'Film detayları alınamadı.')
            return jsonify({'Response': 'False', 'Error': error_message}), 404
    except Exception as e:
        app.logger.error(f'API Hatası: {str(e)}')
        return jsonify({'Response': 'False', 'Error': 'Film detayları alınırken bir hata oluştu.'}), 500

@app.route('/add_movie_to_list', methods=['POST'])
def add_movie_to_list():
    try:
        imdb_id = request.form.get('imdb_id')
        rating = request.form.get('rating', type=float)

        if not imdb_id:
            flash('Film ID bulunamadı.', 'error')
            return redirect(url_for('add_movie'))

        # Film zaten var mı kontrol et
        existing_movie = Movie.query.filter_by(imdb_id=imdb_id).first()
        if existing_movie:
            flash('Bu film zaten listenizde bulunuyor.', 'error')
            return redirect(url_for('movies'))

        # OMDB API'den film detaylarını getir
        url = f'http://www.omdbapi.com/?apikey={app.config["OMDB_API_KEY"]}&i={imdb_id}&plot=full'
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            new_movie = Movie(
                title=data['Title'],
                year=data['Year'],
                genre=data['Genre'],
                description=data['Plot'],
                poster_url=data['Poster'],
                imdb_id=imdb_id,
                rating=rating
            )

            db.session.add(new_movie)
            db.session.commit()
            flash('Film başarıyla eklendi!', 'success')
            return redirect(url_for('movies'))
        else:
            error_message = data.get('Error', 'Film detayları alınamadı.')
            flash(f'Film eklenemedi: {error_message}', 'error')
            return redirect(url_for('add_movie'))

    except Exception as e:
        db.session.rollback()
        app.logger.error(f'Veritabanı Hatası: {str(e)}')
        flash('Film eklenirken bir hata oluştu. Lütfen tekrar deneyin.', 'error')
        return redirect(url_for('add_movie'))

@app.route('/movies')
def movies():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_query = request.args.get('search', '')

    query = Movie.query
    if search_query:
        query = query.filter(Movie.title.ilike(f'%{search_query}%'))
    
    movies = query.order_by(Movie.created_at.desc()).paginate(page=page, per_page=per_page)
    return render_template('movies.html', movies=movies)

@app.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    try:
        movie = Movie.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        flash('Film başarıyla silindi!', 'success')
    except Exception as e:
        db.session.rollback()
        app.logger.error(f'Veritabanı Hatası: {str(e)}')
        flash('Film silinirken bir hata oluştu.', 'error')
    return redirect(url_for('movies'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    






