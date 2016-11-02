"""!@file

"""

def yellow(txt):
    """!@brief Makes inputed string red.

    Returns with inputed string with the prefix '\033[33m' and suffix '\033[0m'.
    The prefix is the ANSI code for red foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as red.
    """
    return '\033[33m' + txt + '\033[0m'
