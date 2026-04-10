msg=input("请输入要遍历的字符串：")

for s in msg:
    print(s,end=" ")#end表示每一次输出以什么结束；默认\n(换行)

# range(end)   range(5) 0,1,2,3,4
# range(start,end)   range(2,8) 2,3,4,5,6,7
# range(start,end,step)   range(0,10,2) 0
# ,2,4,6,8

total=0
for i in range(1,10):
    total+=i
print(total)


#随机数
import random
num1=random.randint(1,10)
print(num1)