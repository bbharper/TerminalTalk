"""!@file

"""

import random, font

class Orator:
    """!@brief Stores information about a connected client.

    An Orator objects is used to represent a client. Each client has a username and color
    associated with them. The username is provided by the client. The color is assigned randomly
    each time the client connects.
    """

    def __init__(self, telegraph):
        """!@brief Constructor for Orator class.

        @param telegraph The socket used to connect with client.
        """
        self.telegraph = telegraph
        self.username = "Anonymous"
        colors = [
            font.Colors.RED,
            font.Colors.YELLOW,
            font.Colors.BLUE,
            font.Colors.MAGENTA,
            font.Colors.CYAN,
            font.Colors.GREEN
            ]
        self.color = colors[ random.randrange(0, len(colors) ) ]
