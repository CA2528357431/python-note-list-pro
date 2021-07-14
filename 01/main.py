# 推导式

# list [ f(x) for x in 组 if 条件]
a = [3, 2, 4, 1, 5, 9, 7, 6, 8, 0]
ax = [(x + 1) ** 2 for x in a if x < 5 and x > 1]
print(ax)

# dic { f(key):g(value) for key,value in 组.items() if 条件 }
b = {'u': 1, 'v': 2, 'w': 9, 'x': 67, 'y': -3, 'z': -7}
bx = {key * 2: value ** 2 for key, value in b.items() if value < 0}
print(bx)

# 集合 { f(x) for x in 组 if 条件}    #集合见下一讲
c = {x for x in range(0, 10) if x % 2 == 0}
print(c)

# 看，是不是优雅许多

# 让我们做点更cool的
d1 = (1, 2)
d2 = (3, 4)
dx = [(nd1, nd2) for nd1 in d1 for nd2 in d2]
print(dx)

e = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 0, 4]
ex = {str(key): e.count(key) for key in e}
print(ex)

# [y for _ in range(x)]     y重复x次       只有list可用
scores = [[None] * 5 for _ in range(3)]
print(scores)
