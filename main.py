from board import *


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
    makeboard()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
