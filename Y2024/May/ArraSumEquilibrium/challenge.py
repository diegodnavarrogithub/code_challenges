def arra_sum_equilibrium(arr):
    for i in range(1, len(arr)):
        left = arr[:i]
        right = arr[i:]
        if sum(left) == sum(right):
            return i - 1

    return -1
