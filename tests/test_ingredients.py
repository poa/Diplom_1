from testconst import Const as TC


class TestIngredients:
    def test_constructor_makes_correct_ingredient(self, ingredient):
        assert (
            ingredient.type == TC.test_ingredient_type
            and ingredient.name == TC.test_ingredient_name
            and ingredient.price == TC.test_ingredient_price
        )

    def test_get_name_returns_correct_name(self, ingredient):
        assert ingredient.get_name() == TC.test_ingredient_name

    def test_get_price_returns_correct_price(self, ingredient):
        assert ingredient.get_price() == TC.test_ingredient_price

    def test_get_type_returns_correct_type(self, ingredient):
        assert ingredient.get_type() == TC.test_ingredient_type
