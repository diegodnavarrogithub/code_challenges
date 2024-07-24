import unittest

from Y2024.May.PasswordChecker.challenge import password_checker


class TestPasswordChecker(unittest.TestCase):
    def test_password_checker(self):
        password = "bB1_89"
        ans = password_checker(password)
        expected_ans = 1
        self.assertEqual(ans, expected_ans)


if __name__ == "__main__":
    unittest.main()
