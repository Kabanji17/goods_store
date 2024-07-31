class Product:
    """Класс для представления товара."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params_product: dict, existing_products: list):
        """Метод, возвращающий созданный объект класса Product из параметров товара в словаре,
        а также ищет одинаковые товары"""
        name = params_product["name"]
        description = params_product["description"]
        price = params_product["price"]
        quantity = params_product["quantity"]
        # Проверка на наличие похожего товара
        for existing_product in existing_products:
            if existing_product.name == name:
                # Если товар найден, обновляем количество и цену
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)
                return existing_product
        # Если товар не найден, создаем новый
        new_product = cls(name, price, description, quantity)
        return new_product
        # return cls(**params_product)

    @property
    def price(self):
        """Геттер цены продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер проверки цены продукта на нулевое и отрицательное значение, и для переопределения цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_answer = input("Подтвердите снижение цены. Введите y/n: ")
            if user_answer == "y":
                self.__price = new_price
            elif user_answer == "n":
                self.__price = self.__price
        elif new_price > self.__price:
            self.__price = new_price
