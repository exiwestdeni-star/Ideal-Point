from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

def get_prices():
    url = "https://store77.net"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    items = soup.find_all("div", class_="product-item")[:20]

    for item in items:
        try:
            name = item.find("div", class_="product-title").text.strip()
            price_text = item.find("div", class_="price").text.replace("₽","").replace(" ","")
            price = int(price_text)

            products.append({
                "name": name,
                "price": price - 3000,
                "image": "https://via.placeholder.com/200",
                "category": "iphone"
            })
        except:
            continue

    return products

@app.route("/products")
def products():
    return jsonify(get_prices())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
