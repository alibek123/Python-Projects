import re


def show_grid(moves):
    print("---------")
    print("\n".join(["| " + "".join(['{:2}'.format(item) for item in row]) + "|" for row in moves]))  # Showing the grid
    print("---------")


def check_coordinates(x, y):
    if not (x.isdigit() and y.isdigit()):
        return 1, "You should enter numbers!"
    elif not ((1 <= int(x) <= 3) and (1 <= int(y) <= 3)):
        return 2, "Coordinates should be from 1 to 3!"
    elif moves[int(x) - 1][int(y) - 1] != " ":
        return 3, "This cell is occupied! Choose another one!"
    else:
        return 4, "OK"


def check_no_moves():
    for i in moves:
        for j in i:
            if j == " ":
                return False
    return True


def check_win_draw():
    global moves
    wins = [[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], \
           [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]
    for i in range(8):
        for j in range(3):
            wins[i][j] = moves[wins[i][j][0]][wins[i][j][1]]  # Changing array "wins" with inputted values
    set_win = [len(set(wins[i])) for i in range(len(wins))]
    if 1 in set_win and set(wins[set_win.index(1)]) != {' '}:  # Checks whether grid has win line and it is not "_"
        return [1, wins[set_win.index(1)][0]]
    elif 1 not in set_win and check_no_moves():  # If no moves present and nobody wins it is draw
        return [2, 2]
    return [0, 0]


# write your code here
moves = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
check_no_moves()
isWin = False

o_turn = False

show_grid(moves)

good_move = False

while not isWin:
    x, y = input("Enter the coordinates:").split()
    n, mes = check_coordinates(x, y)
    if n == 1:
        print(mes)
    if n == 2:
        print(mes)
    if n == 3:
        print(mes)
    if n == 4:
        if o_turn:
            moves[int(x) - 1][int(y) - 1] = "O"
            o_turn = False
        else:
            moves[int(x) - 1][int(y) - 1] = "X"
            o_turn = True
        show_grid(moves)
    wins = check_win_draw()
    if wins[0] == 1:
        print(f"{wins[1]} wins")
        isWin = True
    elif wins[0] == 2:
        print("Draw")
        isWin = True
