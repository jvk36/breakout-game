import turtle
import time
from scoreboard import Scoreboard

# Screen setup
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turns off screen updates

# Paddle setup
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball setup
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 10  # 0.15
ball.dy = 10  # 0.15

# Brick setup
brick_color = "red"
bricks = []
for x in range(-350, 400, 100):
    for y in range(150, 250, 50):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(brick_color)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# Scoreboard setup
scoreboard = Scoreboard()

# Functions
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy *= -1

    # Paddle and ball collision
    if (ball.ycor() > paddle.ycor() - 10 and ball.ycor() < paddle.ycor() + 10) and (ball.xcor() > paddle.xcor() - 75 and ball.xcor() < paddle.xcor() + 75):
        # print("Paddle and Ball Collision")
        ball.sety(-230)
        ball.dy *= -1

    # Brick and ball collision
    for brick in bricks:
        if (ball.ycor() > brick.ycor() - 10 and ball.ycor() < brick.ycor() + 10) and (ball.xcor() > brick.xcor() - 40 and ball.xcor() < brick.xcor() + 40):
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.point()
    
    time.sleep(0.1)  # Adjust for frame rate

# Keep the window open
turtle.done()
