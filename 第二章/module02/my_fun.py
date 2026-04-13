# 指定from..import* 导入哪些功能
__all__=['log_separator2','log_separator3','log_separator4',"PI","NAME"]

#常量（不会发生变化的数据，常量名称全大写）
PI=3.14
NAME="张三"

def log_separator1():
    print("-"*30)

def log_separator2():
    print("+"*30)

def log_separator3():
    print("#"*30)

def log_separator4():
    print("*"*30)

log_separator1()

#测试函数
#__name__:Python中的内置变量，表示当前模块的名字（直接运行当前模块，__name__的值为"__main__"；当模块被导入时，__name__的值就是模块名称）
print(__name__)

#执行当前文件，则会执行如下代码；若被当做模块导入，则不执行
if __name__ == "__main__":
    log_separator2()