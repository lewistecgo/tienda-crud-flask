from flask import render_template

from app import db
from app.products import products
from app.products.forms import AddProductForm
from models import Products


@products.route('/products')
def list_products():
    productos = Products.get_by_id(1)
    print(productos)
    list_prod = Products.query.all()
    size_prod = range(0, len(list_prod))
    print(size_prod)
    pair_prod = zip(list_prod, size_prod)

    return render_template('products/list_products.html', pair_prod=pair_prod)


@products.route('/add_products', methods=['POST', 'GET'])
def add_products():
    products_form = AddProductForm()
    if products_form.validate_on_submit():
        name = products_form.name.data
        description = products_form.description.data
        quantity = products_form.quantity.data
        price = products_form.price.data
        tag = products_form.tag.data

        new_product = Products(product_name=name, product_description=description, product_quantity=quantity,
                               product_price=price, product_tag=tag)
        db.session.add(new_product)
        db.session.commit()

    return render_template('products/add_products.html', title="Agregar producto", form=products_form)
