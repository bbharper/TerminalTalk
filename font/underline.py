"""!@file

"""

def underline(txt):
    """!@brief Makes inputed string underline.

    Returns with inputed string with the prefix '\033[4m' and suffix '\033[24m'.
    The prefix is the ANSI code for underline on. The suffix is the ANSI code
    for underline off.

    @param txt A string. Will be underlined.
    """
    return '\033[4m' + txt + '\033[24m'
