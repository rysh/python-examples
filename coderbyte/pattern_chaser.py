def PatternChaser(str):
  word_size = len(str) // 2
  # print("word_size" ,word_size)

  while word_size > 0:
    for i in range(len(str)):
      # print("i", i)
      i1 = i
      i2 = word_size + i
      # print("i1 i2:", i1, i2)
      a = str[i1:i2]
      b = str[word_size + i - 1:]
      # print("a", a, "b", b)
      if len(a) <= 1:
        break
      if len(a) > len(b):
        continue
      if a in b:
        return "yes " + a
        # print(a, b)
    word_size -= 1

  # code goes here
  return "no null"