from datetime import datetime
from cart import cart
from promotions import apply_promotions

orders = []

class Order:
    def __init__(self, order_id, user, items, total):
        self.id = order_id
        self.user = user
        self.items = items
        self.total = total
        self.timestamp = datetime.now()

def checkout():
    if not cart:
        print("Cart is empty.")
        return

    name = input("Full Name: ")
    address = input("Address: ")
    card = input("Card Number (simulated): ")

    total = 0
    for entry in cart.values():
        item = entry["item"]
        qty = entry["quantity"]
        base = item.price

        if item.category == "pizza":
            if entry["custom"]["size"] == "large":
                base += 2
            if entry["custom"]["crust"] == "stuffed":
                base += 2
            base += 0.75 * len(entry["custom"]["toppings"])

        final_price = apply_promotions(item, base)
        total += final_price * qty

    order = Order(len(orders) + 1, name, cart.copy(), total)
    orders.append(order)

    print(f"\nOrder placed! Total: ${total:.2f}")
    cart.clear()