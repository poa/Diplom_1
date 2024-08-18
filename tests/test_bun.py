import pytest

from testconst import Const as TC
from testdata import TData as TD


class TestBun:
    @pytest.mark.parametrize("bun_name", list(TC.BUNS.keys()))
    def test_constructor_makes_correct_bun(self, bun_name):
        bun = TD.get_bun(bun_name)
        bun_data = TC.BUNS.get(bun_name)
        assert (
                bun.name == bun_data.get("name")
                and bun.price == bun_data.get("price")
        )

    def test_get_name_returns_correct_name(self, test_bun):
        assert test_bun.get_name() == TC.BUNS.get("test").get("name")

    def test_get_price_returns_correct_price(self, test_bun):
        assert test_bun.get_price() == TC.BUNS.get("test").get("price")
