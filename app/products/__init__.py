from flask import Blueprint

products = Blueprint('products', __name__, url_prefix='/', template_folder='templates', static_folder='static')

from . import routes
