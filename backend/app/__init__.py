from flask import Flask
from flask_cors import CORS

from backend.app.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)

    CORS(app, supports_credentials=True)

    return app
