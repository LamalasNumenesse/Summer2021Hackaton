from Colors import *


class Board:
    def __init__(self, length, width):
        # Constructor for the Board class (x, y)
        self.length = length
        self.width = width
        list = []
        for i in range(self.width):  # Creating a 2d array using length and width
            row = []
            for ii in range(self.length):
                row.append(8)  # Default board color is black
            list.append(row)
        self.board = list

    def set_background_color(self, color=8):  # Check color ID on the print function
        for i in range(self.width):
            for ii in range(self.length):
                self.board[i][ii] = color

    def insert_new_color(self, x_cord, y_cord, color):  # Check Color ID on the print function
        self.board[y_cord][x_cord] = color

    def print_array(self):
        for i in range(self.width):
            for ii in range(self.length):
                if self.board[i][ii] == 1:  # Red(number 1)
                    print(colors.RedText, colors.Background_Red, self.board[i][ii], end="")
                elif self.board[i][ii] == 2:  # Green(number 2)
                    print(colors.GreenText, colors.Background_Green, self.board[i][ii], end="")
                elif self.board[i][ii] == 3:  # Yellow(number 3)
                    print(colors.YellowText, colors.Background_Yellow, self.board[i][ii], end="")
                elif self.board[i][ii] == 4:  # Blue(number 4)
                    print(colors.BlueText, colors.Background_Blue, self.board[i][ii], end="")
                elif self.board[i][ii] == 5:  # Cyan(number 5)
                    print(colors.CyanText, colors.Background_Cyan, self.board[i][ii], end="")
                elif self.board[i][ii] == 6:  # Magenta(number 6)
                    print(colors.MagentaText, colors.Background_Magenta, self.board[i][ii], end="")
                elif self.board[i][ii] == 7:  # White(number 7)
                    print(colors.YellowText, colors.Background_White, self.board[i][ii], end="")
                elif self.board[i][ii] == 8:  # Black(number 8)
                    print(colors.BlackText, colors.Background_Black, self.board[i][ii], end="")
            print(colors.Reset)  # Default(number 0)
