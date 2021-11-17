# Falling dodger Game in Python By Steven Weinstein on 11-10-2021
# importing required modules
import turtle
import os
import time
import random
TK_SILENCE_DEPRECATION=1
fallers = 1
delay = 0.00625
score = 0
highscoredoc = open(os.path.expanduser("~/Desktop/DodgerGame/highest_score_local.txt"), "r+")
highscore = highscoredoc.read()
# Creating a window screen
wn = turtle.Screen()
wn.title("Dodger Game Beta 0.1r4")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)
# head of the avoider
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, -280)
head.direction = "Stop"

# fallers in the game
faller = turtle.Turtle()
faller.speed(0)
faller.shape("square")
faller.color("green")
faller.penup()
xpos = random.randint(-280, 280)
global ypos
ypos = 290
faller.goto(xpos, ypos)
faller2 = turtle.Turtle()
faller2.speed(0)
faller2.shape("square")
faller2.color("green")
faller2.penup()
xpos2 = random.randint(-280, 280)
global ypos2
ypos2 = 290
faller2.goto(xpos2, ypos2)
faller3 = turtle.Turtle()
faller3.speed(0)
faller3.shape("square")
faller3.color("green")
faller3.penup()
xpos3 = random.randint(-280, 280)
global ypos3
ypos3 = 290
faller3.goto(xpos2, ypos2)
fallspeed = 1.5

# pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.shapesize(24)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.clear()
pen.write(f"Score : 0  High Score : {highscore}", align="center",
          font=("helvetica", 20, "bold"))

# assigning keys
def goleft():
    head.direction = "right"
def goright():
    head.direction = "left"
def stop():
    head.direction = "Stop"

def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x-3)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x+3)
wn.listen()
wn.onkeypress(goright, "Right")
wn.onkeypress(goleft, "Left")
wn.onkeypress(stop, " ")
# main loop
while True:
    wn.update()
    if score > int(highscore):
        highscore = score
        highscoredoc.seek(0)
        highscoredoc.write(str(highscore))
    ypos = ypos-fallspeed*2
    faller.goto(xpos, ypos)
    ypos2 = ypos2-fallspeed*2
    faller2.goto(xpos2, ypos2)
    ypos3 = ypos3-fallspeed*2
    faller3.goto(xpos3, ypos3)
    move()
    if head.distance(faller) < 20:
        score -= 1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
                score, highscore), align="center", font=("helvetica", 20, "bold"))
        xpos = random.randint(-280, 280)
        ypos = 290
        faller.goto(xpos, ypos)
    if ypos < -280 and head.distance(faller) > 20:
        score += 1
        xpos = random.randint(-280, 280)
        ypos = 290
        faller.goto(xpos, ypos)
        fallspeed += 0.005
    if ypos2 < -280 and head.distance(faller2) > 20:
        score += 1
        xpos2 = random.randint(-280, 280)
        ypos2 = 290
        faller2.goto(xpos, ypos)
        fallspeed += 0.005
        
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, -280)
        head.direction = "Stop"
    pen.clear()
    if int(score) < 0:
        pen.goto(0, 100)
        pen.write("GAME OVER!\nrestart game", align="center", font=("helvetica", 20, "bold"))
        fallspeed = 0
    else:
        pen.write("Score : {} High Score : {} ".format(
                score, highscore), align="center", font=("helvetica", 20, "bold"))
    time.sleep(delay)
wn.mainloop()