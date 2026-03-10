class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, name, email):

        if not name:
            raise ValueError("Name is required")

        user = {"name": name, "email": email}

        return self.repository.save(user)

    def list_users(self):
        return self.repository.find_all()

    def get_user(self, user_id):
        user = self.repository.find_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        return user

    def update_user(self, user_id, data):
        user = self.repository.update(user_id, data)
        if not user:
            raise ValueError("User not found")

        return user

    def delete_user(self, user_id):
        user = self.repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        self.repository.delete(user_id)
        return user
