import unittest

from Y2024.May.ArraSumEquilibrium.challenge import arra_sum_equilibrium


class TestArraSumEquilibrium(unittest.TestCase):
    def test_arra_sum_equilibrium(self):
        array = [1, 3, 5, 6, 3]
        ans = arra_sum_equilibrium(array)
        expected_ans = 2
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
