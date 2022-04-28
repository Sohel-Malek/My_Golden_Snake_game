"""
author:Sohel Malek
Date:28 April 2022
purpose : My first Game in Python
"""

import random
import pygame
import os

# initilaizing
pygame.init()
pygame.mixer.init()

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
gold = (255, 215, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# creating windowṇ
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Backgrounds
bg1 = pygame.image.load("Screen/snk2.jpg")
bg1 = pygame.transform.scale(
    bg1, (screen_width, screen_height)).convert_alpha()
bg2 = pygame.image.load("Screen/gameover.png")
bg2 = pygame.transform.scale(
    bg2, (screen_width, screen_height)).convert_alpha()
bg3 = pygame.image.load("Screen/snake3.jpg")
bg3 = pygame.transform.scale(
    bg3, (screen_width, screen_height)).convert_alpha()


# creating title
pygame.display.set_caption("Golden Snake game by Sohel Malek")
pygame.display.update()

# Music
pygame.mixer.music.load('music/Snake on the Beach - Nico Staf.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
# font = pygame.font.SysFont("Roboto", 45)
font = pygame.font.SysFont("Harrington", 45)
# font = pygame.font.SysFont("Helvetica", 50)
# font = pygame.font.SysFont(None, 50)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snk(gameWindow, color, snk_lst, size):
    for x, y in snk_lst:
        pygame.draw.rect(gameWindow, color, [x, y, size, size])
        # pygame.mixer.music.load("music/Beep Short .mp3")
        # pygame.mixer.music.play()


def welcome():
    exit_game = False
    while not exit_game:
        # gameWindow.fill((233, 210, 229))
        gameWindow.fill(black)
        gameWindow.blit(bg1, (0, 0))
        # text_screen("Welcome to $ohel's Golden Snake game", gold, 75, 90)
        # text_screen("Press Space Bar To Play", gold, 232, 350)
        text_screen("Welcome to $ohel's", gold, 250, 130)
        text_screen("Golden  Snake  game", gold, 240, 230)
        text_screen("Press Space Bar To Play", red, 210, 330)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.fadeout(200)
                    pygame.mixer.music.load(
                        'music/Snake on the Beach - Nico Staf.mp3')
                    pygame.mixer.music.play()
                    Game_loop()
        pygame.display.update()
        clock.tick(60)


def Game_loop():
    # game variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    fps = 60
    v_x = 0
    v_y = 0
    snk_lst = []
    snk_len = 1

    # snake food
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)

    # Highscore saving file
    if(not os.path.exists("highScore.txt")):
        with open("highScore.txt", "w") as f:
            f.write("0")
    with open("highScore.txt", "r") as f:
        highScore = f.read()

    score = 0
    init_v = 5
    # highScore = score

    while not exit_game:
        if game_over:
            with open("highScore.txt", "w") as f:
                f.write(str(highScore))

    # GameOver Screen
            gameWindow.fill(black)
            gameWindow.blit(bg2, (0, 0))
            # text_screen("Game Over! Press Enter To Continue", red, 100, 200)
            # text_screen("Your Score : " + str(score), green, 320, 340)
            text_screen("Your Score : " + str(score), green, 310, 390)
            text_screen("Press Enter To Continue", red, 210, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Game_loop()
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    # print(event)
                    if event.key == pygame.K_RIGHT:
                        # v_x += 10
                        v_x += init_v
                        v_y = 0

                    if event.key == pygame.K_LEFT:
                        v_x -= init_v
                        v_y = 0
                    if event.key == pygame.K_UP:
                        v_y -= init_v
                        v_x = 0
                    if event.key == pygame.K_DOWN:
                        v_y += init_v
                        v_x = 0

                    if event.key == pygame.K_q:
                        score += 50

            snake_x = snake_x + v_x
            snake_y = snake_y + v_y

            if abs(snake_x-food_x) < 16 and abs(snake_y-food_y) < 16:
                score += 10
                # print(f"Score = {score}")
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_len += 5
                if score > int(highScore):
                    highScore = score

        # game background
            # gameWindow.fill(black)
            gameWindow.blit(bg3, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " +
                        str(highScore),  green, 5, 5)

            # image_of_food
            '''
            a1 = pygame.image.load("Screen/snk1.jpg")
            a1.convert()
            a1 = pygame.transform(a1, (snake_size, snake_size))
            # pygame.display.set_mode((food_x,food_y))
            rect = a1.get_rect()
            gameWindow.blit(a1,rect)
            pygame.draw.rect(gameWindow, red, rect, 10)
            '''
            pygame.draw.rect(gameWindow, red, [
                             food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if len(snk_lst) > snk_len:
                del snk_lst[0]

            if head in snk_lst[:-1]:
                game_over = True
                pygame.mixer.music.load('music/Big Explosion Cut Off.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('music/Big Explosion Cut Off.mp3')
                pygame.mixer.music.play()

            # pygame.mixer.music.load("music/Beep Short .mp3")
            # pygame.mixer.music.play()
            plot_snk(gameWindow, gold, snk_lst, snake_size)

            pygame.draw.rect(gameWindow, gold, [
                snake_x, snake_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


# Game_loop()
welcome()
