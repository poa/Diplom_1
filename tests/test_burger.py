import pytest

from praktikum.burger import Burger

from testdata import TData as TD
from testconst import Const as TC


class TestBurger:
    def test_constructor_makes_empty_burger(self):
        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_attribute_equal_to_parameter(self, test_bun):
        burger = Burger()
        burger.set_buns(test_bun)

        assert burger.bun == test_bun

    def test_add_ingredients_one_add_one_get(self, test_ingredient):
        burger = Burger()
        burger.add_ingredient(test_ingredient)

        assert burger.ingredients == [test_ingredient]

    def test_remove_ingredients_one_was_zero_get(self, test_burger):
        test_burger.remove_ingredient(0)

        assert test_burger.ingredients == []

    def test_move_ingredients_move_last_to_first_successfully(self, test_burger):
        new_ingredient = TD.get_ingredient()
        new_ingredient_last = TD.get_ingredient()
        test_burger.add_ingredient(new_ingredient)
        test_burger.add_ingredient(new_ingredient_last)
        test_burger.move_ingredient(len(test_burger.ingredients) - 1, 0)

        assert test_burger.ingredients[0] == new_ingredient_last

    @pytest.mark.parametrize("variant", ["test", "full"])
    def test_get_price_returns_correct_value(self, request, variant):
        burger = request.getfixturevalue(f"{variant}_burger")

        assert burger.get_price() == TD.get_burger_price(variant)

    def test_get_receipt_prints_correct_values(self, full_burger):
        receipt = full_burger.get_receipt()

        assert receipt == TC.FULL_BURGER_RECEIPT
