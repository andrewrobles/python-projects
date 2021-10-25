# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import os

SIZE = 8

mark = "X"

top = ''
side = ''

dash = '+---'
bar = '| '

ROW = 0
COL = 1
'''
dash = +---
top = +---+---+---
'''

def get_ship_coords(x, y, isVertical):
    ship_coords = []

    for i in range(4):
        if isVertical:
            ship_coords.append([x + i, y])
        else:
            ship_coords.append([x, y + i])


    return ship_coords

def get_random_ship_coords():
    x_rand = random.randint(0, SIZE - 1)
    y_rand = random.randint(0, SIZE - 1)

    is_vertical_rand = random.randint(0, 1)
    is_vertical_rand = True if is_vertical_rand == 1 else False

    ship_coords = get_ship_coords(x_rand, y_rand, is_vertical_rand)

    return ship_coords

def randomly_place_ship():
    ship_coords = get_random_ship_coords()

    while not is_valid_ship(ship_coords):
        ship_coords = get_random_ship_coords()

    return ship_coords


def is_valid_ship(ship_coords):
    for x, y in ship_coords:
        if x >= SIZE or y >= SIZE:
            return False
    return True

def print_board(ship_coords, positions):


    matrix = []
    for i in range(SIZE):
        matrix.append([' '] * SIZE)

    hit_count = 0
    for coords in positions:
        if hit_count == len(ship_coords):
            print('Game over!')

        x, y = coords

        if is_hit(x, y, ship_coords):
            hit_count += 1
            matrix[x][y] = 'X'
        else:
            matrix[x][y] = '#'


    for row in range(SIZE):
        top = ''
        side = ''
        # Create the row without the X
        for col in range(SIZE):
            top += dash
            val = matrix[row][col]

            side += (bar + val + " ")

        top = top + '+'
        side = side + '|'

        print(top)
        print(side)

    print('+---'*SIZE + "+")

def is_hit(x, y, ship_coords):
    for curr_x, curr_y in ship_coords:
        if x == curr_x and y == curr_y:
            return True
    return False

def get_user_coords(user_input):
    y = get_alpha_index(user_input[0])
    x = int(user_input[1])
    return [x - 1, y]

def get_alpha_index(letter):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(alpha)):
        if alpha[i] == letter:
            return i

ship_coords = get_ship_coords(0, 0, True)
positions = []
print_board(ship_coords, positions)
GAME_OVER = False

while not GAME_OVER:
    answer = input('Please provide a position: ')
    coords = get_user_coords(answer)
    positions.append(coords)

    matrix = []
    for i in range(SIZE):
        matrix.append([' '] * SIZE)

    hit_count = 0
    for coords in positions:
        if hit_count == len(ship_coords):
            print('Game over!')
            print('You scored a {}'.format(len(positions)))
            GAME_OVER = True

        x, y = coords

        if is_hit(x, y, ship_coords):
            hit_count += 1
            matrix[x][y] = 'X'
        else:
            matrix[x][y] = '#'


    for row in range(SIZE):
        top = ''
        side = ''
        # Create the row without the X
        for col in range(SIZE):
            top += dash
            val = matrix[row][col]

            side += (bar + val + " ")

        top = top + '+'
        side = side + '|'

        print(top)
        print(side)

    print('+---'*SIZE + "+")

    if GAME_OVER:
        break

    
    