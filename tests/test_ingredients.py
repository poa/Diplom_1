from praktikum.ingredient import Ingredient
from testconst import Const as TC


class TestIngredients:
    def test_constructor_makes_correct_ingredient(self, test_ingredient):
        ingredient = TC.INGREDIENTS.get("test")
        assert (
                test_ingredient.type == ingredient.get("type")
                and test_ingredient.name == ingredient.get("name")
                and test_ingredient.price == ingredient.get("price")
        )

    def test_get_name_returns_correct_name(self, test_ingredient):
        assert test_ingredient.get_name() == TC.INGREDIENTS.get("test").get("name")

    def test_get_price_returns_correct_price(self, test_ingredient):
        assert test_ingredient.get_price() == TC.INGREDIENTS.get("test").get("price")

    def test_get_type_returns_correct_type(self, test_ingredient):
        assert test_ingredient.get_type() == TC.INGREDIENTS.get("test").get("type")
