s=[56,90,88,65,90,"A","Hello",True]
print(type(s))

#获取
print(s[0])
print(s[-8])

#修改
s[5]="ABC"
print(s)

#删除
del s[6]
print(s)

#遍历
for item in s:
    print(item)

#-----------切片-----------
print(s[0:5:1])
print(s[:5])
print(s[0:5:3])
print(s[0:-1])

#----------列表常用方法-------------
s=[1,2,3,4,5,6,7,8,9,0]
print(s)

# append(11): 在列表尾部追加元素
s.append(11)
print(s)

# insert(0,92): 在指定索引之前，插入该元素
s.insert(1,12)
print(s)

# remove(3): 移除列表中第一个匹配到的值
s.remove(3)
print(s)

# pop(): 删除列表中指定索引位置的元素（若未指定索引，默认删最后一个）
e=s.pop(3)
print(s)
print(e)

e=s.pop()
print(s)
print(e)


# sort(): 对列表进行排序（列表元素数据类型一致）
s.sort()
print(s)

# reverse(): 反转列表元素
s.reverse()
print(s)

#-------------列表list案例-------------
# #案例1：将用户输入的10个数字，存储到一个列表中，并将列表中的数字排序，输出其中最小值，最大值，平均值
# #1.定义列表
# num_list=[]
#
# #2.将用户输入的10个数字存入列表
# for i in range(10):
#     num=int(input("请输入一个有效的数字："))
#     num_list.append(num)
#
# print("列表：",num_list)
#
# #3.排序
# num_list.sort()
# print(num_list)
#
# #4.输出其中最小值，最大值，平均值
# print("最小值：",num_list[0])
# print("最大值：",num_list[-1])
# print("平均值：",sum(num_list)/len(num_list))


#案例2：合并两个列表中的元素，并对合并的结果进行去重处理
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]

#1.合并列表
for num in num_list2:
    num_list1.append(num)
print(num_list1)

#2.去除重复记录
new_list=[]
for num in num_list1:
    if num not in new_list:
        new_list.append(num)

print(new_list)


#案例2（简化1）：合并两个列表中的元素，并对合并的结果进行去重处理
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]

#1.合并列表
#解包：将列表这一类容器解开成一个一个独立的元素
#组包：将多个值合并到一个容器
num_list=[*num_list1,*num_list2]
print(num_list)

#2.去除重复记录
new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)

#案例2（简化2）：合并两个列表中的元素，并对合并的结果进行去重处理
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]

#1.合并列表
num_list=num_list1+num_list2
print(num_list)

#2.去除重复记录
new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)

#案例3：生成1-20的平方列表
#方式1：
num_list=[]
for i in range(1,21):
    num_list.append(i**2)

print(num_list)

#方式2：列表推导式：按一定规则快速生成一个列表的方法  [要输入的值 for i in 序列/列表]
num_list2=[i**2 for i in range(1,21)]
print(num_list2)


# 案例4：从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表
#列表推导式(格式2)：按一定规则快速生成一个列表的方法  [要输入的值 for i in 序列/列表 if 条件]
num_list=[12,32,45,77,80,92,33,57,97,98,110,111,122]
new_list=[i**2 for i in num_list if i%2==0]
print(new_list)
