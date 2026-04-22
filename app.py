from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API работает"

@app.route("/products")
def products():
    return jsonify([
        {"name": "iPhone 16 256GB", "price": 99900},
        {"name": "iPhone 16 Pro", "price": 119900},
        {"name": "iPhone 17 Pro Max", "price": 149900},
        {"name": "AirPods Pro 2", "price": 20900},
        {"name": "MacBook Air M3", "price": 119900},
        {"name": "PlayStation 5", "price": 64900}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
