#字符串  (无法修改)
s="Hello-Python"
s1="**Hello**"

print(s[4])
print(s[-8])

for i in s:
    print(i)

#切片
print(s[5::-1])

#字符串常用方法
# find() 在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1
index=s.find("Python")
print(index)

# count() 统计子串在字符串中出现的次数
c=s.count("o")
print(c)

# upper() 将字符串中所有字母转换为大写
su=s.upper()
print(su)

# lower() 将字符串中所有字母转换为小写
sl=s.lower()
print(sl)

# split() 将字符串按制定分隔符分割成列表
slist=s.split("-")
print(slist)

# strip() 去除字符串两端的空白字符或指定字符
ss=s1.strip("*")
print(ss)

# replace() 将字符串中的指定子串替换为新的子串
sr=s.replace("-","_")
print(sr)

# startswith() 检查字符串是否以指定子串开头，返回布尔值
print(s.startswith("Python"))
print(s.startswith("H"))


print(s1)#字符串不可变


#-------------字符串案例----------------
#案例1：邮箱格式验证是否正确（至少包含一个@和一个.）

mail=input("请输入邮箱：")

if mail.count("@")>0 and "." in mail:#in运算符
    print("合法")
else:
    print("非法")