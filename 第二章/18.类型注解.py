a:int=3
score:float=0
hobby:str="Python"
flag:bool=False
pic:None=None

names:list[str|int]=["A","B","C"] # |是或的意思
phones:set[str]=["23454634","43875659"]
options:dict[str,int]={"count":2,"total":10}
goods:tuple[str,int,int]=("手机",677,1)

names.append("X")
names.append(1)
names.append(1.1)#会提示，但也能添加


# 函数类型注解(指定参数的类型，指定返回值的类型)
def circle_area_line(r:float) -> tuple[float,float]:
    return 3.14*r**2,round(2*r*3.14,1)  #保留一位小数

al=circle_area_line(10)
print(al)