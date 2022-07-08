from flask import render_template

from app.products import products


@products.route('/products')
def list_products():
    return render_template('products/products.html')

