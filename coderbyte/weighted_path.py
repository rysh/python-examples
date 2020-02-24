import heapq


def WeightedPath(strArr):
  nodes, d = create(strArr)
  # [print(x) for x in nodes]

  start = nodes[0]
  end = nodes[len(nodes) - 1]
  # print(start.name , end.name)

  return start.find(end, d)


class Node():
  def __init__(self, name):
    self.name = name
    self.path = []

  def __str__(self):
    p = [n.name + "(" + str(w) + ")" for n, w in self.path]
    return self.name + str(p)

  def find(self, end, d):
    queue = [(self.name + "-" + node.name, weight, node) for node, weight in self.path]
    ignore = {self.name}
    while len(queue) > 0:
      queue = sorted(queue, key=lambda x: x[1])
      # print("queue:", [q[2].name for q in queue])
      path, weight, node = queue.pop(0)
      if node.name == end.name:
        return path
      # print(path, weight, node.name)
      [queue.append((path + "-" + node2.name, weight + weight2, node2)) for node2, weight2 in node.path if
       not node2.name in ignore]
      ignore.add(node.name)
      # print(len(queue))

    return "-1"


def create(strArr):
  size = int(strArr.pop(0))
  nodes = []
  d = {}
  for i in range(size):
    node = Node(strArr.pop(0))
    d[node.name] = node
    nodes.append(node)

  for pathStr in strArr:
    key1, key2, weight = pathStr.split("|")
    # print(key1, key2, weight)
    node1 = d[key1]
    node2 = d[key2]
    node1.path.append((node2, int(weight)))
    node2.path.append((node1, int(weight)))

  return nodes, d
