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
        self.products = products if products else []
        Category.product_count += 1 if products else 0
        Category.category_count +=1
