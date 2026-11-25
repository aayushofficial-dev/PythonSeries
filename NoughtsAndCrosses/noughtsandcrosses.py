import random
import os.path
import json

random.seed()

def draw_board(board):
    """Draws the Tic-Tac-Toe board"""
    print()
    print(board[0][0], '|', board[0][1], '|', board[0][2])
    print('--+---+--')
    print(board[1][0], '|', board[1][1], '|', board[1][2])
    print('--+---+--')
    print(board[2][0], '|', board[2][1], '|', board[2][2])
    print()

def welcome(board):
    """Prints welcome message and displays the board"""
    print('Welcome to the "Unbeatable Noughts and Crossed" game.')
    print('The board layout is shown below:')
    draw_board(board)

def initialise_board(board):
    """Sets all board cells to a single space."""
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
    return board

def get_player_move(board):
    """Gets a valid move from the player."""
    while True:
        move = input('Choose your square:\n1 2 3\n4 5 6\n7 8 9:')
        if not move.isdigit():
            print('Invalid input. Enter a number 1-9.')
            continue
        move = int(move)
        if move < 1 or move > 9:
            print('Number must between 1 and 9.')
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] != ' ':
            print('Cell already taken. Choose another.')
        else:
            return row, col

def choose_computer_move(board):
    """Computer choosed a move(win > block > random)"""
    # try to win
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'O'
                if check_for_win(board, 'O'):
                    board[r][c] = ' '
                    return r, c
                board[r][c] = ' '
    # try to block player
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                if check_for_win(board, 'X'):
                    board[r][c] = ' '
                    return r, c
                board[r][c] = ' '
    # otherwise random move
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def check_for_win(board, mark):
    """Checks if given mark (X or O) has won."""
    # rows and columns
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
        if all(board[j][i] == mark for j in range(3)):
            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2[0]] == mark:
        return True

    return False

def check_for_draw(board):
    """Checks if board is full."""
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game(board):
    """Main game loop."""
    initialise_board(board)
    draw_board(board)

    while True:
        # player move
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print('You win!')
            return 1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

        # computer move
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        print('Computer played.')
        draw_board(board)

        if check_for_win(board, 'O'):
            print('Computer wins!')
            return -1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    """Displays menu and gets user choice."""
    while True:
        print('\nEnter one of the following options:')
        print('1 - Play the game.')
        print('2 - Save your score in the leaderboard')
        print('3 - Load and display the leaderboard')
        print('q - End the program.')

        choice = input('1, 2, 3 or q?').lower()

        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print('Invalid choice.')

def load_scores():
    """Loads leaderboard scores from file."""
    if not os.path.exists('leaderboard.txt'):
        return {}

    with open("leaderboard.txt", 'r') as file:
        try:
            leaders = json.load(file)
        except json.JSONDecodeError:
            leaders = {}

    return leaders

def save_score(score):
    """Saves player score to leaderboard."""
    name = input('Enter your name:')
    leaders = load_scores()

    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score

    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """Displays leaderboard"""
    if not leaders:
        print('Leaderboard in empty.')
        return 

    print('\nLeaderboard:')
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)

    for name, score in sorted_leaders:
        print(f'{name}: {score}')


        