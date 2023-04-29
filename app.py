from flask import Flask, jsonify
from routes import routesCodigo
from config import app_config, app_active
from Controllers.consultaController import ConsultaController

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(routesCodigo)

    return app