def small_large_sum(nums):
    if len(nums) <= 3:
        return 0

    even = []
    odds = []
    for i, n in enumerate(nums):
        if i % 2 == 0:
            even.append(n)
        else:
            odds.append(n)

    even.sort()
    odds.sort()
    return even[-2] + odds[-2]
