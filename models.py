from app import db


class Products(db.Model):
    __tablename__ = 'table_products'
    product_id = db.Column(db.Integer, nullable=False, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_description = db.Column(db.String(100))
    product_quantity = db.Column(db.Integer)
    product_price = db.Column(db.Float)
    product_tag = db.Column(db.String(50))

    def __repr__(self):
        return f"Products('{self.product_name}', '{self.product_description}', '{self.product_price}', '{self.product_quantity}', '{self.product_tag}') "
