from tests.conftest import product_1, product_2


def test_product_init(product_1, product_2):
    """Тестирование инициализации объекта класса Product"""
    assert product_1.name == "Samsung Galaxy S"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 12899.99
    assert product_1.quantity == 4

    assert product_2.name == "Iphone"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 1100101010.99
    assert product_2.quantity == 1
