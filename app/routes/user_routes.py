from flask import Blueprint

from app.controllers.user_controller import UserController


def create_user_routes(service):
    user_bp = Blueprint("users", __name__)

    controller = UserController(service)

    user_bp.route("/users", methods=["GET"])(controller.list_users)
    user_bp.route("/users", methods=["POST"])(controller.create_user)

    return user_bp
