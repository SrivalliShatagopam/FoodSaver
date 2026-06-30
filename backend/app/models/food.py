from datetime import datetime

from app.database import db


class Food(db.Model):
    __tablename__ = "foods"

    id = db.Column(db.Integer, primary_key=True)

    food_name = db.Column(db.String(120), nullable=False)

    quantity = db.Column(db.String(50), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    expiry_time = db.Column(db.DateTime, nullable=False)

    pickup_address = db.Column(db.String(255), nullable=False)

    description = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        default="Available"
    )

    donor_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "food_name": self.food_name,
            "quantity": self.quantity,
            "category": self.category,
            "expiry_time": self.expiry_time.isoformat(),
            "pickup_address": self.pickup_address,
            "description": self.description,
            "status": self.status,
            "donor_id": self.donor_id,
            "created_at": self.created_at.isoformat()
        }