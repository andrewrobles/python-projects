# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import os


#----------------------------------------------
# Global variables: In a real life software
# engineering project these might be placed in
# a seperate file called a "configuration file"
# or maybe even a database!
# 
# It is always wise to put config variables
# at the top of the file.
#----------------------------------------------

HEIGHT = 6
WIDTH = 7
TOP = ''
SIDE = ''
DASH = '+---'
BAR = '| '
NUM_PLAYERS = 2
CHECKERS = ["X", "O", "V", "H", "M"]
CURR_PLAYER = random.randint(0, NUM_PLAYERS - 1)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def print_board(matrix):
    #----------------------------------------------
    # Create the top line of letters above columns
    #----------------------------------------------

    alphabet = ALPHABET

    # Use index splicing in order to get the correct
    # number of letters from alphabet
    letter_label_list = alphabet[:WIDTH]

    # Create and print the line of letter labels
    label_line = ''
    for label in letter_label_list:
        label_line += "  " + label + " "

    print(label_line)

    #----------------------------------------------
    # Print the board rows and columns
    #----------------------------------------------

    # Print the rows
    for row in range(HEIGHT):
        TOP = ''
        SIDE = ''

        # Print the columns
        for col in range(WIDTH):
            TOP += DASH
            value = matrix[row][col]

            SIDE += (BAR + value + " ")

        TOP = TOP + '+'
        SIDE = SIDE + '|'

        print(TOP)
        print(SIDE)

    # Print the bottom line
    print('+---'*WIDTH + "+")


def initialize_matrix():
    matrix = []

    # Create matrix rows
    for i in range(HEIGHT):
        # Create matrix columns
        matrix.append([' '] * WIDTH)

    return matrix

def get_column_from_player(player_num):
    # Ask player for their column and get user input as a string
    message = "Player {}, please enter a column: ".format(str(player_num))
    val = input(message)

    # Keep attempting to get user input until input is valid
    while not is_valid_user_input(val):
        val = input(message)

    # Convert input from letter to a number
    alphabet_indexes = list(range(len(ALPHABET)))
    alphabet_letters = [letter for letter in ALPHABET]
    letters_to_numbers = {letter:index for letter, index in zip(alphabet_letters, alphabet_indexes)}
    number = letters_to_numbers[val]
    return number

def is_valid_user_input(val):
    # This is what is known as a list comprehension
    # https://www.w3schools.com/python/python_lists_comprehension.asp
    valid_inputs = [str(ALPHABET[x]) for x in range(WIDTH)]
    
    # Return true if user input is one of the values in valid inputs list
    if val in valid_inputs:
        return True
    else:
        return False


matrix = initialize_matrix()

while True:
    print_board(matrix)
    column_number = get_column_from_player(CURR_PLAYER)
    print('User chose column {}!'.format(column_number))

    #----------------------------------------------
    # End current player turn
    #----------------------------------------------

    # Increment player number by one
    CURR_PLAYER = CURR_PLAYER + 1

    # Wrap player number to the beginning if 
    # the last player has gone
    if CURR_PLAYER >= NUM_PLAYERS:
        CURR_PLAYER = 0


#----------------------------------------------
# Grading
#----------------------------------------------
# [x] Creating the board and printing the board, as depicted in Figure 1
# [x] Supporting multiple players (more than 2) and dimensions (other than 6x7)
# [x] Randomly selecting first player and alternating turns
# [x] Checking for invalid input, e.g. numbers, invalid characters, out of board, etc
