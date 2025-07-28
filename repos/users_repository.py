from models.postgres import User
from repos.base_repository import BaseRepository    

class UsersRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, User)

    def get_user_by_name(self, name: str):
        return self.db_session.query(User).filter(User.name == name).first()

    def get_user_by_id(self, user_id: int):
        return self.db_session.query(User).filter(User.id == user_id).first()

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()
            return user
        return None