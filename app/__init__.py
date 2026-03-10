from flask import Flask

from app.controllers.product_controller import ProductController
from app.controllers.user_controller import UserController
from app.repositories.product_repository import ProductRepository
from app.repositories.user_repository import UserRepository
from app.routes.product_routes import create_product_routes
from app.routes.user_routes import create_user_routes
from app.services.product_service import ProductService
from app.services.user_service import UserService


def create_app():

    app = Flask(__name__)

    user_repo = UserRepository()
    user_service = UserService(user_repo)
    user_controller = UserController(user_service)
    user_routes = create_user_routes(user_controller)

    product_repo = ProductRepository()
    product_service = ProductService(product_repo)
    product_controller = ProductController(product_service)
    product_routes = create_product_routes(product_controller)

    app.register_blueprint(user_routes)
    app.register_blueprint(product_routes)

    return app
