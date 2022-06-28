from src import app

from ..usecases.utils import budget_left_if_purchase_uc, total_budget_if_sell_uc


@app.context_processor
def utility_processor():
    def format_price_purchase(user_budget, item_price=0):
        return budget_left_if_purchase_uc(user_budget, item_price)

    def format_price_sell(user_budget, item_price=0):
        return total_budget_if_sell_uc(user_budget, item_price)

    return dict(format_price_purchase=format_price_purchase, format_price_sell=format_price_sell)
