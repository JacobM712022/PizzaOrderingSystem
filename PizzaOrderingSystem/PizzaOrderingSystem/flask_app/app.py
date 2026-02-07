from flask import Flask, render_template, request, redirect, url_for, session
from logic.menu import menu, MenuItem
from logic.cart import cart, add_to_cart
from logic.orders import checkout
from logic.promotions import active_promotions, apply_promotions
from datetime import datetime

users = {}   # temporary in‑memory user storage

app = Flask(__name__)
app.secret_key = "supersecretkey123"   # Needed for login sessions

app.jinja_env.globals.update(apply_promotions=apply_promotions)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/promotions")
def show_promotions():
    return '<h1><a href="/" style="text-decoration:none; color:inherit;">Promotions Page Coming Soon</a></h1>'

@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("home"))

        return "Invalid username or password!"

    return render_template("login.html")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login_page"))
    return render_template("profile.html", user=session["user"])

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if request.method == "POST":
        # update user fields here
        # save to database
        return redirect("/profile")

    username = session.get("user")
    user = users.get(username)
    return render_template("edit_profile.html", user=user)

@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    user = users.get(username)

    if request.method == "POST":
        current = request.form["current_password"]
        new = request.form["new_password"]
        confirm = request.form["confirm_password"]

        # Check current password
        if user.password != current:
            return "Incorrect current password"

        # Check new passwords match
        if new != confirm:
            return "New passwords do not match"

        # Update password
        user.password = new
        return redirect("/profile")

    return render_template("change_password.html", user=user)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "Username already exists!"

        users[username] = password
        return redirect(url_for("login_page"))

    return render_template("create_account.html")

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Hardcoded admin credentials for now
        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect("/admin_dashboard")

        return "Invalid admin credentials"

    return render_template("admin_login.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/admin")
    return render_template("admin_dashboard.html")

@app.route("/manage_menu")
def manage_menu():
    if not session.get("admin"):
        return redirect("/admin")

    return render_template("admin_manage_menu.html", menu_items=menu)

@app.route("/admin/add_item", methods=["GET", "POST"])
def add_item():
    if not session.get("admin"):
        return redirect("/admin")

    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        price = float(request.form["price"])
        active = request.form["active"] == "yes"

        # Generate new ID
        new_id = max(menu.keys()) + 1 if menu else 1

        # Create new MenuItem object
        new_item = MenuItem(
            item_id=new_id,
            name=name,
            description="No description provided",
            category=category,
            price=price
        )
        new_item.active = active

        # Add to dictionary
        menu[new_id] = new_item

        return redirect("/manage_menu")

    return render_template("admin_add_item.html")

@app.route("/admin/edit_item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    if not session.get("admin"):
        return redirect("/admin")

    item = menu.get(item_id)
    if not item:
        return "Item not found"

    if request.method == "POST":
        item.name = request.form["name"]
        item.description = request.form["description"]
        item.category = request.form["category"]
        item.price = float(request.form["price"])
        item.active = request.form["active"] == "yes"

        return redirect("/manage_menu")

    return render_template("admin_edit_item.html", item=item)

@app.route("/admin/delete_item/<int:item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    if not session.get("admin"):
        return redirect("/admin")

    item = menu.get(item_id)
    if not item:
        return "Item not found"

    # If user confirms deletion
    if request.method == "POST":
        menu.pop(item_id, None)
        return redirect("/manage_menu")

    # Show confirmation page
    return render_template("admin_delete_item.html", item=item)

@app.route("/menu")
def show_menu():
    return render_template(
        "menu.html",
        menu=menu,
        promotions=active_promotions()
    )

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart_route():
    item_id = int(request.form["item_id"])
    qty = int(request.form["qty"])
    size = request.form.get("size", "medium") # default to medium
    
    add_to_cart(item_id, qty, size)
    return redirect(url_for("show_cart"))

@app.route("/cart")
def show_cart():
    return render_template("cart.html", cart=cart)

@app.route("/update_cart", methods=["POST"])
def update_cart():
    item_id = int(request.form["id"])
    new_qty = int(request.form["qty"])
    new_size = request.form.get("size")

    # Update the cart entry
    for entry in cart:
        if entry["id"] == item_id:
            entry["qty"] = new_qty
            entry["size"] = new_size

            # Recalculate price based on size
            base_price = menu[item_id].price
            if new_size == "medium":
                base_price += 1
            elif new_size == "large":
                base_price += 2

            # Apply promotions again
            entry["price"] = apply_promotions(menu[item_id], base_price)

    return redirect(url_for("show_cart"))

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    item_id = int(request.form["id"])

    # Remove the matching item
    for entry in cart[:]:  # iterate over a copy so removal is safe
        if entry["id"] == item_id:
            cart.remove(entry)
            break

    return redirect(url_for("show_cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout_page():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]

        # Secure card handling
        full_card = request.form["card"]
        last4 = full_card[-4:]

        exp = request.form.get("exp")
        cvv = request.form.get("cvv")

        if not cvv.isdigit() or len(cvv) not in (3, 4):
            return "Invalid CVV"

        # Calculate total
        total = sum(entry["price"] * entry["qty"] for entry in cart)

        # Generate confirmation number
        confirmation_number = int(datetime.now().timestamp())

        # Build order dictionary
        order = {
            "id": confirmation_number,
            "name": name,
            "address": address,
            "last4": last4,
            "exp": exp,
            "timestamp": datetime.now(),
            "total": total
        }

        return render_template("confirmation.html", order=order)

    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)