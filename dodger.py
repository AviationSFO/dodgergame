# V2 of Falling dodger Game in Python By Steven Weinstein on 3-3-2022
# Import and initialize required modules and functions
import pygame
import random
import time
import os
import threading as thr
from platform import python_version
from pathlib import Path
script_path = Path(__file__, '..').resolve()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(script_path.joinpath("sounds/boop.mp3"))
pygame.mixer.music.set_volume(0.7)
pygame.font.init()
from pygame.locals import(
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_p,
    K_r,
    K_m,
    K_a,
    K_d,
    K_s,
    KEYUP,
    QUIT,
    K_0,
)

mute = True
print("Your python version is:")
print(python_version())
pyversion = python_version()
if "3.7" in pyversion or "3.8" in pyversion or "3.9" in pyversion or "3.10" in pyversion or "3.11" in pyversion:
    print("Python version check pass")
else:
    print("v"*20)
    print("Please upgrade your python to be version 3.7 or newer, terminating process")
    print("^"*20)
    quit()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
highscore = 0
score = 0
APIon = False
APIdata = [None, None, None, None]
APIfrun = False
global fallersurvived
fallersurvived = 0
pause = False
highscoredoc = open(script_path.joinpath("highest_score_local.txt"), "r")
highscore = highscoredoc.read()
highscoredoc.close()
highscoredoc = open(script_path.joinpath("highest_score_local.txt"), "w")
try:
    highscore = int(highscore)
except ValueError:
    print("Error, high score is not an integer. Please fix this in order to save your high score.")
    highscore = 0

datadoc = open(script_path.joinpath("data.txt"), "a")
# Setting up game window
running = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dodger Game v2.1.0')
screen.fill((0,0,0))
banner = f"Score : {score}  High Score : {highscore}"
font = pygame.font.Font(pygame.font.get_default_font(), 36)
myfont = pygame.font.SysFont('helvetica', 22)
screen.fill((0,0,0))
def writehs():
    highscoredoc = open(script_path.joinpath("highest_score_local.txt"), "w")
    highscoredoc.write(score)
def DEVTOOLRESET():
    global score, highscore
    highscoredoc = open(script_path.joinpath("highest_score_local.txt"), "w")
    highscoredoc.write(str(score))
    score = 0
    highscore = 0
    player.xpos = 300
    player.direction = "stop"
    time.sleep(2)
def togglemute():
    global mute
    if mute:
        mute = False
    else:
        mute = True
# Setting up player classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((24, 24))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.xpos = 300
        self.ypos = 576
        self.direction = "stop"
    def update(self, pressed_keys, pause = False):
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.direction = "left"
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.direction = "right"
        if pressed_keys[K_SPACE] or pressed_keys[K_s]:
            self.direction = "stop"
        if pressed_keys[K_0]:
            APItoggle()
        if not pause:
            if self.direction == "left":
                self.xpos -= 3
            elif self.direction == "right":
                self.xpos += 3
# Faller class for falling objects
class Faller(pygame.sprite.Sprite):
    def __init__(self):
        super(Faller, self).__init__()
        self.surf = pygame.Surface((24,24))
        self.surf.fill((48, 196, 22))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2, 4)
        self.xpos = random.randint(0,600)
        self.ypos = 0

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, score):
        global fallersurvived
        newscore = score
        self.ypos += self.speed
        if self.ypos >= SCREEN_HEIGHT-24:
            if abs(self.xpos - player.xpos) >= 32:
                fallersurvived = fallersurvived + 1
            else:
                score -= 1
            if fallersurvived >= 3:
                newscore = newscore + 1
                fallersurvived = 0
            self.reset_location()
        return newscore
    def reset_location(self):
        oldxpos = self.xpos
        if oldxpos == faller1.xpos:
            current = 1
        elif oldxpos == faller2.xpos:
            current = 2
        elif oldxpos == faller3.xpos:
            current = 3
        if current == 1:
            while True:
                newxpos = random.randint(0,600)
                if abs(newxpos - faller2.xpos) > 50 and abs(newxpos - faller2.xpos) > 50:
                    self.xpos = newxpos
                    self.ypos = 0
                    if not mute:
                        pygame.mixer.music.play()
                    return; break
        elif current == 2:
            while True:
                newxpos = random.randint(0,600)
                if abs(newxpos - faller1.xpos) > 50 and abs(newxpos - faller3.xpos) > 50:
                    self.xpos = newxpos
                    self.ypos = 0
                    if not mute:
                        pygame.mixer.music.play()
                    return; break
        elif current == 3:
            while True:
                newxpos = random.randint(0,600)
                if abs(newxpos - faller1.xpos) > 50 and abs(newxpos - faller2.xpos) > 50:
                    self.xpos = newxpos
                    self.ypos = 0
                    pygame.mixer.music.play()
                    return; break

def showtext(highscore, score, end = False):
    if not end:
        banner = f"Score : {score}  High Score : {highscore}"
        myfont = pygame.font.SysFont('helvetica', 30)
        textsurface = myfont.render(banner, False, (255, 255, 255))
        # screen.blit(textsurface,(150,0))
    else:
        banner = "You Died!\nGame Over!"
        myfont = pygame.font.SysFont('helvetica', 30)
        textsurface = myfont.render(banner, False, (255, 255, 255))
    return textsurface

player = Player()
faller1 = Faller()
faller2 = Faller()
faller3 = Faller()

def APIproc():
    global APIfrun
    if APIfrun:
        print("API toggled")
        APIfrun = False
    dist1 = abs(faller1.xpos - player.xpos)
    dist2 = abs(faller2.xpos - player.xpos)
    dist3 = abs(faller3.xpos - player.xpos)
    APIdata[0] = str(dist1)
    APIdata[1] = str(dist2)
    APIdata[2] = str(dist3)
    # APIdata[3] = dist4
    # APIdata[4] = dist5
    APIdata[3] = (int(APIdata[0]) + int(APIdata[1]) + int(APIdata[2]))/3
    datadoc.write(
        f"({round(int(APIdata[0]), 2)}),({round(int(APIdata[1]), 2)}),({round(int(APIdata[2]), 2)}),({round(int(APIdata[3]), 2)}),\n")
def APItoggle():
    global APIon, APIfrun
    if APIon:
        APIon = False
        APIfrun = False
    elif not APIon:
        APIon = True
        APIfrun = True

end = False

# Main loop for gameplay
while running:
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[K_p]:
        if pause:
            pause = False
        if not pause:
            pause = True
    while pause:
        player.update(pressed_keys)
        time.sleep(0.5)
        if pressed_keys[K_p]:
            if pause:
                pause = False
            if not pause:
                pause = True
    if score > int(highscore):
        highscore = score
        highscoredoc = open(script_path.joinpath("highest_score_local.txt"), "w")
        highscoredoc.write(str(score))
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
                break; quit()
            if event.key == K_r:
                DEVTOOLRESET()
            if event.key == K_m:
                togglemute()
        elif event.type == QUIT:
            running = False
            break
    player.update(pressed_keys)
    score = faller1.update(score)
    score = faller2.update(score)
    score = faller3.update(score)
    # Keeps player on the screen
    if player.xpos <= 24:
        player.xpos = 300
        player.direction = "stop"
    if player.xpos >= 576:
        player.xpos = 300
        player.direction = "stop"
    if APIon == True:
        if __name__ == "__main__":
            # creating thread
            APIthr = thr.Thread(target=APIproc, args=())
            APIthr.start()
    if score < 0:
        end = True
    screen.blit(player.surf, (player.xpos, player.ypos))
    screen.blit(faller1.surf, (faller1.xpos, faller1.ypos))
    screen.blit(faller2.surf, (faller2.xpos, faller2.ypos))
    screen.blit(faller3.surf, (faller3.xpos, faller3.ypos))
    if not end:
        textsurface = showtext(highscore, score)
    else:
        textsurface = showtext(highscore, score, True)
        screen.blit(textsurface,(150,0))
        pygame.display.flip()
        screen.fill((0,0,0))
        time.sleep(2)
        break
    time.sleep(0.01)
    screen.blit(textsurface,(150,0))
    pygame.display.flip()
    screen.fill((0, 0, 0))