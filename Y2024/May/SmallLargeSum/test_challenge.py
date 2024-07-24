import unittest

from Y2024.May.SmallLargeSum.challenge import small_large_sum


class TestSmallLargeSum(unittest.TestCase):
    def test_small_large_sum_3_or_less(self):
        nums = [1, 2, 3]
        ans = small_large_sum(nums)
        expected_ans = 0
        self.assertEqual(ans, expected_ans)

    def test_small_large_sum_empty_arr(self):
        nums = []
        ans = small_large_sum(nums)
        expected_ans = 0
        self.assertEqual(ans, expected_ans)

    def test_small_large_sum_7(self):
        nums = [3, 2, 1, 7, 5, 4]
        ans = small_large_sum(nums)
        expected_ans = 7
        self.assertEqual(ans, expected_ans)

    def test_small_large_sum_10(self):
        nums = [4, 0, 7, 9, 6, 4, 2]
        ans = small_large_sum(nums)
        expected_ans = 10
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
