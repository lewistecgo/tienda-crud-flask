from flask import render_template

from app.products import products


@products.route('/products')
def list_products():
    return render_template('products/list_products.html')


@products.route('/add_products')
def add_products():
    return render_template('products/add_products.html')