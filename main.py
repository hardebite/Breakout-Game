from turtle import Turtle,Screen
from paddle import *
from ball import *
from car_manager import CarManager
import time
COLORS = ["yellow","green","orange","red"]
screen = Screen()
screen.title("Break Out Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
paddle=Paddle((0,-250))

screen.listen()
screen.onkey(paddle.go_left,"Up")
screen.onkey(paddle.go_right,"Down")
ball=Ball()
car_manager=CarManager()
car_manager.create_first_line()
def ball_location():
    global x
    global y
    x=ball.xcor()
    y= ball.ycor()
game_is_on = True
while game_is_on:
    screen.update()

    ball.move()

    # Detect collision with wall
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() > -250 :
        ball.bounce_y()


    if ball.ycor() > 100 :
        ball_location()

        if car_manager.destroy4(x,y):
            print("4")
            ball.bounce_y()
        elif car_manager.destroy3(x, y):
            print("3")
            ball.bounce_y()
        elif car_manager.destroy2(x, y):
            print("2")
            ball.bounce_y()
        elif car_manager.destroy1(x, y):
            print("1")
            ball.bounce_y()
    if ball.ycor() < -370:
        ball.reset_position()








screen.exitonclick()