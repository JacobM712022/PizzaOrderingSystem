import users
from logic.menu import menu, MenuItem
from logic.promotions import promotions, Promotion
from datetime import datetime

def manager_menu():
    print("DEBUG current_user =", users.current_user)
    if not users.current_user or users.current_user["role"] != "manager":
        print("Access denied. Manager login required.")
        return

    while True:
        print("\n=== MANAGER DASHBOARD ===")
        print("1. View Menu Items")
        print("2. Add Menu Item")
        print("3. Toggle Menu Item Active")
        print("4. View Promotions")
        print("5. Add Promotion")
        print("6. Toggle Promotion Active")
        print("7. Back to Main Menu")

        choice = input("Choice: ")

        if choice == "1":
            view_menu_items()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            toggle_menu_item()
        elif choice == "4":
            view_promotions()
        elif choice == "5":
            add_promotion()
        elif choice == "6":
            toggle_promotion()
        elif choice == "7":
            return
        else:
            print("Invalid choice.")


# ============================================================
# MENU MANAGEMENT (US‑10)
# ============================================================

def view_menu_items():
    print("\n=== MENU ITEMS ===")
    for item in menu.values():
        print(f"{item.id}. {item.name} - ${item.price:.2f} | Active={item.active}")
        print(f"   {item.description}")


def add_menu_item():
    print("\n=== ADD MENU ITEM ===")
    name = input("Name: ")
    desc = input("Description: ")
    category = input("Category: ")
    try:
        price = float(input("Price: "))
    except:
        print("Invalid price.")
        return

    new_id = max(menu.keys()) + 1
    menu[new_id] = MenuItem(new_id, name, desc, category, price)
    print("Menu item added.")


def toggle_menu_item():
    try:
        item_id = int(input("Enter item ID to toggle: "))
    except:
        print("Invalid input.")
        return

    if item_id not in menu:
        print("Item not found.")
        return

    menu[item_id].active = not menu[item_id].active
    print(f"{menu[item_id].name} active status is now {menu[item_id].active}")


# ============================================================
# PROMOTION MANAGEMENT (US‑11)
# ============================================================

def view_promotions():
    print("\n=== PROMOTIONS ===")
    for promo in promotions.values():
        print(f"{promo.id}. {promo.name} | Type={promo.type} | Value={promo.value} | Active={promo.active}")
        print(f"   Valid: {promo.start.date()} to {promo.end.date()}")


def add_promotion():
    print("\n=== ADD PROMOTION ===")
    name = input("Name: ")
    promo_type = input("Type (percent/fixed): ").lower()
    try:
        value = float(input("Value: "))
    except:
        print("Invalid value.")
        return

    try:
        start = datetime.fromisoformat(input("Start date (YYYY-MM-DD): "))
        end = datetime.fromisoformat(input("End date (YYYY-MM-DD): "))
    except:
        print("Invalid date format.")
        return

    new_id = max(promotions.keys()) + 1 if promotions else 1
    promotions[new_id] = Promotion(new_id, name, promo_type, value, start, end)
    print("Promotion added.")


def toggle_promotion():
    try:
        promo_id = int(input("Enter promotion ID to toggle: "))
    except:
        print("Invalid input.")
        return

    if promo_id not in promotions:
        print("Promotion not found.")
        return

    promotions[promo_id].active = not promotions[promo_id].active
    print(f"{promotions[promo_id].name} active status is now {promotions[promo_id].active}")