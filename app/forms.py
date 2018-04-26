from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange
from wtforms.fields.html5 import DecimalRangeField

class DatabaseQueryForm(FlaskForm):
    movie = StringField('Movie')
    tag = StringField('Tag')
    min_rating = DecimalField('Min_Rating', places=1)
    max_rating = DecimalField('Max_Rating', places=1)
    rating_slider = DecimalRangeField('Rating', [NumberRange(min=1, max=100)])
    submit = SubmitField('Submit')



