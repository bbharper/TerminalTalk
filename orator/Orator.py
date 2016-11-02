import random

class Orator:

    def __init__(self, socket):
        self.socket = socket
        self.username = "Anonymous"
        colors = ['\033[34m', '\033[36m', '\033[32m', '\033[35m', '\033[31m', '\033[33m']
        self.color = colors[ random.randrange(0, len(colors) ) ]
