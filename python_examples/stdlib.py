import string
import re
import itertools
import math
import functools


# 文字列定数
# import string
print("40:", string.ascii_lowercase)
print("41:", string.ascii_uppercase)
print("42:", string.ascii_letters)
print("43:", string.digits)
print("44:", string.hexdigits)

# import re
text = '<h1 style="width: 100px; height: 200px;">'
result = re.search(r'width: (\d*)px; height: (\d*)px;', text)

if result:
    print("45:", result.group(0))
    print("46:", result.group(1))
    print("47:", result.group(2))
    print("48:", result.groups())
else:
    print('no match')

# itertoolsを使った操作
# import itertools
a = list(range(1, 11))
b = list(itertools.accumulate(a))     # itertoolsの戻り値はイテレータとなっているので必要に応じてlist化します．
print("49:", a)
print("50:", b)

a = [3, 6, 1, 7, 2, 5]

b = itertools.dropwhile(lambda x: x != 1, a)  # 1が出るまでを除外する
print("51:", list(b))

c = itertools.takewhile(lambda x: x != 1, a)  # 1が出るまでを取り出す
print("52:", list(c))

print("53:")
a = [1, 1, 2, 3, 3, 3, 1, 2, 2]
for key, value in itertools.groupby(a):
    print(key, list(value))


# 2の余りを算出するラムダを指定して，奇数・偶数ごとにグループ化
print("54:")
a = [1, 3, 2, 4, 3, 1, 1, 2, 4]
for key, value in itertools.groupby(a, key=lambda x: x % 2):
    print(key, list(value))
a = [1, 1, 2, 3, 3, 3, 1, 2, 2]
print("55:")
for key, value in itertools.groupby(sorted(a)):
    print(key, list(value))


def permutations_count(n, r):
    """ 順列 """
    return math.factorial(n) // math.factorial(n - r)


def combinations_count(n, r):
    """ 組み合わせ """
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print("56:", permutations_count(5, 2))
print("57:", combinations_count(5, 2))


# メモ化
# import functools
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("58:", fibonacci(35))
