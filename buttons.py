# Import of needed python modules and class files
import sys, os, time
import pygame

# Initialization of pygame modules
pygame.init()

# Global variables section


# FS = pygame.FULLSCREEN

# Creating a window
def menu():
    SIZE = width, height = 1280, 700
    BLACK = (255, 255, 255)
    screen = pygame.display.set_mode(SIZE)
    with open("username.txt", 'r') as f:
        username = str(f.read())
    font = pygame.font.SysFont("comicsansms", 30)
    bg = pygame.image.load("buttons/bg.jpg")
    bgrect = bg.get_rect()

    play_button = pygame.image.load("buttons/play.jpg")
    play_buttonrect = play_button.get_rect()

    score_button = pygame.image.load("buttons/high_score.jpg")
    score_buttonrect = score_button.get_rect()

    help_button = pygame.image.load("buttons/help.jpg")
    help_buttonrect = help_button.get_rect()
    #
    quit_button = pygame.image.load("buttons/quit.jpg")
    quit_buttonrect = quit_button.get_rect()



    pposx = ((width / 2)-60) - (play_buttonrect.width / 2)
    # pposy = (height / 2)
    pposy = (height-620)



    sposx = ((width / 2)-60) - (score_buttonrect.width / 2)
    # sposy = (height / 2) + (play_buttonrect.height + 20)
    sposy = (height-510)

    hposx = ((width / 2)-60) - (help_buttonrect.width / 2)
    # hposy = (height / 2) + (play_buttonrect.height + 20)
    hposy = (height-270)
    #
    qposx = ((width / 2)-60) - (quit_buttonrect.width / 2)
    # qposy = (height / 2) + (help_buttonrect.height + 20)
    qposy = (height-160)

    click_button = pygame.mixer.Sound('Sound/click.wav')
    bgrect = 0, 0
    RectScreen = screen.blit(bg, bgrect)

    play_buttonrect = pposx, pposy
    RectPlay = screen.blit(play_button, play_buttonrect)

    score_buttonrect = sposx, sposy
    RectScore = screen.blit(score_button, score_buttonrect)

    help_buttonrect = hposx, hposy
    RectHelp = screen.blit(help_button, help_buttonrect)

    quit_buttonrect = qposx, qposy
    RectQuit = screen.blit(quit_button, quit_buttonrect)
    screen.blit(font.render("Welcome..! "+str(username), True, (255, 255, 255)), (20, 630))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # bgrect = 0, 0
        # RectScreen = screen.blit(bg, bgrect)
        #
        # play_buttonrect = pposx, pposy
        # RectPlay = screen.blit(play_button, play_buttonrect)
        #
        # score_buttonrect = sposx, sposy
        # RectScore = screen.blit(score_button, score_buttonrect)
        #
        # help_buttonrect = hposx, hposy
        # RectHelp = screen.blit(help_button, help_buttonrect)
        #
        # quit_buttonrect = qposx, qposy
        # RectQuit = screen.blit(quit_button, quit_buttonrect)
        #
        # pygame.display.flip()



        if event.type == pygame.MOUSEMOTION:
            if RectPlay.collidepoint(pygame.mouse.get_pos()):
                mouseover_play_button = pygame.image.load("buttons/mouseover/play.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_play_buttonrect = pposx, pposy
                screen.blit(mouseover_play_button, mouseover_play_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            elif RectScore.collidepoint(pygame.mouse.get_pos()):
                mouseover_score_button = pygame.image.load("buttons/mouseover/high_score.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_score_buttonrect = sposx, sposy
                screen.blit(mouseover_score_button, mouseover_score_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            elif RectHelp.collidepoint(pygame.mouse.get_pos()):
                mouseover_help_button = pygame.image.load("buttons/mouseover/help.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_help_buttonrect = hposx, hposy
                screen.blit(mouseover_help_button, mouseover_help_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            elif RectQuit.collidepoint(pygame.mouse.get_pos()):
                mouseover_quit_button = pygame.image.load("buttons/mouseover/quit.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_quit_buttonrect = qposx, qposy
                screen.blit(mouseover_quit_button, mouseover_quit_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            else:
                screen.blit(play_button, play_buttonrect)
                screen.blit(score_button, score_buttonrect)
                screen.blit(help_button, help_buttonrect)
                screen.blit(quit_button, quit_buttonrect)
                pygame.display.update()

            # pygame.display.flip()
            pygame.display.update()


# ye line button blink krane k liy hai................
#             pygame.display.update()



        # if event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_button.play()
            # print('Clicked')
            # if quit_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            #     print('Colided')
            #     # pygame.quit()
            #     sys.exit()

            # x, y = event.pos
            # if event.button == 1:
            if RectPlay.collidepoint(pygame.mouse.get_pos()):
                # click_button.play()
                print("You Clicked on play button")
                return
                # sys.exit()

            elif RectScore.collidepoint(pygame.mouse.get_pos()):
                # click_button.play()
                score()
                print("You Clicked on high score button")
                # sys.exit()

            elif RectHelp.collidepoint(pygame.mouse.get_pos()):
                # click_button.play()
                about()
                print("You Clicked on help button")
                # sys.exit()

            elif RectQuit.collidepoint(pygame.mouse.get_pos()):
                # click_button.play()
                print("You Clicked on quit button")
                pygame.time.wait(100)
                pygame.QUIT
                sys.exit()

            pygame.display.update()

WHITE = (255, 255, 255)

# with open("highscore.txt", 'r') as f:
#     topscore = str(f.read())


def score():
    with open("highscore.txt", 'r') as f:
        topscore = str(f.read())
    SIZE = width, height = 1280, 700
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode(SIZE)

    bg = pygame.image.load("buttons/highscore.jpg")
    bgrect = bg.get_rect()
    print(topscore)
    # back button
    back_button = pygame.image.load("buttons/back.jpg")
    back_buttonrect = back_button.get_rect()
    # reset button
    reset_button = pygame.image.load("buttons/reset.jpg")
    reset_buttonrect = reset_button.get_rect()

    bposx = (width-950) - (back_buttonrect.width / 2)
    # pposy = (height / 2)
    bposy = (height-120)

    rposx = (width - 350) - (back_buttonrect.width / 2)
    # pposy = (height / 2)
    rposy = (height - 120)

    click_button = pygame.mixer.Sound('Sound/click.wav')
    font = pygame.font.SysFont("comicsansms", 100)

    bgrect = 0, 0
    RectScreen = screen.blit(bg, bgrect)

    back_buttonrect = bposx, bposy
    RectBack = screen.blit(back_button, back_buttonrect)

    reset_buttonrect = rposx,rposy
    RectReset = screen.blit(reset_button,reset_buttonrect)

    screen.blit(font.render(str(topscore), True, (255, 255, 255)), (870, 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # bgrect = 0, 0
        # RectScreen = screen.blit(bg, bgrect)
        #
        # back_buttonrect = bposx, bposy
        # RectBack = screen.blit(back_button, back_buttonrect)
        #
        # screen.blit(font.render(str(topscore), True, (255, 255, 255)), (870, 10))
        # pygame.display.flip()



        if event.type == pygame.MOUSEMOTION:
            if RectBack.collidepoint(pygame.mouse.get_pos()):
                mouseover_back_button = pygame.image.load("buttons/mouseover/back.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_back_buttonrect = bposx, bposy
                screen.blit(mouseover_back_button, mouseover_back_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            elif RectReset.collidepoint(pygame.mouse.get_pos()):
                mouseover_reset_button = pygame.image.load("buttons/mouseover/reset.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_reset_buttonrect = rposx, rposy
                screen.blit(mouseover_reset_button, mouseover_reset_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            else:
                screen.blit(back_button, back_buttonrect)
                screen.blit(reset_button,reset_buttonrect)
                pygame.display.update()




        # if event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('Clicked')
            # if quit_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            #     print('Colided')
            #     # pygame.quit()
            #     sys.exit()

            # x, y = event.pos
            # if event.button == 1:
                if RectBack.collidepoint(pygame.mouse.get_pos()):
                    click_button.play()
                    return menu()
                    print("You Clicked on back button")
                    # sys.exit()

                elif RectReset.collidepoint(pygame.mouse.get_pos()):
                    click_button.play()
                    with open("highscore.txt", 'w') as f:
                        f.write("0")
                    score()
                    # return menu()
                    print("You Clicked on reset button")
                    # sys.exit()

        pygame.display.update()


def countDown():
    SIZE = width, height = 1280, 700
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode(SIZE)
    bg = pygame.image.load("buttons/bg.jpg")
    bgrect = bg.get_rect()
    clock = pygame.time.Clock()
    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont("comicsansms", 250)

    while True:


        bgrect = 0, 0


        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else "BooM...!"
            if e.type == pygame.QUIT : exit()
        else:
            # Canvas.blit(startimage, startimagerect)
            screen.fill((0, 0, 0))
            RectScreen = screen.blit(bg, bgrect)
            if text != "BooM...!":
                screen.blit(font.render(text, True, (255, 255, 255)), (360, 0))
                pygame.display.flip()
                clock.tick(60)
                continue
            else:
                break




def about():
    SIZE = width, height = 1280, 700
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode(SIZE)

    bg = pygame.image.load("buttons/instruction.jpg")
    bgrect = bg.get_rect()
    # print(topscore)

    back_button = pygame.image.load("buttons/back.jpg")
    back_buttonrect = back_button.get_rect()

    bposx = ((width ) - 300) - (back_buttonrect.width / 2)
    # pposy = (height / 2)
    bposy = (height - 120)

    click_button = pygame.mixer.Sound('Sound/click.wav')

    bgrect = 0, 0
    RectScreen = screen.blit(bg, bgrect)

    back_buttonrect = bposx, bposy
    RectBack = screen.blit(back_button, back_buttonrect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # bgrect = 0, 0
        # RectScreen = screen.blit(bg, bgrect)
        #
        # back_buttonrect = bposx, bposy
        # RectBack = screen.blit(back_button, back_buttonrect)
        #
        # pygame.display.flip()

        if event.type == pygame.MOUSEMOTION:
            if RectBack.collidepoint(pygame.mouse.get_pos()):
                mouseover_back_button = pygame.image.load("buttons/mouseover/back.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_back_buttonrect = bposx, bposy
                screen.blit(mouseover_back_button, mouseover_back_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            else:
                screen.blit(back_button, back_buttonrect)
                pygame.display.update()

            # pygame.display.update()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('Clicked')
            # if quit_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            #     print('Colided')
            #     # pygame.quit()
            #     sys.exit()

            # x, y = event.pos
            # if event.button == 1:
            if RectBack.collidepoint(pygame.mouse.get_pos()):
                click_button.play()
                return menu()
                print("You Clicked on back button")
                # sys.exit()

        pygame.display.update()




def game_over(score, gameoversong):
    SIZE = width, height = 1280, 700
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode(SIZE)

    bg = pygame.image.load("Images/game_over.jpg")
    bgrect = bg.get_rect()

    back_button = pygame.image.load("buttons/back.jpg")
    back_buttonrect = back_button.get_rect()

    play_again_button = pygame.image.load("buttons/play_again.jpg")
    play_again_buttonrect = play_again_button.get_rect()

    bposx = ((width/2)-300) - (back_buttonrect.width / 2)
    # pposy = (height / 2)
    bposy = (height-120)

    paposx = ((width)-400) - (play_again_buttonrect.width / 2)
    # pposy = (height / 2)
    paposy = (height - 120)
    click_button = pygame.mixer.Sound('Sound/click.wav')
    font = pygame.font.SysFont("comicsansms", 40)
    # gameover = pygame.mixer.Sound('Sound/mario_dies.wav')
    gameoversong.play()
    bgrect = 0, 0
    RectScreen = screen.blit(bg, bgrect)

    back_buttonrect = bposx, bposy
    RectBack = screen.blit(back_button, back_buttonrect)

    play_again_buttonrect = paposx, paposy
    RectPlayAgain = screen.blit(play_again_button, play_again_buttonrect)

    screen.blit(font.render(str(score), True, (255, 255, 255)), (610, 165))
    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # bgrect = 0, 0
        # RectScreen = screen.blit(bg, bgrect)
        #
        # back_buttonrect = bposx, bposy
        # RectBack = screen.blit(back_button, back_buttonrect)
        #
        # play_again_buttonrect = paposx, paposy
        # RectPlayAgain = screen.blit(play_again_button, play_again_buttonrect)
        #
        # screen.blit(font.render(str(score), True, (255, 255, 255)), (610, 165))
        # pygame.display.flip()

        # pygame.display.update()
        # pygame.time.wait(3000)
        # pygame.event.clear()



        if event.type == pygame.MOUSEMOTION:
            if RectBack.collidepoint(pygame.mouse.get_pos()):
                mouseover_back_button = pygame.image.load("buttons/mouseover/back.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_back_buttonrect = bposx, bposy
                screen.blit(mouseover_back_button, mouseover_back_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            elif RectPlayAgain.collidepoint(pygame.mouse.get_pos()):
                mouseover_play_again_button = pygame.image.load("buttons/mouseover/play_again.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_play_again_buttonrect = paposx, paposy
                screen.blit(mouseover_play_again_button, mouseover_play_again_buttonrect)
                # print("mouse is over")
                pygame.display.update()

            else:
                screen.blit(back_button, back_buttonrect)
                screen.blit(play_again_button, play_again_buttonrect)
                pygame.display.update()
            # pygame.display.flip()

            pygame.display.update()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('Clicked')
            # if quit_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            #     print('Colided')
            #     # pygame.quit()
            #     sys.exit()

            # x, y = event.pos
            # if event.button == 1:
                if RectBack.collidepoint(pygame.mouse.get_pos()):
                    click_button.play()
                    return menu()
                    print("You Clicked on back button")
                    # sys.exit()

                elif RectPlayAgain.collidepoint(pygame.mouse.get_pos()):
                    click_button.play()
                    print("You Clicked on play Again button")
                    return
                    # sys.exit()


# def input():
#     SIZE = width, height = 1280, 700
#     BLACK = (255, 255, 255)
#     screen = pygame.display.set_mode(SIZE)
#     # click_button = pygame.mixer.Sound('Sound/click.wav')
#     click_button = pygame.mixer.Sound('Sound/click.wav')
#     bg = pygame.image.load("buttons/bg.jpg")
#     name = pygame.image.load("buttons/name.png")
#     bgrect = bg.get_rect()
#     namerect = name.get_rect()
#     naposx = ((width/2)-530)
#     naposy = 70
#     namerect = naposx, naposy
#
#     start_button = pygame.image.load("buttons/start.png")
#     start_buttonrect = start_button.get_rect()
#
#     sposx = (width )-200
#     # pposy = (height / 2)
#     sposy = (height - 215)
#
#     # box_button = pygame.image.load("buttons/name_box.jpg")
#     # box_buttonrect = box_button.get_rect()
#     #
#     # bposx = ((width / 2) - 60) - (next_buttonrect.width / 2)
#     # # pposy = (height / 2)
#     # bposy = (height - 620)
#     start_buttonrect = sposx, sposy
#     input_box = pygame.Rect(20, 550, 680, 50)
#     font = pygame.font.SysFont('comicsansms', 32)
#     clock = pygame.time.Clock()
#     # input_box = pygame.Rect(20, 550, 680, 50)
#     # color_inactive = pygame.Color('lightskyblue3')
#     color_inactive = pygame.Color('red')
#     # color_active = pygame.Color('dodgerblue2')
#     color_active = pygame.Color('green')
#     color = color_inactive
#     active = False
#     text = ''
#     done = False
#     # screen.fill((30, 30, 30))
#     #
#     # screen.blit(bg, bgrect)
#     # screen.blit(name, namerect)
#     # RectStart = screen.blit(start_button, start_buttonrect)
#     # pygame.display.flip()
#     while not done:
#
#
#         # pygame.display.update()
#         # input_box = pygame.Rect(20, 550, 680, 50)
#
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 # done = True
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 # If the user clicked on the input_box rect.
#                 if input_box.collidepoint(event.pos):
#                     # Toggle the active variable.
#                     click_button.play()
#                     active = not active
#                 else:
#                     active = False
#
#                 if RectStart.collidepoint(pygame.mouse.get_pos()):
#
#                     click_button.play()
#                     with open("username.txt", 'w') as f:
#                         f.write(text)
#                     return menu()
#                 color = color_active if active else color_inactive
#
#
#                 # Change the current color of the input box.
#
#
#
#             if event.type == pygame.KEYDOWN:
#                 if active:
#                     if event.key == pygame.K_RETURN:
#                         print(text)
#                         # text = text
#                         # text = ''
#                     elif event.key == pygame.K_BACKSPACE:
#                         click_button.play()
#                         text = text[:-1]
#                     else:
#                         click_button.play()
#                         text += event.unicode
#
#         # if event.type == pygame.MOUSEMOTION:
#         #     if RectStart.collidepoint(pygame.mouse.get_pos()):
#         #         mouseover_start_button = pygame.image.load("buttons/mouseover/start.jpg")
#         #         # mouseover_play_buttonrect = mouseover_play_button.get_rect()
#         #         mouseover_start_buttonrect = sposx, sposy
#         #         screen.blit(mouseover_start_button, mouseover_start_buttonrect)
#         #         # print("mouse is over")
#         #         pygame.display.update()
#         #     else:
#         #         screen.blit(start_button, start_buttonrect)
#         #         pygame.display.update()
#
#
#         screen.blit(bg, bgrect)
#         screen.blit(name, namerect)
#         RectStart = screen.blit(start_button, start_buttonrect)
#         # Render the current text.
#         txt_surface = font.render(text, True, color)
#         # Resize the box if the text is too long.
#         width = max(300, txt_surface.get_width()+10)
#         input_box.w = width
#         # Blit the text.
#         screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#         # screen.blit(txt_surface, (100, 50))
#         # Blit the input_box rect.
#         pygame.draw.rect(screen, color, input_box, 2)
#         pygame.display.update()
#
#         pygame.display.flip()
#         clock.tick(30)


def input_name():
    SIZE = width, height = 1280, 700
    BLACK = (255, 255, 255)
    screen = pygame.display.set_mode(SIZE)
    # click_button = pygame.mixer.Sound('Sound/click.wav')
    click_button = pygame.mixer.Sound('Sound/click.wav')
    bg = pygame.image.load("buttons/bg.jpg")
    name = pygame.image.load("buttons/name.png")
    bgrect = bg.get_rect()
    namerect = name.get_rect()
    naposx = ((width/2)-530)
    naposy = 70
    namerect = naposx, naposy

    start_button = pygame.image.load("buttons/start_light.jpg")
    start_buttonrect = start_button.get_rect()

    sposx = (width )-220
    # pposy = (height / 2)
    sposy = (height - 185)

    # box_button = pygame.image.load("buttons/name_box.jpg")
    # box_buttonrect = box_button.get_rect()
    #
    # bposx = ((width / 2) - 60) - (next_buttonrect.width / 2)
    # # pposy = (height / 2)
    # bposy = (height - 620)
    start_buttonrect = sposx, sposy
    input_box = pygame.Rect(20, 550, 680, 50)
    font = pygame.font.SysFont('comicsansms', 32)
    clock = pygame.time.Clock()
    # input_box = pygame.Rect(20, 550, 680, 50)
    # color_inactive = pygame.Color('lightskyblue3')
    color_inactive = pygame.Color('red')
    # color_active = pygame.Color('dodgerblue2')
    color_active = pygame.Color('green')
    color = color_inactive
    active = False
    text = ''
    done = False
    # screen.fill((30, 30, 30))
    #
    # screen.blit(bg, bgrect)
    # screen.blit(name, namerect)
    # RectStart = screen.blit(start_button, start_buttonrect)
    # pygame.display.flip()
    while not done:


        # pygame.display.update()
        # input_box = pygame.Rect(20, 550, 680, 50)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # done = True
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    click_button.play()
                    active = not active
                else:
                    active = False

                if RectStart.collidepoint(pygame.mouse.get_pos()):

                    click_button.play()
                    with open("username.txt", 'w') as f:
                        f.write(text)
                    # menu()
                color = color_active if active else color_inactive


                # Change the current color of the input box.



            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        # text = text
                        # text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        click_button.play()
                        text = text[:-1]
                    else:
                        click_button.play()
                        text += event.unicode

        if event.type == pygame.MOUSEMOTION:
            if RectStart.collidepoint(pygame.mouse.get_pos()):
                mouseover_start_button = pygame.image.load("buttons/mouseover/start.jpg")
                # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                mouseover_start_buttonrect = sposx, sposy
                screen.blit(mouseover_start_button, mouseover_start_buttonrect)
                # print("mouse is over")
                pygame.display.update()
            # else:
            #     screen.blit(start_button, start_buttonrect)
            #     pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if RectStart.collidepoint(pygame.mouse.get_pos()):
                # mouseover_start_button = pygame.image.load("buttons/mouseover/start.jpg")
                # # mouseover_play_buttonrect = mouseover_play_button.get_rect()
                # mouseover_start_buttonrect = sposx, sposy
                # screen.blit(mouseover_start_button, mouseover_start_buttonrect)
                # # print("mouse is over")
                # pygame.display.update()
                return menu()

        screen.blit(bg, bgrect)
        screen.blit(name, namerect)
        RectStart = screen.blit(start_button, start_buttonrect)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # screen.blit(txt_surface, (100, 50))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.update()

        pygame.display.flip()
        clock.tick(60)
