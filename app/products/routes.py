from flask import render_template, request, redirect, url_for, flash

from app import db
from app.products import products
from app.products.forms import AddProductForm, EditProductForm
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


@products.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    product = Products.query.filter_by(product_id=id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect('/products')

    # prod = db.session.query(Products).filter(Products.product_id==id).first()
    # print("PROD 2: ", prod)
    # print("PRODUCTO: ", product)
    # if request.method == 'POST':
    #     if product:
    #         db.session.delete(product)
    #         db.session.commit()
    #         return redirect('/products/list_products.html')
    # return render_template('products/list_products.html')


@products.route('/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    # product = Products.query.filter_by(product_id=id).first()
    product = Products.query.get(id)
    print("UPDATE PROD: ", product)

    product_form = EditProductForm(obj=product)
    product_form.populate_obj(product)

    if product_form.validate_on_submit():
        product.product_name = product_form.name.data
        product.product_description = product_form.description.data
        product.product_quantity = product_form.quantity.data
        product.product_price = product_form.price.data
        product.product_tag = product_form.tag.data

        print(f'name: {product.product_name} - descr: {product.product_description} - q: {product.product_quantity} - '
              f'price: {product.product_price} - tag: {product.product_tag}')
        #
        # product = Products(product_name=name, product_description=description, product_quantity=quantity,
        #                    product_price=price, product_tag=tag)


        # db.session.add(product)
        db.session.commit()

        flash("Changes saved")
        return redirect(url_for('products.list_products'))

    return render_template('products/edit_products.html', title="Editar producto", form=product_form)
