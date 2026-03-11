from flask import jsonify, request

from app.services.user_service import UserService


class UserController:
    def __init__(self, service: UserService):
        self.service = service

    def create_user(self):

        try:
            data = request.json

            user = self.service.create_user(data.get("name"), data.get("email"))

            return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        except Exception as e:
            print("Unexpected error:", e)
            return jsonify({"error": "Internal server error"}), 500

    def list_users(self):
        # users = self.service.list_users()
        # return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
        try:
            page = request.args.get("page", 1, type=int)
            limit = request.args.get("limit", 10, type=int)
            email = request.args.get("email")
            sort = request.args.get("sort")
            search = request.args.get("search")

            result = self.service.list_users(page, limit, email, sort, search)

            return jsonify(result)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_user(self, user_id):
        try:
            user = self.service.get_user(user_id)

            return jsonify({"id": user.id, "name": user.name, "email": user.email})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    def update_user(self, user_id):
        try:
            data = request.json
            user = self.service.update_user(user_id, data)

            return jsonify({"id": user.id, "name": user.name, "email": user.email})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            print("Unexpected error:", e)
            return jsonify({"error": "Internal server error"}), 500

    def delete_user(self, user_id):
        try:
            user = self.service.delete_user(user_id)

            return jsonify({"message": f"User {user.name} has been deleted"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            print("Unexpected error:", e)
            return jsonify({"error": "Internal server error"}), 500
