import pygame
import time
import random

pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = 15

# Food settings
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

score = 0

def show_score():
    font = pygame.font.SysFont('arial', 24)
    score_surface = font.render(f'Score: {score}', True, white)
    screen.blit(score_surface, (10, 10))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if (snake_pos[0] < 0 or snake_pos[0] > width-10 or
        snake_pos[1] < 0 or snake_pos[1] > height-10):
        break
    for block in snake_body[1:]:
        if snake_pos == block:
            break

    show_score()
    pygame.display.update()
    clock.tick(speed)

time.sleep(2)
pygame.quit()