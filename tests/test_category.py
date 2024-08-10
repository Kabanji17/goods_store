import pytest


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
    assert len(category.products_in_list) == 2
    category.add_product(product_1)
    assert len(category.products_in_list) == 3


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 4 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Iphone"
    assert next(product_iterator).name == "Samsung Galaxy S"

    with pytest.raises(StopIteration):
        next(product_iterator)
