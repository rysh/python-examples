import itertools

A = [1, 2, 3, 4]
print("1: ", list(itertools.permutations(A, 2)))
print("2: ", list(itertools.combinations(A, 2)))
print("3: ", list(itertools.product("ABC", repeat=1)))
print("4: ", list(itertools.product("ABC", repeat=2)))
print("5: ", list(itertools.product("ABC", repeat=3)))

