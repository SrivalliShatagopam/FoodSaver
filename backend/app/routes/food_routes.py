from flask import Blueprint, jsonify, request

from app.services.food_service import add_food

food_bp = Blueprint("food", __name__)


@food_bp.route("/", methods=["POST"])
def create_food():
    data = request.get_json()

    response, status_code = add_food(data)

    return jsonify(response), status_code