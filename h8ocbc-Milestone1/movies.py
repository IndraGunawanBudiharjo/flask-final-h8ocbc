from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema

def read_all():
    """
    This function responds to a request for /api/director/movies
    with the complete list of movies, sorted by movie id
    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movie.query.order_by(db.desc(Movie.id)).limit(15).all()

    # Serialize the list of movies from our data
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def create(director_id, movie):
    """
    This function creates a new note related to the passed in person id.
    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    # get the parent person
    director = Director.query.filter(Director.id == director_id).one_or_none()

    # Was a person found?
    if director is None:
        abort(404, f"Director not found for Id: {director_id}")

    # Create a note schema instance
    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    # Add the note to the person and database
    director.movies.append(new_movie)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_movie)

    return data, 201

def read_one(director_id, movie_id):
    """
    This function responds to a request for
    /api/people/{director_id}/notes/{movie_id}
    with one matching movie for the associated director
    :param director_id:         Id of director the movie is related to
    :param movie_id:            Id of the movie
    :return:                    json string of note contents
    """
    # Query the database for the note
    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # Was a note found?
    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Movie not found for Id: {movie_id}")

def update(director_id, movie_id, movie):
    update_movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    if update_movie is not None:

        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        update.director_id = update_movie.director_id
        update.id = update_movie.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_movie)

        return data, 200

    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def delete(director_id, movie_id):
    movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )
    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(f"movies {movie_id} deleted", 200)

    else:
        abort(404, f"Movie not found for Id: {movie_id}")

def read_by_title(title):
    """
    This function responds to a request for /api/directors/{name}
    with one matching director from directors
    :param name:        Name of director to find
    :return:            director matching the name
    """
    movie = (
        Movie.query.filter(Movie.title.like(f"%{title}%"))
        # .outerjoin(Movie)
        # .one_or_none()
    )
    # Did we find a person?
    if movie is not None:

        # Serialize the data for the response
        movie_schema = MovieSchema(many=True)
        data = movie_schema.dump(movie)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Movie's title not found: {title}")