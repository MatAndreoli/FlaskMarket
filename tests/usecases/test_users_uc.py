import pytest

from src.usecases.users_uc import user_sell_item, user_buy_item, check_password, can_buy_item, bcrypt


class TestUsersUC():

    def setup(self):
        print('setup123')

    @pytest.mark.parametrize('password', ['123', '456', '789'])
    def test_check_password(self, password):
        password_hash = bcrypt.generate_password_hash(password)
        assert check_password(password_hash, password)

    def test_can_buy_item(self, get_user, get_item_price_less_than_a_thousand):
        u = get_user()
        i = get_item_price_less_than_a_thousand()
        assert can_buy_item(u.budget, i.price) is True

    def test_cannot_buy_item(self, get_user, get_item_price_more_than_a_thousand):
        u = get_user()
        i = get_item_price_more_than_a_thousand()
        assert can_buy_item(u.budget, i.price) is False

    def test_user_sell_item(self, get_user, get_item):
        u = get_user()

        i = get_item()

        u.items.append(i)
        initial_budget = u.budget
        user_sell_item(u, i)

        assert i.user_id is None
        assert u.budget == initial_budget + i.price

    def test_user_buy_item(self, get_user, get_item):
        u = get_user()

        i = get_item()

        initial_budget = u.budget
        user_buy_item(u, i)

        assert i.user_id is u.id
        assert u.budget == initial_budget - i.price
