# Importing the necessary libraries
from random import choice
import time


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print('+-------+-------+-------+')
        for j in range(3):
            if j != 1:
                print('|       |       |       |')
            else:
                print(f'|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |')
    return print('+-------+-------+-------+')


def enter_move(board, free_fields):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    while True:

        row = int(input('\nEnter your move (row):'))
        column = int(input('Enter your move (column):'))
        print()
        
        if row not in range(0, 3):
            print(f'Sorry, row entered ({row}) is out of range (0, 1, 2)')
            continue

        if column not in range(0, 3):
            print(f'Sorry, column entered ({column}) is out of range (0, 1, 2)')
            continue
        
        move = row, column

        if move not in free_fields:
            print('Sorry, this move have already been made')
            continue

        break

    for idx, i in enumerate(free_fields):
        if i == move:
            del free_fields[idx]

    board[row][column] = 'X'

    print(f'\nPlayer has made it\'s move: {move}!\n')
    
    return


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    free_fields = []
    
    for k, i in enumerate(board):
        for a, j in enumerate(i):
            if type(j) is int:
                free_fields.append((a, k))
    
    return free_fields


def victory_for(board, sign, free_fields):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    win_list = [
        (board[0][0], board[0][1], board[0][2]),
        (board[1][0], board[1][1], board[1][2]),
        (board[2][0], board[2][1], board[2][2]),
        (board[0][0], board[1][0], board[2][0]),
        (board[0][1], board[1][1], board[2][1]),
        (board[0][2], board[1][2], board[2][2]),
        (board[0][0], board[1][1], board[2][2]),
        (board[0][2], board[1][1], board[2][0])
    ]

    win_cond = (sign, sign, sign)

    for i in win_list:
        if i == win_cond:

            print()
            display_board(board)
            print(f'\n----------------- {sign} won! -----------------')
            
            return True

    if len(free_fields) == 0:

        print()
        display_board(board)
        print('\n----------------- Draw! -----------------')

        return True

    return


def draw_move(board, free_fields):
    # The function draws the computer's move and updates the board.
    display_board(board)
    
    if len(free_fields) == 9:
        row, column = (1, 1)
    
    else:
        row, column = choice(free_fields)

    board[row][column] = 'O'

    move = row, column

    for idx, i in enumerate(free_fields):
        if i == move:
            del free_fields[idx]


    time.sleep(2)

    print(f'\nComputer has made it\'s move: {move}!\n')

    time.sleep(1)

    return display_board(board)


def play_game():
    # This function calls the other functions to orchestrate the game, prints a message on the start and end of the game,
    # creates the board and coordinates a 'lag' between each action with the time.sleep() function
    board = [[x for x in range(1, 4)], [x for x in range(4, 7)], [x for x in range(7,10)]]

    print('\nStarting game...\n')
    time.sleep(2)

    free_fields = make_list_of_free_fields(board)

    while True:

        draw_move(board, free_fields)

        time.sleep(1)
        
        if len(free_fields) <= 5:

            if victory_for(board, 'O', free_fields) == True:

                break

        time.sleep(1)

        enter_move(board, free_fields)
        
        if len(free_fields) <= 5:

            if victory_for(board, 'X', free_fields) == True:
                break

        time.sleep(1)
    
    return print('\nGame Over!\n')


play_game()