import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Game window
WIDTH = 600
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 35)

# Block size
BLOCK = 20
SPEED = 10   # a bit faster


def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], BLOCK, BLOCK])


# NEW: Score display
def show_score(score):
    value = font.render("Score: " + str(score), True, BLUE)
    win.blit(value, [10, 10])


def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [WIDTH / 6, HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK) / 20.0) * 20.0

    while not game_over:

        while game_close:
            win.fill(WHITE)
            message("Game Over! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK
                    x_change = 0

        # Boundary conditions
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(BLACK)

        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK, BLOCK])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        # If snake hits itself
        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake)

        # NEW: Show score
        show_score(length - 1)

        pygame.display.update()

        # Food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK) / 20.0) * 20.0
            length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()


gameLoop()

