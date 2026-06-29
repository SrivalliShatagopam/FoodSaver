from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.database import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return {
            "message": "FoodSaver Backend Running Successfully 🚀"
        }

    return app