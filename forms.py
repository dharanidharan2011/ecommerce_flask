from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CheckoutForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=200)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=50)])
    zip_code = StringField('ZIP Code', validators=[DataRequired(), Length(min=5, max=10)])
    submit = SubmitField('Proceed to Payment')