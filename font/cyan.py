"""!@file

"""

def cyan(txt):
    """!@brief Makes inputed string cyan.

    Returns with inputed string with the prefix '\033[36m' and suffix '\033[0m'.
    The prefix is the ANSI code for cyan foreground. The suffix is the ANSI code
    for reset (white forground, black background).

    @param txt A string. Will be displayed as cyan.
    """
    return '\033[36m' + txt + '\033[0m'
