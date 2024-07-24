class BinaryOp(int):
    def __init__(self, val):
        self.val = val

    def __and__(self, num):
        return self.val and num

    def __or__(self, num):
        return self.val or num

    def __or__(self, num):
        return self.val ^ num


def binary_operations(expression):
    operators = {"A": BinaryOp.__and__, "B": BinaryOp.__or__, "C": BinaryOp.__xor__}
    start = 0
    end = 3

    while len(expression) > 1:
        current_op = expression[start:end]

        num1, op, num2 = list(current_op)
        num1 = BinaryOp(int(num1))
        num2 = BinaryOp(int(num2))

        expression = str(operators[op](num1, num2)) + expression

    return int(expression)
