from repos.movies_repository import MovieRepository

class MovieService:
    def __init__(self, db_session):
        self.repository = MovieRepository(db_session)

    def create_movie(self, movie_create):
        movie = self.repository.create(movie_create)
        return movie

    def get_movies(self, limit=100):
        return self.repository.get_all(limit=limit)

    def get_movie_by_id(self, movie_id):
        return self.repository.get_movie_by_id(movie_id)

    def delete_movie(self, movie_id):
        return self.repository.delete_movie(movie_id)