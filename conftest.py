import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient

from testconst import Const as TC


@pytest.fixture(scope="session")
def db():
    db = Database()
    yield db
    del db


@pytest.fixture(scope="class")
def bun():
    bun = Bun(TC.test_bun_name, TC.test_bun_price)
    yield bun
    del bun


@pytest.fixture(scope="class")
def ingredient():
    ingredient = Ingredient(
        TC.test_ingredient_type, TC.test_ingredient_name, TC.test_ingredient_price
    )
    yield ingredient
    del ingredient
