"""!@file

"""

def bold(txt):
    """!@brief Makes inputed string bold.

    Returns with inputed string with the prefix '\033[1m' and suffix '\033[22m'.
    The prefix is the ANSI code for bold font on. The suffix is the ANSI code
    for bold font off.

    @param txt A string. Will be made bold.
    """
    return '\033[1m' + txt + '\033[22m'
