import re


def choose_sign(matrix):
    # the game always starts with X, so if the number of X's and O's on the field is the same,
    # the user should make a move with X, and if X's is one more than O's,
    # then the user should make a move with O.

    count_x = sum(line.count('X') for line in matrix)
    count_o = sum(line.count('O') for line in matrix)
    if count_x == count_o:
        return 'X'
    else:
        return 'O'


def move(x, y, matrix, sign):
    matrix = write_to_cell(x, y, matrix, sign)
    return  matrix


def check_win(matrix):
    if (matrix[0][0] == 'X' and matrix[0][1] == 'X' and matrix[0][2] == 'X') or \
            (matrix[1][0] == 'X' and matrix[1][1] == 'X' and matrix[1][2] == 'X') or \
            (matrix[2][0] == 'X' and matrix[2][1] == 'X' and matrix[2][2] == 'X') or \
            (matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X') or \
            (matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X'):
        print('X wins')
    elif (matrix[0][0] == 'O' and matrix[0][1] == 'O' and matrix[0][2] == 'O') or \
            (matrix[1][0] == 'O' and matrix[1][1] == 'O' and matrix[1][2] == 'O') or \
            (matrix[2][0] == 'O' and matrix[2][1] == 'O' and matrix[2][2] == 'O') or \
            (matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O') or \
            (matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O'):
        print('O wins')
    else:
        matrix_as_line = ''.join([str(i) for line in matrix for i in line])
        if ' ' in matrix_as_line:
            print('Game not finished')
        else:
            print('Draw')


def read_cell(x, y, matrix):
    # cells look like this:
    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)

    x -= 1
    y -= 1
    return matrix[2-y][x]


def write_to_cell(x, y, matrix, sign):
    # cells look like this:
    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)

    x -= 1
    y -= 1
    matrix[2 - y][x] = sign
    return matrix


def check_the_cell_is_empty(x, y, matrix):
    if read_cell(x, y, matrix) == " ":
        return True
    else:
        return False


def check_input(input_string, cells):
    # input should be: 2 numbers separated by a space
    if not re.match('^\\d+ \\d+$', input_string):
        print('You should enter numbers!')
        return False

    else:
        x = int(input_string.split()[0])
        y = int(input_string.split()[1])

        # each coordinate should be within field size (from 1 to 3)
        if x > 3 or y > 3 or x < 1 or y < 1:
            print('Coordinates should be from 1 to 3!')
            return False

        # cell should be empty
        elif not check_the_cell_is_empty(x, y, cells):
            print('This cell is occupied! Choose another one!')
            return False
        else:
            return True


def print_the_grid(matrix):
    print("---------")
    print("| " + " ".join(matrix[0]) + " |")
    print("| " + " ".join(matrix[1]) + " |")
    print("| " + " ".join(matrix[2]) + " |")
    print("---------")


def tick_tack_toe():
    line = input("Enter cells: ")
    line = line.replace("_", " ")
    matrix = [[i for i in line[0:3]],
              [i for i in line[3:6]],
              [i for i in line[6:9]]]
    print_the_grid(matrix)

    coordinates = input("Enter the coordinates: ")
    while not check_input(coordinates, matrix):
        coordinates = input("Enter the coordinates: ")
    x, y = [int(i) for i in coordinates.split(' ')]
    sign = choose_sign(matrix)
    matrix = move(x, y, matrix, sign)
    print_the_grid(matrix)
    check_win(matrix)


tick_tack_toe()