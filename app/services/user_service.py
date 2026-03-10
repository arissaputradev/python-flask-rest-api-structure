from app.models.user import User


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, name, email):

        if not name:
            raise ValueError("Name is required")

        user = User(name, email)

        return self.repository.save(user)

    def list_users(self):
        return self.repository.find_all()
