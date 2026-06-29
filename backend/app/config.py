import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "foodsaver_secret_key"

    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'foodsaver.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False