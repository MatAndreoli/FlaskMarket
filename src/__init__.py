from flask import Flask, render_template, redirect, url_for, flash, request, Request

from .constants import SECRET_KEY, PORT, HOST
from .models.Items import Items
from .models.Users import Users
from .used_all_over import init_login_manager, update_db, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'

db.init_app(app)
init_login_manager(app)

with app.app_context():
    db.create_all()

from .router import market_routes, users_routes, main_routes, utils_processor
