import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S",
        description="256GB, Серый цвет, 200MP камера",
        price=12899.99,
        quantity=4
    )

@pytest.fixture
def product_2():
    return Product(
        name="Iphone",
        description="512GB, Gray space",
        price=1100101010.99,
        quantity=1
    )

@pytest.fixture
def category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Iphone", "512GB, Gray space", 1100101010.99, 1),
            Product("Samsung Galaxy S", "256GB, Серый цвет, 200MP камера", 12899.99, 3)
        ]
    )