from flask import Blueprint


def create_product_routes(controller):
    product_bp = Blueprint("product", __name__)

    product_bp.route("/products", methods=["GET"])(controller.list_products)
    product_bp.route("/products", methods=["POST"])(controller.create_product)

    return product_bp
