import turtle
import random
import sys
import locale
import platform
import os
from matplotlib import font_manager  # 用于注册字体

# 尝试设置区域

locale.setlocale(locale.LC_ALL, '')  # 使用默认

# 设置屏幕和画笔
screen = turtle.Screen()
screen.setup(1000, 1400)  # 增加画布尺寸以获得更大视图
screen.bgcolor("sky blue")
screen.title("春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。 —— 孟浩然《春晓》")

# 创建画笔
t = turtle.Turtle()
t.speed(0)  # 最快速度
t.hideturtle()

# 注册本地字体
def setup_font():
    # 字体文件路径
    font_path = "SimHei.ttf"  # 假设字体文件在同一目录
    
    # 检查字体文件是否存在
    if os.path.exists(font_path):
        print(f"找到字体文件: {font_path}")
        # 注册字体
        try:
            font_manager.fontManager.addfont(font_path)
            return "SimHei"  # 返回字体名称
        except Exception as e:
            print(f"注册字体失败: {e}")
    else:
        print(f"字体文件不存在: {font_path}")
        
    # 如果注册失败或文件不存在，返回系统字体
    return get_chinese_font()

# 使用设置好的字体
chinese_font = setup_font()
default_font = (chinese_font, 20, "normal")  # 增大字体大小
title_font = (chinese_font, 30, "bold")

# 根据操作系统选择合适的中文字体
def get_chinese_font():
    print("操作系统：", platform.system())
    system = platform.system()
    if system == 'Windows':
        return 'SimHei'  # 黑体，Windows中文字体
    elif system == 'Darwin':
        return 'PingFang SC'  # macOS中文字体
    else:
        return 'WenQuanYi Zen Hei'  # Linux中文字体

# 定义通用字体 - 使用中文友好字体
chinese_font = get_chinese_font()
default_font = (chinese_font, 15, "normal")  # 使用中文字体
title_font = (chinese_font, 30, "bold")      # 使用中文字体

# 绘制区域分隔线
def draw_grid():
    t.penup()
    t.pensize(4)  # 加粗分隔线
    t.color("black")
    
    # 绘制垂直线
    t.goto(0, 500)  # 扩大垂直线的范围
    t.setheading(270)  # 向下
    t.pendown()
    t.forward(1000)  # 墛加线长
    
    # 绘制水平线
    t.penup()
    t.goto(-500, 0)  # 扩大水平线的范围
    t.setheading(0)  # 向右
    t.pendown()
    t.forward(1000)  # 墛加线长  # 修正"墛加"为"增加"
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
    x_offset = -250  # 左上角中心点x坐标，向左增大区域
    y_offset = 250   # 左上角中心点y坐标，向上增大区域
    scale = 1.0      # 墛加缩放比例，画面更大
    
    # 绘制背景
    t.penup()
    t.goto(x_offset-250, y_offset+250)  # 调整背景位置
    t.pendown()
    t.color("light blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(500)  # 墛加背景大小
        t.right(90)
    t.end_fill()
    
    draw_ground(x_offset, y_offset-250, scale)
    draw_mountain(x_offset-220, y_offset-125, 180*scale, "dark green")
    draw_mountain(x_offset-60, y_offset-125, 210*scale, "forest green")
    
    # 绘制太阳
    t.penup()
    t.goto(x_offset-60, y_offset+60)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(30*scale)  # 墛加太阳大小
    t.end_fill()
    
    # 绘制小屋
    t.penup()
    t.goto(x_offset+60, y_offset-90)  # 调整小屋位置
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(4):
        t.forward(50*scale)  # 墛加小屋大小
        t.left(90)
    t.end_fill()
    
    # 房顶
    t.penup()
    t.goto(x_offset+60, y_offset-40)  # 调整房顶位置
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(x_offset+85, y_offset+15)
    t.goto(x_offset+110, y_offset-40)
    t.goto(x_offset+60, y_offset-40)
    t.end_fill()
    
    t.penup()
    t.goto(x_offset, y_offset+150)  # 将文字移到更上方
    t.color("black")
    t.write("春眠不觉晓", align="center", font=default_font)  # 修正字体设置

def scene2():
    """处处闻啼鸟 - 处处都能听到鸟儿在鸣叫"""
    x_offset = 250   # 右上角中心点x坐标，向右增大区域
    y_offset = 250   # 右上角中心点y坐标，向上增大区域
    scale = 1.0      # 墛加缩放比例  # 修正"墛加"为"增加"
    
    # 绘制背景
    t.penup()
    t.goto(x_offset-250, y_offset+250)  # 调整背景位置
    t.pendown()
    t.color("sky blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(500)  # 墛加背景大小
        t.right(90)
    t.end_fill()
    
    draw_ground(x_offset, y_offset-250, scale)
    
    for _ in range(7):  # 墛加树的数量
        draw_tree(random.randint(x_offset-200, x_offset+200), y_offset-125, scale*0.8)
    
    for _ in range(12):  # 墛加鸟的数量  # 修正"墛加"为"增加"
        draw_bird(random.randint(x_offset-200, x_offset+200), random.randint(y_offset-60, y_offset+150), scale*0.8)
    
    t.penup()
    t.goto(x_offset, y_offset+150)  # 将文字移到更上方
    t.color("black")
    t.write("处处闻啼鸟", align="center", font=default_font)  # 修正字体设置

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
    
    scale = 1.0  # 墛加缩放比例  # 修正"墛加"为"增加"
    
    # 绘制背景 - 确保填充整个左下区域
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
    
    # 绘制地面 - 地面在区域底部
    ground_height = int(120 * scale)  # 墛加地面高度  # 修正"墛加"为"增加"
    t.penup()
    t.goto(left_edge, bottom_edge)  # 区域左下角
    t.pendown()
    t.color("dark green")
    t.begin_fill()
    t.setheading(0)  # 确保方向正确
    t.forward(right_edge - left_edge)  # 区域宽度
    t.left(90)
    t.forward(ground_height)  # 地面高度
    t.left(90)
    t.forward(right_edge - left_edge)
    t.left(90)
    t.forward(ground_height)
    t.end_fill()
    
    # 黑夜中的屋子轮廓 - 放在地面上
    house_width = 70 * scale
    house_height = 100 * scale
    house_x = x_center - 70  # 房子位置偏左
    house_y = bottom_edge + ground_height  # 房子建在地面上
    
    t.penup()
    t.goto(house_x, house_y)
    t.pendown()
    t.color("dim gray")
    t.begin_fill()
    t.setheading(0)  # 确保方向正确
    for _ in range(2):
        t.forward(house_width)
        t.left(90)
        t.forward(house_height)
        t.left(90)
    t.end_fill()
    
    # 房顶 - 与房子顶部对齐
    roof_height = 40 * scale
    t.penup()
    t.goto(house_x, house_y + house_height)  # 屋顶从房子顶部开始
    t.pendown()
    t.color("dark gray")
    t.begin_fill()
    t.setheading(0)
    t.goto(house_x + house_width/2, house_y + house_height + roof_height)  # 屋顶中间点
    t.goto(house_x + house_width, house_y + house_height)  # 右侧
    t.goto(house_x, house_y + house_height)  # 回到起点
    t.end_fill()
    
    # 窗户有灯光
    window_width = 25 * scale
    window_height = 25 * scale
    window_x = house_x + (house_width - window_width)/2  # 窗户水平居中
    window_y = house_y + (house_height - window_height)/2  # 窗户垂直居中
    
    t.penup()
    t.goto(window_x, window_y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.setheading(0)
    for _ in range(4):
        t.forward(window_width)
        t.left(90)
        t.forward(window_height)
        t.left(90)
    t.end_fill()
    
    # 月亮 - 在夜空中的位置
    t.penup()
    t.goto(x_center + 150, y_center + 180)  # 调整月亮位置
    t.color("light gray") 
    t.begin_fill()
    t.circle(25 * scale)  # 墛加月亮大小
    t.end_fill()
    
    # 云层 - 使用更自然的云的绘制方法
    cloud_positions = [
        (x_center + 80, y_center + 150),  # 右侧云
        (x_center - 120, y_center + 170),  # 左侧云
        (x_center, y_center + 120)         # 中间云
    ]
    
    for base_x, base_y in cloud_positions:
        # 绘制更自然的云 - 使用多个重叠的圆
        cloud_size = 15 * scale
        t.color("dim gray")
        t.penup()
        
        # 左侧圆
        t.goto(base_x - cloud_size/2, base_y)
        t.pendown()
        t.begin_fill()
        t.circle(cloud_size)
        t.end_fill()
        
        # 中间圆 - 稍大一些并且位置靠上
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
        
        # 底部填充 - 连接各个圆形底部
        t.penup()
        t.goto(base_x - cloud_size/2, base_y + cloud_size)
        t.pendown()
        t.begin_fill()
        t.goto(base_x + cloud_size * 1.5, base_y + cloud_size)
        t.goto(base_x + cloud_size * 1.5, base_y)
        t.goto(base_x - cloud_size/2, base_y)
        t.goto(base_x - cloud_size/2, base_y + cloud_size)
        t.end_fill()
    
    # 闪电 - 从云层发出
    t.penup()
    t.goto(x_center - 100, y_center + 160)  # 从左侧云层下方发出
    t.pendown()
    t.pensize(4)  # 墛加闪电宽度
    t.color("yellow")
    t.setheading(270)
    t.forward(50 * scale)
    t.left(45)
    t.forward(25 * scale)
    t.right(90)
    t.forward(50 * scale)
    t.pensize(1)
    
    # 雨滴 - 满布整个区域
    t.color("white")
    for _ in range(150):  # 墛加雨滴数量
        x = random.randint(int(left_edge + 10), int(right_edge - 10))  # 边界内随机位置
        y = random.randint(int(bottom_edge + ground_height), int(top_edge - 10))  # 地面以上
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(2)
        t.setheading(260 + random.randint(-10, 10))  # 随机方向表现风
        t.forward(18 * scale)
    
    # 恢复默认线宽
    t.pensize(1)
    
    t.penup()
    t.goto(x_center, top_edge - 60)  # 距离顶部一定距离
    t.color("white")
    t.write("夜来风雨声", align="center", font=default_font)  # 修正字体设置

def scene4():
    """花落知多少 - 不知道有多少花瓣落下了"""
    # 定义右下区域的边界
    left_edge = 0
    right_edge = 500
    bottom_edge = -500
    top_edge = 0
    
    # 计算区域中心点
    x_center = (left_edge + right_edge) / 2  # 250
    y_center = (bottom_edge + top_edge) / 2  # -250 - 修复中文字符"top边"
    
    scale = 1.0  # 墛加缩放比例  # 修正"墛加"为"增加"
    
    # 绘制背景 - 确保填充整个右下区域
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
    
    # 绘制地面 - 地面在区域底部
    ground_height = int(120 * scale)
    t.penup()
    t.goto(left_edge, bottom_edge)  # 区域左下角
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.setheading(0)  # 确保方向正确
    t.forward(right_edge - left_edge)  # 区域宽度
    t.left(90)
    t.forward(ground_height)  # 地面高度
    t.left(90)
    t.forward(right_edge - left_edge)
    t.left(90)
    t.forward(ground_height)
    t.end_fill()
    
    # 樱花树 - 放在地面上居中位置
    trunk_width = 30 * scale
    trunk_height = 100 * scale
    trunk_x = x_center  # 树干位置居中
    trunk_y = bottom_edge + ground_height  # 树干放在地面上
    
    # 树干
    t.penup()
    t.goto(trunk_x - trunk_width/2, trunk_y)  # 从树干底部中心点开始
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
    crown_radius = 70 * scale  # 墛加樱花大小  # 修正"墛加"为"增加"
    crown_x = trunk_x  # 树冠中心与树干中心对齐
    crown_y = trunk_y + trunk_height  # 树冠从树干顶部开始
    
    t.penup()
    t.goto(crown_x, crown_y)
    t.color("light pink")
    t.begin_fill()
    t.circle(crown_radius)
    t.end_fill()
    
    # 落花 - 只在地面上和树冠附近散落
    petal_colors = ["pink", "light pink", "hot pink", "deep pink"]
    
    # 地面上的花瓣
    for _ in range(70):  # 墛加数量  # 修正"墛加"为"增加"
        petal_x = random.randint(int(left_edge + 30), int(right_edge - 30))
        petal_y = random.randint(int(bottom_edge + 15), int(bottom_edge + ground_height - 15))
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale)
    
    # 空中飘落的花瓣
    for _ in range(50):  # 墛加数量  # 修正"墛加"为"增加"
        # 集中在树冠周围和下方
        petal_x = random.randint(int(crown_x - crown_radius*2.5), int(crown_x + crown_radius*2.5))
        petal_y = random.randint(int(trunk_y + trunk_height/2), int(trunk_y + trunk_height + crown_radius*2))
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale)
    
    t.penup()
    t.goto(x_center, top_edge - 60)  # 距离顶部一定距离
    t.color("black")
    t.write("花落知多少", align="center", font=default_font)  # 修正字体设置

# 写诗标题
def write_poem_title():
    # 添加背景
    t.penup()
    t.goto(-250, 500)  # 调整位置，与扩大的网格一致
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(500)  # 墛加背景宽度  # 修正"墛加"为"增加"
        t.right(90)
        t.forward(70)   # 墛加背景高度  # 修正"墛加"为"增加"
        t.right(90)
    t.end_fill()
    
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