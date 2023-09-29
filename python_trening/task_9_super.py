class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


# print(B().y)  - 'это ошибка ---- так как обращаемся ранее к классу, а он задан НИЖе  b = D()

b = D()
print(b.y)
