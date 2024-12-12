# Film_Log_App
Purpose of the Project

This project allows users to log the movies they have watched, rate them, and list these movies. The application also fetches movie information automatically via the OMDB API and provides a visual interface.

Project Components

1. Backend: Flask Framework

	•	Flask: The core framework of the application.
	•	SQLAlchemy: Used for database operations.
	•	SQLite: Chosen as a lightweight and portable database.
	•	OMDB API: Used to fetch movie information.

2. Database Models

	1.	Movie:
	•	Stores movie information.
	•	Fields:
	•	id: Movie ID (Primary Key)
	•	title: Movie title
	•	year: Release year
	•	genre: Genre
	•	description: Description
	•	poster_url: Poster URL
	•	Relationships:
	•	logs: Viewing records of the movie.
	•	ratings: Rating records of the movie.
	2.	Rating:
	•	Stores ratings given to movies.
	•	Fields:
	•	id: Rating ID (Primary Key)
	•	movie_id: ID of the related movie (Foreign Key)
	•	rating: Rating given by the user.
	3.	Log:
	•	Stores viewing dates of movies.
	•	Fields:
	•	id: Log ID (Primary Key)
	•	movie_id: ID of the related movie (Foreign Key)
	•	watched_date: Viewing date.

Frontend Components

	1.	HTML Pages:
	•	index.html: Home page introducing the application and providing user entry points.
	•	add_movie.html: Form for users to add new movies.
	•	movie_list.html: Page listing added movies, with options to delete them.
	2.	CSS (styles.css):
	•	A modern and user-friendly interface design.
	•	Responsive layout ensures compatibility across devices.
	•	Movies are visually presented using card components.
 
 API Usage

	•	OMDB API: When a user wants to add a movie, the application sends a request to the OMDB API using the movie title. The returned data is stored in the database.
	•	Endpoint: http://www.omdbapi.com/?t=<title>&apikey=<api_key>
 Main Functions

1. Add Movie

	•	The user enters a movie title and optionally a rating.
	•	The application sends a request to the OMDB API and retrieves movie details.
	•	The movie and its rating (if provided) are saved to the database.
	•	A viewing log is created.

2. List Movies

	•	All movies are fetched from the Movie model.
	•	Movie details (poster, year, genre, description, rating) are displayed in a list.
	•	Users can view and delete movies.

3. Delete Movie

	•	When a user wants to delete a movie:
	•	The movie record (Movie), associated ratings (Rating), and logs (Log) are removed from the database.

Project Structure

1. config.py

	•	Contains application configuration settings:
	•	Database connection (SQLALCHEMY_DATABASE_URI).
	•	Secret key (SECRET_KEY).

2. models.py

	•	Contains SQLAlchemy models:
	•	Movie, Rating, Log classes.

3. app.py

	•	The main file of the application.
	•	Defines application routes and functions.

4. Static Files

	•	styles.css: Visual styling file.
	•	Poster URL: Posters provided by the OMDB API are directly displayed.

Example Usage

Add Movie

	1.	The user enters a title in the Add Movie form.
	2.	Information retrieved from the OMDB API is saved to the database.
	3.	The user can list the added movie.

List Movies

	1.	All movies are displayed as a list.
	2.	Users can view details, check ratings, or delete a movie.

Delete Movie

	1.	When a user clicks the delete button for a movie:
	2.	The movie information, along with related ratings and logs, is deleted.

 Summary

This application provides users with a functional tool to organize and evaluate the movies they watch. It is built with Flask, ensuring simplicity and extensibility. The interface is user-friendly and visually appealing, offering a seamless experience for movie enthusiasts.
