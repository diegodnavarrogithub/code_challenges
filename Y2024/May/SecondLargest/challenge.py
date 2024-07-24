def second_largest(nums):
    index = 0
    largest = float('-inf')
    second_largest = 0
    while index < len(nums):
        if nums[index] > largest:
            second_largest = largest
            largest = nums[index]
        index += 1
    return second_largest
