



import pygame, sys
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

        # if event.type == pygame.MOUSEMOTION:
        #     if RectStart.collidepoint(pygame.mouse.get_pos()):
        #         mouseover_start_button = pygame.image.load("buttons/mouseover/start.jpg")
        #         # mouseover_play_buttonrect = mouseover_play_button.get_rect()
        #         mouseover_start_buttonrect = sposx, sposy
        #         screen.blit(mouseover_start_button, mouseover_start_buttonrect)
        #         # print("mouse is over")
        #         pygame.display.update()
        #     else:
        #         screen.blit(start_button, start_buttonrect)
        #         pygame.display.update()


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

pygame.init()
input_name()
pygame.quit()