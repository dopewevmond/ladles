from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import DishCategory

def category_query():
    return DishCategory.query

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PostDishForm(FlaskForm):
    name = StringField('Name of dish', validators=[DataRequired()])
    price = IntegerField('Price of dish', validators=[DataRequired()])
    image = StringField('Enter a link to an image', validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    category = QuerySelectField(label='Select dish category', query_factory=category_query, allow_blank=True)
    submit = SubmitField('Upload dish')
    