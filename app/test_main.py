import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture
def list_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_all_bad_product(list_template):
    today = datetime.date(2022, 2, 25)
    with mock.patch('datetime.date') as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(list_template) == ["salmon", "chicken", "duck"]


def test_one_good_product(list_template):
    today = datetime.date(2022, 2, 2)
    with mock.patch('datetime.date') as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(list_template) == ["duck"]


def test_all_good_product(list_template):
    today = datetime.date(2022, 1, 1)
    with mock.patch('datetime.date') as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(list_template) == []


def test_product_with_outdated_today(list_template):
    today = datetime.date(2022, 2, 5)
    with mock.patch('datetime.date') as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(list_template) == ["duck"]