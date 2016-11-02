"""!@file

"""

def italic(txt):
    """!@brief Makes inputed string italic.

    Returns with inputed string with the prefix '\033[3m' and suffix '\033[23m'.
    The prefix is the ANSI code for italic on. The suffix is the ANSI code
    for italic off.

    @param txt A string. Will be displayed as italic.
    """
    return '\033[3m' + txt + '\033[23m'
