# This is a sample Python script.
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# ustawienie rozmiaru ekranu
size = (700, 500)
display_width = 700
display_height = 500
screen = pygame.display.set_mode(size)

# ustawienie ikonki oraz tekstu okna
icon = pygame.image.load('pong_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Pong")

# paletka A
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
paddleAup = pygame.K_w
paddleAdown = pygame.K_s

# paletka B
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
paddleBup = pygame.K_UP
paddleBdown = pygame.K_DOWN

# piłeczka
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Fonty
font = "Retro.ttf"

# Sprajty
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

FPS = 60

clock = pygame.time.Clock()


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


# -------- Loop gry -----------
def game():
    carryOn = True
    scoreA = 0
    scoreB = 0
    while carryOn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        # Poruszanie się graczy
        keys = pygame.key.get_pressed()
        if keys[paddleAup]:
            paddleA.moveUp(5)
        if keys[paddleAdown]:
            paddleA.moveDown(5)
        if keys[paddleBup]:
            paddleB.moveUp(5)
        if keys[paddleBdown]:
            paddleB.moveDown(5)

        all_sprites_list.update()

        # Sprwadzenie czy się odbija od ściany
        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

            # Wykrycie kolizji
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()

        # Wyczyszczenie ekranu
        screen.fill(BLACK)
        # Siatka
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        all_sprites_list.draw(screen)

        # Rysowanie wyniku
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420, 10))

        pygame.display.flip()

        clock.tick(FPS)


# Niedokończone ze względu na brak czasu
def game_intro():
    intro = True
    while intro:
        for EVENT in pygame.event.get():
            print(EVENT)
            if EVENT.type == pygame.KEYDOWN:
                if EVENT.type == pygame.K_RETURN:
                    print("działa")
                    intro = False
                if EVENT.type == pygame.K_SPACE:
                    intro = False
                if EVENT.type == pygame.K_ESCAPE:
                    intro = False

            if EVENT.type == pygame.MOUSEBUTTONUP:
                intro = False

            if EVENT.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)

        largeText = pygame.font.Font('Retro.ttf', 40)
        smallText = pygame.font.Font('Retro.ttf', 20)
        TextSurf, TextRect = text_objects("Radex presents - Ping", largeText)
        Text2Surf, Text2Rect = text_objects("Click with a mouse to proceed", smallText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(TextSurf, TextRect)
        screen.blit(Text2Surf, Text2Rect)
        pygame.display.flip()
        clock.tick(FPS)


# Ustalenie pozycji w menu
def selection(pos, i, list):
    if i == 1:
        if pos >= len(list) - 1:
            pos = 0
        else:
            pos = pos + 1
    if i == -1:
        if pos <= 0:
            pos = len(list) - 1
        else:
            pos = pos - 1
    return pos


# Niedokończone ze względu na brak czasu
def change_key_menu(selected):
    change_key_menu = True
    text_menu = ""
    while change_key_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if selected == "p1up":
                paddleAup = pygame.KEYDOWN
                print(paddleAup)
                options_menu()
            if selected == "p1down":
                paddleAdown = pygame.KEYDOWN
                print(paddleAdown)
                options_menu()
            if selected == "p2up":
                paddleBup = pygame.KEYDOWN
                print(paddleBup)
            if selected == "p2down":
                paddleBdown = pygame.KEYDOWN
                print(paddleBdown)

        # UI głównego Menu
        screen.fill(BLACK)
        if selected == "p1up":
            text_menu = "Change Player 1 Up Button"
        if selected == "p1down":
            text_menu = "Change Player 1 Down Button"
        if selected == "p2up":
            text_menu = "Change Player 2 Up Button"
        if selected == "p2down":
            text_menu = "Change Player 2 Down Button"
        title = text_format(text_menu, font, 30, BLUE)

        title_rect = title.get_rect()

        # Teksty głównego Menu
        screen.blit(title, (display_width / 2 - (title_rect[2] / 2), 40))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Options")


def main_menu():
    menu = True
    # selectionList = ["start", "options", "quit"]
    selectionList = ["start", "quit"]
    selected = "start"
    pos = 0
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pos = selection(pos, -1, selectionList)
                    selected = selectionList[pos]
                    print(selected)
                if event.key == pygame.K_DOWN:
                    pos = selection(pos, 1, selectionList)
                    selected = selectionList[pos]
                    print(selected)
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        menu = False
                        game()
                    # if selected == "options":
                    #     menu = False
                    #     options_menu()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # UI głównego Menu
        screen.fill(BLACK)
        title = text_format("Ping", font, 90, BLUE)
        if selected == "start":
            text_start = text_format("START", font, 60, YELLOW)
        else:
            text_start = text_format("START", font, 60, WHITE)
        # if selected == "options":
        #     text_options = text_format("OPTIONS", font, 60, YELLOW)
        # else:
        #     text_options = text_format("OPTIONS", font, 60, WHITE)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 60, YELLOW)
        else:
            text_quit = text_format("QUIT", font, 60, WHITE)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        # options_rect = text_options.get_rect()
        quit_rect = text_quit.get_rect()

        # Teksty głównego Menu
        screen.blit(title, (display_width / 2 - (title_rect[2] / 2), 40))
        screen.blit(text_start, (display_width / 2 - (start_rect[2] / 2), 200))
        # screen.blit(text_options, (display_width / 2 - (options_rect[2] / 2), 250))
        screen.blit(text_quit, (display_width / 2 - (quit_rect[2] / 2), 300))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Ping")


# def options_menu():
#     options = True
#     selectionList = ["p1up", "p1down", "p2up", "p2down", "back"]
#     selected = "p1up"
#     pos = 0
#
#     while options:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     pos = selection(pos, -1, selectionList)
#                     selected = selectionList[pos]
#                     print(selected)
#                 if event.key == pygame.K_DOWN:
#                     pos = selection(pos, 1, selectionList)
#                     selected = selectionList[pos]
#                     print(selected)
#                 if event.key == pygame.K_RETURN:
#                     if selected == "p1up" or "p1down" or "p2up" or "p2down":
#                         options = False
#                         change_key_menu(selected)
#                     if selected == "back":
#                         options = False
#                         main_menu()
#                     if selected == "quit":
#                         pygame.quit()
#                         quit()
#
#         # UI opcji
#         screen.fill(BLACK)
#         options = text_format("Options", font, 90, BLUE)
#
#         if selected == "p1up":
#             text_p1_up = text_format("PLAYER 1 UP", font, 45, YELLOW)
#         else:
#             text_p1_up = text_format("PLAYER 1 UP", font, 45, WHITE)
#         if selected == "p1down":
#             text_p1_down = text_format("PLAYER 1 DOWN", font, 45, YELLOW)
#         else:
#             text_p1_down = text_format("PLAYER 1 DOWN", font, 45, WHITE)
#         if selected == "p2up":
#             text_p2_up = text_format("PLAYER 2 UP", font, 45, YELLOW)
#         else:
#             text_p2_up = text_format("PLAYER 2 UP", font, 45, WHITE)
#         if selected == "p2down":
#             text_p2_down = text_format("PLAYER 2 DOWN", font, 45, YELLOW)
#         else:
#             text_p2_down = text_format("PLAYER 2 DOWN", font, 45, WHITE)
#         if selected == "back":
#             text_back = text_format("BACK", font, 45, YELLOW)
#         else:
#             text_back = text_format("BACK", font, 45, WHITE)
#
#         options_rect = options.get_rect()
#         p1_up_rect = text_p1_up.get_rect()
#         p1_down_rect = text_p1_down.get_rect()
#         p2_up_rect = text_p2_up.get_rect()
#         p2_down_rect = text_p2_down.get_rect()
#         back_rect = text_back.get_rect()
#
#         # Teksty opcji
#
#         screen.blit(options, (display_width / 2 - (options_rect[2] / 2), 40))
#         screen.blit(text_p1_up, (display_width / 2 - (p1_up_rect[2] / 2), 240))
#         screen.blit(text_p1_down, (display_width / 2 - (p1_down_rect[2] / 2), 280))
#         screen.blit(text_p2_up, (display_width / 2 - (p2_up_rect[2] / 2), 320))
#         screen.blit(text_p2_down, (display_width / 2 - (p2_down_rect[2] / 2), 360))
#         screen.blit(text_back, (display_width / 2 - (back_rect[2] / 2), 400))
#         pygame.display.update()
#         clock.tick(FPS)
#         pygame.display.set_caption("Ping")


game_intro()
main_menu()

pygame.quit()
