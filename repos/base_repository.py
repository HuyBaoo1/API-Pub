from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

class BaseRepository:
    def __init__(self, db_session: Session, model):
        self.db_session = db_session
        self.model = model

    def get_by_id(self, id):
        return self.db_session.query(self.model).filter(self.model.id == id).first()

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.db_session.add(obj)
        self.db_session.commit()
        self.db_session.refresh(obj)
        return obj

    def update(self, id, **kwargs):
        obj = self.get_by_id(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            self.db_session.commit()
            self.db_session.refresh(obj)
        return obj

    def delete(self, id):
        obj = self.get_by_id(id)
        if obj:
            self.db_session.delete(obj)
            self.db_session.commit()
        return obj
