from sqlalchemy import *

from src.used_all_over import db


class Items(db.Model):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=30), nullable=False, unique=True)
    price = Column(Integer(), nullable=False)
    barcode = Column(String(length=12), nullable=False, unique=True)
    description = Column(String(length=100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "'id': {0}, 'name': '{1}', 'price': {2}, 'barcode': '{3}', 'description': '{4}'" \
            .format(self.id, self.name, self.price, self.barcode, self.description)

    def assign_owner(self, user):
        self.user_id = user.id

    def unassign_owner(self):
        self.user_id = None

    @property
    def formatted_price(self):
        return "R${:,.2f}".format(self.price)
