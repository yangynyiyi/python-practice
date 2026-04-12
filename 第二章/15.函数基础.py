def out_line():
    print("-------------------------")

out_line()

def rectangle_area(l,w):
    """
    根据长方形长度宽度，计算长方形面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积
    """
    area = l*w
    return area

help(rectangle_area) # 输出说明文档，不常用
area = rectangle_area(10,5) # 把鼠标悬浮放在函数名上也能看到说明文档
print(area)

#两个返回值(多个返回值会封装到元组)
def circle_area_line(r):
    return 3.14*r**2,round(2*r*3.14,1)  #保留一位小数

al=circle_area_line(10)
print(al)

area,line=circle_area_line(10)
print(area)
print(line)


#案例：定义函数，计算传入学员成绩最高分，最低分，平均分并返回
def calc_score(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list)/len(score_list),1)
    return max_score,min_score,avg_score

s_list=[300,456,764,254]
max_score,min_score,avg_score=calc_score(s_list)
print(max_score,min_score,avg_score)