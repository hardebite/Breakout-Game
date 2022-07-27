
from turtle import Turtle
import random


COLORS = ["yellow","green","orange","red"]
COUNT = 0
position=[-350,-250,-150,-50,50,150,250,350]
class CarManager():

    def __init__(self):
        self.cars1= []
        self.cars2 = []
        self.cars3 = []
        self.cars4 = []
        self.create_first_line()
        self.create_second()
        self.create_third()
        self.create_fourth()


    def create_first_line(self):
        random_chance = random.randint(1, 6)
        global new_car
        for items in position:

            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=5)
            new_car.penup()
            new_car.color(COLORS[3])
            new_car.goto(items, 280)
            self.cars1.append(new_car)



    def create_second(self):
        random_chance = random.randint(1, 6)
        for items in position:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=5)
            new_car.penup()
            new_car.color(COLORS[2])
            new_car.goto(items, 250)
            self.cars2.append(new_car)

    def create_third(self):
        random_chance = random.randint(1, 6)
        for items in position:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=5)
            new_car.penup()
            new_car.color(COLORS[1])
            new_car.goto(items, 220)
            self.cars3.append(new_car)


    def create_fourth(self):
        random_chance = random.randint(1, 6)
        for items in position:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=5)
            new_car.penup()
            new_car.color(COLORS[0])
            new_car.goto(items, 190)
            self.cars4.append(new_car)


    def destroy1(self,x,y):
        for items in self.cars1:
            y_cordinate=items.ycor()
            x_cordinate=items.xcor()
            x_location= x-x_cordinate
            y_location = y-y_cordinate
            if x_location <40 and x_location > -40 :
                if y_location < 20 and y_location > -20:
                    items.reset()
                    return True

    def destroy2(self,x,y):
        for items in self.cars2:
            y_cordinate=items.ycor()
            x_cordinate=items.xcor()
            x_location= x-x_cordinate
            y_location = y-y_cordinate
            if x_location < 40 and x_location > -40:
                if y_location < 20 and y_location > -20:
                    items.reset()
                    return True

    def destroy3(self,x,y):
        # print(x,y)
        for items in self.cars3:
            y_cordinate=items.ycor()
            x_cordinate=items.xcor()
            x_location= x-x_cordinate
            y_location = y-y_cordinate
            if x_location <40 and x_location > -40 :
                if y_location < 20 and y_location > -20:
                    items.reset()
                    return True

    def destroy4(self,x,y):
        for items in self.cars4:
            y_cordinate=items.ycor()
            x_cordinate=items.xcor()
            x_location= x-x_cordinate
            y_location = y-y_cordinate
            if x_location <40 and x_location > -40 :
                if y_location <20 and y_location > -20 :
                    items.reset()
                    return True



