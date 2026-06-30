from flask import Blueprint, request, jsonify

from app.services.auth_service import register_user, login_user
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from app.models.user import User
from flask import jsonify
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    response, status_code = register_user(data)

    return jsonify(response), status_code
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    response, status_code = login_user(data)

    return jsonify(response), status_code
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()

    user = User.query.get(int(user_id))

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    return jsonify({
        "success": True,
        "user": user.to_dict()
    }), 200