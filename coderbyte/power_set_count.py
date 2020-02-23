import math


def PowerSetCount(arr):
    size = len(arr)

    return sum([combination_count(size, i) for i in range(size + 1)])


def combination_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print(PowerSetCount([1, 2, 3]))
