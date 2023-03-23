from turtle import Turtle, Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.screen1=Screen()
        # self.screen1.tracer(0)
        self.shape("circle")
        self.shapesize(.5, .5)
        self.penup()
        self.refresh()
        # self.screen1.update()
    
    def refresh(self):
        x_1=random.randint(-250, 250)
        y_1=random.randint(-250, 250)
        self.goto(x_1, y_1)