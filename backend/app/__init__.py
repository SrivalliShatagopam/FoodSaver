from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.database import db

from app.routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
from app.routes.food_routes import food_bp
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)
    jwt = JWTManager(app)
    CORS(app)

    db.init_app(app)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(food_bp, url_prefix="/api/foods")
    with app.app_context():
        from app.models.user import User
        from app.models.food import Food
        db.create_all()

    @app.route("/")
    def home():
        return {
            "message": "FoodSaver Backend Running Successfully 🚀"
        }

    return app