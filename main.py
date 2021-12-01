from board import *
from saveFile import SaveFile


def makeboard():
    boardnumber = 0
    for row in Board:
        boardnumber += 1
        print(boardnumber, end="| ")
        for square in row:
            print(square, end=" ")
        print("")
    print("-------------------")
    print("   a b c d e f g h ")


def whitemoves():
    wselectedpice = input("selcect the player you want to move")
    wmoveloaction = input("where do you want to move")


def blackmoves():
    bselectedpice = input("selcect the player you want to move")
    bmoveloaction = input("where do you want to move")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #mkaing board
    board = Board()
    board.makeboard()
    file = SaveFile()
    file.save(board)

    iswhitemove= True

    while True:
        if iswhitemove == True:
            print("Whites Move")
        else:
            print("Blacks Move")
        selectedpice = input("selcect the player you want to move ")
        moveloaction = input("where do you want to move ")

        if board.isValid(iswhitemove, selectedpice, moveloaction):
            board.move(selectedpice, moveloaction)
            iswhitemove = not iswhitemove
            board.makeboard()

        else:
            print("That move was inValid")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
