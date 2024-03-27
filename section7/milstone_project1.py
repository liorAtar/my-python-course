from IPython.display import clear_output
import random


def display_board(board: list):
    """
    Displays the Tic Tac Toe board.

    Args:
    - board (list): A list representing the Tic Tac Toe board.

    Returns:
    - None
    """
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print(f'-   -   - ')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'-   -   - ')
    print(f'{board[0]} | {board[1]} | {board[2]}')


def player_input():
    """
    Prompts players to choose their markers ('X' or 'O').

    Returns:
    - tuple: A tuple containing the markers chosen by player 1 and player 2.
    """
    player1 = ''
    player2 = 'X'
    while player1 != 'X' and player1 != 'O':
        player1 = input("Please pick a marker 'X' or 'O' ").upper()

    if player1 == 'X':
        player2 = 'O'

    return player1, player2


def place_marker(board: list, marker: str, position: int):
    """
    Places the marker on the board at the specified position.

    Args:
    - board (list): A list representing the Tic Tac Toe board.
    - marker (str): Marker to be placed on the board ('X' or 'O').
    - position (int): Position on the board where the marker will be placed.

    Returns:
    - None
    """
    board[position - 1] = marker


def win_check(board: list, mark: str):
    """
    Checks if the player with the given marker has won the game.

    Args:
    - board (list): A list representing the Tic Tac Toe board.
    - mark (str): Marker of the player ('X' or 'O').

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    winning_poz = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))

    for option in winning_poz:
        poz1 = option[0]
        poz2 = option[1]
        poz3 = option[2]

        if board[poz1] == board[poz2] == board[poz3] == mark:
            return True

    return False


def choose_first():
    """
    Randomly selects which player goes first.

    Returns:
    - int: 1 if player 1 goes first, 2 if player 2 goes first.
    """
    return random.randint(1, 2)


def space_check(board: list, position: int):
    """
    Checks if a position on the board is available.

    Args:
    - board (list): A list representing the Tic Tac Toe board.
    - position (int): Position on the board to be checked.

    Returns:
    - bool: True if the position is available, False otherwise.
    """
    return board[position] == ' '


def full_board_check(board: list):
    """
    Checks if the board is full.

    Args:
    - board (list): A list representing the Tic Tac Toe board.

    Returns:
    - bool: True if the board is full, False otherwise.
    """
    if ' ' in board:
        return False
    return True


def player_choice(board: list):
    """
    Allows the current player to choose a position on the board.

    Args:
    - board (list): A list representing the Tic Tac Toe board.

    Returns:
    - int: Chosen position on the board.
    """
    position = ''
    while not position.isdigit() or int(position) not in range(1, 10) or not space_check(board, int(position)):
        position = input('Please enter next position: ')
        if not position.isdigit() or int(position) not in range(1, 10):
            print('Position unavailable')
        elif not space_check(board, int(position)-1):
            print('Position occupied')
            position = ''
        else:
            return position


def replay():
    """
    Asks the players if they want to play another game.

    Returns:
    - bool: True if players want to play again, False otherwise.
    """
    ans = ''
    while ans != 'Y' and ans != 'N':
        ans = input('Do you want to play again? Y/N ')

    return ans == 'Y'


def play_game():
    """
    Plays a game of Tic Tac Toe.

    Returns:
    - None
    """
    print('Welcome to Tic Tac Toe!')
    is_game_on = True

    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    curr_user = choose_first()
    display_board(game_board)

    user1_mark, user2_mark = player_input()

    print(f'Player 1#, you are {user1_mark}')
    print(f'Player 2#, you are {user2_mark}\n')
    print(f'Player {curr_user}# starts!')

    while is_game_on:
        if curr_user == 1:
            curr_mark = user1_mark
            curr_user = 2
        else:
            curr_mark = user2_mark
            curr_user = 1

        print("Player 1# turn.") if curr_mark == user1_mark else print("Player 2# turn.")
        user_poz = player_choice(game_board)
        place_marker(game_board, curr_mark, int(user_poz))
        display_board(game_board)

        if win_check(game_board, curr_mark):
            print("Player 1# won!") if curr_mark == user1_mark else print("Player 2# won!")
            is_game_on = False
        elif full_board_check(game_board):
            print("It's a tie!")
            is_game_on = False

    if replay():
        play_game()


play_game()
