from datetime import datetime

from app.database import db
from app.models.food import Food


def add_food(data):
    required_fields = [
        "food_name",
        "quantity",
        "category",
        "expiry_time",
        "pickup_address",
        "donor_id"
    ]

    for field in required_fields:
        if not data.get(field):
            return {
                "success": False,
                "message": f"{field} is required."
            }, 400

    try:
        expiry_time = datetime.fromisoformat(data["expiry_time"])
    except ValueError:
        return {
            "success": False,
            "message": "Invalid expiry_time format. Use YYYY-MM-DDTHH:MM:SS"
        }, 400

    food = Food(
        food_name=data["food_name"],
        quantity=data["quantity"],
        category=data["category"],
        expiry_time=expiry_time,
        pickup_address=data["pickup_address"],
        description=data.get("description", ""),
        donor_id=data["donor_id"]
    )

    db.session.add(food)
    db.session.commit()

    return {
        "success": True,
        "message": "Food donation added successfully.",
        "data": food.to_dict()
    }, 201