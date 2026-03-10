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
