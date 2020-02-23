import collections
import heapq

# deque
l = [0, 1, 2, 3]
q = collections.deque(l)

# 後ろから4を挿入, l=deque([0,1,2,3,4])
q.append(4)
print("1: ", q)

# 前から5を挿入, l=deque([5,0,1,2,3,4])
q.appendleft(5)
print("2: ", q)

# 後ろの要素を取り出す, x=4, l=deque([5,0,1,2,3])
x = q.pop()
print("3: ", x, q)

# 前の要素を取り出す, y=5, l = deque([0,1,2,3])
y = q.popleft()
print("4: ", y, q)


# defaultdict
dd = collections.defaultdict(int)
print("5: ", dd["a"], dd)
dd["a"] += 1
print("6: ", dd["a"], dd)


# Counter
l = ['a', 'b', 'b', 'c', 'b', 'a', 'c', 'c', 'b', 'c', 'b', 'a']
# カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
S = collections.Counter(l)

print("7: ", S.items())
print("8: ", S['a'])
print("9: ", S.most_common(2))
print("10: ", S.keys())
print("11: ", S.values())
print("12: ", list(S.keys())[0])


# heapq
L = [3, 0, 2, 5, 7, 2]
H = []
[heapq.heappush(H, l) for l in L]

print("13: ", H)
print("14: ", heapq.heappop(H))
print("15: ", heapq.heappop(H))
print("16: ", heapq.heappop(H))
# ダイクストラ法で使う
