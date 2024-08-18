from random import choice

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from testconst import Const as TC


class TData:
    # @staticmethod
    # def get_const_buns():
    #     return list(TC.BUNS.keys())
    #
    # @staticmethod
    # def get_const_ingredients():
    #     return list(TC.INGREDIENTS.keys())
    #

    @staticmethod
    def get_bun(name=None):
        if name is None:
            bun_data = TC.BUNS[choice(list(TC.BUNS.keys()))]
        else:
            bun_data = TC.BUNS.get(name)

        return Bun(bun_data["name"], bun_data["price"])

    @staticmethod
    def get_test_bun():
        return TData.get_bun("test")
        # bun_data = TC.BUNS["test"]
        # return Bun(bun_data["name"], bun_data["price"])

    @staticmethod
    def get_ingredient(name=None):
        if name is None:
            ingredient_data = TC.INGREDIENTS[choice(list(TC.INGREDIENTS.keys()))]
        else:
            ingredient_data = TC.INGREDIENTS.get(name)

        return Ingredient(
            ingredient_data["type"], ingredient_data["name"], ingredient_data["price"]
        )

    @staticmethod
    def get_test_ingredient():
        return TData.get_ingredient("test")

    #     ingredient_data = TC.INGREDIENTS["test"]
    #     return Ingredient(
    #         ingredient_data["type"], ingredient_data["name"], ingredient_data["price"]
    #     )

    @staticmethod
    def get_burger_price(name=None):
        if name == "test":
            bun_data = TC.BUNS["test"]
            ingredient_data = TC.INGREDIENTS["test"]
            burger_price = 2 * bun_data["price"] + ingredient_data["price"]
        else:
            burger_price = TC.FULL_BURGER_PRICE

        return burger_price
