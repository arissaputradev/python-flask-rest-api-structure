from flask import Flask

from app.repositories.user_repository import UserRepository
from app.routes.user_routes import create_user_routes
from app.services.user_service import UserService


def create_app():

    app = Flask(__name__)

    repo = UserRepository()
    service = UserService(repo)

    user_routes = create_user_routes(service)

    app.register_blueprint(user_routes)

    return app
