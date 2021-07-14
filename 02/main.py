#集合



#创建集合
a={False,'hello',12,34,56}
b=set(['HI',13982,None,False,34]) # ()内是list

#无法访问单个元素

#并集
c=a|b
print(c)
#交集
d=a&b
print(d)

# 增 删
a.add(True)
print(a)
a.discard(False)
print(a)

# 元素个数
print(len(a))

# 清空
a.clear()
print(a)



