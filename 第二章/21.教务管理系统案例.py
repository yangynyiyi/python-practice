class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语:{self.english} | 总分：{self.chinese+self.math+self.english}"

    def score_update(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english

class EduSystem:
    system_version="1.0"
    system_name="教务管理系统"

    def __init__(self):
        self.students_list=[]

    # 添加指定学生成绩
    def add_student(self):
        name=input("请输入学生姓名：")

        for s in self.students_list:
            if s.name==name:
                print("该学生已存在，添加失败")
                return

        chinese=int(input("请输入语文成绩："))
        math=int(input("请输入数学成绩："))
        english=int(input("请输入英语成绩："))

        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu=Student(name,chinese,math,english)
            self.students_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生各科成绩需在0-100之间")

    # 修改指定学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")

        for s in self.students_list:
            if s.name == name:
                print("当前成绩",s)
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.score_update(chinese,math,english)
                    print("学生信息修改成功")
                    print("修改后的成绩", s)
                    return
                else:
                    print("学生各科成绩需在0-100之间")
                    return

        print("未找到学生，修改失败")

    # 删除指定学生成绩
    def del_student(self):
        name = input("请输入要删除的学生姓名：")

        for s in self.students_list:
            if s.name == name:
                self.students_list.remove(s)
                print("学生信息删除成功")
                return

        print("未找到学生，删除失败")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")

        for s in self.students_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return

        print("未找到学生")

    # 展示全部学生成绩
    def query_students(self):
        for s in self.students_list:
            print(s)

    def run(self):
        print("欢迎使用教务管理系统")

        while True:
            print()
            print("###############################################################")
            print("1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统")
            print("###############################################################")
            print()

            choice=input("请选择要执行的操作，输入1-6：")

            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.del_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.query_students()
                    case "6":
                        break
                    case _:
                        print("输入有误，请输入1-6之间的菜单功能")
            except ValueError as e:
                print("输入的数据有问题，请检查并重新输入")
            except Exception as e:
                print("出错")


#测试
if __name__ == "__main__":
    edu_system=EduSystem()
    edu_system.run()




