from repos.tvshows_repository import TVShowRepository

class TVShowService:
    def __init__(self, db_session):
        self.repository = TVShowRepository(db_session)

    def create_tvshow(self, tvshow_create):
        tvshow = self.repository.create(tvshow_create)
        return tvshow

    def get_tvshows(self, limit=100):
        return self.repository.get_all(limit=limit)

    def get_tvshow_by_id(self, tvshow_id):
        return self.repository.get_tvshow_by_id(tvshow_id)

    def delete_tvshow(self, tvshow_id):
        return self.repository.delete_tvshow(tvshow_id)