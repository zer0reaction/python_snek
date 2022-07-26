import pygame
import random

grid_size = 35
snake_length = 1
show_grid = []
data_grid = []
tile_size = 30
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (80, 80, 80)
SOFT_BLACK = (14, 14, 14)
SOFT_RED = (100, 0, 0)
speed = 10

q = None
c = pygame.time.Clock()

direction = 'right'


# generating the data grid and filling it with 0s
def data_grid_generate_clear():
    global data_grid

    data_grid = []

    for i in range(grid_size * grid_size):
        data_grid.append(0)


# make the tail move
def tail_shrink():
    global data_grid

    counter = 0
    for i in data_grid:
        if data_grid[counter] > 0:
            data_grid[counter] -= 1
        counter += 1


# getting the line of the head
def get_head_line(head_pos):
    counter = 0
    _line = 1
    for i in range(grid_size):
        for x in range(grid_size):
            if counter == head_pos:
                return _line
            counter += 1
        _line += 1


# getting the position in the line
def get_head_line_position(head_pos):
    counter = 0
    for i in range(grid_size):
        line_position = 1
        for x in range(grid_size):
            if counter == head_pos:
                return line_position
            counter += 1
            line_position += 1


# moving the snake :)
def move(_direction):
    global data_grid

    # snake's head pos
    head_position = get_head_position()
    # on what line the snake is
    line = get_head_line(head_position)
    # on what position in line the snake is
    head_line_position = get_head_line_position(head_position)

    # RIGHT
    # if we hit the snekk
    if direction == 'right' and head_line_position < grid_size and data_grid[head_position + 1] > 0:
        quit()
    # if we hit an apple
    elif direction == 'right' and head_line_position < grid_size and data_grid[head_position + 1] == -2:
        on_apple_hit()
        data_grid[head_position + 1] = -1
        data_grid[head_position] = snake_length
    # if we just move
    elif direction == 'right' and head_line_position < grid_size:
        tail_shrink()
        data_grid[head_position + 1] = -1
        data_grid[head_position] = snake_length
    # if we hit the grid side
    elif direction == 'right' and head_line_position == grid_size:
        tail_shrink()
        data_grid[head_position - grid_size + 1] = -1
        data_grid[head_position] = snake_length

    # LEFT
    # if we hit the snekk
    if direction == 'left' and head_line_position > 1 and data_grid[head_position - 1] > 0:
        quit()
    # if we hit an apple
    elif direction == 'left' and head_line_position > 1 and data_grid[head_position - 1] == -2:
        on_apple_hit()
        data_grid[head_position - 1] = -1
        data_grid[head_position] = snake_length
    # if we just move
    elif direction == 'left' and head_line_position > 1:
        tail_shrink()
        data_grid[head_position - 1] = -1
        data_grid[head_position] = snake_length
    # if we hit the grid side
    elif direction == 'left' and head_line_position == 1:
        tail_shrink()
        data_grid[head_position + grid_size - 1] = -1
        data_grid[head_position] = snake_length

    # UP
    # if we hit the snekk
    if direction == 'up' and line > 1 and data_grid[head_position - grid_size] > 0:
        quit()
    # if we hit an apple
    elif direction == 'up' and line > 1 and data_grid[head_position - grid_size] == -2:
        on_apple_hit()
        data_grid[head_position - grid_size] = -1
        data_grid[head_position] = snake_length
    # if we just move
    elif direction == 'up' and line > 1:
        tail_shrink()
        data_grid[head_position - grid_size] = -1
        data_grid[head_position] = snake_length
    # if we hit the grid side
    elif direction == 'up' and line == 1:
        tail_shrink()
        data_grid[grid_size * grid_size - 1 - (grid_size - head_line_position)] = -1
        data_grid[head_position] = snake_length

    # DOWN
    # if we hit the snekk
    if direction == 'down' and line < grid_size and data_grid[head_position + grid_size] > 0:
        quit()
    # if we hit an apple
    elif direction == 'down' and line < grid_size and data_grid[head_position + grid_size] == -2:
        on_apple_hit()
        data_grid[head_position + grid_size] = -1
        data_grid[head_position] = snake_length
    # if we just move
    elif direction == 'down' and line < grid_size:
        tail_shrink()
        data_grid[head_position + grid_size] = -1
        data_grid[head_position] = snake_length
    # if we hit the grid side
    elif direction == 'down' and line == grid_size:
        tail_shrink()
        data_grid[head_line_position - 1] = -1
        data_grid[head_position] = snake_length

    check_apple()
    render()


# getting the head position in data grid
def get_head_position():
    counter = 0
    for i in data_grid:
        if i == -1:
            return counter
        counter += 1


# print out the data grid to the console
def print_data_grid():
    counter = 0
    for i in range(grid_size):
        for x in range(grid_size):
            print(data_grid[counter], end=' ')
            counter += 1
        print()


# print out the show grid to the console
def print_show_grid():
    counter = 0
    for i in range(grid_size):
        for x in range(grid_size):
            print(show_grid[counter], end=' ')
            counter += 1
        print()


# rendering the grid to whatever we want
def render():

    # sync()
    # print()
    # print_show_grid()

    q.fill(BLACK)

    counter = 0
    for height in range(grid_size):
        for width in range(grid_size):
            width_position = width * tile_size
            height_position = height * tile_size

            if data_grid[counter] == 0:
                pygame.draw.rect(q, SOFT_BLACK, (width_position, height_position, tile_size, tile_size), 1)
            elif data_grid[counter] > 0:
                pygame.draw.rect(q, WHITE, (width_position, height_position, tile_size, tile_size))
            elif data_grid[counter] == -1:
                pygame.draw.rect(q, WHITE, (width_position, height_position, tile_size, tile_size))
            elif data_grid[counter] == -2:
                pygame.draw.rect(q, RED, (width_position, height_position, tile_size, tile_size))
                pygame.draw.rect(q, SOFT_RED, (width_position, height_position, tile_size, tile_size), 5)

            counter += 1

    pygame.display.update()


# generating apples
def apple_generate():
    global data_grid
    g = False
    while not g:
        r = random.randint(0, (grid_size * grid_size - 1))
        if data_grid[r] == 0:
            data_grid[r] = -2
            g = True


def check_apple():
    found = False
    for i in data_grid:
        if i == -2:
            found = True

    if not found:
        apple_generate()


# when a player hits an apple
def on_apple_hit():
    global snake_length
    apple_generate()
    snake_length += 1
    pygame.display.set_caption('Score: ' + str(snake_length - 1))


# TEST ZONE
data_grid_generate_clear()
data_grid[0] = -1
pygame.display.set_caption('Score: ' + str(snake_length - 1))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_d:
#                 direction = 'right'
#
#             if event.key == pygame.K_a:
#                 direction = 'left'
#
#             if event.key == pygame.K_w:
#                 direction = 'up'
#
#             if event.key == pygame.K_s:
#                 direction = 'down'
#
#     move(direction)
#
#     c.tick(speed)