from flask import Flask, render_template, request, redirect, url_for
from logic.menu import menu
from logic.cart import cart, add_to_cart
from logic.orders import checkout
from logic.promotions import active_promotions, apply_promotions

app = Flask(__name__)

app.jinja_env.globals.update(apply_promotions=apply_promotions)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/menu")
def show_menu():
    return render_template(
        "menu.html",
        menu=menu,
        promotions=active_promotions()
    )

@app.route("/add_to_cart", methods=["POST"])
def add_item():
    item_id = int(request.form["item_id"])
    qty = int(request.form["qty"])
    add_to_cart(item_id, qty)
    return redirect(url_for("show_cart"))

@app.route("/cart")
def show_cart():
    return render_template("cart.html", cart=cart)

@app.route("/checkout", methods=["GET", "POST"])
def checkout_page():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        card = request.form["card"]
        order = checkout(name, address, card)
        return render_template("confirmation.html", order=order)
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)