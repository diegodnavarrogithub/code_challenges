class LogEx(int):
    def __init__(self, num):
        self.num = num

    def __add__(self, num):
        return self.num + num

    def __sub__(self, num):
        return self.num - num


Operators = {"+": LogEx.__add__, "-": LogEx.__sub__}
nums_dict = {"one": 1, "two": 2}


def sum_one_two(strs):
    expression_list = []
    while strs:
        num = strs[:3]
        expression_list.append(nums_dict[num])
        try:
            sign = strs[3]
            expression_list.append(sign)
            strs = strs[4:]
        except IndexError:
            break

    final_sum = 0
    while len(expression_list) > 2:
        cur_operation = expression_list[:3]
        expression_list = expression_list[3:]
        num1, sign, num2 = cur_operation
        num1 = LogEx(num1)
        num2 = LogEx(num2)
        ans = Operators[sign](num1, num2)
        final_sum += ans
        expression_list.insert(0, ans)
        print(expression_list)
    return expression_list[0]
