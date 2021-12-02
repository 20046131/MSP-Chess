class SaveFile:
    def __init__(self):
        self.filename = "GameBoard.txt"

    #createsthe file and will save the start og the game
    def save(self, board):
        try:
            with open(self.filename, mode='w') as file:
                file.write(board.tostring())
        except Exception as error:
            print("Error writing to file: " + str(error))

    def update(self, value, row, coll):
        try:
            with open(self.filename, mode='r+')as file:
                offset = (row)*8 +(coll)
                file.seek(offset)
                file.write(value)
        except Exception as error:
            print("Error writing to file: " + str(error))



