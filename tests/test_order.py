import pytest

from src.order import Order


def test_order_init(product_3):
    order = Order(product_3, 10)
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 10
    assert order.total_price == 40000


def test_order_new_quantity(product_3):
    order = Order(product_3, 10)
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 10
    assert order.total_price == 40000
    order.quantity = 15
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 25
    assert order.total_price == 100000


def test_order_new_product(product_3):
    order = Order(product_3, 10)
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 10
    assert order.total_price == 40000
    with pytest.raises(ValueError):
        order.products = "New_product"
