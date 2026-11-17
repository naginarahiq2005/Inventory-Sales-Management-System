import json
from pathlib import Path

from products import Product
from Inventory import Inventory

DATA_FILE = Path("data.json")


def save_data(inventory, sales):
    data = {
        "products": [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity,
            }
            for product in inventory.products
        ],
        "sales": sales,
    }

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data():
    if not DATA_FILE.exists():
        return Inventory(), []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    inventory = Inventory()

    for item in data.get("products", []):
        product = Product(
            item["id"],
            item["name"],
            item["price"],
            item["quantity"],
        )
        inventory.products.append(product)

    saved_sales = data.get("sales", [])
    return inventory, saved_sales