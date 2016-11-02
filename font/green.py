"""!@file

"""

def green(txt):
    """!@brief Makes inputed string green.

    Returns with inputed string with the prefix '\033[32m' and suffix '\033[0m'.
    The prefix is the ANSI code for green foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as green.
    """
    return '\033[32m' + txt + '\033[0m'
