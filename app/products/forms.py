from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length


class AddProductForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    description = StringField('Descripción', validators=[DataRequired(), Length(max=64)])
    quantity = IntegerField('Cantidad', validators=[DataRequired()])
    price = FloatField('Precio', validators=[DataRequired()])
    tag = StringField('Etiqueta', validators=[DataRequired()])

    submit = SubmitField("Agregar producto")
