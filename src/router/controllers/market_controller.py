from src.used_all_over import update_db
from ... import Request, render_template, flash, redirect, url_for
from ...constants import POST, GET, SUCCESS, ERROR
from ...models.Items import Items
from ...models.forms.ItemAcionsForm import PurchaseItemForm, SellItemForm
from ...usecases.users_uc import can_buy_item, user_buy_item, user_sell_item


def market_controller(request: Request, current_user):
    purchase_item_form = PurchaseItemForm()
    sell_item_form = SellItemForm()
    if request.method == GET:
        no_owned_items = Items.query.filter(Items.user_id == None).all()
        current_user_items = current_user.items
        return render_template('components/market.html',
                               items=no_owned_items,
                               purchaseItemForm=purchase_item_form,
                               sellItemForm=sell_item_form,
                               current_user_items=current_user_items)

    if request.method == POST:
        if purchase_item_form.validate_on_submit():
            item_id = request.form.get('purchased_item')
            p_item_ob = Items.query.filter(Items.id == item_id).first()
            if p_item_ob:
                if can_buy_item(current_user.budget, p_item_ob.price):
                    user_buy_item(current_user, p_item_ob)
                    update_db()
                    flash(f"Congrats! You've purchased {p_item_ob.name}. You have R${current_user.budget} left.",
                          SUCCESS)
                else:
                    flash("You don't have enough to buy this item. :(", ERROR)

        if sell_item_form.validate_on_submit():
            sold_item_id = request.form.get('sold_item')
            s_item_ob = Items.query.filter(Items.id == sold_item_id).first()
            if s_item_ob:
                user_sell_item(current_user, s_item_ob)
                update_db()
                flash(f"You've sold {s_item_ob.name}. You got R${s_item_ob.price} back.", SUCCESS)
        return redirect(url_for('market_page'))
