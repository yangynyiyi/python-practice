"""
    案例：
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1.添加购物车：用户根据提示录入商品名称，以及商品的价格、数量，保存该商品信息到购物车
        2.修改购物车：要求用户输入要修改的购物车商品名称，然后根据提示输入商品的价格、数量
        3.删除购物车：要求用户输入要删除的购物车商品名称并删除
        4.查询购物车，将购物车中的商品信息展示出来

    结构：shopping_cart={"Meta80":{"price":6999,"num":2},"鼠标"：{...}}
"""
shopping_cart={}

menu="""
##########购物车系统##########
#        1.添加购物车        #
#        2.修改购物车        #
#        3.删除购物车        #
#        4.查询购物车        #
#        5.退出购物车        #
############################
"""

print("欢迎使用购物车管理系统")

while True:
    # 1.制作菜单
    print(menu)

    # 2.执行的具体操作
    choice = input("请选择要执行的操作（1-5）：")

    match choice:
        case "1":
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            # 若商品存在，则不添加，输出提示信息
            if goods_name in shopping_cart:
                print("商品已存在")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕")
        case "2":
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            # 若商品不存在，提示错误信息，不修改
            if goods_name not in shopping_cart:
                print("商品不存在")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品修改完毕")

        case "3":
            goods_name = input("请输入商品名称：")

            # 若商品不存在，提示错误信息
            if goods_name not in shopping_cart:
                print("商品不存在")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")

        case "4":
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_info["price"]},商品数量：{goods_info["num"]}")

        case "5":
            print("bye")
            break

        case _:
            print("非法操作，不支持")