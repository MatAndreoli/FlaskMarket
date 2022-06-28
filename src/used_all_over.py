from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .constants import INFO

db = SQLAlchemy()

bcrypt = Bcrypt()
login_manager = LoginManager()


def insert_into_db(data):
    db.session.add(data)
    db.session.commit()


def update_db():
    db.session.commit()


def init_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = 'login_page'
    login_manager.login_message_category = INFO
