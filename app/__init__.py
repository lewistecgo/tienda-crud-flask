from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.home import home
    from app.products import products

    # Routes
    app.register_blueprint(home)
    app.register_blueprint(products)

    return app
