from app.database import db
from app.models.user import User


def register_user(data):
    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone")
    role = data.get("role")

    if not all([full_name, email, password, phone, role]):
        return {
            "success": False,
            "message": "All fields are required."
        }, 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return {
            "success": False,
            "message": "Email already exists."
        }, 409

    user = User(
        full_name=full_name,
        email=email,
        phone=phone,
        role=role
    )

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return {
        "success": True,
        "message": "User registered successfully.",
        "data": user.to_dict()
    }, 201