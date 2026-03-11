from sqlalchemy import or_

from app.database import db
from app.models.user import User
from app.repositories.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    ALLOWED_SORT_FIELDS = ["name", "email", "id"]

    def save(self, user):

        db_user = User(name=user["name"], email=user["email"])

        db.session.add(db_user)
        db.session.commit()

        return db_user

    # def find_all(self):
    #     # return User.query.all()
    #     return db.session.execute(db.select(User)).scalars().all()

    @staticmethod
    def validate_allowed_fields(field):

        if field and field not in SQLAlchemyUserRepository.ALLOWED_SORT_FIELDS:
            raise ValueError("Invalid sort field")

    def find_all(self, page, limit, email=None, sort=None, search=None):
        query = User.query

        if email:
            query = query.filter(User.email == email)

        # search
        if search:
            query = query.filter(
                or_(User.name.ilike(f"%{search}%"), User.email.ilike(f"%{search}%"))
            )

        if sort:
            field = sort.lstrip("-")
            SQLAlchemyUserRepository.validate_allowed_fields(field)

            column = getattr(User, field, None)
            if sort.startswith("-"):
                query = query.order_by(column.desc())
            else:
                query = query.order_by(column.asc())

        pagination = query.paginate(page=page, per_page=limit)

        # -- DEBUG WAY --
        # print(vars(pagination))
        # print(dir(pagination))

        users = pagination.items

        return {
            "data": [{"id": u.id, "name": u.name, "email": u.email} for u in users],
            "page": page,
            "limit": limit,
            "total": pagination.total,
            "total_pages": pagination.pages,
        }

    def find_by_id(self, id):
        # return User.query.get(id)
        return db.session.get(User, id)

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
