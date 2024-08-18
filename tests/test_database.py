from unittest.mock import patch
from praktikum.database import Database
from testdata import TData as TD


class TestDatabase:
    def test_constructor_db_has_expected_values(self):
        db = Database()
        assert len(db.buns) == 3 and len(db.ingredients) == 6

    def test_available_buns_returns_expected_value(self, test_db, test_bun):
        bun_from_db = test_db.available_buns().pop()
        assert bun_from_db.get_name() == test_bun.name and bun_from_db.get_price() == test_bun.price

    def test_available_ingredients_returns_expected_value(self, test_db, test_ingredient):
        ingredient_from_db = test_db.available_ingredients().pop()
        assert (
            ingredient_from_db.get_name() == test_ingredient.name
            and ingredient_from_db.get_price() == test_ingredient.price
        )


