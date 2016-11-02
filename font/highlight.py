"""!@file

"""

def highlight(txt):
    """!@brief Highlights inputed string.

    Returns with inputed string with the prefixes '\033[47m', '\033[30m', and'\033[3m', and with
    the suffix '\033[0m'. The prefix is the ANSI code for italic, white background, and black
    foreground. The suffix is the ANSI code for reset (white forground, black background).

    @param txt A string. Will be highlighted.
    """
    return '\033[47m' + '\033[30m'+'\033[3m' + txt + '\033[0m'
