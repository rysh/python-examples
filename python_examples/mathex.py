import math


print("1: ", 7/3)
print("2: ", math.ceil(7/3))
print("3: ", math.floor(7/3))
print("4: ", 7//3)

print("5: ", math.sqrt(4))
# math.cos
# math.sin
# math.pi


# 最大公約数
print("6: ", math.gcd(78627872, 1798742872))


# 最小公倍数
def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // math.gcd(x, a[i])
    return x


print("7: ", lcm([3, 4, 6]))

# 繰り返し２乗法（べき乗の高速化アルゴリズム）
# 「nのm乗をpで割った余り」
n = 2
m = 10
p = 100
print("8: ", pow(n, m, p))
