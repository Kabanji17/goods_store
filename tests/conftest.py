import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def params_product():
    return {"name": "Samsung", "description": "512GB", "price": 12132.6, "quantity": 2}


@pytest.fixture
def product_iterator(category):
    return ProductIterator(category)


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
