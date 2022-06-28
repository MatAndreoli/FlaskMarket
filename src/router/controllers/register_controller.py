from ... import render_template, redirect, url_for, flash
from flask_login import login_user

from src.constants import POST, SUCCESS, ERROR
from ...models import Users
from ...models.forms import RegisterForm
from ...used_all_over import insert_into_db


def register_controller(request):
    register_form = RegisterForm()
    if request.method == POST:
        if register_form.validate_on_submit():
            user_created = Users(username=register_form.username.data, email_address=register_form.email_address.data,
                                 password=register_form.password.data)
            try:
                insert_into_db(user_created)
                flash(f'Account created successfully! You\'re logged in as "{user_created.username}".', SUCCESS)
                login_user(user_created)
                return redirect(url_for('market_page'))
            except Exception as error:
                print(error)
    if register_form.errors != {}:
        for err_msg in register_form.errors:
            for err in register_form.errors[err_msg]:
                flash(err, ERROR)
    return render_template('components/register.html', form=register_form)
