#导入模块
import utils.my_fun
utils.my_fun.log_separator4()

from utils import my_fun
my_fun.log_separator4()

#注意：如果用from utils import *导入包下所有模块，需要在__init__.py文件中添加__all__=[]
from utils import *
my_fun.log_separator1()

#导入模块中的功能
from utils.my_fun import log_separator2 # 相对路径
from 第二章.utils.my_fun import log_separator2 # 绝对路径
log_separator2()