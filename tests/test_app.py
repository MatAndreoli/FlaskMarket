from src.constants import SECRET_KEY


class TestApp:

    def test_app(self, get_app):
        assert get_app == 'src'

    def test_app_configs(self, get_app_configs):
        assert get_app_configs['SECRET_KEY'] == SECRET_KEY
