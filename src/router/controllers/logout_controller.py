from ... import redirect, url_for, flash
from flask_login import logout_user

from src.constants import INFO


def logout_controller():
    logout_user()
    flash("Logged out.", INFO)
    return redirect(url_for('home_page'))
