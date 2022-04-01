# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------
# colors.py - Contains functionality for colors and their console codes.
#
# Description:
# This module is responsible for the encapsulation of console color codes
# and their corresponding functionality.
# -------------------------------------------------------------------------
import os, random
from random import randint

class Colors:
    """Encapsulates colors that can be used to modify and or customize the current bot terminal."""
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Foreground:
        """A collection of available escape code colors for system terminals that change the color of the text itself."""
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class Background:
        """A collection of available escape code colors for system terminals that change the color of the background of the text."""
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

    def random_color(self: "Colors") -> int:
        """Returns a random color as an integer."""
        return random.randint(0, 0xfffff)

    def clear_terminal(self: "Colors") -> None:
        """Clears the current terminal of any characters and associated formatting."""
        _ = os.system('cls') if os.name == 'nt' else os.system('clear') 
  





