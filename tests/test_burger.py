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
        new_ingredient1 = TD.get_ingredient()
        new_ingredient2 = TD.get_ingredient()
        test_burger.add_ingredient(new_ingredient1)
        test_burger.add_ingredient(new_ingredient2)
        test_burger.move_ingredient(len(test_burger.ingredients) - 1, 0)

        assert test_burger.ingredients[0] == new_ingredient2

    def test_get_price_simple_burger_returns_correct_value(self, test_burger):
        assert test_burger.get_price() == TD.get_burger_price("test")

    def test_get_price_full_burger_returns_correct_value(self, full_burger):
        assert full_burger.get_price() == TD.get_burger_price("full")

    def test_get_receipt_prints_correct_values(self, full_burger):
        receipt = full_burger.get_receipt()

        assert receipt == TC.FULL_BURGER_RECEIPT
