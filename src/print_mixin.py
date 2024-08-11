class PrintMixin:
    """Класс-миксин при создании объекта выводит в консоль информацию, от какого класса
    и с какими параметрами создан объект."""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
