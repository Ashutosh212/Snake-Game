from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("/home/ab/Documents/100-python/100 days python/snake game/data.txt",) as file:
            self.high_score=int(file.read())
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align="center", font=("Arial", 16, "normal"))
        self.hideturtle()

    def print_score(self):
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align="center", font=("Arial", 16, "normal"))
    
    def score_plus_one(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("E:/100 days python/snake game/data.txt", mode= "w") as file:
                file.write(f"{self.high_score}")
        self.score=0
    
    def print_score_new(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align="center", font=("Arial", 16, "normal"))
