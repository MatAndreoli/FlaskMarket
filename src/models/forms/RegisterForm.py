from flask_wtf import FlaskForm
from wtforms import *

from src.models.Users import Users


class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[validators.Length(min=2, max=30), validators.DataRequired()])
    email_address = StringField(label='Email', validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField(label='Password', validators=[validators.Length(min=6), validators.DataRequired()])
    password2 = PasswordField(label='Confirm Password',
                              validators=[validators.EqualTo('password'), validators.DataRequired()])
    submit = SubmitField(label='Create account')

    def validate_username(self, username):
        for user in Users.query.filter(Users.username == username.data):
            if user:
                raise ValidationError("Username already taken! Try a different one.")

    def validate_email_address(self, email_address):
        for user in Users.query.filter(Users.email_address == email_address.data):
            if user:
                raise ValidationError("Email already taken! Try a different one.")
