from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    print("config name: ", config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.home import home
    from app.products import products

    # Routes
    app.register_blueprint(home)
    app.register_blueprint(products)

    # db
    db.init_app(app)

    return app
