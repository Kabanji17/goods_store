from src.base_product_list import BaseProductList
from src.product import Product


class Order(BaseProductList):
    """Класс описывает заказ продуктов. В заказе может содержаться только один вид продуктов,
    возможно изменение количества единиц продукта в заказе. При попытке изменения либо добавления продукта поднимается ошибка.
    Выводит суммарную стоимость за единицы продукта в заказе. Родительский класс - BaseProductList."""

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity
        self.__total_price = 0

    @property
    def products(self):
        return f"{self.__product.name}, {self.__product.description}"

    @products.setter
    def products(self, new_product):
        if new_product:
            raise ValueError("Добавлять новый товар в уже созданный заказ невозможно!")

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity += new_quantity

    @property
    def total_price(self):
        self.__total_price = self.__quantity * self.__product.price
        return self.__total_price
