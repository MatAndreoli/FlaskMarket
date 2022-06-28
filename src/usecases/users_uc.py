from src.used_all_over import bcrypt
from ..models.Items import Items
from ..models.Users import Users


def check_password(password_hash, password_received):
    return bcrypt.check_password_hash(password_hash, password_received)


def can_buy_item(user_budget, item_price):
    return user_budget - item_price >= 0


def user_buy_item(current_user: Users, item: Items):
    item.assign_owner(current_user)
    current_user.buy_item(item.price)


def user_sell_item(current_user: Users, item: Items):
    if item in current_user.items:
        item.unassign_owner()
        current_user.sell_item(item)
