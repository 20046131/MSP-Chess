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

    def move(self, from_lastLoaction, to_newLoaction):
        wselectedpice = input("selcect the player you want to move")
        wmoveloaction = input("where do you want to move")

        # A1
        # wselectedpice[0] # A1 = AS
        # wselectedpice[1] # A1 = 1

        pickedup = self.board[vertical[wselectedpice[1]]][horizonal[wselectedpice[0]]]
        self.board[vertical[wselectedpice[1]]][horizonal[wselectedpice[0]]] = "."
        self.board[vertical[wselectedpice[1]]][horizonal[wselectedpice[0]]] = pickedup

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



