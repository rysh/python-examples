def twoSum(nums, target):
  S = set(nums)
  nums2 = nums[:]
  for x, numX in enumerate(nums):
    nums2.pop(0)
    numY = target - numX
    if numY in S:
      try:
        y = nums2.index(numY) + x + 1
        return [x, y]
      except:
        pass


print(twoSum([0, 4, 3, 0], 0))
