import pytest

import test.calculation as calculation

"""
preferences => Tools => Python Integrated Tools のTestingにてpytestを指定してやる必要あり  

APIは https://docs.pytest.org/en/6.2.x/
"""

stage = "prd"


class TestPytestCalc(object):

    @classmethod
    def setup_class(cls):
        print("### start")
        cls.calc = calculation.Calc(2, 3)

    @classmethod
    def teardown_class(cls) -> None:
        print("### end:{}")
        del cls.calc

    def setup_method(self, method) -> None:
        print("### setup method:{}".format(method.__name__))

    def teardown_method(self, method) -> None:
        print("### teardown method:{}".format(method.__name__))

    def test_glb_calc(self):
        # 2 * 1 + 3 * 1 = 5 が期待値
        assert calculation.glb_calc(1, 1) == 5

    def test_cls_calc(self):
        # 2 + 3 + 1 = 6 が期待値
        assert self.calc.cls_calc(1) == 6

    def test_cls_calc_exception(self):
        # 例外テスト
        with pytest.raises(ValueError):
            self.calc.cls_calc("1")

    @pytest.mark.skip(reason='skip')
    def test_cls_calc_skip(self):
        print("### not skip test!")

        # 実行された場合はテスト失敗
        with pytest.raises(ValueError):
            self.calc.cls_calc(1)

    @pytest.mark.skipif(stage == 'test', reason='skip')
    def test_cls_calc_skip_with_condition(self):
        print("### not skip test!")

        # 実行される
        with pytest.raises(ValueError):
            self.calc.cls_calc("1")

    @pytest.mark.parametrize("x, y", [
        (1, 6)
        , (4, 9)
    ])
    def test_cls_calc_param(self, x, y):
        # 2 + 3 + 1 = 6 が期待値
        # 2 + 3 + 4 = 9 が期待値
        assert self.calc.cls_calc(x) == y

    @pytest.fixture()
    def fixture_calc(self, x, y):
        print("# before fixture_calc")
        yield calculation.Calc(x, y)

        # test_fixture_calcが実行された後に表示されている事に注意
        print("# after fixture_calc")

    @pytest.mark.parametrize("x, y", [(5, 6)])
    def test_fixture_calc(self, fixture_calc):
        # 5 + 6 + 7 = 18 が期待値
        print("## before test_fixture_calc")
        assert fixture_calc.cls_calc(18)
        print("## after test_fixture_calc")
