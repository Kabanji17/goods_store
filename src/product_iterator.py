class ProductIterator:
    """Класс, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, category_obj):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Магический метод, который создает объект для итераций"""
        self.index = 0
        return self

    def __next__(self):
        """Магический метод, который возвращает очередной элемент при выполнении итерации"""
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration