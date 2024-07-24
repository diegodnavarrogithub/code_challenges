def chocolate_distribution(chocolates, n):
    chocolates.sort()
    min_diff = chocolates[-1] - chocolates[0]
    start = 0
    end = n
    while end <= len(chocolates):
        print(chocolates[start:end])
        current_diff = chocolates[start:end][-1] - chocolates[start:end][0]
        print(current_diff)
        if current_diff < min_diff:
            min_diff = current_diff
        end += 1
        start += 1

    return min_diff
