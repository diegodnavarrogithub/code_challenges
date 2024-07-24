import unittest

from Y2024.May.FibbonacciRecurssion.challenge import fibbonacci_recurssion


class TestFibbonacciRecurssion(unittest.TestCase):
    def test_fibbonacci_recurssion(self):
        n = 5
        ans = fibbonacci_recurssion(n)
        print(ans)
        expected_ans = 13
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
