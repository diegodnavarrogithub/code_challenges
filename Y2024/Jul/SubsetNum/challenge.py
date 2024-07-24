def subset_num(nums, n, target_sum):
    if target_sum == 0:
        return True
    if n == 0 and target_sum != 0:
        return False

    if nums[n - 1] > target_sum:
        return subset_num(nums, n - 1, target_sum)

    return subset_num(nums, n - 1, target_sum) or subset_num(nums, n - 1, target_sum - nums[n - 1])
