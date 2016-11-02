"""!@file

"""

def blue(txt):
    """!@brief Makes inputed string blue.

    Returns with inputed string with the prefix '\033[34m' and suffix '\033[0m'.
    The prefix is the ANSI code for blue foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as blue.
    """
    return '\033[34m' + txt + '\033[0m'
