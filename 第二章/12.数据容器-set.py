#集合set（不能重复,无序，可修改）
s1={5,3,2,0,9,12,43,64,22,5,0}
print(s1)
print(type(s1))

#定义空集合（直接用{}表示的是空字典）
s2=set()
print(s2)
print(type(s2))

#常用方法
s1={100,200,300,400,500,600,700,800}
print(s1)
# add() 添加元素到集合中
s1.add(1200)
print(s1)

# remove() 移除集合中的指定元素（不存在则报错）
s1.remove(200)
print(s1)

# pop() 随机删除集合中的元素并返回
e=s1.pop()
print(e)
print(s1)

# clear() 清空集合
s1.clear()
print(s1)


s2={"A","B","C","D"}
s3={"C","D","E"}
s4={"E","F","G"}
# difference() 求两个集合的差集（包含在集合1但不包含在集合2）
print(s2.difference(s3))
print(s3.difference(s2))
# -号也能求差集
print(s2-s3)
#集合推导式
sj={s for s in s2 if s not in s3}
print(sj)

# union() 求两个集合的并集
print(s2.union(s3))
#可以多个连一起
print(s2.union(s3).union(s4))
#可以用运算符|
print(s2|s3|s4)


# intersection() 求两个集合的交集
print(s2.intersection(s3))
# 运算符&也是求交集
print(s2&s3)


#获取几个集合加起来各字母的数量
list=[*s2,*s3,*s4]
print(list)

for s in s2|s3|s4:
    print(f"{s}有{list.count(s)}个")