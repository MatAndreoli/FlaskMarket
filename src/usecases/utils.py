def budget_left_if_purchase_uc(user_budget, item_price=0):
    return '{:,.2f}'.format(user_budget - item_price)


def total_budget_if_sell_uc(user_budget, item_price=0):
    return '{:,.2f}'.format(user_budget + item_price)
