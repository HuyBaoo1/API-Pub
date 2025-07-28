from repos.trino_user_repo import TrinoUserRepository

class TrinoUserService:
    def __init__(self, user_repo: TrinoUserRepository):
        self.user_repo = user_repo

    def fetch_users_from_dwh(self):
        return self.repo.get_all_users()