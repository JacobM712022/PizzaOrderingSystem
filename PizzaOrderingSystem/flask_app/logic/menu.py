class MenuItem:
    def __init__(self, item_id, name, description, category, price):
        self.id = item_id
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.active = True

menu = {
    1: MenuItem(1, "Cheese Pizza", "Our signature three-cheese blend", "pizza", 10.99),
    2: MenuItem(2, "Pepperoni Pizza", "Pepperoni and cheese", "pizza", 11.49),
    3: MenuItem(3, "Margherita Pizza", "Tomato, mozzarella, basil", "pizza", 12.99),
    4: MenuItem(4, "Sausage Pizza", "Ground pork sausage and cheese", "pizza", 11.69),
    5: MenuItem(5, "Veggie Pizza", "Green bell pepper, diced onion, tomato, cheese", "pizza", 12.79),
    6: MenuItem(6, "Meat Lover's Pizza", "Pepperoni, sausage, bacon, ground beef", "pizza", 14.29),
    7: MenuItem(7, "BBQ Chicken Pizza", "Grilled chicken, diced onion, mozzarella, and honey BBQ sauce", "pizza", 13.79),
    8: MenuItem(8, "Hawaiian Pizza", "Ham, pineapple, and mozzarella", "pizza", 12.99),
    9: MenuItem(9, "Garlic Butter Breadsticks", "6 traditional breadsticks brushed with our signature garlic butter glaze", "sides", 5.99),
    10: MenuItem(10, "Cheesy Bread", "Golden crust with melty cheese", "sides", 5.49),
    11: MenuItem(11, "Chocolate Chip Cookie", "Warm, double chocolate chip cookie", "dessert", 6.99),
    12: MenuItem(12, "Soft Drink", "Assorted Pepsi products", "drinks", 2.49),
    13: MenuItem(13, "Fire-Your-Fave Pizza", "You tell us how you want it", "pizza", 9.99)
    
}

def view_menu():
    print("\n=== MENU ===")
    for item in menu.values():
        if item.active:
            print(f"{item.id}. {item.name} - ${item.price:.2f}")
            print(f"   {item.description}")