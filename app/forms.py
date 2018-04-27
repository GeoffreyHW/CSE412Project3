from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange
from wtforms.fields.html5 import DecimalRangeField

class DatabaseQueryForm(FlaskForm):
    movie = StringField('Movie')
    tag = StringField('Tag')
    submit = SubmitField('Submit')



