import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display sizes
display_width = 800
display_height = 600

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Set the clock
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

# Set the font
font_style = pygame.font.SysFont(None, 50)

# Display messages to the user
def message(msg, color):
    m = font_style.render(msg, True, color)
    dis.blit(m, [display_width / 6, display_height / 3])

# Main game loop
def game_loop():
    game_close = False
    game_over = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    len_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # Logic for when the snake game is active
    while not game_close:

        # Logic for when the game is over
        while game_over == True:
            dis.fill(blue)
            message('You Lost! Press "esc" to quit or "c" to play again', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        game_loop()
                        return

        # Key press actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_ESCAPE:
                    game_close = True
        
        # Game over if the snake collides with the borders of the display
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_over = True

        # Update the location of the snake
        x1 += x1_change
        y1 += y1_change

        # Draw the display
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > len_of_snake:
            del snake_list[0]

        # End the game if the snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        
        # Draw the snake
        for x in snake_list:
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()

        # Spawn a new piece of food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            len_of_snake += 1

        # Add a tick using snake speed
        clock.tick(snake_speed)


    pygame.quit()
    quit()

game_loop()
