from repo.users_repository import UsersRepository

class UserService:
    def __init__(self, db_session):
        self.users_repository = UsersRepository(db_session)

    def create_user(self, data):
        try:
            existing_user = self.users_repository.get_user_by_name(data['name'])
            if existing_user:
                return {'error': 'User name already exists'}, 409            
            new_user = self.users_repository.create(name=data['name'])
            return {'message': 'User created successfully', 'user_id': new_user.id}, 201
        except Exception as e:
            return {'error': str(e)}, 500
        
    def get_users(self, limit=100):
        try:
            users = self.users_repository.get_all(limit=limit)
            return [{'id': user.id, 'name': user.name} for user in users], 200
        except Exception as e:
            return {'error': str(e)}, 500
        
    def get_user_by_id(self, user_id):
        return self.repository.get_user_by_id(user_id)
    
    def delete_user(self, user_id):
        return self.repository.delete_user(user_id)