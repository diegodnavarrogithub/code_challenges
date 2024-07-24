import unittest

from Y2024.May.SumOneTwo.challenge import sum_one_two


class TestSumOneTwo(unittest.TestCase):
    def test_sum_one_two(self):
        strs = "one+two-one+one+two-one"
        ans = sum_one_two(strs)
        expected_ans = 4
        self.assertEqual(ans, expected_ans)

    def test_sum_one_two_one(self):
        strs = "one+two-one+one+two-one+one"
        ans = sum_one_two(strs)
        expected_ans = 5
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
