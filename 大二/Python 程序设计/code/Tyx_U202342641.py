import turtle
import random
import locale

locale.setlocale(locale.LC_ALL, '')  # 设置为系统默认语言环境

# 设置屏幕和画笔
screen = turtle.Screen()
screen.setup(1400, 1400)  # 设置画布尺寸
screen.bgcolor("sky blue")  # 背景颜色
screen.title("春晓 - 孟浩然")  # 标题

# 创建画笔
t = turtle.Turtle()
t.speed(0)  # 设置最快速度
t.hideturtle()  # 隐藏画笔

# 字体设置
default_font = ("SimHei", 20, "normal")  # 默认字体
title_font = ("SimHei", 30, "bold")  # 标题字体

# 绘制网格线，用于分隔四个场景
def draw_grid():
    t.penup()
    t.pensize(4)  # 设置线条粗细
    t.color("black")
    # 绘制垂直线
    t.goto(0, 500)
    t.setheading(270)  # 向下
    t.pendown()
    t.forward(1000)
    # 绘制水平线
    t.penup()
    t.goto(-500, 0)
    t.setheading(0)  # 向右
    t.pendown()
    t.forward(1000)
    t.penup()

# 辅助函数：绘制地面、山、树、花瓣、鸟等

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

# 场景1：春眠不觉晓
def scene1():
    """绘制左上角场景：春天的早晨"""
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
    
    # 绘制地面 - 使用春天草地的颜色
    ground_height = 100 * scale
    t.penup()
    t.goto(left_edge, bottom_edge + ground_height)  # 从地面高度开始
    t.pendown()
    t.color("lawn green")  # 春天的嫩绿色
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
    
    # 绘制简单的太阳
    t.penup()
    t.goto(x_center + 180, y_center + 70)
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
    
    # 在小屋旁边绘制一些花朵，表示春天的到来
    flower_positions = [
        (house_x - 30, house_y + 10),
        (house_x - 20, house_y + 5),
        (house_x - 40, house_y + 8),
        (house_x + house_width + 15, house_y + 7),
        (house_x + house_width + 25, house_y + 12)
    ]
    
    for flower_x, flower_y in flower_positions:
        # 花茎
        t.penup()
        t.goto(flower_x, flower_y)
        t.pendown()
        t.color("green")
        t.setheading(90)  # 向上
        t.pensize(2)
        t.forward(15 * scale)
        t.pensize(1)
        
        # 花朵
        t.penup()
        t.goto(flower_x, flower_y + 15 * scale)
        t.pendown()
        t.color("yellow")
        t.begin_fill()
        t.circle(5 * scale)
        t.end_fill()
        
        # 花瓣
        petal_colors = ["red", "pink", "purple", "orange"]
        t.color(random.choice(petal_colors))
        for angle in range(0, 360, 60):
            t.penup()
            t.goto(flower_x, flower_y + 15 * scale)
            t.setheading(angle)
            t.forward(5 * scale)
            t.pendown()
            t.begin_fill()
            t.circle(3 * scale)
            t.end_fill()
    
    # 添加一个窗户
    window_width = 15 * scale
    window_height = 20 * scale
    window_x = house_x + 10 * scale
    window_y = house_y + 15 * scale
    
    # 窗户
    t.penup()
    t.goto(window_x, window_y)
    t.pendown()
    t.color("light blue")  # 窗户颜色
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(window_width)
        t.left(90)
        t.forward(window_height)
        t.left(90)
    t.end_fill()
    
    # 窗框
    t.penup()
    t.goto(window_x, window_y)
    t.pendown()
    t.color("white")
    t.pensize(2)
    t.setheading(0)
    for _ in range(2):
        t.forward(window_width)
        t.left(90)
        t.forward(window_height)
        t.left(90)
    
    # 窗户十字格
    t.penup()
    t.goto(window_x, window_y + window_height/2)
    t.pendown()
    t.forward(window_width)
    t.penup()
    t.goto(window_x + window_width/2, window_y)
    t.pendown()
    t.setheading(90)
    t.forward(window_height)
    t.pensize(1)
    
    # 添加几只早起的小鸟，表示天亮了但人还在睡
    for _ in range(3):
        bird_x = random.randint(int(x_center - 150), int(x_center + 100))
        bird_y = random.randint(int(y_center + 50), int(y_center + 150))
        draw_bird(bird_x, bird_y, scale * 0.6)
    
    # 定义不同类型的花朵
    
    def draw_daisy(x, y, size):
        """绘制雏菊风格的花"""
        petal_colors = ["white", "lavender", "misty rose"]
        center_colors = ["gold", "dark orange", "goldenrod"]
        
        # 花瓣
        t.penup()
        t.goto(x, y)
        t.color(random.choice(petal_colors))
        t.pendown()
        t.begin_fill()
        
        # 绘制花瓣
        for _ in range(8):
            t.setheading(_ * 45)
            t.forward(size)
            t.left(90)
            t.forward(size / 2)
            t.left(90)
            t.forward(size)
            t.left(90)
            t.forward(size / 2)
            t.left(90)
        t.end_fill()
        
        # 花蕊
        t.penup()
        t.goto(x, y)
        t.color(random.choice(center_colors))
        t.pendown()
        t.begin_fill()
        t.circle(size / 3)
        t.end_fill()
        
    def draw_tulip(x, y, size):
        """绘制郁金香风格的花"""
        stem_length = 15 * scale
        flower_colors = ["red", "pink", "purple", "orange", "hot pink"]
        
        # 花茎
        t.penup()
        t.goto(x, y)
        t.setheading(90)  # 向上
        t.pendown()
        t.color("green")
        t.pensize(2)
        t.forward(stem_length)
        t.pensize(1)
        
        # 绘制叶子
        leaf_y = y + stem_length * 0.4
        t.penup()
        t.goto(x, leaf_y)
        t.color("dark green")
        t.pendown()
        t.begin_fill()
        t.setheading(30)  # 向右上
        t.forward(size * 1.2)
        t.left(120)
        t.forward(size * 1.5)
        t.setheading(270)  # 回到茎
        t.forward(size * 0.4)
        t.end_fill()
        
        # 花朵
        flower_top = y + stem_length
        t.penup()
        t.goto(x, flower_top)
        t.color(random.choice(flower_colors))
        t.pendown()
        t.begin_fill()
        
        # 绘制郁金香特有的形状
        t.setheading(0)
        t.forward(size)
        t.setheading(120)
        t.forward(size * 1.5)
        t.setheading(240)
        t.forward(size * 1.5)
        t.setheading(0)
        t.forward(size)
        t.end_fill()
    
    def draw_sunflower(x, y, size):
        """绘制向日葵风格的花"""
        stem_length = 15 * scale
        
        # 花茎
        t.penup()
        t.goto(x, y)
        t.setheading(90)  # 向上
        t.pendown()
        t.color("green")
        t.pensize(2)
        t.forward(stem_length)
        t.pensize(1)
        
        # 花朵
        flower_top = y + stem_length
        t.penup()
        t.goto(x, flower_top)  # 修复：使用x和flower_top作为坐标，而不是只传flower_top
        t.color("gold")
        
        # 花瓣
        t.pendown()
        t.begin_fill()
        for _ in range(18):
            t.setheading(_ * 20)
            t.forward(size * 1.2)
            t.left(160)
            t.forward(size * 1.2)
            t.left(20)
        t.end_fill()
        
        # 花蕊
        t.penup()
        t.goto(x, flower_top)
        t.color("brown")
        t.pendown()
        t.begin_fill()
        t.circle(size / 2)
        t.end_fill()
    
    # 随机在小屋周围绘制各种花朵
    flower_positions = [
        (house_x - 80, house_y + 10),
        (house_x - 120, house_y + 8),
        (house_x - 40, house_y + 15),
        (house_x + house_width + 30, house_y + 12),
        (house_x + house_width + 70, house_y + 15),
        (house_x + house_width + 50, house_y + 8),
        (x_center - 180, bottom_edge + ground_height + 10),
        (x_center - 140, bottom_edge + ground_height + 15)
    ]
    
    # 绘制草丛作为装饰
    for i in range(20):
        grass_x = random.randint(int(left_edge + 30), int(right_edge - 30))
        grass_y = bottom_edge + ground_height
        t.penup()
        t.goto(grass_x, grass_y)
        t.pendown()
        t.color("dark green")
        t.setheading(90)  # 向上
        
        # 绘制3-5根草
        for _ in range(random.randint(3, 5)):
            t.penup()
            t.goto(grass_x + random.randint(-3, 3), grass_y)
            t.pendown()
            t.setheading(90 + random.randint(-15, 15))  # 随机偏移角度
            t.pensize(1)
            t.forward(random.randint(5, 15) * scale)
    
    # 确定每个位置绘制哪种花
    flower_types = [draw_daisy, draw_tulip, draw_sunflower]
    
    for pos_x, pos_y in flower_positions:
        # 随机选择一种花绘制
        flower_func = random.choice(flower_types)
        flower_func(pos_x, pos_y, 8 * scale)
        
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("black")
    t.write("春眠不觉晓", align="center", font=default_font)

# 场景2：处处闻啼鸟
def scene2():
    """绘制右上角场景：鸟鸣的春天"""
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
    
    # 绘制地面 - 使用明亮的绿色
    ground_height = 100 * scale
    t.penup()
    t.goto(left_edge, bottom_edge + ground_height)  # 从地面高度开始
    t.pendown()
    t.color("chartreuse")  # 明亮的黄绿色
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
    
    # 绘制树木 - 避免树木重叠
    tree_positions = []  # 存储已放置的树的位置
    min_tree_distance = 50 * scale  # 树之间的最小距离
    max_attempts = 20  # 每棵树最大尝试次数
    
    for _ in range(6):
        placed = False
        attempts = 0
        
        # 尝试找到合适的位置
        while not placed and attempts < max_attempts:
            # 生成随机位置
            tree_x = random.randint(int(left_edge + 50), int(right_edge - 50))
            tree_y = bottom_edge + ground_height  # y位置固定在地面上
            
            # 检查与现有树的距离
            valid_position = True
            for pos_x, pos_y in tree_positions:
                distance = ((tree_x - pos_x) ** 2) ** 0.5  # 只检查x轴距离
                if distance < min_tree_distance:
                    valid_position = False
                    break
            
            if valid_position:
                # 找到合适的位置，放置树
                tree_positions.append((tree_x, tree_y))
                draw_tree(tree_x, tree_y, scale * 0.8)
                placed = True
            
            attempts += 1
    
    # 如果因为空间不够没有放置所有的树，可以尝试放置剩余的树
    # 但使用较小的尺寸和较小的最小距离
    remaining_trees = 6 - len(tree_positions)
    
    if remaining_trees > 0:
        min_tree_distance = 30 * scale  # 较小的最小距离
        
        for _ in range(remaining_trees):
            placed = False
            attempts = 0
            
            while not placed and attempts < max_attempts:
                tree_x = random.randint(int(left_edge + 40), int(right_edge - 40))
                tree_y = bottom_edge + ground_height
                
                valid_position = True
                for pos_x, pos_y in tree_positions:
                    distance = ((tree_x - pos_x) ** 2) ** 0.5
                    if distance < min_tree_distance:
                        valid_position = False
                        break
                
                if valid_position:
                    tree_positions.append((tree_x, tree_y))
                    draw_tree(tree_x, tree_y, scale * 0.6)  # 使用较小的缩放比例
                    placed = True
                
                attempts += 1
    
    # 在地面上添加花朵装饰 - 这部分需要移到树木绘制之后
    def draw_simple_flower(x, y, size=1.0):
        """绘制简单的小花"""
        flower_colors = ["yellow", "pink", "purple", "white", "light blue", "red"]
        center_colors = ["gold", "orange", "dark red"]
        
        # 花茎
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("green")
        t.pensize(2)
        t.setheading(90)  # 向上
        t.forward(10 * size)
        t.pensize(1)
        
        # 花朵
        flower_color = random.choice(flower_colors)
        center_color = random.choice(center_colors)
        
        # 花瓣
        t.penup()
        t.goto(x, y + 10 * size)
        t.pendown()
        t.color(flower_color)
        t.begin_fill()
        
        for i in range(6):  # 六瓣花
            t.setheading(i * 60)
            # 绘制椭圆形花瓣
            t.circle(5 * size, 180)
            t.left(90)
            t.circle(5 * size, 180)
            t.left(90)
        t.end_fill()
        
        # 花蕊
        t.penup()
        t.goto(x, y + 10 * size)
        t.pendown()
        t.color(center_color)
        t.begin_fill()
        t.circle(3 * size)
        t.end_fill()
    
    # 在地面上随机添加花朵，避开树木位置
    flowers_count = 20  # 添加的花朵数量
    flower_min_distance = 15 * scale  # 花朵之间的最小距离
    
    # 创建花朵位置列表
    flower_positions = []
    
    # 尝试放置花朵
    for _ in range(flowers_count):
        max_attempts = 15
        attempts = 0
        placed = False
        
        while not placed and attempts < max_attempts:
            # 随机位置
            flower_x = random.randint(int(left_edge + 30), int(right_edge - 30))
            flower_y = bottom_edge + ground_height
            
            # 检查与树木的距离
            valid_position = True
            for tree_x, tree_y in tree_positions:
                if abs(flower_x - tree_x) < 25 * scale:  # 避开树木周围
                    valid_position = False
                    break
            
            # 检查与其他花朵的距离
            for other_x, other_y in flower_positions:
                if ((flower_x - other_x) ** 2) ** 0.5 < flower_min_distance:
                    valid_position = False
                    break
            
            if valid_position:
                flower_positions.append((flower_x, flower_y))
                draw_simple_flower(flower_x, flower_y, scale * 0.7)
                placed = True
            
            attempts += 1
    
    # 额外添加一些草丛和野花
    for _ in range(15):
        grass_x = random.randint(int(left_edge + 20), int(right_edge - 20))
        grass_y = bottom_edge + ground_height
        
        # 确保不与树木和花朵重叠
        valid_position = True
        for tree_x, tree_y in tree_positions:
            if abs(grass_x - tree_x) < 20 * scale:
                valid_position = False
                break
        
        for flower_x, flower_y in flower_positions:
            if abs(grass_x - flower_x) < 10 * scale:
                valid_position = False
                break
        
        if valid_position:
            # 绘制草丛
            t.penup()
            t.goto(grass_x, grass_y)
            t.color("forest green")
            t.pendown()
            
            for i in range(random.randint(3, 7)):
                t.penup()
                t.goto(grass_x + random.randint(-5, 5), grass_y)
                t.pendown()
                t.setheading(90 + random.randint(-20, 20))
                t.pensize(1)
                t.forward(random.randint(5, 12) * scale)
    
    # 绘制鸟
    for _ in range(8):
        bird_x = random.randint(int(left_edge + 50), int(right_edge - 50))
        bird_y = random.randint(int(bottom_edge + ground_height + 100), int(top_edge - 100))
        draw_bird(bird_x, bird_y, scale*0.8)
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("black")
    t.write("处处闻啼鸟", align="center", font=default_font)

# 场景3：夜来风雨声
def scene3():
    """绘制左下角场景：夜晚的风雨"""
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
    
    # 绘制地面 - 使用湿润的深色
    ground_height = 120 * scale
    t.penup()
    t.goto(left_edge, bottom_edge)  # 区域左下角
    t.pendown()
    t.color("dark olive green")  # 湿润的橄榄绿色
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
    
    # 添加雨水痕迹
    t.color("midnight blue")
    for _ in range(20):
        puddle_x = random.randint(int(left_edge + 30), int(right_edge - 30))
        puddle_y = bottom_edge + ground_height - 5
        puddle_size = random.randint(5, 15)
        t.penup()
        t.goto(puddle_x, puddle_y)
        t.pendown()
        t.begin_fill()
        t.circle(puddle_size / 2)
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
    
    # 在窗户上添加雨水流痕
    t.pensize(1)
    for i in range(5):
        streak_x = window_x + (i+1) * window_width/6
        t.penup()
        t.goto(streak_x, window_y + window_height)
        t.pendown()
        t.color("light blue")
        # 蜿蜒的雨水痕迹
        t.setheading(270)
        for j in range(int(window_height)):
            t.forward(1)
            if random.random() < 0.3:  # 30%的概率微微偏转
                t.right(random.randint(1, 3))
            if random.random() < 0.3:
                t.left(random.randint(1, 3))
    
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
    
    # 绘制闪电 - 添加多道闪电
    lightning_positions = [
        (x_center - 100, y_center + 160),
        (x_center + 50, y_center + 140),
        (x_center - 150, y_center + 180)
    ]
    
    for lx, ly in lightning_positions:
        # 随机决定是否绘制这道闪电
        if random.random() < 0.7:  # 70%的概率绘制
            t.penup()
            t.goto(lx, ly)
            t.pendown()
            t.pensize(random.randint(2, 5))  # 不同粗细的闪电
            t.color("yellow")
            t.setheading(270)
            
            # 第一段
            length1 = random.randint(40, 60) * scale
            t.forward(length1)
            
            # 转弯
            angle = random.choice([30, 45, 60])
            direction = random.choice([-1, 1])  # 随机左转或右转
            t.left(angle * direction)
            
            # 第二段
            length2 = random.randint(20, 35) * scale
            t.forward(length2)
            
            # 再转弯，往相反方向
            t.right(angle * direction * 2)  # 转两倍角度到反方向
            
            # 第三段
            length3 = random.randint(40, 70) * scale
            t.forward(length3)
    
    t.pensize(1)  # 恢复默认线宽
    
    # 绘制被风吹动的树枝
    t.penup()
    t.goto(x_center - 180, bottom_edge + ground_height)
    t.pendown()
    t.color("sienna")
    t.pensize(3)
    t.setheading(80)  # 略微倾斜的树干
    t.forward(70 * scale)
    
    # 绘制被风吹弯的树枝
    branch_start_x = x_center - 180
    branch_start_y = bottom_edge + ground_height + 70 * scale
    
    # 主要树枝
    branches = [
        (branch_start_x, branch_start_y, 45, 40),  # (x, y, 角度, 长度)
        (branch_start_x, branch_start_y, 30, 35),
        (branch_start_x, branch_start_y, 60, 30)
    ]
    
    for bx, by, angle, length in branches:
        t.penup()
        t.goto(bx, by)
        t.pendown()
        t.setheading(angle)
        t.forward(length * scale)
        
        # 添加树叶，被风吹动
        leaf_x = t.xcor()
        leaf_y = t.ycor()
        t.color("dark green")
        t.pensize(1)
        
        # 绘制被风吹曲的树叶
        t.setheading(angle - 30)  # 向风的方向弯曲
        t.begin_fill()
        for i in range(3):  # 三角形树叶
            t.forward(15 * scale)
            t.right(120)
        t.end_fill()
    
    t.pensize(1)  # 恢复默认线宽
    
    # 增加雨水积聚和流动效果
    puddle_positions = [
        (x_center - 30, bottom_edge + 10),
        (x_center - 150, bottom_edge + 15),
        (house_x + house_width + 20, bottom_edge + 5)
    ]
    
    for px, py in puddle_positions:
        # 绘制水坑
        t.penup()
        t.goto(px, py)
        t.pendown()
        t.color("midnight blue")
        t.begin_fill()
        t.setheading(0)
        
        # 不规则形状的水坑
        for i in range(8):
            t.forward(random.randint(10, 20) * scale)
            t.left(45)
        t.end_fill()
        
        # 添加水波纹
        t.penup()
        t.goto(px + 5, py + 5)
        t.pendown()
        t.color("steel blue")
        for i in range(3):  # 3个同心圆
            t.circle(i * 3 * scale)
    
    # 绘制雨滴
    t.color("white")
    for _ in range(45):  # 增加雨滴数量
        x = random.randint(int(left_edge + 10), int(right_edge - 10))
        y = random.randint(int(bottom_edge + ground_height), int(top_edge - 10))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(2)
        
        # 根据风向调整雨滴角度
        wind_angle = 260 + random.randint(-5, 25)  # 更倾斜的角度表示大风
        t.setheading(wind_angle)
        
        # 随机雨滴长度
        rain_length = random.randint(15, 25) * scale
        t.forward(rain_length)
    
    # 恢复默认线宽
    t.pensize(1)
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("white")
    t.write("夜来风雨声", align="center", font=default_font)

# 场景4：花落知多少
def scene4():
    """绘制右下角场景：落花的春天"""
    # 定义右下区域的边界
    left_edge = 0
    right_edge = 500
    bottom_edge = -500
    top_edge = 0
    
    # 计算区域中心点
    x_center = (left_edge + right_edge) / 2  # 250
    y_center = (bottom_edge + top_edge) / 2  # -250
    
    scale = 1.0  # 缩放比例
    
    # 绘制背景 - 修改背景色为更淡的蓝色
    t.penup()
    t.goto(left_edge, top_edge)  # 区域左上角
    t.setheading(0)  # 确保方向正确
    t.pendown()
    t.color("pale turquoise")  # 更淡的蓝色背景，与河流区分
    t.begin_fill()
    for _ in range(4):
        t.forward(right_edge - left_edge)  # 区域宽度
        t.right(90)
    t.end_fill()
    
    # 绘制地面 - 使用带有花瓣色调的绿色
    ground_height = 120 * scale
    t.penup()
    t.goto(left_edge, bottom_edge)  # 区域左下角
    t.pendown()
    t.color("medium spring green")  # 春天的绿色
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
    
    # 定义花瓣颜色 - 移到前面，避免引用错误
    petal_colors = ["pink", "light pink", "hot pink", "deep pink"]
    
    # 为地面添加一些粉色调和花瓣痕迹
    t.color("misty rose")
    for _ in range(15):
        mark_x = random.randint(int(left_edge + 50), int(right_edge - 50))
        mark_y = bottom_edge + random.randint(10, int(ground_height - 10))
        mark_size = random.randint(10, 25)
        t.penup()
        t.goto(mark_x, mark_y)
        t.pendown()
        t.begin_fill()
        # 半透明的花痕
        for i in range(5):
            t.setheading(i * 72)
            t.forward(mark_size)
            t.right(144)
            t.forward(mark_size)
            t.right(144)
        t.end_fill()
    
    # 简化河流绘制 - 使用简单的曲线
    river_start_x = left_edge + 50
    river_start_y = bottom_edge + ground_height/4
    
    # 定义河流路径的控制点 - 使用简单的S形曲线
    river_width = 30 * scale
    river_points = []
    
    t.penup()
    t.goto(river_start_x, river_start_y)
    t.pendown()
    t.color("dodger blue")  # 使用明亮的蓝色
    t.begin_fill()
    
    # 顶部边缘
    t.setheading(0)  # 向右
    
    # 第一段 - 右上方向
    t.forward(100 * scale)
    point1_x, point1_y = t.position()
    river_points.append((point1_x, point1_y - river_width/2))  # 记录中点作为花瓣位置
    
    # 转向
    t.setheading(45)  # 右上角度
    t.forward(80 * scale)
    point2_x, point2_y = t.position()
    river_points.append((point2_x, point2_y - river_width/2))
    
    # 再转向
    t.setheading(0)  # 向右
    t.forward(120 * scale)
    point3_x, point3_y = t.position()
    river_points.append((point3_x, point3_y - river_width/2))
    
    # 转向下方
    t.setheading(-45)  # 右下角度
    t.forward(80 * scale)
    point4_x, point4_y = t.position()
    river_points.append((point4_x, point4_y - river_width/2))
    
    # 最后一段
    t.setheading(0)  # 向右
    t.forward(100 * scale)
    end_x, end_y = t.position()
    
    # 下边缘 - 宽度固定
    t.setheading(180)  # 向左
    t.penup()
    t.goto(end_x, end_y + river_width)
    t.pendown()
    
    # 反向绘制每一段
    t.forward(100 * scale)
    t.setheading(135)  # 左上角度
    t.forward(80 * scale)
    t.setheading(180)  # 向左
    t.forward(120 * scale)
    t.setheading(225)  # 左下角度
    t.forward(80 * scale)
    t.setheading(180)  # 向左
    t.forward(100 * scale)
    
    # 闭合路径
    t.goto(river_start_x, river_start_y)
    t.end_fill()
    
    # 添加河流边缘线，增强视觉效果
    t.penup()
    t.goto(river_start_x, river_start_y)
    t.pendown()
    t.pensize(2)
    t.color("steel blue")
    
    # 重新绘制上边缘
    t.setheading(0)
    t.forward(100 * scale)
    t.setheading(45)
    t.forward(80 * scale)
    t.setheading(0)
    t.forward(120 * scale)
    t.setheading(-45)
    t.forward(80 * scale)
    t.setheading(0)
    t.forward(100 * scale)
    
    # 绘制下边缘
    t.penup()
    t.goto(end_x, end_y + river_width)
    t.pendown()
    t.setheading(180)
    t.forward(100 * scale)
    t.setheading(135)
    t.forward(80 * scale)
    t.setheading(180)
    t.forward(120 * scale)
    t.setheading(225)
    t.forward(80 * scale)
    t.setheading(180)
    t.forward(100 * scale)
    
    t.pensize(1)  # 恢复默认线宽
    
    # 在河流上放置花瓣 - 使用预定义点
    more_river_points = []
    # 添加更多的河流中心点
    for point in river_points:
        px, py = point
        # 围绕原始点添加几个新点
        for _ in range(3):
            offset_x = random.uniform(-20, 20) * scale
            offset_y = random.uniform(-5, 5) * scale
            more_river_points.append((px + offset_x, py + offset_y))
    
    # 合并点列表
    river_points.extend(more_river_points)
    
    # 在河流上随机放置花瓣
    river_petal_count = 10
    
    # 确保河流点不为空
    if river_points:
        for _ in range(river_petal_count):
            # 随机选择一个点
            point = random.choice(river_points)
            petal_x, petal_y = point
            draw_petal(petal_x, petal_y, random.choice(petal_colors), scale * random.uniform(1.0, 1.5))
    
    # 添加石头
    stone_count = 6
    for _ in range(stone_count):
        if river_points:
            point = random.choice(river_points)
            stone_x, stone_y = point
            stone_x += random.uniform(-15, 15) * scale
            stone_y += random.uniform(-5, 15) * scale
            stone_size = random.randint(5, 12) * scale
            
            t.penup()
            t.goto(stone_x, stone_y)
            t.pendown()
            t.color("gray")
            t.begin_fill()
            t.circle(stone_size)
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
    

    # 地面上的花瓣
    for _ in range(30):
        petal_x = random.randint(int(left_edge + 30), int(right_edge - 30))
        petal_y = random.randint(int(bottom_edge + 15), int(bottom_edge + ground_height - 15))
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale)
    
    # 空中飘落的花瓣
    for _ in range(20):
        petal_x = random.randint(int(crown_x - crown_radius*2.5), int(crown_x + crown_radius*2.5))
        petal_y = random.randint(int(trunk_y + trunk_height/2), int(trunk_y + trunk_height + crown_radius*2))
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale)
    
    # 添加远处的几棵树 - 增加层次感
    distant_trees = [
        (left_edge + 70, bottom_edge + ground_height, 0.5),  # (x, y, scale)
        (left_edge + 400, bottom_edge + ground_height, 0.7),
        (right_edge - 50, bottom_edge + ground_height, 0.4)
    ]
    
    for tree_x, tree_y, tree_scale in distant_trees:
        # 树干
        trunk_width_far = 25 * tree_scale
        trunk_height_far = 80 * tree_scale
        
        t.penup()
        t.goto(tree_x, tree_y)
        t.pendown()
        t.color("brown")
        t.begin_fill()
        t.setheading(0)
        for _ in range(2):
            t.forward(trunk_width_far)
            t.left(90)
            t.forward(trunk_height_far)
            t.left(90)
        t.end_fill()
        
        # 树冠
        crown_radius_far = 60 * tree_scale
        crown_x_far = tree_x + trunk_width_far/2
        crown_y_far = tree_y + trunk_height_far
        
        t.penup()
        t.goto(crown_x_far, crown_y_far)
        t.pendown()
        # 随机不同深浅的粉色
        t.color(random.choice(["light pink", "pink", "misty rose"]))
        t.begin_fill()
        t.circle(crown_radius_far)
        t.end_fill()
    
    # 替换人物为石凳和落花 - 表现"人去花还在"的意境
    bench_x = x_center - 120
    bench_y = bottom_edge + ground_height
    bench_scale = 0.9 * scale
    
    # 绘制石凳
    t.penup()
    t.goto(bench_x, bench_y)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    
    # 凳子座面
    t.setheading(0)
    seat_width = 50 * bench_scale
    seat_height = 15 * bench_scale
    for _ in range(2):
        t.forward(seat_width)
        t.left(90)
        t.forward(seat_height)
        t.left(90)
    t.end_fill()
    
    # 凳子腿
    leg_width = 8 * bench_scale
    leg_height = 20 * bench_scale
    leg_positions = [
        bench_x + 5 * bench_scale,
        bench_x + (seat_width - 5 * bench_scale - leg_width)
    ]
    
    for leg_x in leg_positions:
        t.penup()
        t.goto(leg_x, bench_y - leg_height)
        t.pendown()
        t.begin_fill()
        for _ in range(2):
            t.forward(leg_width)
            t.left(90)
            t.forward(leg_height)
            t.left(90)
        t.end_fill()
    
    # 在凳子上和周围添加更多落花，表现刚刚有人离开的感觉
    for _ in range(15):
        petal_x = bench_x + random.uniform(0, seat_width)
        petal_y = bench_y + random.uniform(0, seat_height)
        draw_petal(petal_x, petal_y, random.choice(petal_colors), scale * random.uniform(0.8, 1.2))
    
    # 添加一只停在凳子上的小鸟，正在看花瓣
    bird_x = bench_x + seat_width * 0.75
    bird_y = bench_y + seat_height
    
    # 绘制更精细的小鸟
    t.penup()
    t.goto(bird_x, bird_y)
    t.pendown()
    t.color("black")
    
    # 鸟身体
    t.begin_fill()
    t.circle(8 * bench_scale)
    t.end_fill()
    
    # 鸟头
    t.penup()
    t.goto(bird_x + 5 * bench_scale, bird_y + 10 * bench_scale)
    t.pendown()
    t.begin_fill()
    t.circle(5 * bench_scale)
    t.end_fill()
    
    # 鸟嘴
    t.penup()
    t.goto(bird_x + 10 * bench_scale, bird_y + 12 * bench_scale)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.setheading(0)
    for _ in range(3):  # 三角形嘴
        t.forward(6 * bench_scale)
        t.left(120)
    t.end_fill()
    
    # 鸟眼睛
    t.penup()
    t.goto(bird_x + 7 * bench_scale, bird_y + 14 * bench_scale)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(1.5 * bench_scale)
    t.end_fill()
    
    # 眼球
    t.penup()
    t.goto(bird_x + 7 * bench_scale, bird_y + 15 * bench_scale)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(0.8 * bench_scale)
    t.end_fill()
    
    # 添加地面上的小花
    flower_positions = [
        (bench_x - 30 * bench_scale, bench_y - 10 * bench_scale),
        (bench_x + seat_width + 25 * bench_scale, bench_y - 5 * bench_scale),
        (bench_x + seat_width/2, bench_y - leg_height - 5 * bench_scale)
    ]
    
    for fx, fy in flower_positions:
        # 花茎
        t.penup()
        t.goto(fx, fy)
        t.pendown()
        t.color("green")
        t.pensize(2)
        t.setheading(90)
        t.forward(15 * bench_scale)
        t.pensize(1)
        
        # 花朵
        t.color(random.choice(["yellow", "white", "lavender"]))
        t.begin_fill()
        flower_top_y = fy + 15 * bench_scale
        t.penup()
        t.goto(fx, flower_top_y)
        t.pendown()
        
        # 绘制花瓣
        for i in range(8):
            t.setheading(i * 45)
            t.forward(8 * bench_scale)
            t.backward(8 * bench_scale)
        t.end_fill()
        
        # 花蕊
        t.penup()
        t.goto(fx, flower_top_y)
        t.pendown()
        t.color("orange")
        t.begin_fill()
        t.circle(3 * bench_scale)
        t.end_fill()
    
    # 添加蝴蝶和其他飞行昆虫
    butterflies_count = 5
    for _ in range(butterflies_count):
        butterfly_x = random.randint(int(left_edge + 100), int(right_edge - 100))
        butterfly_y = random.randint(int(bottom_edge + ground_height + 50), int(top_edge - 100))
        butterfly_size = random.randint(5, 10) * scale
        butterfly_colors = ["yellow", "white", "light blue", "lavender"]
        
        # 蝴蝶身体
        t.penup()
        t.goto(butterfly_x, butterfly_y)
        t.pendown()
        t.color("black")
        t.pensize(2)
        t.setheading(0)
        t.forward(butterfly_size)
        t.pensize(1)
        
        # 蝴蝶翅膀
        t.color(random.choice(butterfly_colors))
        t.penup()
        t.goto(butterfly_x + butterfly_size/2, butterfly_y)
        t.pendown()
        t.begin_fill()
        
        # 左翅
        t.setheading(120)
        t.circle(butterfly_size * 2, 60)
        t.left(30)
        t.circle(butterfly_size, 60)
        t.setheading(-60)
        t.forward(butterfly_size * 2)
        
        # 右翅
        t.penup()
        t.goto(butterfly_x + butterfly_size/2, butterfly_y)
        t.pendown()
        t.setheading(60)
        t.circle(-butterfly_size * 2, 60)
        t.right(30)
        t.circle(-butterfly_size, 60)
        t.setheading(-120)
        t.forward(butterfly_size * 2)
        
        t.end_fill()
    
    # 写场景文字
    t.penup()
    t.goto(x_center, top_edge - 60)
    t.color("black")
    t.write("花落知多少", align="center", font=default_font)

# 写诗标题
def write_poem_title():
    """在画布顶部写诗的标题"""
    t.penup()
    t.goto(0, 550)  # 标题位置
    t.color("black")
    t.write("春晓 - 孟浩然", align="center", font=title_font)

# 绘制整体画面
write_poem_title()  # 绘制标题
draw_grid()         # 绘制分隔线
scene1()            # 绘制场景1
scene2()            # 绘制场景2
scene3()            # 绘制场景3
scene4()            # 绘制场景4

# 保持画面显示
turtle.mainloop()  # 保持窗口打开