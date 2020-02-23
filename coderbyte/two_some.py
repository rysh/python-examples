def TwoSum(arr):
  result = ""
  head = arr.pop(0)
  for a in range(len(arr)):
    for b in range(len(arr)):
      if arr[a] + arr[b] == head and a < b:
        result = result + str(arr[a]) + "," + str(arr[b]) + " "

  if result == "":
    return result
  else:
    return result.strip()
