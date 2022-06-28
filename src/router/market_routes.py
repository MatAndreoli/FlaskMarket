from .. import request
from flask_login import login_required, current_user

from src import app
from .controllers.market_controller import market_controller
from ..constants import GET, POST


@app.route('/market', methods=[GET, POST])
@login_required
def market_page():
    return market_controller(request, current_user)
