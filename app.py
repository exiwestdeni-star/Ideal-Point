from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/products")
def products():
    return jsonify([
        {
            "name": "iPhone 15 128GB",
            "oldPrice": 53200,
            "price": 50200,
            "image": "https://via.placeholder.com/300",
            "category": "apple"
        },
        {
            "name": "PlayStation 5",
            "oldPrice": 62000,
            "price": 59000,
            "image": "https://via.placeholder.com/300",
            "category": "ps"
        }
    ])

app.run(host="0.0.0.0", port=10000)
