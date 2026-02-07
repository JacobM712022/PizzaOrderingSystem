from logic.menu import menu
from logic.promotions import apply_promotions

cart = []

def add_to_cart(item_id, qty, size):
    item = menu[item_id]

    # Base price
    base_price = item.price

    # ⭐ Adjust price based on size
    if size == "medium":
        base_price += 1
    elif size == "large":
        base_price += 2

    # Apply promotions (if any)
    final_price = apply_promotions(item, base_price)

    # Add to cart
    cart.append({
        "id": item_id,
        "name": item.name,
        "qty": qty,
        "size": size,
        "price": final_price
    })