import unittest

import test.calculation as calculation

stage = "prd"


class CalcTest(unittest.TestCase):

    def setUp(self) -> None:
        print("### setup")
        self.calc = calculation.Calc(2, 3)

    def tearDown(self) -> None:
        del self.calc
        print("### tearDown")

    def test_glb_calc(self):
        # 2 * 1 + 3 * 1 = 5 が期待値
        self.assertEqual(calculation.glb_calc(1, 1), 5)

    def test_cls_calc(self):
        # 2 + 3 + 1 = 6 が期待値
        self.assertEqual(self.calc.cls_calc(1), 6)

    def test_cls_calc_exception(self):
        # 例外テスト
        with self.assertRaises(ValueError):
            self.calc.cls_calc("1")

    @unittest.skip('skip')
    def test_cls_calc_skip(self):
        print("### not skip test!")

    @unittest.skipIf(stage == 'test', 'skip')
    def test_cls_calc_skip_with_condition(self):
        # 実行される
        print("### not skip test!")


if __name__ == '__main__':
    unittest.main()
