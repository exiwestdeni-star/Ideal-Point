from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

def minus_price(price):
    return price - random.randint(2000, 3000)

@app.route("/products")
def products():
    products = []

    # iPhone 16 / 17
    iphones = [
        ("iPhone 16 256GB", 109900),
        ("iPhone 16 Pro 256GB", 129900),
        ("iPhone 16 Pro Max 256GB", 149900),
        ("iPhone 17 256GB", 119900),
        ("iPhone 17 Pro 256GB", 139900),
        ("iPhone 17 Pro Max 256GB", 159900),
    ]

    # Mac
    mac = [
        ("MacBook Air M3", 119900),
        ("MacBook Pro M3", 159900),
    ]

    # iPad
    ipad = [
        ("iPad 10", 59900),
        ("iPad Pro M2", 109900),
    ]

    # AirPods
    airpods = [
        ("AirPods 2", 13900),
        ("AirPods Pro 2", 20900),
    ]

    # PlayStation
    ps = [
        ("PlayStation 5", 64900),
        ("DualSense Controller", 7900),
    ]

    all_data = [
        (iphones, "iphone"),
        (mac, "mac"),
        (ipad, "ipad"),
        (airpods, "airpods"),
        (ps, "ps")
    ]

    for group, category in all_data:
        for name, price in group:
            products.append({
                "name": name,
                "price": minus_price(price),
                "image": "https://via.placeholder.com/200",
                "category": category
            })

    return jsonify(products)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
