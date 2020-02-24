def GasStation(strArr):
  size = strArr.pop(0)
  for x in range(len(strArr)):
    a, b = strArr[x].split(":")
    receive = int(a)
    spend = int(b)
    if receive >= spend:
      current = x + 1
      count = 1
      remaining = receive - spend
      # print(current, strArr)
      while count < len(strArr):
        if current == len(strArr):
          current = 0

        a, b = strArr[current].split(":")
        receive1 = int(a)
        spend1 = int(b)
        # print(current, remaining, receive1, spend1, flush=True)
        remaining = remaining + receive1 - spend1

        current += 1
        if remaining < 0:
          count = 1
          break

        count += 1
        if count == len(strArr):
          return str(x + 1)

  # code goes here
  return "impossible"

