horizonal = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
vertical = {
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7
}


class Board:
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
        # "a2"        "a4"

    def makeboard(self):
        boardnumber = 0
        for row in self.board:
            boardnumber += 1
            print(boardnumber, end="| ")
            for square in row:
                print(square, end=" ")
            print("")
        print("-------------------")
        print("   a b c d e f g h ")


    def move(self, selectedpice, moveloaction):
        # A1
        # wselectedpice[0] # A1 = AS
        # wselectedpice[1] # A1 = 1


                            #vertical = selected piace
        pickedup = self.board[vertical[selectedpice[1]]][horizonal[selectedpice[0]]]
        self.board[vertical[selectedpice[1]]][horizonal[selectedpice[0]]] = "."
        self.board[vertical[moveloaction[1]]][horizonal[moveloaction[0]]] = pickedup



        # self.board[3][0]
        #
        # from_row #  1
        # from_col #  0
        #
        # to_row    # 3
        # to_column # 0
        #
        # self.board[]
        #
        # from_lastLoactio

    def isValid(self, iswhitemove, selectedpice, moveloaction):
        # Validate the selcted peice is the right colour
        peice = self.board[vertical[selectedpice[1]]][horizonal[selectedpice[0]]]
        movedto = self.board[vertical[moveloaction[1]]][horizonal[moveloaction[0]]]
        if peice == ".":
            return False

        if iswhitemove and peice.islower():
            #invald as white is upper case
            return False

        if not iswhitemove and peice.isupper():
            #invald as Black is lower case
            return False

        # Validate the move location is either empty or the opposite colour
        if iswhitemove and movedto != "." and movedto.isupper():
            return False
        if not iswhitemove and movedto != "." and movedto.islower():
            return False

        return True

        pass



