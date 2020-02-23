import bisect

# ソートされたリストに対して使う
L = [1, 3, 6, 6, 6, 9, 11]

print("1: ", bisect.bisect_left(L, 0))
print("1': ", bisect.bisect(L, 0))

print("2: ", bisect.bisect_left(L, 5))
print("2': ", bisect.bisect(L, 5))

print("3: ", bisect.bisect_left(L, 6))
# 同じものがある場合は一番左の番号
print("4: ", bisect.bisect(L, 6))
# 同じものがある場合は一番右の隣の番号

print("5: ", bisect.bisect_left(L, 12))
print("5': ", bisect.bisect(L, 12))
