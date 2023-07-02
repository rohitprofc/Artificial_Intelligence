import random

# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to check if the board is full
def check_draw():
    return ' ' not in board

# Function to make a move
def make_move(player, position):
    board[position] = player

# Function for the bot player's move
def bot_move():
    # Check for winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win('O'):
                return

            board[i] = ' '

    # Check for blocking move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win('X'):
                board[i] = 'O'
                return

            board[i] = ' '

    # Choose a random move
    while True:
        position = random.randint(0, 8)
        if board[position] == ' ':
            make_move('O', position)
            return

# Function to play the game
def play_game():
    current_player = 'X'

    while True:
        display_board()

        if current_player == 'X':
            position = int(input('Player ' + current_player + ', choose a position (1-9): ')) - 1

            if board[position] == ' ':
                make_move(current_player, position)
            else:
                print('Invalid move. Try again.')
                continue
        else:
            bot_move()

        if check_win(current_player):
            display_board()
            if current_player == 'X':
                print('Player X wins!')
            else:
                print('Bot wins!')
            break
        elif check_draw():
            display_board()
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()

# Output:-
# -------------
# |   |   |   |
# -------------
# |   |   |   |
# -------------
# |   |   |   |
# -------------
# Player X, choose a position (1-9): 5
# -------------
# |   |   |   |
# -------------
# |   | X |   |
# -------------
# |   |   |   |
# -------------
# -------------
# | O |   |   |
# -------------
# |   | X |   |
# -------------
# |   |   |   |
# -------------
# Player X, choose a position (1-9): 4
# -------------
# | O |   |   |
# -------------
# | X | X |   |
# -------------
# |   |   |   |
# -------------
# -------------
# | O |   |   |
# -------------
# | X | X | O |
# -------------
# |   |   |   |
# -------------
# Player X, choose a position (1-9): 7
# -------------
# | O |   |   |
# -------------
# | X | X | O |
# -------------
# | X |   |   |
# -------------
# -------------
# | O |   | O |
# -------------
# | X | X | O |
# -------------
# | X |   |   |
# -------------
# Player X, choose a position (1-9): 2
# -------------
# | O | X | O |
# -------------
# | X | X | O |
# -------------
# | X |   |   |
# -------------
# -------------
# | O | X | O |
# -------------
# | X | X | O |
# -------------
# | X |   | O |
# -------------
# Bot wins!