import unittest

from Y2024.May.Fibbonacci.challenge import fibbonacci


class TestFibbonacci(unittest.TestCase):
    def test_fibbonacci3(self):
        num = 3
        ans = fibbonacci(num)
        expected_ans = [1, 1, 2]
        self.assertEqual(ans, expected_ans)

    def test_fibbonacci7(self):
        num = 6
        ans = fibbonacci(num)
        expected_ans = [1, 1, 2, 3, 5, 8]
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
