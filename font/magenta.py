"""!@file

"""

def magenta(txt):
    """!@brief Makes inputed string magenta.

    Returns with inputed string with the prefix '\033[35m' and suffix '\033[0m'.
    The prefix is the ANSI code for magenta foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as magenta.
    """
    return '\033[35m' + txt + '\033[0m'
