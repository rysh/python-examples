import itertools


def ParallelSums(arr):
  group1 = list(itertools.combinations(arr, len(arr) // 2))

  for x in group1:
    group2 = arr[:]
    for y in x:
      group2.remove(y)
    if sum(x) == sum(group2):
      # print(x, group2)
      list1 = list(x)
      list2 = group2
      list1.sort()
      list2.sort()
      temp = []
      if list1[0] < list2[0]:
        temp = list1 + list2
      else:
        temp = list2 + list1
      return ",".join([str(i) for i in (temp)])

  return "-1"