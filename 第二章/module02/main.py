#导入自定义模块
import  my_fun
# 导入模块时，会运行该文件里的测试代码
# 测试代码中使用__name__帮助区分可避免

print(my_fun.PI)
print(my_fun.NAME)

my_fun.log_separator1()
my_fun.log_separator2()

#导入自定义模块中的功能
from my_fun import log_separator2,log_separator4

log_separator2()

from my_fun import *  # 导入my_fun中 __all__列表中指定的功能