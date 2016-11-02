"""!@file

Defines classes contains ANSI constants for formating text.
"""

class Styles:
    """!@brief Contains constants for ANSI text style codes

    Prefix a string with a style constant to change subsequent text style.
    Example: print( font.Styles.BOLD + "This text will be bold.")
    """
    RESET = '\033[0m'
    BOLD = '\033[1m'
    BOLD_OFF = '\033[22m'
    ITALIC = '\033[3m'
    ITALIC_OFF = '\033[23m'
    UNDERLINE = '\033[4m'
    UNDERLINE_OFF = '\033[24m'
    STRIKETHROUGH = '\033[9m'
    STRIKETHROUHG_OFF = '\033[29m'
    INVERSE = '\033[7m'
    INVERSE_OFF = '\033[27m'


class Colors:
    """!@brief Contains constants for ANSI color codes

    Prefix a string with color constant to change subsequent text to the color.
    Example: print( font.Colors.RED + "This text will be red.")
    """
    BLACK = '\033[30m]'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
