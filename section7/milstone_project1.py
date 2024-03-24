from IPython.display import clear_output
import random


def display_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'-   -   - ')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'-   -   - ')
    print(f'{board[1]} | {board[2]} | {board[3]}')


def player_input():
    player1 = ''
    player2 = 'X'
    while player1 != 'X' and player1 != 'O':
        player1 = input("Please pick a marker 'X' or 'O' ").upper()

    if player1 == 'X':
        player2 = 'O'

    return {'player1': player1, 'player2': player2}


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    winning_poz = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))

    for option in winning_poz:
        poz1 = option[0]
        poz2 = option[1]
        poz3 = option[2]

        if board[poz1] == board[poz2] == board[poz3] == mark:
            return True

    return False


def choose_first():
    return random.randint(1, 2)


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for num in range(1, 10):
        if space_check(board, num):
            return False
    return True


def player_choice(board):
    position = ''
    while not position.isdigit() or int(position) not in range(1, 10) or not space_check(board, int(position)):
        position = input('Please enter next position: ')
        if not position.isdigit() or int(position) not in range(1, 10):
            print('Position unavailable')
        elif not space_check(board, int(position)):
            print('Position occupied')
            position = ''
        else:
            return position


def replay():
    ans = ''
    while ans != 'Y' and ans != 'N':
        ans = input('Do you want to play again? Y/N ')

    return ans == 'Y'


def play_game():
    print('Welcome to Tic Tac Toe!')
    is_game_on = True

    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    curr_user = choose_first()
    display_board(game_board)

    users_marks = player_input()
    user1_mark = users_marks['player1']
    user2_mark = users_marks['player2']

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
