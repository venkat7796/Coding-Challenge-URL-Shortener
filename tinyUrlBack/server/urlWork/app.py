from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
import os

from flow.urlmap import blp as urlBluePrint
from db import db
def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "Tiny URL Feature"
    cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST"]}}, supports_credentials=True)
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["PROPOGATE_EXCEPTIONS"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app=app)

    api = Api(app=app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(urlBluePrint)

    return app
