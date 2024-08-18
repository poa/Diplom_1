from testconst import Const as TC


class TestBun:
    def test_constructor_makes_correct_bun(self, test_bun):
        assert (
                test_bun.name == TC.BUNS.get("test").get("name")
                and test_bun.price == TC.BUNS.get("test").get("price")
        )

    def test_get_name_returns_correct_name(self, test_bun):
        assert test_bun.get_name() == TC.BUNS.get("test").get("name")

    def test_get_price_returns_correct_price(self, test_bun):
        assert test_bun.get_price() == TC.BUNS.get("test").get("price")
