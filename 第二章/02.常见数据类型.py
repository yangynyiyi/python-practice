#type()获取指定字面量或变量的值
print("Hello")
print(type("Hello"))

print(type(10))

num=1
print(type(num))

#isinstance(数据,类型),返回bool值，判断数据是否为指定类型
print(isinstance(num,int))
print(isinstance(num,bool))

#转义字符 \, \n, \t(tab缩进)
msg1='It\'s very easy!'
print(msg1)

msg2="It's very easy!"
print(msg2)

m='a''b'
print(m)
m='a'+'b'
print(m)

s1='a'
s2='b'
print('c:'+s1+','+s2)

#  +只能拼接字符串
#  str( ),转为字符串类型
name='张三'
age=18
print("我叫"+name+",年龄"+str(age))

#字符串格式化 方法一：%s占位符
print("我叫%s,年龄%s"%(name,age))

#字符串格式化 方法二：f"..{变量名/表达式}.."  常用
print(f"我叫{name},年龄{age}")
print("我叫{name},年龄{age}")