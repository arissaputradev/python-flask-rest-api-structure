from app.repositories.user_repository import UserRepository


class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []
        self.current_id = 1

    def save(self, user):
        user.id = self.current_id
        self.current_id += 1
        self.users.append(user)
        return user

    def find_all(self):
        return self.users
