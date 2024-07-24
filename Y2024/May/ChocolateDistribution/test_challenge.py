import unittest

from Y2024.May.ChocolateDistribution.challenge import chocolate_distribution


class TestChocolateDistribution(unittest.TestCase):
    def test_chocolate_distribution1(self):
        chocolates = [10, 4, 12, 3, 1]
        n = 3
        ans = chocolate_distribution(chocolates, n)
        expected_ans = 3
        self.assertEqual(ans, expected_ans)

    def test_chocolate_distribution2(self):
        chocolates = [10, 4, 12, 3, 1]
        n = 4
        ans = chocolate_distribution(chocolates, n)
        expected_ans = 9
        self.assertEqual(ans, expected_ans)

    def test_chocolate_distribution3(self):
        chocolates = [10, 4, 12, 3, 1]
        n = 3
        ans = chocolate_distribution(chocolates, n)
        expected_ans = 3
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
