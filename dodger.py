# Falling dodger Game in Python By Steven Weinstein on 12-13-2021
# importing required modules
import turtle
import os
import time
import random
TK_SILENCE_DEPRECATION=1
# fallers = 1
delay = 0.00625
score = 0
score_this_round = 0
highscoredoc = open(os.path.expanduser(
    "~/Desktop/DodgerGame/highest_score_local.txt"), "r+")
highscore = highscoredoc.read()
# Creating a window screen
wn = turtle.Screen()
wn.title("Dodger Game BETA v0.5.1")
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
fallspeed = 1.5
# main faller class
class Faller:
    def __init__(self):
        self.faller = turtle.Turtle()
        self.faller.shape("square")
        self.faller.color("green")
        self.faller.penup()
        self.randomize_location().move_down()

    def goto(self):
        self.faller.goto(self.xpos, self.ypos)
        return self

    def move_down(self):
        self.ypos -= 2 * fallspeed
        self.faller.goto(self.xpos, self.ypos)
        return self

    def randomize_location(self):
        self.xpos = random.randint(-280, 280)
        self.ypos = 290        
        return self
# fallers in the game
faller1 = Faller()
faller2 = Faller()
faller3 = Faller()
faller4 = Faller()
faller5 = Faller()

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

# assigning keystrokes
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
    faller1.move_down()
    faller2.move_down()
    faller3.move_down()
    faller4.move_down()
    faller5.move_down()
    move()
    if head.distance(faller1.faller) < 20:
        score_this_round -= 1
        pen.clear()
        pen.write(f"Score : {score} High Score : {highscore} ",
            align="center", font=("helvetica", 20, "bold"))
        faller1.randomize_location()
    if head.distance(faller2.faller) < 20:
        score_this_round -= 1
        pen.clear()
        pen.write(f"Score : {score} High Score : {highscore} ",
            align="center", font=("helvetica", 20, "bold"))
        faller1.randomize_location()
    if head.distance(faller3.faller) < 20:
        score_this_round -= 1
        pen.clear()
        pen.write(f"Score : {score} High Score : {highscore} ",
            align="center", font=("helvetica", 20, "bold"))
    if head.distance(faller4.faller) < 20:
        score_this_round -= 1
        pen.clear()
        pen.write(f"Score : {score} High Score : {highscore} ",
            align="center", font=("helvetica", 20, "bold"))
        faller1.randomize_location()
    if faller1.ypos < -280 and head.distance(faller1.faller) > 20:
        score_this_round += 1
        faller1.randomize_location()
        fallspeed += 0.005
    if faller2.ypos < -280 and head.distance(faller2.faller) > 20:
        score_this_round += 1
        faller2.randomize_location()
        fallspeed += 0.005
    if faller3.ypos < -280 and head.distance(faller3.faller) > 20:
        score_this_round += 1
        faller3.randomize_location()
        fallspeed += 0.005
    if faller4.ypos < -280 and head.distance(faller4.faller) > 20:
        score_this_round += 1
        faller4.randomize_location()
        fallspeed += 0.005
    if faller5.ypos < -280 and head.distance(faller5.faller) > 20:
        score_this_round += 1
        faller5.randomize_location()
        fallspeed += 0.005

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, -280)
        head.direction = "Stop"
    if score_this_round == 5 or score_this_round > 5:
        score += 1
        score_this_round = 0
    if int(score) < 0:
        pen.goto(0, 100)
        pen.write("GAME OVER!\nrestart game", align="center", font=("helvetica", 20, "bold"))
        fallspeed = 0
        time.sleep(3)
        break
    else:
        pen.write(f"Score : {score} High Score : {highscore} ",
            align="center", font=("helvetica", 20, "bold"))
    pen.clear()
    pen.write(f"Score : {score} High Score : {highscore} ",
        align="center", font=("helvetica", 20, "bold"))
    time.sleep(delay)
wn.mainloop()