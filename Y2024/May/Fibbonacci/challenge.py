def fibbonacci(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1, 1]
    fib = [1, 1]
    counter = 3
    while counter <= num:
        cur = fib[-1] + fib[-2]
        fib.append(cur)
        counter += 1

    return fib
