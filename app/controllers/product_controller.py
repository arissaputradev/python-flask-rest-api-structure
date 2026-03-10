from flask import jsonify, request


class ProductController:
    def __init__(self, service):
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
