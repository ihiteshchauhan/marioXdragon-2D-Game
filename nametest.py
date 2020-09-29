import pygame, sys
def input():
    SIZE = width, height = 1280, 700
    BLACK = (255, 255, 255)
    screen = pygame.display.set_mode(SIZE)

    bg = pygame.image.load("buttons/bg.jpg")
    name = pygame.image.load("buttons/name.png")
    click_button = pygame.mixer.Sound('Sound/click.wav')
    bgrect = bg.get_rect()
    namerect = name.get_rect()
    nposx = ((width/2)-530)
    nposy = 70
    namerect = nposx, nposy
    font = pygame.font.SysFont('comicsansms', 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(470, 500, 680, 50)
    # color_inactive = pygame.Color('lightskyblue3')
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    start_button = pygame.image.load("buttons/start_light.jpg")
    start_buttonrect = start_button.get_rect()

    sposx = (width) - 220
    # pposy = (height / 2)
    sposy = (height - 185)
    start_buttonrect = sposx, sposy
    # screen.blit(bg, bgrect)
    # screen.blit(name, namerect)
    RectStart = screen.blit(start_button, start_buttonrect)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # screen.fill((30, 30, 30))
        screen.blit(bg, bgrect)
        screen.blit(name, namerect)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
pygame.init()
input()
pygame.quit()
