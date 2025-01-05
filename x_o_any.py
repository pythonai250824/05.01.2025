
turn = 1 # BAD
game = {
    'turn': 1, # GOOD
    'player1': 'name',
    'board': [
        ['_', '_', 'O'],
        ['X', 'O', 'O'],
        ['O', 'X', 'O'],
    ]
}

def check_win(my_board: list, search: str):
    for row in my_board:
        if all(shape == search for shape in row):
            return True
        # [True True True]
        # [False True False]

    # board[0][0] board[1][0] board[2][0]
    # board[0][1] board[1][1] board[2][1]
    # board[0][2] board[1][2] board[2][2]
    for col in range (0, 2 + 1):
        if all(my_board[row][col] == search for row in range (0, 2 + 1)):
            return True

    # board[0][0] [1][1] [2][2]
    if all(my_board[index][index] == search for index in range(0, 2 + 1)):
        return True

    # board[0][2] [1][1] [2][0]
    row = 0
    win = True
    if all(my_board[row][col] == search for col in range(2, 0 - 1, -1)):
        return True

    return False

x_won = check_win(game['board'], 'X')
o_won = check_win(game['board'], 'O')

def is_full(my_board):
    for row in range(0, 2 + 1):
        for col in range(0, 2 + 1):
            if my_board[row][col] != '_':
                return False
    return True

while not is_full(game['board']):
    input_row = int(input('row?'))
    input_col = int(input('col?'))
    # check if number and between 0-2

    # check if empty
    if game['board'][input_row][input_col] == '_':
        game['board'][input_row][input_col] = 'X'
        break
    print('this square is not empty ...')

print(game['board'])


