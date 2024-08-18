from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from testconst import Const as TC


class TData:
    @staticmethod
    def get_const_buns():
        return [bun for bun in TC.BUNS]

    @staticmethod
    def get_const_ingredients():
        return [ing for ing in TC.INGREDIENTS]

    @staticmethod
    def get_test_bun():
        bun_data = TC.BUNS["test"]
        return Bun(bun_data["name"], bun_data["price"])

    @staticmethod
    def get_test_ingredient():
        ingredient_data = TC.INGREDIENTS["test"]
        return Ingredient(
            ingredient_data["type"], ingredient_data["name"], ingredient_data["price"]
        )
