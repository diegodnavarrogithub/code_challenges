import unittest

from Y2024.May.SortingNRemoving.challenge import sorting_n_removing


class TestSortingNRemoving(unittest.TestCase):
    def test_sorting_n_removing(self):
        nums = [5, 8, 6, 4, 3, 54, 7, 6, 2]
        ans = sorting_n_removing(nums)
        expected_ans = [2, 3, 4, 5, 6, 7, 8, 54]
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
