import random, font

class Orator:

    def __init__(self, socket):
        self.socket = socket
        self.username = "Anonymous"
        colors = [font.Colors.RED,font.Colors.YELLOW,font.Colors.BLUE,font.Colors.MAGENTA,font.Colors.CYAN,font.Colors.GREEN]
        self.color = colors[ random.randrange(0, len(colors) ) ]
