#函数参数类型

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calc(x,y,oper):
    return oper(x,y)

print(calc(10,20,add))

#匿名函数(单行表达式，可在高阶函数参数使用)
# lambda 参数列表 ： 函数体

out_line=lambda:print("-----------")
out_line()

add=lambda x,y:x+y
print(add(1,2))

#需求：完成如下列表排序，按每个元素的字符个数，从大到小排序
data_list=["C++","C","Python","Jack","PHP","Go"]
print(data_list)

data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)

#-------------------案例------------------------
#案例1：计算n的阶乘(递归)
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

result=jc(10)
print(result)