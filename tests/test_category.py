import pytest

from src.product import Product


def test_category_init(category):
    """Тестирование инициализации объекта класса Category"""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products_in_list) == 2


def test_category_count(category):
    """Тестирование счетчиков класса Category"""
    assert category.category_count == 2
    assert category.product_count == 4


def test_category_products_list_property(category):
    """Тестирование геттера получения информации о продукте"""
    assert category.products == (
        "Iphone, 1100101010.99 руб. Остаток: 1 шт.\n" "Samsung Galaxy S, 12899.99 руб. Остаток: 3 шт.\n"
    )


def test_category_add_product(category, product_1):
    """Тестирование метода добавления продукта в категорию"""
    assert len(category.products_in_list) == 2
    category.add_product(product_1)
    assert len(category.products_in_list) == 3


def test_category_add_invalid(category, product_1):
    with pytest.raises(TypeError):
        new_list = category.add_product(1)


def test_category_add_smartphone(category, smartphone_1):
    """Тестирование метода добавления продукта в категорию"""
    new_list = category.add_product(smartphone_1)
    assert category.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 4 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Iphone"
    assert next(product_iterator).name == "Samsung Galaxy S"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_middle_price(category, category_without_products):
    assert category.middle_price() == 550056955.49
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys, category):
    assert len(category.products_in_list) == 2

    prod_add = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category.add_product(prod_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Продукт добавлен успешно"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления продукта завершена"

    # prod_add = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
    # category.add_product(prod_add)
    # message = capsys.readouterr()
    # assert message.out.strip().split("\n")[-1] == "Нельзя добавить товар с нулевым или отрицательным количеством"
    # assert message.out.strip().split("\n")[-1] == "Обработка добавления продукта завершена"

    with pytest.raises(ValueError, match="с нулевым количеством не может быть добавлен"):
        prod_add = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        category.add_product(prod_add)
