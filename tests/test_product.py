from src.product import Product


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


def test_product_create(params_product):
    """Тестирование метода создания нового продукта"""
    new_product = Product.new_product(params_product, [])
    new_product.name = "Samsung"
    new_product.description = "512GB"
    new_product.price = 12132.6
    new_product.quantity = 2


def test_product_update(capsys, product_1):
    """Тестирование работы сеттера"""
    product_1.price = -800
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product_1, product_2):
    """Тестирование магического метода str"""
    assert str(product_1) == "Samsung Galaxy S, 12899.99 руб. Остаток: 4 шт."
    assert str(product_2) == "Iphone, 1100101010.99 руб. Остаток: 1 шт."


def test_product_add(product_1, product_2):
    """Тестирование магического метода add"""
    assert product_1 + product_2 == 1100152610.95
