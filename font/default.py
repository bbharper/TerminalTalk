"""!@file

"""

def default(txt):
    """!@brief Gives inputed string default formatting.

    Returns with inputed string with the prefix '\033[0m'.
    The prefix is the ANSI code for reset (white foreground, black background).

    @param txt A string. Will be formatted as default.
    """
    return '\033[0m'+txt
