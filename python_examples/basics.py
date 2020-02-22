import copy

a = "1 2 3"
A, B, C = a.split()
print("1:", a)
print("2:", A, B, C)
print("3:", A + B + C)

A, B, C = [int(x) for x in "1 2 3".split()]
print("4:", A + B + C)

# 内包表記 Comprehension
print("5:", len([x for x in range(1, 10) if x % 3 == 0]))

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("6:", *data, sep='\n')

# 行列の縦と横を入れ替える
print("7:", *[x for x in zip(*data)], sep='\n')

# 列毎の和
print("8:", [sum(x) for x in zip(*data)])

# flatten
print("9:", [flatten for inner in data for flatten in inner])
print("10:", sum(data, []))

a = [1, 2]

print("11:", a + a)
print("12:", a * 2)

print("13:", 1 in a)
print("14:", 3 in a)

# delete
a = [1, 2, 3, 4, 5]
del a[1]
print("15:", a)

a = [1, 2, 3, 4, 5]
del a[1:3]
print("16:", a)

a = [1, 2, 3, 4, 5]
x = a.pop(1)
print("17:", a, x)

d = [1, 2, 3, 4, 5]
d.remove(3)
print("17:", d)

# sort or sorted
a = [3, 2, 1]
print("18:", sorted(a))
print("19:", a)
a.sort()
print("20:", a)
print("21:", sorted(a, reverse=True))


a = ['B', 'C', 'a', 'd', 'e']
print("22:", sorted(a))
print("23:", sorted(a, key=lambda x: x.upper()))
a = [(1, 'One', '1'), (1, 'One', '01'),
     (2, 'Two', '2'), (2, 'Two', '02'),
     (3, 'Three', '3'), (3, 'Three', '03')]
print("24:", sorted(a, key=lambda x: (x[1], x[2], x[0])))


a = [1, 2, 3, 4, 5]
print("25:", a[len(a) - 1])
print("26:", a[-1])
print("27:", a[-2])


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("28:", a[3:7])
print("29:", a[3:])    # 終点の省略
print("30:", a[:7])    # 始点の省略

print("31:", a[2:8:2])     # 2番目以上8番目未満を2step（1つ飛ばし）で取得
print("32:", a[6:1:-2])


# スライスの応用
a = [1, 2, 3, 4, 5]
# 簡易 deep copy
b = a[:]
b[0] *= 10
print("33:", a)
print("34:", b)
# 逆転
s = 'ABCDEFG'
print("35:", s[::-1])


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# import copy
b = copy.deepcopy(a)     # ディープコピー
b[0].append(0)      # b[0]（内部のリスト）はaとは別のオブジェクト

print("36:", a)            # aに影響はない
print("37:", b)


# 和集合と積集合
a = [2, 4, 6, 8]
b = [3, 6, 9]

print("38:", list(set(a) | set(b)))  # 和集合
print("39:", list(set(a) & set(b)))  # 積集合
