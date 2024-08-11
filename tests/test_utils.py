from unittest.mock import patch

from src.utils import create_objects_from_json, read_json


@patch("json.load")
def test_read_json(mock_json_load, json_data):
    mock_json_load.return_value = json_data
    assert read_json("../data/products.json") == json_data


def test_create_objects_from_json(json_data):
    objects = create_objects_from_json(json_data)
    assert objects[0].name == "Смартфоны"
    assert objects[1].name == "Телевизоры"
    assert (
        objects[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
