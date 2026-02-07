from datetime import datetime
from logic.cart import cart
from logic.promotions import apply_promotions

orders = []

class Order:
    def __init__(self, order_id, name, address, card, items, total):
        self.id = order_id
        self.name = name
        self.address = address
        self.card = card[-4:]
        self.items = items
        self.total = total
        self.timestamp = datetime.now()

def checkout(name, address, card):
    if not cart:
        return 0  # nothing to checkout

    total = 0
    for item in cart:
        total += item["price"] * item["qty"]

    # Create order record
    order = Order(
        order_id=len(orders) + 1,
        name=name,
        address=address,
        card=card,
        items=cart.copy(),
        total=total
    )
    orders.append(order)
    cart.clear()

    return order