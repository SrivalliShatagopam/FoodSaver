from flask import Blueprint, request, jsonify

from app.services.auth_service import register_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    response, status_code = register_user(data)

    return jsonify(response), status_code