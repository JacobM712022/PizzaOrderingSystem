from logic.menu import menu
from logic.promotions import apply_promotions

cart = []

def add_to_cart(item_id, qty):
    item = menu[item_id]

    # Base price
    base_price = item.price

    # Apply promotions (if any)
    final_price = apply_promotions(item, base_price)

    # Add to cart
    cart.append({
        "id": item_id,
        "name": item.name,
        "qty": qty,
        "price": final_price
    })