from flask import Blueprint


def create_user_routes(controller):
    user_bp = Blueprint("users", __name__)

    user_bp.route("/users", methods=["GET"])(controller.list_users)
    user_bp.route("/users", methods=["POST"])(controller.create_user)

    return user_bp
