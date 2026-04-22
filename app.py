from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

def price(base):
    return base - random.randint(2000,3000)

@app.route("/products")
def products():
    data = []

    # iPhone 16 / 17
    iphones = [
        ("iPhone 16 256GB", 109900),
        ("iPhone 16 Pro 256GB", 129900),
        ("iPhone 16 Pro Max 256GB", 149900),
        ("iPhone 17 256GB", 119900),
        ("iPhone 17 Pro 256GB", 139900),
        ("iPhone 17 Pro Max 256GB", 159900),
    ]

    for name, p in iphones:
        data.append({
            "name": name,
            "price": price(p),
            "image": "https://via.placeholder.com/200",
            "category": "iphone"
        })

    # MacBook
    macs = [
        ("MacBook Air M3", 119900),
        ("MacBook Pro M3", 159900),
    ]

    for name, p in macs:
        data.append({
            "name": name,
            "price": price(p),
            "image": "https://via.placeholder.com/200",
            "category": "mac"
        })

    # iPad
    ipads = [
        ("iPad 10", 59900),
        ("iPad Pro M2", 109900),
    ]

    for name, p in ipads:
        data.append({
            "name": name,
            "price": price(p),
            "image": "https://via.placeholder.com/200",
            "category": "ipad"
        })

    # AirPods
    airpods = [
        ("AirPods 2", 13900),
        ("AirPods Pro 2", 20900),
    ]

    for name, p in airpods:
        data.append({
            "name": name,
            "price": price(p),
            "image": "https://via.placeholder.com/200",
            "category": "airpods"
        })

    # PlayStation
    ps = [
        ("PlayStation 5", 64900),
        ("DualSense Controller", 7900),
    ]

    for name, p in ps:
        data.append({
            "name": name,
            "price": price(p),
            "image": "https://via.placeholder.com/200",
            "category": "ps"
        })

    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
