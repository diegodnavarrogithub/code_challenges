def fibbonacci_recurssion(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return fibbonacci_recurssion(n - 1) + fibbonacci_recurssion(n - 2)
