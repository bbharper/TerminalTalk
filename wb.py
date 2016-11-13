import font, sys, socket, random

def choose_color(color):
    switch = {
        "black": '\033[30m]',
        "red": '\033[31m',
        "green":  '\033[32m',
        "yellow": '\033[33m',
        "blue": '\033[34m',
        "magenta": '\033[35m',
        'cyan': '\033[36m',
        "white": '\033[37m'
    }
    color = switch.get(color, "Specified color does not exist.")
    return color

print( font.get_color_code("green") + "I am green")

"""
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def op(operator,a,b):
    switch = {
        '+': add,
        '-': subtract,
    }
    foo = switch.get(operator, lambda x,y: x*y)
    return foo(a,b)

result = op('k', 5,3)
print(result)
"""

"""
class MyClass:
    def __init__(self, name):
        self.name = name


def foo(obj):
    obj.name = "Sally"


bob = MyClass("Bob")
foo(bob)

print(bob.name)

"""

"""
arry = []
my_string = "\setcolor blue powerpuff mongoose stew"

if my_string[0] == "\\":
    arry = my_string.split(" ")
    print( "The command is " + arry[0][1:] )
    print( "The argument is " + my_string[ len(arry[0]) +1 :  ] )
else:
    print( "No a command" )

"""
