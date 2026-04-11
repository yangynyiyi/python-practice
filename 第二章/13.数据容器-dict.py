#字典
#key不能重复，如果重复后面的值会覆盖前面的值
dict1={"王林":670,"李武":608,"张三":580,"王林":700}
print(dict1)
print(type(dict1))

#key要为不可变类型（str,int,float,tuple），不能为list,set,dict
dict2={0.5:670,(1,2):608,"[1,2]":580}

#访问
#无索引下标，只能根据key获取value
dict3={"王林":670,"李武":608,"张三":580}
print(dict3["王林"])
dict3["王林"]=700
print(dict3)

#----------字典常见操作（增删改查）--------------
#添加 - key不存在就是添加
dict3["小美"]=730
print(dict3)

#修改 - key存在就是修改
dict3["小美"]=630
print(dict3)

#查询
print(dict3["小美"])#根据key获取value
print(dict3.get("小美"))#根据key获取value

print(dict3.keys())#获取所有key
print(dict3.values())#获取所有value
print(dict3.items())#获取所有键值对 key:value

#删除
score=dict3.pop("王林")
print(score)
print(dict3)

del dict3["小美"]
print(dict3)

#遍历
for k in dict3.keys():
    print(f"{k}:{dict3[k]}")

for item in dict3.items():
    print(f"{item[0]}:{item[1]}")

for k,v in dict3.items():
    print(f"{k}:{v}")