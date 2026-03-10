from app.database import db
from app.models.user import User
from app.repositories.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    def save(self, user):

        db_user = User(name=user["name"], email=user["email"])

        db.session.add(db_user)
        db.session.commit()

        return db_user

    def find_all(self):
        return User.query.all()

    def find_by_id(self, id):
        return User.query.get(id)

    def update(self, user_id, data):

        user = User.query.get(user_id)

        if not user:
            return None

        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)

        db.session.commit()

        return user

    def delete(self, user_id):

        user = User.query.get(user_id)

        if not user:
            return False

        db.session.delete(user)
        db.session.commit()

        return True
