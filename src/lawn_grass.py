from src.product import Product


class LawnGrass(Product):
    """Класс описывает газонную траву. Родительский класс - Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Магический метод для сложения двух объектов"""
        if type(other) is LawnGrass:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError
