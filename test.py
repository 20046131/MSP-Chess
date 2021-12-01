def __init__(self):
    self.board = [
        ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
    ]
def makeboard():
    boardnumber = 0
    for row in board:
        boardnumber += 1
        print(boardnumber, end="| ")
        for square in row:
            print(square, end=" ")
        print("")
    print("-------------------")
    print("   a b c d e f g h ")


makeboard()

pickedup= board[1][0]
board[1][0] = "."
board[3][0] = pickedup

makeboard()



if user input == 0-0
    check itwite move is ture
    move  1c-b1

    eslse
    move b8 c8
