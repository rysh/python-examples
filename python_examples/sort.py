import operator

B = [(5, 8), (6, 10), (7, 2), (4, 1), (3, 11), (9, 0)]
# 第1変数で昇順ソートしてる
print("1: ", sorted(B, key=operator.itemgetter(0)))

# 第1変数で降順ソートしてる
print("1: ", sorted(B, key=operator.itemgetter(0), reverse=True))

# 第2変数で昇順ソートしてる
print("1: ", sorted(B, key=operator.itemgetter(1)))

# 第2変数で降順ソートしてる
print("1: ", sorted(B, key=operator.itemgetter(1), reverse=True))
