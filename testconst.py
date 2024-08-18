from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class Const:

    BUNS = {
        "black": {"name": "black bun", "price": 100},
        "red": {"name": "red bun", "price": 300},
        "white": {"name": "white bun", "price": 200},
        "test": {"name": "test bun", "price": 99},
    }

    INGREDIENTS = {
        "cutlet": {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        "dinosaur": {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
        "sausage": {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
        "chili": {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
        "hot": {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
        "sourcreame": {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
        "test": {"type": INGREDIENT_TYPE_SAUCE, "name": "test sauce", "price": 199},
    }
