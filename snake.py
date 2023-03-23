from turtle import Turtle
import random
color_list=["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
shape_turtle=["arrow", "turtle", "circle", "square", "triangle"]
class Snake:
    def __init__(self):
        self.turtles=[]
        self.create()

    def create(self):
        for i in range(0, 3):
            k=Turtle()
            k.shape(random.choice(shape_turtle))
            k.penup()
            k.goto(x=-200-i*25, y=0)
            k.color(random.choice(color_list))
            self.turtles.append(k)

    def extend(self):   
        x_corl=self.turtles[-1].xcor()
        y_corl=self.turtles[-1].ycor()
        k=Turtle()
        k.shape(random.choice(shape_turtle))
        k.penup()
        k.goto(x_corl, y_corl)
        k.color(random.choice(color_list))
        self.turtles.append(k)

    def reset(self):
        self.turtles.clear()
        self.create()

    def move(self):
        for t in range(len(self.turtles)-1, 0, -1):
            # print(t)
            # screen.update() 
            x_new=self.turtles[t-1].xcor()
            y_new=self.turtles[t-1].ycor()
            self.turtles[t].goto(x_new, y_new)
            self.turtles[t-1].fd(25)



    def down(self):
        if self.turtles[0].heading()!=90:
            self.turtles[0].setheading(270)
    def up(self):
        if self.turtles[0].heading()!=270:
            self.turtles[0].setheading(90)
    def bk(self):
        if self.turtles[0].heading()!=0:
            self.turtles[0].setheading(180)
    def fd(self):
        if self.turtles[0].heading()!=180:
            self.turtles[0].setheading(0)  


