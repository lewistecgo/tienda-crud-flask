from flask import render_template

from app.products import products
from models import Products


@products.route('/products')
def list_products():
    productos = Products.get_by_id(1)
    print(productos)
    return render_template('products/list_products.html')


@products.route('/add_products')
def add_products():
    return render_template('products/add_products.html')
