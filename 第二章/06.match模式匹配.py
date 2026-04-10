# day=input("请输入星期几（1-7）：")
#
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6"|"7":  #|或
#         print("周末")
#     case _:  #匹配其他所有情况
#         print("输入有误")

num1=float(input("请输入第一个数："))
num2=float(input("请输入第二个数："))
oper=input("请输入运算符：")

match oper:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
        print(f"{num1}-{num2}={num1-num2}")
    case "*":
        print(f"{num1}*{num2}={num1*num2}")
    case "/" if num2!=0: #if条件成立才匹配这个case
        print(f"{num1}//{num2}={num1/num2}")
    case _:
        print("no")