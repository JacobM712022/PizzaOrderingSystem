from users import register, login, logout, current_user
from menu import view_menu
from cart import add_to_cart, view_cart, cart
from orders import checkout
from promotions import active_promotions
from manager import manager_menu

def main_menu():
    while True:
        print("\n=== PIZZA ORDERING SYSTEM ===")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Register")
        print("6. Login")
        print("7. Logout")
        print("8. Manager Dashboard")
        print("9. Exit")

        choice = input("Choice: ")

        if choice == "1":
            view_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            register()
        elif choice == "6":
            login()
        elif choice == "7":
            logout()
        elif choice == "8":
            manager_menu()
        elif choice == "9":
            print("Goodbye.")
            break

if __name__ == "__main__":
    main_menu()