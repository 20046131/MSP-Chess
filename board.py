from saveFile import SaveFile

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
            ['R', '.', '.', 'K', '.', '.', '.', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', '.', '.', 'k', '.', '.', '.', 'r']
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

    def tostring(self):
        stringgameboard = ""
        for row in self.board:
            for square in row:
                stringgameboard += square

        return stringgameboard

    def move(self, selectedpice, moveloaction):
        # A1
        # wselectedpice[0] # A1 = AS
        # wselectedpice[1] # A1 = 1


                            #vertical = selected piace
        pickedup = self.board[vertical[selectedpice[1]]][horizonal[selectedpice[0]]]
        self.board[vertical[selectedpice[1]]][horizonal[selectedpice[0]]] = "."
        self.board[vertical[moveloaction[1]]][horizonal[moveloaction[0]]] = pickedup

        file = SaveFile()
        # Update the selectedpice
        row = vertical[selectedpice[1]]
        col = horizonal[selectedpice[0]]
        val = "."
        file.update(val, row, col)
        # Update the moveloaction
        row = vertical[moveloaction[1]]
        col = horizonal[moveloaction[0]]
        val = pickedup
        file.update(val, row, col)

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

    def isValidCastle(self, iswhitemove, iskingside ):
        if iswhitemove and iskingside:
            return  self.board[0][1]=="." and self.board[0][2] == "." and self.board[0][0] == "R"and self.board[0][3] == "K"
        if iswhitemove and not iskingside:
            return self.board[0][6] == "." and self.board[0][5] == "." and self.board[0][4] == "." and self.board[0][7] == "R" and self.board[0][3] == "K"
        if not iswhitemove and iskingside:
            return self.board[7][1] == "." and self.board[7][2] == "." and self.board[7][0] == "r" and self.board[7][3] == "k"
        if not iswhitemove and not iskingside:
            return self.board[7][6] == "." and self.board[7][5] == "." and self.board[7][4] == "." and self.board[7][7] == "r" and self.board[7][3] == "k"



    def castle (self, iswhitemove, iskingside ):
        file = SaveFile()
        if iswhitemove and iskingside:
            self.board[0][1] = "K"
            self.board[0][2] = "R"
            self.board[0][0] = "."
            self.board[0][3] = "."
            file.update("K", 0, 1)
            file.update("R", 0, 2)
            file.update(".", 0, 0)
            file.update(".", 0, 3)

        if iswhitemove and not iskingside:
            self.board[0][6] = "."
            self.board[0][5] = "K"
            self.board[0][4] = "R"
            self.board[0][7] = "."
            self.board[0][3] = "."
            file.update(".", 0, 6)
            file.update("K", 0, 5)
            file.update("R", 0, 4)
            file.update(".", 0, 7)
            file.update(".", 0, 3)
        if not iswhitemove and iskingside:
            self.board[7][1] = "k"
            self.board[7][2] = "r"
            self.board[7][0] = "."
            self.board[7][3] = "."
            file.update("k", 7, 1)
            file.update("r", 7, 2)
            file.update(".", 7, 0)
            file.update(".", 7, 3)
        if not iswhitemove and not iskingside:
            self.board[7][6] = "."
            self.board[7][5] = "k"
            self.board[7][4] = "r"
            self.board[7][7] = "."
            self.board[7][3] = "."
            file.update(".", 7, 6)
            file.update("k", 7, 5)
            file.update("r", 7, 4)
            file.update(".", 7, 7)
            file.update(".", 7, 3)




