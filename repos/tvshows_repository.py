from models.postgres import TVShow
from repos.base_repository import BaseRepository

class TVShowRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, TVShow)

    def get_tvshow_by_title(self, title: str):
        return self.db_session.query(TVShow).filter(TVShow.title == title).first()

    def get_tvshow_by_id(self, tvshow_id: int):
        return self.db_session.query(TVShow).filter(TVShow.id == tvshow_id).first()

    def delete_tvshow(self, tvshow_id: int):
        tvshow = self.get_tvshow_by_id(tvshow_id)
        if tvshow:
            self.db_session.delete(tvshow)
            self.db_session.commit()
            return tvshow
        return None
