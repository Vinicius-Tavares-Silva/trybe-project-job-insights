from flask import Flask
from . import routes_and_views

# Iiniciando Projeto


def create_app() -> Flask:
    app = Flask(__name__)
    routes_and_views.init_app(app)

    return app
