from tests.conftest import category


def test_category_init(category):
    """Тестирование инициализации объекта класса Category"""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products_in_list) == 2


def test_category_count(category):
    """Тестирование счетчиков класса Category"""
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_products_list_property(category):
    """Тестирование геттера получения информации о продукте"""
    assert category.products == (
        "Iphone, 1100101010.99 руб. Остаток: 1 шт.\n" "Samsung Galaxy S, 12899.99 руб. Остаток: 3 шт.\n"
    )


def test_category_add_product(category, product_1):
    assert len(category.products_in_list) == 2
    category.add_product(product_1)
    assert len(category.products_in_list) == 3
