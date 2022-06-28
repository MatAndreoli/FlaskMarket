import pytest
from src import app
from src.models.Items import Items
from src.models.Users import Users


@pytest.fixture()
def get_app():
    return app.name


@pytest.fixture()
def get_app_configs():
    return app.config


@pytest.fixture(scope="function")
def get_user():
    def create():
        u = Users()
        u.id = 1
        u.username = 'math'
        u.budget = 1000
        u.password_hash = 'kd94ifakf04r'
        u.email_address = 'fskf@fkajf.com'

        return u

    return create


@pytest.fixture(scope="function")
def get_item():
    def create():
        i = Items()
        i.id = 1
        i.price = 3
        i.name = 'fd'
        i.description = 'kfjkafjidjfiafi'
        i.barcode = 'fjf90rifiafi'
        i.user_id = 1

        return i

    return create


@pytest.fixture(scope="function")
def get_item_price_less_than_a_thousand():
    def create():
        i = Items()
        i.id = 1
        i.price = 999
        i.name = 'fd'
        i.description = 'kfjkafjidjfiafi'
        i.barcode = 'fjf90rifiafi'
        i.user_id = 1

        return i

    return create


@pytest.fixture(scope="function")
def get_item_price_more_than_a_thousand():
    def create():
        i = Items()
        i.id = 1
        i.price = 1001
        i.name = 'fd'
        i.description = 'kfjkafjidjfiafi'
        i.barcode = 'fjf90rifiafi'
        i.user_id = 1

        return i

    return create
