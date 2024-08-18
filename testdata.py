from random import choice
from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

from testconst import Const as TC


class TData:
    burger_param_list = [
        ("test", ["test"]),
        ("black", ["sour cream", "cutlet", "dinosaur"]),
        ("red", ["chili", "sausage", "dinosaur", "hot"]),
    ]

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
    def get_burger(bun_name, ingredient_names):
        bun = TData.get_bun(bun_name)
        ingredients = [TData.get_ingredient(ing) for ing in ingredient_names]

        burger = Burger()

        burger.set_buns(bun)
        for ing in ingredients:
            burger.add_ingredient(ing)

        return burger

    @staticmethod
    def get_test_ingredient():
        return TData.get_ingredient("test")

    @staticmethod
    def get_burger_price(bun_name, ingredients_names):
        price = 2 * TC.BUNS.get(bun_name)["price"]

        for ingredient in ingredients_names:
            price += TC.INGREDIENTS.get(ingredient)["price"]

        return price

    @staticmethod
    def get_burger_receipt(bun_name, ingredients_names):

        _bun_name = TC.BUNS.get(bun_name)["name"]
        receipt: List[str] = [f"(==== {_bun_name} ====)"]

        for ingredient in ingredients_names:
            receipt.append(
                f"= {TC.INGREDIENTS.get(ingredient)['type'].lower()} {TC.INGREDIENTS.get(ingredient)['name']} ="
            )

        receipt.append(f"(==== {_bun_name} ====)\n")
        receipt.append(f"Price: {TData.get_burger_price(bun_name, ingredients_names)}")

        return "\n".join(receipt)
