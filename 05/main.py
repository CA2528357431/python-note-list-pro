import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
# 前n个最大/小的



list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(2, list2, key=lambda tar: tar['shares']))
print(heapq.nsmallest(2, list2, key=lambda tar: tar['shares']))
#dic 用key指定排序依据

#创建heapq对象
ak=[1,2,4,1,2,9,8]
heapq.heapify(ak)
print(ak)
# 二叉树，父节点小与等于子节点
# 从父节点到子节点排列
# ak[k]<=ak[2k+1] ak[k]<=ak[2k+2]

#添加
al=[1,2,0,3,4,1,2,3,0,9,8,5,6]
ao=[0,0]
for r in al:
    heapq.heappush(ao,r)
print(ao)

#返回最小值并能将其删除
x=heapq.heappop(ao)
print(ao)
print(x)

#添加新元素，返回最小值并能将其删除
x=heapq.heappushpop(ao,9)
print(ao)
print(x)

#返回最小值并能将其删除，添加新元素
x=heapq.heapreplace(ao,-1)
print(ao)
print(x)

#合并      返回一个heapq类，然而无法正常输出，唯有转化为list
a1=[1,2,0,3,4,1,2,3,0,9,8,5,6]
a2=[-1, 0, 1, 1, 3, 3, 4, 2, 2, 9, 6, 9, 8, 5]
a3=heapq.merge(a1,a2)
print(list(a3))


#


