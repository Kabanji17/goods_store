from src.base_product_list import BaseProductList
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category(BaseProductList):
    """Класс для обозначения категории товара. Родительский класс - BaseProductList"""

    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def __str__(self):
        """Магический метод для строкового отображения объекта"""
        total_quantity = 0
        for item in self.__products:
            total_quantity += item.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Метод для добавления товаров в категорию"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Нельзя добавить товар с нулевым количеством")
            except ZeroQuantityProduct as e_info:
                print(str(e_info))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка добавления продукта завершена")
        else:
            raise TypeError

    @property
    def products(self) -> str:
        products = ""
        for product in self.__products:
            products += f"{str(product)}\n"
        return products

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
