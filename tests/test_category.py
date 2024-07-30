from tests.conftest import category


def test_category_init(category):
    """Тестирование инициализации объекта класса Category"""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products) == 2


def test_category_count(category):
    """Тестирование счетчиков класса Category"""
    assert category.category_count == 1
    assert category.product_count == 2
