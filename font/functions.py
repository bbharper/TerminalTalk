"""!@file

Defines functions for surronding strings with ANSI codes for formating text.
"""
from constants import Colors

def get_color_code(color):
    """!@brief Returns ANSI color code for specified color.

    Returns ANSI code necessary to make subsequent text into specified color. Example:
    print( get_color_code("green") + "This text will be green." )

    If color is not availbe, the function will return False

    @param color A string containing color name. Example "green"
    """
    
    switch = {
        "black": Colors.BLACK,
        "red": Colors.RED,
        "green": Colors.GREEN,
        "yellow": Colors.YELLOW,
        "blue": Colors.BLUE,
        "magenta": Colors.MAGENTA,
        'cyan': Colors.CYAN,
        "white": Colors.WHITE
    }
    result = switch.get(color, False)
    return result

def blue(txt):
    """!@brief Makes inputed string blue.

    Returns with inputed string with the prefix '\033[34m' and suffix '\033[0m'.
    The prefix is the ANSI code for blue foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as blue.
    """
    return '\033[34m' + txt + '\033[0m'


def cyan(txt):
    """!@brief Makes inputed string cyan.

    Returns with inputed string with the prefix '\033[36m' and suffix '\033[0m'.
    The prefix is the ANSI code for cyan foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as cyan.
    """
    return '\033[36m' + txt + '\033[0m'


def green(txt):
    """!@brief Makes inputed string green.

    Returns with inputed string with the prefix '\033[32m' and suffix '\033[0m'.
    The prefix is the ANSI code for green foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as green.
    """
    return '\033[32m' + txt + '\033[0m'


def magenta(txt):
    """!@brief Makes inputed string magenta.

    Returns with inputed string with the prefix '\033[35m' and suffix '\033[0m'.
    The prefix is the ANSI code for magenta foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as magenta.
    """
    return '\033[35m' + txt + '\033[0m'


def red(txt):
    """!@brief Makes inputed string red.

    Returns with inputed string with the prefix '\033[31m' and suffix '\033[0m'.
    The prefix is the ANSI code for red foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as red.
    """
    return '\033[31m' + txt + '\033[0m'


def yellow(txt):
    """!@brief Makes inputed string red.

    Returns with inputed string with the prefix '\033[33m' and suffix '\033[0m'.
    The prefix is the ANSI code for red foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as red.
    """
    return '\033[33m' + txt + '\033[0m'


def underline(txt):
    """!@brief Makes inputed string underline.

    Returns with inputed string with the prefix '\033[4m' and suffix '\033[24m'.
    The prefix is the ANSI code for underline on. The suffix is the ANSI code
    for underline off.

    @param txt A string. Will be underlined.
    """
    return '\033[4m' + txt + '\033[24m'


def bold(txt):
    """!@brief Makes inputed string bold.

    Returns with inputed string with the prefix '\033[1m' and suffix '\033[22m'.
    The prefix is the ANSI code for bold font on. The suffix is the ANSI code
    for bold font off.

    @param txt A string. Will be made bold.
    """
    return '\033[1m' + txt + '\033[22m'

def italic(txt):
    """!@brief Makes inputed string italic.

    Returns with inputed string with the prefix '\033[3m' and suffix '\033[23m'.
    The prefix is the ANSI code for italic on. The suffix is the ANSI code
    for italic off.

    @param txt A string. Will be displayed as italic.
    """
    return '\033[3m' + txt + '\033[23m'


def default(txt):
    """!@brief Gives inputed string default formatting.

    Returns with inputed string with the prefix '\033[0m'.
    The prefix is the ANSI code for reset (white foreground, black background).

    @param txt A string. Will be formatted as default.
    """
    return '\033[0m'+txt


def highlight(txt):
    """!@brief Highlights inputed string.

    Returns with inputed string with the prefixes '\033[47m', '\033[30m', and'\033[3m', and with
    the suffix '\033[0m'. The prefix is the ANSI code for italic, white background, and black
    foreground. The suffix is the ANSI code for reset (white forground, black background).

    @param txt A string. Will be highlighted.
    """
    return '\033[47m' + '\033[30m'+'\033[3m' + txt + '\033[0m'
