# itertools
import  itertools

#处理对象可以是 string list tuple，以下以list为例
#string也理解为数组



#链接
a='well'
b=(132,None,'cool')
c=(0,0,0)
abc=itertools.chain(a,b,c)
abcbata=itertools.chain(a,b,c)
print(type(abc))
#返回 iterable d对象


#输出
print(list(abc))
#一旦输出，则元素消失
for x in abcbata:
    print(x)
#可转化成list输出，也可for遍历

#无界数表
i=0
for x in itertools.count(100,3):
    #设定起始数字和步长
    print(x)
    i+=1
    if i>=5:
        break

#cycle
i=0
for x in itertools.cycle('abc'):
    print(x)
    i += 1
    if i >= 5:
        break

#fliter
numbers = [23, 20, 44, 32, 7, 12]
fli1=itertools.filterfalse(lambda x : x < 20,numbers)
print(list(fli1))
#前者设置条件函数，保留不符合条件的，后者设置目标list
# 不符合条件则条件函数返回false
#lambda下一讲
booleans = [1,'well', 0, None,False]
fli2=itertools.filterfalse(None,booleans)
print(list(fli2))
#若无条件，返回false，‘空’

#compress markup
nubo=itertools.compress(numbers,booleans)
print(list(nubo))
#根据b筛选a,若b中元素是（false，‘空’），则剔除a中元素

#重复
rep=itertools.repeat('well',6)
print(list(rep))

#starmap
def hk(*a):
    x=max(a)
    y=min(a)
    return x**2,y-2
smp=itertools.starmap(hk,[[1,4,5,3,5],[3,-9,-3,10]])
print(list(smp))

#对list中每个数据执行前面的函数并将返回值保存

#组合迭代

comx=itertools.combinations([ 2, 3,1], 2)
print (list(comx))
comy=itertools.combinations_with_replacement([2, 3,1], 2)
print (list(comy))
#将a中的元素任意抽取b个自由组合
#前者无不会对a中同一个元素重复提取，后者则会
#元素按照原list顺序排列
comx=itertools.combinations([2, 1,1], 2)
print (list(comx))
# #然而a中仍然可以有一样的元素
per=itertools.permutations([2, 3, 1], 2)
print (list(per))
#将a中的元素任意抽取b个自由组合
#不会对a中同一个元素重复提取
#元素顺序也是自由组合

#持续丢弃元素，直到有元素不符合条件，不丢弃该元素
dw=itertools.dropwhile(lambda x: x<5, [1,4,6,4,1])
print(list(dw))

#持续保留元素，直到有元素不符合条件，不丢保留该元素
tw=itertools.takewhile(lambda x: x<5, [1,4,6,4,1])
print(list(tw))

#切片   参数是 目标，开头，结尾（不包括），步长
sl=itertools.islice([123,44,2,3,4,45,5,6,7], 1, 7, 2)
print(list(sl))

#笛卡尔乘积
pro=itertools.product([1,2],['a','b','c'],[True,False])
print(list(pro))

#邻同分组
for [key, group] in itertools.groupby('AAABBBCCAAA'):
    print (key,':',list(group))

