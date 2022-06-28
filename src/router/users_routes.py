from .. import request

from src import app
from src.constants import GET, POST
from .controllers.login_controller import login_controller
from .controllers.logout_controller import logout_controller
from .controllers.register_controller import register_controller


@app.route('/register', methods=[GET, POST])
def register_page():
    return register_controller(request)


@app.route('/login', methods=[GET, POST])
def login_page():
    return login_controller(request)


@app.route('/logout')
def logout_page():
    return logout_controller()
