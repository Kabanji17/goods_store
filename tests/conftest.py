import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def product_1():
    return Product(name="Samsung Galaxy S", description="256GB, Серый цвет, 200MP камера", price=12899.99, quantity=4)


@pytest.fixture
def product_2():
    return Product(name="Iphone", description="512GB, Gray space", price=1100101010.99, quantity=1)


@pytest.fixture
def category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Iphone", "512GB, Gray space", 1100101010.99, 1),
            Product("Samsung Galaxy S", "256GB, Серый цвет, 200MP камера", 12899.99, 3),
        ],
    )


@pytest.fixture
def params_product():
    return {"name": "Samsung", "description": "512GB", "price": 12132.6, "quantity": 2}


@pytest.fixture
def product_iterator(category):
    return ProductIterator(category)
