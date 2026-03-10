from flask import Blueprint


def create_product_routes(controller):
    product_bp = Blueprint("product", __name__)

    product_bp.route("/products", methods=["GET"])(controller.list_products)
    product_bp.route("/products", methods=["POST"])(controller.create_product)
    product_bp.route("/products/<int:product_id>", methods=["GET"])(
        controller.get_product
    )
    product_bp.route("/products/<int:product_id>", methods=["PUT"])(
        controller.update_product
    )
    product_bp.route("/products/<int:product_id>", methods=["DELETE"])(
        controller.delete_product
    )

    return product_bp
