import os
if os.name == 'nt':
    os.system('color')


class colors:
    # Color Class to make it easier to color the text and background
    BlackText = '\033[30m'
    RedText = '\033[31m'
    GreenText = '\033[32m'
    YellowText = '\033[33m'
    BlueText = '\033[34m'
    MagentaText = '\033b[35m'
    CyanText = '\033[36m'
    WhiteText = '\033[37m'

    Reset = '\033[0m'  # Sets the colors back to default

    Background_Black = '\033[40m'
    Background_Red = '\033[41m'
    Background_Green = '\033[42m'
    Background_Yellow = '\033[43m'
    Background_Blue = '\033[44m'
    Background_Magenta = '\033[45m'
    Background_Cyan = '\033[46m'
    Background_White = '\033[47m'
