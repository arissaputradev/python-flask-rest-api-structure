from flask import jsonify, request

from app.services.product_service import ProductService


class ProductController:
    def __init__(self, service: ProductService):
        self.service = service

    def create_product(self):
        try:
            data = request.json
            product = self.service.create_product(data.get("name"), data.get("price"))
            # product = self.service.create_product(data["name"], data["price"])

            return jsonify(
                {"id": product.id, "name": product.name, "price": product.price}
            ), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        except Exception as e:
            print("Unexpected error:", e)
            return jsonify({"error": "Internal server error"}), 500

    def list_products(self):
        products = self.service.list_products()

        return jsonify(
            [{"id": p.id, "name": p.name, "price": p.price} for p in products]
        )

    def get_product(self, product_id):
        try:
            product = self.service.get_product(product_id)
            print("type", type(product))
            return jsonify(
                {"id": product.id, "name": product.name, "price": product.price}
            )
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def update_product(self, product_id):
        try:
            data = request.json
            product = self.service.update_product(product_id, data)

            return jsonify(
                {"id": product.id, "name": product.name, "price": product.price}
            )
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            print("Unexpected error:", e)
            return jsonify({"error": "Internal server error"}), 500

    def delete_product(self, product_id):
        try:
            product = self.service.delete_product(product_id)
            return jsonify({"message": f"Product {product.name} has been deleted"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            print("Unexpected error:", e)
            return jsonify({"error": "Internal server error"}), 500
