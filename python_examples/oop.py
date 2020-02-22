class Hoge:
    name = "hogex"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiply(self):
        return self.a * self.b


x = Hoge(2,3)
print("1: ", x.name, x.a, x.b, x.multiply())
x = x.multiply
print("2: ", x())


class Fuga(Hoge):
    name = "fugax"

    def plus(self):
        return self.a + self.b


x = Fuga(3, 4)

print("3: ", x.name, x.plus())
