import unittest

from Y2024.Jul.SubsetNum.challenge import subset_num


class TestSubsetNum(unittest.TestCase):
    def test_subset_num(self):
        nums = [3, 34, 4, 12, 5, 2]
        target = 9

        ans = subset_num(nums, target)
        self.assertEqual(ans, True)

if __name__ == '__main__':
    unittest.main()

