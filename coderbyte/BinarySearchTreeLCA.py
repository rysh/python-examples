def BinarySearchTreeLCA(strArr):
    a, b, c = strArr
    a = eval(a)

    tree, d = create(a[:])
    # print(tree)
    # print(d.keys())

    return tree.lca(d[int(b)], d[int(c)])


class Node:
    def __init__(self, value, parent, left, right):
        self.value = value
        self.pareint = parent
        self.left = left
        self.right = right

    def __str__(self):
        a = str(self.value)
        if not self.parent == None:
            a += "(" + str(self.parent.value) + ")"
        a += "["
        if not self.left == None:
            a += str(self.left.value)
        a += ","
        if not self.right == None:
            a += str(self.right.value)
        a += "]"
        if not self.left == None:
            a += ", " + self.left.__str__()
        if not self.right == None:
            a += ", " + self.right.__str__()
        return a

    def hasEmptybranch(self):
        return self.left == None or self.right == None

    def depth(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.depth() + 1

    def lca(self, node1, node2):
        # print("search lca start:", node1.value, node2.value)
        temp = set()

        while not (node1 == None and node2 == None):
            if not node1 == None:
                if node1.value in temp:
                    return node1.value
                temp.add(node1.value)
                # print(node1.value, "->", node1.parent.value)
                node1 = node1.parent

            if not node2 == None:
                if node2.value in temp:
                    return node2.value
                temp.add(node2.value)
                # print(node2.value, "->", node2.parent.value)
                node2 = node2.parent

        return None


def create(arr):
    top = Node(arr[0], None, None, None)
    d = {arr[0]: top}

    for i in range(1, len(arr)):
        current = top
        newValue = arr[i]
        node = Node(newValue, None, None, None)
        d[newValue] = node
        while True:
            if newValue < current.value:
                if current.left == None:
                    current.left = node
                    node.parent = current
                    break
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = node
                    node.parent = current
                    break
                else:
                    current = current.right

    return top, d
