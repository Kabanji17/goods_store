from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс описания продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Базовый метод для создания нового продукта."""
        pass
