from flask import Flask

from app.controllers.product_controller import ProductController
from app.controllers.user_controller import UserController
from app.database import db

# from app.repositories.memory_product_repository import MemoryProductRepository as ProductRepository
# from app.repositories.memory_user_repository import MemoryUserRepository as UserRepository
from app.repositories.sqlalchemy_product_repository import (
    SQLAlchemyProductRepository as ProductRepository,
)
from app.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository as UserRepository,
)
from app.routes.product_routes import create_product_routes
from app.routes.user_routes import create_user_routes
from app.services.product_service import ProductService
from app.services.user_service import UserService


def create_app():

    app = Flask(__name__)

    # SQL Alchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # User
    user_repo = UserRepository()
    user_service = UserService(user_repo)
    user_controller = UserController(user_service)
    user_routes = create_user_routes(user_controller)

    # Product
    product_repo = ProductRepository()
    product_service = ProductService(product_repo)
    product_controller = ProductController(product_service)
    product_routes = create_product_routes(product_controller)

    app.register_blueprint(user_routes)
    app.register_blueprint(product_routes)

    return app
