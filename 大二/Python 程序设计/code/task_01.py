import turtle
import math

# 初始化设置
turtle.setup(800, 600)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)

def draw_moon(x, y):
    """绘制带光晕的满月"""
    # 主月体
    turtle.color("#FFD700")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    
    # 光晕效果
    for i in range(12):
        angle = math.radians(i * 30)
        turtle.penup()
        turtle.goto(x + 60 * math.cos(angle), y + 60 * math.sin(angle) + 60)
        turtle.pendown()
        turtle.dot(15 - i//2, "#FFD700" if i%2 else "#FFA500")

def draw_mooncake(x, y):
    """绘制传统纹样月饼"""
    # 饼身
    turtle.color("#D4AF37")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    
    # 传统纹样
    turtle.color("#8B4513")
    for _ in range(8):
        turtle.penup()
        turtle.goto(x, y + 30)
        turtle.pendown()
        turtle.circle(30, 45)
        turtle.right(90)
        turtle.forward(15)
        turtle.backward(15)
        turtle.left(90)
    
    # 浮雕文字
    turtle.penup()
    turtle.goto(x, y + 25)
    turtle.color("red")
    turtle.write("月", align="center", font=("华文楷体", 24, "bold"))

def draw_cloud(x, y):
    """绘制云朵"""
    turtle.color("white")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.circle(30, 180)
        turtle.right(180)
    turtle.end_fill()

def draw_lantern(x, y):
    """绘制立体灯笼"""
    turtle.color("red")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40, 180)
    turtle.end_fill()
    turtle.circle(40, -180)
    turtle.forward(20)
    turtle.circle(40, 180)
    turtle.end_fill()

def scene1():
    """第一格：月下独思"""
    turtle.setworldcoordinates(-400, 300, 0, 0)
    draw_moon(-200, 100)
    
    # 绘制云朵
    draw_cloud(-300, 150)
    draw_cloud(-150, 180)

def scene2():
    """第二格：阖家共餐"""
    turtle.setworldcoordinates(0, 300, 400, 0)
    
    # 餐桌
    turtle.color("#8B4513")
    turtle.penup()
    turtle.goto(100, 200)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    
    # 摆放月饼
    draw_mooncake(120, 150)
    draw_mooncake(180, 150)
    draw_mooncake(240, 150)

def scene3():
    """第三格：童嬉花灯"""
    turtle.setworldcoordinates(-400, 0, 0, -300)
    
    # 绘制灯笼
    for i in range(3):
        draw_lantern(-300 + i*120, -100)
    
    # 添加装饰线条
    turtle.color("#FFA500")
    for x in range(-350, 50, 100):
        turtle.penup()
        turtle.goto(x, -200)
        turtle.pendown()
        turtle.goto(x + 50, -250)
        turtle.goto(x + 100, -200)

def scene4():
    """第四格：合家赏月"""
    turtle.setworldcoordinates(0, 0, 400, -300)
    
    # 人物简笔画
    turtle.color("black")
    for i in range(3):
        x = 100 + i*80
        y = -150
        
        # 身体
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(20)  # 头
        turtle.goto(x, y - 50)  # 身体
        turtle.goto(x - 20, y - 30)  # 左手
        turtle.goto(x, y - 50)  # 回到身体
        turtle.goto(x + 20, y - 30)  # 右手
        
        # 装饰
        turtle.penup()
        turtle.goto(x - 10, y - 10)
        turtle.dot(5, "red")  # 左眼
        turtle.goto(x + 10, y - 10)
        turtle.dot(5, "red")  # 右眼
        turtle.goto(x, y - 5)
        turtle.color("red")
        turtle.write(")", font=("Arial", 12, "normal"))  # 嘴巴

def main():
    scenes = [scene1, scene2, scene3, scene4]
    for scene in scenes:
        scene()
    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()