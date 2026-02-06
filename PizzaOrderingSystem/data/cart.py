from menu import menu
from promotions import apply_promotions

cart = {}

def add_to_cart():
    print("\n=== ADD TO CART ===")
    try:
        item_id = int(input("Item ID: "))
        if item_id not in menu:
            print("Invalid item.")
            return
    except:
        print("Invalid input.")
        return

    qty = int(input("Quantity: "))

    custom = {}
    if menu[item_id].category == "pizza":
        size = input("Size (small/medium/large): ")
        crust = input("Crust (regular/stuffed): ")
        toppings = input("Toppings (comma separated): ").split(",")

        custom = {
            "size": size,
            "crust": crust,
            "toppings": [t.strip() for t in toppings if t.strip()]
        }

    key = f"{item_id}-{str(custom)}"
    if key in cart:
        cart[key]["quantity"] += qty
    else:
        cart[key] = {"item": menu[item_id], "quantity": qty, "custom": custom}

    print("Added to cart.")

def view_cart():
    print("\n=== CART ===")
    if not cart:
        print("Cart is empty.")
        return

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
        line_total = final_price * qty
        total += line_total

        print(f"{item.name} x{qty} - ${line_total:.2f}")

    print(f"\nTOTAL: ${total:.2f}")