from board import *
from saveFile import SaveFile


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #mkaing board
    board = Board()
    board.makeboard()
    file = SaveFile()
    file.save(board)

    iswhitemove= True

    while True:
        # Will keep track of whose turn it is
        if iswhitemove == True:
            print("Whites Move")
        else:
            print("Blacks Move")
        # Will lower the users input
        selectedpice = input("selcect the player you want to move ").lower()
        if selectedpice == ("o-o"):
            # if o-o is entered it will check it the spots are available and if so it will make the move
            if board.isValidCastle(iswhitemove, True):
                board.castle(iswhitemove, True)
                iswhitemove = not iswhitemove
                board.makeboard()
            else:
                print("That move was inValid")
        elif selectedpice == ("o-o-o"):
            # if o-o-o is entered it will check it the spots are available and if so it will make the move
            if board.isValidCastle(iswhitemove, False):
                board.castle(iswhitemove, False)
                iswhitemove = not iswhitemove
                board.makeboard()
            else:
                print("That move was inValid")
        else:
            #if it not calling it will get the ask for the place for the pace
            moveloaction = input("where do you want to move ")

            if board.isValid(iswhitemove, selectedpice, moveloaction):
                # will check if the move is vaild and will reprint the board
                board.move(selectedpice, moveloaction)
                iswhitemove = not iswhitemove
                board.makeboard()

            else:
                # it ether it own peace or not a proper move
                print("That move was inValid")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
