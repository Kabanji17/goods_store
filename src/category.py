from src.product import Product


class Category:
    """Класс для обозначения категории товара."""

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

    def add_product(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products = ""
        for product in self.__products:
            products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products

    @property
    def products_in_list(self):
        return self.__products
