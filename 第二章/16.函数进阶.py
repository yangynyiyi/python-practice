#变量作用域

num=100#全局变量

def b(r):
    num=200#局部变量

def a(r):
    global num#全局变量
    num=200

b(1)
print(num)
a(1)
print(num)

#传参方式
def reg_stu(name,age,gender,city):
    print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

# 位置参数
stu=reg_stu("张三",18,"男","北京")
print(stu)

# 关键字参数(不需要位置一致)
stu=reg_stu(name="张三",age=18,gender="男",city="北京")
print(stu)
stu=reg_stu(gender="男",city="北京",name="张三",age=18)
print(stu)

# 若位置参数和关键字参数混用，关键字参数必须在位置参数之后
stu=reg_stu("张三",18,gender="男",city="北京")
print(stu)



#默认参数(必须放在没有默认值的参数列表后边，若为默认参数传递值则修改值)
def reg_stu1(name,age,gender='男',city='北京'):
    print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

stu=reg_stu1("张三",18)
print(stu)
stu=reg_stu1("张三",18,"女")
print(stu)
stu=reg_stu1("张三",18,city="上海")
print(stu)

#不定长参数
#传递的所有匹配的位置参数会被args变量收集（args名称是约定俗成）这些参数会合并封装为一个元组
def calc_data(*args):
    min_data=min(*args)
    max_data=max(*args)
    avg_data=sum(args)/len(args)
    return min_data,max_data,avg_data

print(calc_data(2,4,6,8))
print(calc_data(2,4,6,8,76,99))

#不定长参数，关键字传递（**kwargs），这些参数会合并封装为一个字典
def calc_data(*args,**kwargs):
    """
    根据传入的这批数据，计算最大值，最小值，平均值
    :param args: 不定长位置参数，需要计算的这批数据
    :param kwargs: 不定长关键字参数
        round： 保留的小数位个数
        print： 是否打印输出
    :return: 最小值，最大值，平均值
    """
    min_data=min(*args)
    max_data=max(*args)
    avg_data=sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data=round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(min_data,max_data,avg_data)

    return min_data,max_data,avg_data

print(calc_data(2,4.8888,6,8,round=3,print=True))
