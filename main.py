from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen=Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
snake1=Snake()
food=Food()
s=Score()
t=True
screen.listen()
while t:
    screen.update()
    time.sleep(.1)
    snake1.move()
    screen.onkey(snake1.up, "Up")
    screen.onkey(snake1.down, "Down")
    screen.onkey(snake1.bk, "Left")
    screen.onkey(snake1.fd, "Right")
    # time.sleep(1)
    if snake1.turtles[0].distance(food)<20:
        food.refresh()
        # s.score+=1
        s.score_plus_one()
        s.print_score()
        snake1.extend()
    if snake1.turtles[0].xcor()>300 or snake1.turtles[0].xcor()<-300 or snake1.turtles[0].ycor()<-300 or snake1.turtles[0].ycor()>300:
        s.reset()
        snake1.reset()
        s.print_score_new()
    for i in range(0, len(snake1.turtles)):
        if i!=0:
            if snake1.turtles[0].distance(snake1.turtles[i])<20:
                s.reset()
                snake1.reset()
                s.print_score_new()
                
                
                
                
                
screen.exitonclick()