import pygame
import random
import os
import time
localtime = time.asctime((time.localtime(time.time())))

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('super.mp3')
pygame.mixer.music.play()

# Creating window
screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

bgimg = pygame.image.load('neymar.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (9, 0, 0)
green = (0, 255, 0)

blue = (0, 0, 255)
score = 0

# Game Title
pygame.display.set_caption("Snakes With Saurav")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):

    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def self():
    exit_game = False
    while not exit_game:
        gameWindow.fill((55, 88, 109))
        text_screen('hello how are you?', red, 250, 210)
        text_screen(' If yes press y to continue', red, 250, 260)
        text_screen(f'current time is{localtime}',green,20, 300 )
        for event in pygame.event.get():
            gameWindow.fill((55, 88, 109))
            text_screen('hello how are you?', red, 250, 210)
            text_screen(' If yes press y to continue', red, 250, 260)
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    welcome()
        pygame.display.update()
        clock.tick(90)


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((2, 120, 190))
        text_screen("Welcome to Saurav game:!!", black, 100, 250)
        text_screen("Please press space bar to play??", black, 105, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(90)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # Check if Highscore file exists
    if not os.path.exists('highscore.txt'):
        with open("highscore.txt", "w") as s:
            s.write('0')

    with open("highscore.txt", "r") as s:
        highscore = s.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill((10, 220, 190))
            text_screen("Game Over! Press enter To Continue", red, 70, 250)
            text_screen(' your score is :' + str(score), black, 15, 150)
            text_screen('high score is :' + str(highscore), blue, 15, 100)
            if int(score) < int(highscore):
                text_screen('you could not beat current high score!!', black, 50, 320)
                text_screen('Try again next time: best of luck', black, 100, 350)
                text_screen(f'Current time is {localtime}',red,10,50)

            else:

                text_screen('you are able to create an unbeatable score!!!', black, 1, 360)
                text_screen('congratulation:::', black, 50, 320)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('super.mp3')
                        pygame.mixer.music.play()

                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        score += 50
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 3
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(green)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  highscore: " + str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-2]:
                game_over = True
                pygame.mixer.music.load('sover.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('sover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()
    quit()
self()
welcome()