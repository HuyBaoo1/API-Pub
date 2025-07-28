from models.postgres import Movie
from repos.base_repository import BaseRepository

class MovieRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, Movie)

    def get_movie_by_title(self, title: str):
        return self.db_session.query(Movie).filter(Movie.title == title).first()

    def get_movie_by_id(self, movie_id: int):
        return self.db_session.query(Movie).filter(Movie.id == movie_id).first()

    def delete_movie(self, movie_id: int):
        movie = self.get_movie_by_id(movie_id)
        if movie:
            self.db_session.delete(movie)
            self.db_session.commit()
            return movie
        return None