import json
import os

from src.product import Product
from src.category import Category


def read_json(file_path: str) -> dict:
    """Функция для открытия json-файла"""
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="utf-8") as open_file:
        products_data = json.load(open_file)
    return products_data


def create_objects_from_json(products_data: dict) -> list:
    """Функция для конвертации данных из json-файла в объекты классов"""
    categories = []
    for category in products_data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    products_data = create_objects_from_json(raw_data)
    print(products_data[0].name)