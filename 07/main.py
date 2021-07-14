# lamaba


# 优雅的小函数


# 实例
import itertools

x = lambda a, b, c: (a * b * c, a + b + c)
print(x(1, 2, 4))
iter = itertools.starmap(x, [[9, 3, 1], [0, 2, 3], [3, 4, 5]])
print(list(iter))
# 或者也可以这样写
iter = itertools.starmap(lambda a, b, c: (a * b * c, a + b + c), [[9, 3, 1], [0, 2, 3], [3, 4, 5]])
print(list(iter))
