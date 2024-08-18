from testconst import Const as TC


class TestBun:
    def test_constructor_makes_correct_bun(self, bun):
        assert bun.name == TC.test_bun_name and bun.price == TC.test_bun_price

    def test_get_name_returns_correct_name(self, bun):
        assert bun.get_name() == TC.test_bun_name

    def test_get_price_returns_correct_price(self, bun):
        assert bun.get_price() == TC.test_bun_price
