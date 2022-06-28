from ... import render_template, redirect, url_for, flash
from flask_login import login_user

from src.constants import SUCCESS, ERROR, WARNING
from ...models import Users
from ...models.forms import LoginForm
from ...usecases.users_uc import check_password


def login_controller(request):
    form = LoginForm()
    if form.validate_on_submit():
        user_found = Users.query.filter(Users.username == form.username.data).first()
        if user_found and check_password(user_found.password_hash, form.password.data):
            login_user(user_found)
            flash(f'You\'re logged in as: {user_found.username}', SUCCESS)
            return redirect(url_for('market_page'))
        elif not user_found:
            flash('User was\'t found on database.', WARNING)
        else:
            flash('Username and/or password are incorrect!', ERROR)
    return render_template('components/login.html', form=form)
