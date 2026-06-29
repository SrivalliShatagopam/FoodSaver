from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.database import db

from app.routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)
    jwt = JWTManager(app)
    CORS(app)

    db.init_app(app)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    with app.app_context():
        from app.models.user import User
        db.create_all()

    @app.route("/")
    def home():
        return {
            "message": "FoodSaver Backend Running Successfully 🚀"
        }

    return app