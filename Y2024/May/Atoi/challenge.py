def Atoi(s):
    s = s.strip()
    if s == "":
        return 0
    negative_flag = 1
    if s[0] in ["+", "-"]:
        if s.startswith("+"):
            s = s[1:]
        elif s.startswith("-"):
            s = s[1:]
            negative_flag = -1

    if s == "":
        return 0

    while True:
        if s[0] == "0":
            s = s[1:]
        else:
            break
        if not s:
            return 0

    list_nums = []
    for char in s:
        try:
            list_nums.append(f"{int(char)}")
        except ValueError:
            break

    num_in = (int("".join(list_nums)) if list_nums else 0) * negative_flag
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1
    return max(INT_MIN, min(num_in, INT_MAX))
