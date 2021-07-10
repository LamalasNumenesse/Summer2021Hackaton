from Colors import *
class Board:
    def __init__(self, length, width):
    # Constructor for the Board class (x, y)
        self.length = length
        self.width = width
        list = []
        for i in range(self.width): # Creating a 2d array using length and width
            row = []
            for ii in range(self.length):
                row.append(0)
            list.append(row)
        self.board = list

    def print_array(self):
        self.board[0][2] = 1 # Testing for different colors
        for i in range(self.width):
            for ii in range(self.length):
                if self.board[i][ii] == 1: # If we find the one it will print Red box
                    print(colors.RedText, colors.Background_Red, self.board[i][ii], colors.Reset, end="")
                else: # Green is default color
                    print(colors.GreenText, colors.Background_Green, self.board[i][ii], colors.Reset, end="")
            print("")
