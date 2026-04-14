try:
    print("====================")
    # print(my_name)
    # print(1/0)
    print("ABC".c)
    print("====================")
except NameError as e:
    print("名字出错,异常信息：",e)
except ZeroDivisionError as e:
    print("0不能做除数,异常信息：",e)
except IndexError as e:
    print("索引出错,异常信息：", e)
except Exception as e:# 捕获所有异常
    print("程序运行出错,异常信息：",e)
finally: # 无论程序是否正常运行，finally代码块中代码都会执行
    print("资源释放")