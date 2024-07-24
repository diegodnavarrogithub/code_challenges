import re


def password_checker(password):
    pat = r"^(?![0-9])(?=.*\d)(?=.*[A-Z])[A-Za-z\d_]{4,}$"

    return 1 if re.match(pat, password) else 0
