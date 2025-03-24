import turtle
import random
import sys
import locale
import platform
import os

locale.setlocale(locale.LC_ALL, '')  # 使用默认

# 设置屏幕和画笔
screen = turtle.Screen()
screen.setup(1000, 1200)  # 增加画布尺寸以获得更大视图
screen.bgcolor("sky blue")
screen.title("春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。 —— 孟浩然《春晓》")

# 创建画笔
t = turtle.Turtle()
t.speed(0)  # 最快速度
t.hideturtle()


# 使用设置好的字体
default_font = ("SimHei", 20, "normal")  # 墛加字体大小
title_font = ("SimHei", 30, "bold")

# 绘制区域分隔线
def draw_grid():
    t.penup()
    t.pensize(4)  # 加粗分隔线
    t.color("black")
    
    # 绘制垂直线
    t.goto(0, 500)  # 扩大垂直线的范围
    t.setheading(270)  # 向下
    t.pendown()
    t.forward(1000)  
    
    # 绘制水平线
    t.penup()
    t.goto(-500, 0)  # 扩大水平线的范围
    t.setheading(0)  # 向右
    t.pendown()
    t.forward(1000)  
    t.penup()

# 辅助函数

# 绘制大地
def draw_ground(x_offset, y_offset, scale=1.0):
    width = 400 * scale
    height = 100 * scale
    
    t.penup()
    t.goto(x_offset - width/2, y_offset - height)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# 绘制山
def draw_mountain(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.goto(x + size/2, y + size/2)
    t.goto(x + size, y)
    t.end_fill()

# 绘制树 - 修复树叶和树干对齐问题
def draw_tree(x, y, scale=1.0):
    trunk_width = 20 * scale
    trunk_height = 80 * scale
    crown_size = 40 * scale
    
    # 树干
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(trunk_width)
        t.left(90)
        t.forward(trunk_height)
        t.left(90)
    t.end_fill()
    
    # 树冠 - 修正对齐问题
    # 计算树干中心点位置
    trunk_center_x = x + trunk_width/2
    trunk_top_y = y + trunk_height
    
    t.penup()
    t.goto(trunk_center_x, trunk_top_y)  # 将树冠底部中点放在树干顶部中心
    t.pendown()
    t.color("dark green")
    t.begin_fill()
    t.circle(crown_size)  # circle方法从圆底部中点开始绘制
    t.end_fill()

# 绘制花瓣
def draw_petal(x, y, color, scale=1.0):
    size = 3 * scale
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# 绘制鸟
def draw_bird(x, y, scale=1.0):
    body_size = 10 * scale
    wing_length = 20 * scale
    wing_width = 5 * scale
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.setheading(0)
    
    # 鸟的体型
    t.begin_fill()
    t.circle(body_size)
    t.end_fill()
    
    # 鸟的翅膀
    t.penup()
    t.goto(x+body_size/2, y+body_size+body_size/2)
    t.pendown()
    t.setheading(45)
    t.begin_fill()
    for _ in range(2):
        t.forward(wing_length)
        t.right(90)
        t.forward(wing_width)
        t.right(90)
    t.end_fill()

# 创建四个场景函数，对应诗的四句
def scene1():
    """春眠不觉晓 - 春天睡觉，不知不觉天亮了"""
    # 定义左上区域的边界
    left_edge = -500
    right_edge = 0
    bottom_edge = 0
    top_edge = 500
    
    # 计算区域中心点
    x_center = (left_edge + right_edge) / 2  # -250
    y_center = (bottom_edge + top_edge) / 2  # 250
    
    scale = 1.0  # 缩放比例
    
    # 绘制背景
    t.penup()
    t.goto(left_edge, top_edge)  # 区域左上角
    t.setheading(0)  # 确保方向正确
    t.pendown()
    t.color("light blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(right_edge - left_edge)  # 区域宽度
        t.right(90)
    t.end_fill()
    
    # 绘制地面
    ground_height = 100 * scale
    t.penup()
    t.goto(left_edge, bottom_edge + ground_height)  # 从地面高度开始
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.setheading(0)
    t.forward(right_edge - left_edge)  # 区域宽度
    t.right(90)
    t.forward(ground_height)
    t.right(90)
    t.forward(right_edge - left_edge)
    t.right(90)
    t.forward(ground_height)
    t.end_fill()
    
    # 绘制山脉
    t.color("dark green")
    t.begin_fill()
    t.penup()
    t.goto(left_edge + 30, bottom_edge + ground_height)
    t.pendown()
    t.goto(x_center - 70, y_center + 70)
    t.goto(x_center - 20, bottom_edge + ground_height)
    t.end_fill()
    
    t.color("forest green")
    t.begin_fill()
    t.penup()
    t.goto(x_center - 100, bottom_edge + ground_height)
    t.pendown()
    t.goto(x_center + 40, y_center + 90)
    t.goto(x_center + 150, bottom_edge + ground_height)
    t.end_fill()
    
    # 绘制太阳
    t.penup()
    t.goto(x_center + 90, y_center + 60)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(30 * scale)
    t.end_fill()
    
    # 绘制小屋
    house_width = 50 * scale
    house_height = 50 * scale
    house_x = x_center + 10
    house_y = bottom_edge + ground_height
    
    t.penup()
    t.goto(house_x, house_y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.setheading(0)  # 确保方向正确
    for _ in range(2):  # 使用2次循环绘制矩形，与其他场景保持一致
        t.forward(house_width)
        t.left(90)
        t.forward(house_height)
        t.left(90)
    t.end_fill()
    
    # 房顶
    roof_height = 40 * scale
    t.penup()
    t.goto(house_x, house_y + house_height)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.setheading(0)  # 确保方向正确
    t.goto(house_x + house_width/2, house_y + house_height + roof_height)
    t.goto(house_x + house_width, house_y + house_height)
    t.goto(house_x, house_y + house_height)
    t.end_fill()
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("black")
    t.write("春眠不觉晓", align="center", font=default_font)

def scene2():
    """处处闻啼鸟 - 处处都能听到鸟儿在鸣叫"""
    # 定义右上区域的边界
    left_edge = 0
    right_edge = 500
    bottom_edge = 0
    top_edge = 500
    
    # 计算区域中心点
    x_center = (left_edge + right_edge) / 2  # 250
    y_center = (bottom_edge + top_edge) / 2  # 250
    
    scale = 1.0  # 缩放比例
    
    # 绘制背景
    t.penup()
    t.goto(left_edge, top_edge)  # 区域左上角
    t.setheading(0)  # 确保方向正确
    t.pendown()
    t.color("sky blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(right_edge - left_edge)  # 区域宽度
        t.right(90)
    t.end_fill()
    
    # 绘制地面
    ground_height = 100 * scale
    t.penup()
    t.goto(left_edge, bottom_edge + ground_height)  # 从地面高度开始
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.setheading(0)
    t.forward(right_edge - left_edge)  # 区域宽度
    t.right(90)
    t.forward(ground_height)
    t.right(90)
    t.forward(right_edge - left_edge)
    t.right(90)
    t.forward(ground_height)
    t.end_fill()
    
    # 绘制树木
    for _ in range(6):
        tree_x = random.randint(int(left_edge + 50), int(right_edge - 50))
        tree_y = bottom_edge + ground_height
        draw_tree(tree_x, tree_y, scale * 0.8)
    
    # 绘制鸟
    for _ in range(10):
        bird_x = random.randint(int(left_edge + 50), int(right_edge - 50))
        bird_y = random.randint(int(bottom_edge + ground_height + 50), int(top_edge - 100))
        draw_bird(bird_x, bird_y, scale*0.8)
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("black")
    t.write("处处闻啼鸟", align="center", font=default_font)

def scene3():
    """夜来风雨声 - 夜晚伴随着风雨的声音"""
    # 定义左下区域的边界
    left_edge = -500
    right_edge = 0
    bottom_edge = -500
    top_edge = 0
    
    # 计算区域中心点
    x_center = (left_edge + right_edge) / 2  # -250
    y_center = (bottom_edge + top_edge) / 2  # -250
    
    scale = 1.0  # 缩放比例
    
    # 绘制背景
    t.penup()
    t.goto(left_edge, top_edge)  # 区域左上角
    t.setheading(0)  # 确保方向正确
    t.pendown()
    t.color("navy")  # 更深的蓝色代表夜空
    t.begin_fill()
    for _ in range(4):
        t.forward(right_edge - left_edge)  # 区域宽度
        t.right(90)
    t.end_fill()
    
    # 绘制地面
    ground_height = 120 * scale
    t.penup()
    t.goto(left_edge, bottom_edge)  # 区域左下角
    t.pendown()
    t.color("dark green")
    t.begin_fill()
    t.setheading(0)
    t.forward(right_edge - left_edge)  # 区域宽度
    t.left(90)
    t.forward(ground_height)  # 地面高度
    t.left(90)
    t.forward(right_edge - left_edge)
    t.left(90)
    t.forward(ground_height)
    t.end_fill()
    
    # 绘制房子和屋顶
    house_width = 70 * scale
    house_height = 100 * scale
    house_x = x_center - 70
    house_y = bottom_edge + ground_height
    
    # 房子主体
    t.penup()
    t.goto(house_x, house_y)
    t.pendown()
    t.color("dim gray")
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(house_width)
        t.left(90)
        t.forward(house_height)
        t.left(90)
    t.end_fill()
    
    # 房顶
    roof_height = 40 * scale
    t.penup()
    t.goto(house_x, house_y + house_height)
    t.pendown()
    t.color("dark gray")
    t.begin_fill()
    t.setheading(0)
    t.goto(house_x + house_width/2, house_y + house_height + roof_height)
    t.goto(house_x + house_width, house_y + house_height)
    t.goto(house_x, house_y + house_height)
    t.end_fill()
    
    # 窗户有灯光
    window_width = 25 * scale
    window_height = 25 * scale
    window_x = house_x + (house_width - window_width)/2
    window_y = house_y + (house_height - window_height)/2
    
    t.penup()
    t.goto(window_x, window_y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.setheading(0)
    for _ in range(4):
        t.forward(window_width)
        t.left(90)
    t.end_fill()
    
    # 绘制月亮
    t.penup()
    t.goto(x_center + 150, y_center + 180)
    t.color("light gray")
    t.begin_fill()
    t.circle(25 * scale)
    t.end_fill()
    
    # 绘制云层
    cloud_positions = [
        (x_center + 80, y_center + 150),
        (x_center - 120, y_center + 170),
        (x_center, y_center + 120)
    ]
    
    for base_x, base_y in cloud_positions:
        cloud_size = 15 * scale
        t.color("dim gray")
        
        # 左侧圆
        t.penup()
        t.goto(base_x - cloud_size/2, base_y)
        t.pendown()
        t.begin_fill()
        t.circle(cloud_size)
        t.end_fill()
        
        # 中间圆
        t.penup()
        t.goto(base_x + cloud_size/2, base_y + cloud_size/3)
        t.pendown()
        t.begin_fill()
        t.circle(cloud_size * 1.2)
        t.end_fill()
        
        # 右侧圆
        t.penup()
        t.goto(base_x + cloud_size * 1.5, base_y)
        t.pendown()
        t.begin_fill()
        t.circle(cloud_size)
        t.end_fill()
        
        # 底部填充
        t.penup()
        t.goto(base_x - cloud_size/2, base_y + cloud_size)
        t.pendown()
        t.begin_fill()
        t.goto(base_x + cloud_size * 1.5, base_y + cloud_size)
        t.goto(base_x + cloud_size * 1.5, base_y)
        t.goto(base_x - cloud_size/2, base_y)
        t.goto(base_x - cloud_size/2, base_y + cloud_size)
        t.end_fill()
    
    # 绘制闪电
    t.penup()
    t.goto(x_center - 100, y_center + 160)
    t.pendown()
    t.pensize(4)
    t.color("yellow")
    t.setheading(270)
    t.forward(50 * scale)
    t.left(45)
    t.forward(25 * scale)
    t.right(90)
    t.forward(50 * scale)
    t.pensize(1)
    
    # 绘制雨滴
    t.color("white")
    for _ in range(50):
        x = random.randint(int(left_edge + 10), int(right_edge - 10))
        y = random.randint(int(bottom_edge + ground_height), int(top_edge - 10))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(2)
        t.setheading(260 + random.randint(-10, 10))
        t.forward(18 * scale)
    
    # 恢复默认线宽
    t.pensize(1)
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("white")
    t.write("夜来风雨声", align="center", font=default_font)

def scene4():
    """花落知多少 - 不知道有多少花瓣落下了"""
    # 定义右下区域的边界
    left_edge = 0
    right_edge = 500
    bottom_edge = -500
    top_edge = 0
    
    # 计算区域中心点
    x_center = (left_edge + right_edge) / 2  # 250
    y_center = (bottom_edge + top_edge) / 2  # -250
    
    scale = 1.0  # 缩放比例
    
    # 绘制背景
    t.penup()
    t.goto(left_edge, top_edge)  # 区域左上角
    t.setheading(0)  # 确保方向正确
    t.pendown()
    t.color("light blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(right_edge - left_edge)  # 区域宽度
        t.right(90)
    t.end_fill()
    
    # 绘制地面
    ground_height = 120 * scale
    t.penup()
    t.goto(left_edge, bottom_edge)  # 区域左下角
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.setheading(0)
    t.forward(right_edge - left_edge)  # 区域宽度
    t.left(90)
    t.forward(ground_height)  # 地面高度
    t.left(90)
    t.forward(right_edge - left_edge)
    t.left(90)
    t.forward(ground_height)
    t.end_fill()
    
    # 樱花树
    trunk_width = 30 * scale
    trunk_height = 100 * scale
    trunk_x = x_center - trunk_width/2
    trunk_y = bottom_edge + ground_height
    
    # 树干
    t.penup()
    t.goto(trunk_x, trunk_y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(trunk_width)
        t.left(90)
        t.forward(trunk_height)
        t.left(90)
    t.end_fill()
    
    # 树冠 - 樱花
    crown_radius = 70 * scale
    crown_x = trunk_x + trunk_width/2
    crown_y = trunk_y + trunk_height
    
    t.penup()
    t.goto(crown_x, crown_y)
    t.color("light pink")
    t.begin_fill()
    t.circle(crown_radius)
    t.end_fill()
    
    # 落花
    petal_colors = ["pink", "light pink", "hot pink", "deep pink"]
    
    # 地面上的花瓣
    for _ in range(60):
        petal_x = random.randint(int(left_edge + 30), int(right_edge - 30))
        petal_y = random.randint(int(bottom_edge + 15), int(bottom_edge + ground_height - 15))
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale)
    
    # 空中飘落的花瓣
    for _ in range(35):
        petal_x = random.randint(int(crown_x - crown_radius*2.5), int(crown_x + crown_radius*2.5))
        petal_y = random.randint(int(trunk_y + trunk_height/2), int(trunk_y + trunk_height + crown_radius*2))
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale)
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("black")
    t.write("花落知多少", align="center", font=default_font)

# 写诗标题
def write_poem_title():

    # 写文字
    t.penup()
    t.goto(0, 550)  # 调整y坐标到背景中央
    t.color("black")
    t.write("春晓 - 孟浩然", align="center", font=title_font)  # 修正字体设置

# 绘制整体画面 - 修改绘制顺序，先画标题和分隔线，再画场景
write_poem_title()  # 先绘制标题
draw_grid()         # 再绘制网格线
scene1()
scene2()
scene3()
scene4()

# 保持画面显示直到手动关闭
turtle.mainloop()  # 替换screen.exitonclick()，保持画面显示