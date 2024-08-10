from src.product import Product


class Smartphone(Product):
    """Класс описывает смартфоны. Родительский класс - Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Магический метод для сложения двух объектов"""
        if type(other) is Smartphone:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError
