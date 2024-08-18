import pytest

from testconst import Const as TC
from testdata import TData as TD


class TestIngredients:
    @pytest.mark.parametrize("ingredient_name", list(TC.INGREDIENTS.keys()))
    def test_constructor_makes_correct_ingredient(self, ingredient_name):
        ingredient = TD.get_ingredient(ingredient_name)
        ingredient_data = TC.INGREDIENTS.get(ingredient_name)
        assert (
            ingredient.type == ingredient_data.get("type")
            and ingredient.name == ingredient_data.get("name")
            and ingredient.price == ingredient_data.get("price")
        )

    def test_get_name_returns_correct_name(self, test_ingredient):
        assert test_ingredient.get_name() == TC.INGREDIENTS.get("test").get("name")

    def test_get_price_returns_correct_price(self, test_ingredient):
        assert test_ingredient.get_price() == TC.INGREDIENTS.get("test").get("price")

    def test_get_type_returns_correct_type(self, test_ingredient):
        assert test_ingredient.get_type() == TC.INGREDIENTS.get("test").get("type")
