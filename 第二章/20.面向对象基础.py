#定义类
#命名类时用大驼峰命名法
class Car:
    pass

#创建对象
c1=Car()

#动态的为对象添加属性
c1.color="red"
c1.name="X5"

print(c1)
print(c1.color)
print(c1.__dict__) # 将对象中的所有属性以字典的形式输出


#定义类
class CarNew:
    wheel = 4 # 类属性（通过实例查找属性时，先查找实例属性，不存在时查找类属性）

    # __init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
    # self：是第一个参数，表示当前所创建出来的实例对象
    def __init__(self,c_color,c_brand,c_name,c_price): # 实例属性
        self.color=c_color
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
        print("Car类型对象初始化完毕")

    def running(self):
        print(f"{self.brand} {self.name}正在行驶中")

    def total_price(self,discount,rate):
        """
        计算提车的总费用，包含车的价格，税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost=self.price*discount+rate*self.price
        return total_cost

    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    def __eq__(self,other):
        return self.color==other.color and self.brand==other.brand and self.name==other.name and self.price==other.price
    def __lt__(self,other):
        return self.price<other.price


c2=CarNew("red","BNM","X5",10000)
c3=CarNew("red","BNM","X5",10000)
print(c2.__dict__)

#调用对象中的方法
c2.running()
total=c2.total_price(discount=0.9,rate=0.1)
print("提车的总费用为：",total)

#魔法方法
#__init__ 初始化方法
#__str__ 字符串表示的方法
#__eq__ 比较两个对象是否相等
#__lt__,__le__,__gt__,__ge__ 支持比较两个对象的大小（小于（less than），小于等于（less then or equal）,大于（greater than），大于等于）

print(c2==c3) # 若未用魔法方法（__str__..），输出False 默认输出的是对象地址
            # 若定义，则调用的是__eq__
print(c2<c3)
print(c2)

#可以通过类名或对象名访问类属性
print(c2.wheel)
print(CarNew.wheel)