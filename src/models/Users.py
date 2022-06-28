from flask_login import UserMixin
from sqlalchemy import *
from sqlalchemy.orm import *

from src.used_all_over import bcrypt, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email_address = Column(String(length=50), nullable=False, unique=True)
    password_hash = Column(String(length=60), nullable=False)
    budget = Column(Integer, nullable=False, default=1000)
    items = relationship('Items', backref='owner_user')

    def __repr__(self):
        return "'id': {0}, 'username': '{1}', 'email_address': {2}, 'password_hash': '{3}', 'budget': '{4}', " \
               "'items': '{5}'" \
            .format(self.id, self.username, self.email_address, self.password_hash, self.budget, self.items)

    @property
    def formatted_budget(self):
        return "R${:,.2f}".format(self.budget)

    @formatted_budget.setter
    def formatted_budget(self, value):
        self.budget = value

    def buy_item(self, item_price):
        self.budget -= item_price

    def sell_item(self, item):
        self.budget += item.price

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = bcrypt.generate_password_hash(value).decode('utf-8')
