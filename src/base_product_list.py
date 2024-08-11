from abc import ABC, abstractmethod


class BaseProductList(ABC):
    """Базовый класс описания категории продуктов и заказа продуктов.
    Обладает абстрактным методом отображения продуктов в категории либо в заказе."""

    @abstractmethod
    def products(self):
        pass
