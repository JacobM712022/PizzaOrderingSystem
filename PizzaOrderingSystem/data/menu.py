class MenuItem:
    def __init__(self, item_id, name, description, category, price):
        self.id = item_id
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.active = True

menu = {
    1: MenuItem(1, "Cheese Pizza", "Three-cheese blend", "pizza", 10.99),
    2: MenuItem(2, "Margherita Pizza", "Tomato, mozzarella, basil", "pizza", 11.99),
    3: MenuItem(3, "Pepperoni Pizza", "Pepperoni and cheese", "pizza", 12.49),
    4: MenuItem(4, "Soft Drink", "Assorted flavors", "drinks", 2.49)
}

def view_menu():
    print("\n=== MENU ===")
    for item in menu.values():
        if item.active:
            print(f"{item.id}. {item.name} - ${item.price:.2f}")
            print(f"   {item.description}")