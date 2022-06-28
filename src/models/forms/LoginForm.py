from flask_wtf import FlaskForm
from wtforms import *

from src.models.Users import Users


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.DataRequired()])
    submit = SubmitField(label='Sign in')
