from flask import jsonify, request


class UserController:
    def __init__(self, service):
        self.service = service

    def create_user(self):

        try:
            data = request.json

            user = self.service.create_user(data.get("name"), data.get("email"))

            return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def list_users(self):

        users = self.service.list_users()

        return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
