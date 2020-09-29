import pygame, random, sys, os
from pygame.locals import *
from buttons import *
import time
from moviepy.editor import *

pygame.init()
x = 140
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

window_height = 700
window_width = 1280

blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

fps = 25
level = 0
addnewflamerate = 20


# file which store the high_score
HS_FILE = "highscore.txt"



# Dragon Class
# its attributes and behaviours
class dragon:
    global firerect, imagerect, Canvas, ran_height
    up = False
    down = True
    velocity = 15
    # ran_height = random.Random(window_height)
    def __init__(self):
        self.image = load_image('Images/dragon.png')
        self.imagerect = self.image.get_rect()
        # self.imagerect.right = window_width
        self.imagerect.right = window_width-10
        # self.imagerect.top = window_height / 2
        self.imagerect.top = random.randint(100,600)

    def update(self):

        if self.imagerect.top < cactusrect.bottom:
            self.up = False
            self.down = True

        if self.imagerect.bottom > firerect.top:
            self.up = True
            self.down = False

        if self.down:
            self.imagerect.bottom += self.velocity

        if self.up:
            self.imagerect.top -= self.velocity

        Canvas.blit(self.image, self.imagerect)

    def return_height(self):

        h = self.imagerect.top
        return h



# Flames(Fireball) Class
class flames:
    flamespeed = 25
    def __init__(self):
        self.image = load_image('Images/fireball.png')
        self.imagerect = self.image.get_rect()
        self.height = Dragon.return_height() + 20
        # self.height = self.ran_height

        self.surface = pygame.transform.scale(self.image, (20, 20))
        self.imagerect = pygame.Rect(window_width - 106, self.height, 20, 20)

    def update(self):
        self.imagerect.left -= self.flamespeed

    def collision(self):
        if self.imagerect.left == 0:
            return True
        else:
            return False




# Player(Mario) Class
class maryo:
    global moveup, movedown, gravity, cactusrect, firerect
    speed = 10
    downspeed = 20

    def __init__(self):
        self.image = load_image('Images/mario.png')
        self.imagerect = self.image.get_rect()
        # self.imagerect.topleft = (50, window_height / 2)
        self.imagerect.topleft = (15, 100)
        self.score = 0

    def update(self):

        if moveup and self.imagerect.top > cactusrect.bottom:
            self.imagerect.top -= self.speed
            self.score += 1

        if movedown and self.imagerect.bottom < firerect.top:
            self.imagerect.bottom += self.downspeed
            self.score += 1

        if gravity and self.imagerect.bottom < firerect.top:
            self.imagerect.bottom += self.speed




# some important function

# function to terminate the program
def terminate():
    pygame.quit()
    sys.exit()

# function to write highscore to the file
def load_score( highscore):
    with open("highscore.txt", 'w') as f:
        f.write(highscore)

space_button = pygame.mixer.Sound('Sound/click.wav')
# function to wait for user to enter a key
def waitforkey():
    while True:  # to wait for user to start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                space_button.play()
                # to terminate if the user presses the escape key
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return


# function which return player is collide with fireball or not
def flamehitsmario(playerrect, flames):  # to check if flame has hit mario or not
    for f in flame_list:
        if playerrect.colliderect(f.imagerect):
            return True
        return False

# functio to display score, topscore and level
def drawtext(text, font, surface, x, y):  # to display text on the screen
    textobj = font.render(text, 1, white)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# function to check level
def check_level(score):
    global window_height, level, cactusrect, firerect
    if score in range(0, 250):
        firerect.top = window_height - 50
        cactusrect.bottom = 50
        level = 1
    elif score in range(250, 500):
        firerect.top = window_height - 100
        cactusrect.bottom = 100
        level = 2
    elif score in range(500, 750):
        level = 3
        firerect.top = window_height - 150
        cactusrect.bottom = 150
    elif score in range(750, 1000):
        level = 4
        firerect.top = window_height - 200
        cactusrect.bottom = 200


# function to load any image
def load_image(imagename):
    return pygame.image.load(imagename)


# end of functions, begin to start the main code



mainClock = pygame.time.Clock()
Canvas = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('marioXdragon')
icon = load_image('Images/icon.png')
pygame.display.set_icon(icon)
# setting up font and sounds and images

font = pygame.font.SysFont("comicsansms", 48)
scorefont = pygame.font.SysFont("comicsansms", 30)

fireimage = load_image('Images/fire_bricks.png')
firerect = fireimage.get_rect()

cactusimage = load_image('Images/cactus_bricks.png')

cactusrect = cactusimage.get_rect()

startimage = load_image('Images/start.jpg')
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width / 2
startimagerect.centery = window_height / 2

endimage = load_image('Images/game_over.jpg')
endimagerect = startimage.get_rect()
endimagerect.centerx = window_width / 2
endimagerect.centery = window_height / 2

# pygame.mixer.music.load('Sound/mario_theme.wav')
#
#
# gameover = pygame.mixer.Sound('Sound/mario_dies.wav')

# getting to the start screen

drawtext('Mario', font, Canvas, (window_width / 3), (window_height / 3))
# start_video()
# f = True
# while f:  # to wait for user to start
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             terminate()
#         if event.type == pygame.KEYDOWN:
#             space_button.play()
#             # to terminate if the user presses the escape key
#             if event.key == pygame.K_ESCAPE:
#                 terminate()
#     else:
#         clip = VideoFileClip('Sound/startvid.mp4')
#         clip_r = clip.resize((window_width, window_height))
#         clip_r.preview()
#         f = False
#         continue
#         Canvas.blit(startimage, startimagerect)

clip = VideoFileClip('Sound/startvid.mp4')
clip_r = clip.resize((window_width, window_height))
clip_r.preview()

# pygame.display.update()
Canvas.blit(startimage, startimagerect)

pygame.display.update()
waitforkey()

pygame.mixer.music.load('Sound/mario_theme.wav')


gameover = pygame.mixer.Sound('Sound/mario_dies.wav')
# blit the menu page after pressing the key
# menu()
if topscore == "0":
    input()
else:
    menu()

# start for the main code

topscore = 0
with open ("highscore.txt", 'r') as f:
    topscore = int(f.read())
    # print(type(topscore))
Dragon = dragon()

# to show a 3 seconds countdown before start the game
# def countDown():
#     clock = pygame.time.Clock()
#     counter, text = 3, '3'.rjust(3)
#     pygame.time.set_timer(pygame.USEREVENT, 1000)
#     font = pygame.font.SysFont("comicsansms", 100)
#
#     while True:
#         for e in pygame.event.get():
#             if e.type == pygame.USEREVENT:
#                 counter -= 1
#                 text = str(counter).rjust(3) if counter > 0 else "BooM...!"
#             if e.type == pygame.QUIT : exit()
#         else:
#             # Canvas.blit(startimage, startimagerect)
#             Canvas.fill((0, 0, 0))
#             if text != "BooM...!":
#                 Canvas.blit(font.render(text, True, (255, 255, 255)), (460, 120))
#                 pygame.display.flip()
#                 clock.tick(60)
#                 continue
#             else:
#                 break


while True:
    countDown()
    flame_list = []
    player = maryo()
    moveup = False
    movedown = False
    gravity = True
    flameaddcounter = 0

    gameover.stop()
    pygame.mixer.music.play(-1, 0.0)

    while True:  # the main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    movedown = False
                    moveup = True
                    gravity = False

                if event.key == K_DOWN:
                    movedown = True
                    moveup = False
                    gravity = False

            if event.type == KEYUP:

                if event.key == K_UP:
                    moveup = False
                    gravity = True
                if event.key == K_DOWN:
                    movedown = False
                    gravity = True

                if event.key == K_ESCAPE:
                    terminate()

        flameaddcounter += 1
        check_level(player.score)

        if flameaddcounter == addnewflamerate:
            flameaddcounter = 0
            newflame = flames()
            flame_list.append(newflame)

        for f in flame_list:
            flames.update(f)

        for f in flame_list:
            if f.imagerect.left <= 0:
                flame_list.remove(f)

        player.update()
        Dragon.update()

        Canvas.fill(black)
        Canvas.blit(fireimage, firerect)
        Canvas.blit(cactusimage, cactusrect)
        Canvas.blit(player.image, player.imagerect)
        Canvas.blit(Dragon.image, Dragon.imagerect)

        # topscore = read_score()
        drawtext('Score : %s        |      Top score : %s       |      Level : %s' % (player.score, topscore, level), scorefont, Canvas, 225,
                 cactusrect.bottom + 8)

        for f in flame_list:
            Canvas.blit(f.surface, f.imagerect)

        if flamehitsmario(player.imagerect, flame_list):
            if player.score > topscore:
                topscore = player.score

            break

        if player.imagerect.top <= cactusrect.bottom or player.imagerect.bottom >= firerect.top:
            if player.score > topscore:
                topscore = player.score

            break



        pygame.display.update()

        mainClock.tick(fps)

    pygame.mixer.music.stop()
    # gameover.play()

    # pygame.display.flip()
    load_score(str(topscore))
    # print(topscore)
    # time.sleep(3)


    # Canvas.blit(endimage, endimagerect)

    game_over(player.score, gameover)

    # pygame.display.update()
    # pygame.time.wait(3000)
    # pygame.event.clear()
    # waitforkey()
