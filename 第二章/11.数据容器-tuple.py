#元组基本操作
t1=(80,95,78,50,76,80,85,20)

print(t1)
print(type(t1))
print(t1[0])
print(t1[0:5:1])

#count() 统计元素的个数
print(t1.count(80))

#index() 获取元素索引（第一个元素位置）
print(t1.index(80))


#注意：若定义单元素的元组，单个元素后面要加逗号
t2=()
print(t2)
print(type(t2))

t3=(100,)
print(t3)
print(type(t3))

#------------元组tuple组包与解包-----------
#组包
t1=(5,7,9,10,2,23,12)
t2=5,7,9,10,2,23,12

print(t1)
print(t2)

#解包
a,b,c,d,e,f,g=t1
print(a,b,c,d,e,f,g)

first,second,*other,last=t1
print(first,second)
print(other)
print(last)

*other,last1,last2=t1
print(other)
print(last1,last2)


#案例1：有两个变量a，b，交换两个变量值
a=10
b=20

#组包
# t=b,a
#解包
# a,b=t

a,b=b,a
print(a,b)


#案例2：计算每个学生总分，平均分。各科成绩最低分，最高分，平均分。查找平均分大于90学生并输出
students=(
    ("S001","王林",85,92,78),
    ("S002","张三",92,97,84),
    ("S003","十四",89,98,87),
    ("S004","李武",81,73,90)
)

for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{total} {avg: .1f}")#保留一位小数

#写法2：
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    print(f"{total} {avg: .1f}")#保留一位小数

chinese_score=[s[2] for s in students]
math_score=[s[3] for s in students]
english_score=[s[4] for s in students]

print(f"语文最低分：{min(chinese_score)},最高分：{max(chinese_score)},平均分：{sum(chinese_score)/len(chinese_score)}")
print(f"数学最低分：{min(math_score)},最高分：{max(math_score)},平均分：{sum(math_score)/len(math_score)}")
print(f"英语最低分：{min(english_score)},最高分：{max(english_score)},平均分：{sum(english_score)/len(english_score)}")

for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    if avg>90:
        print(f"优秀学生：{s[1]}")