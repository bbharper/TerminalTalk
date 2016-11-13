"""!@file

Defines functions for procesing user inputed commands.
"""
import font, socket
from server import Orator

def setcolor(telegraph, orator, color):
    """!@brief Changes user's display color to specified value.

    This function is inteded to be called by the obey function. When called, the function
    calls the get_color_code functions from the font module. If the color is available,
    setcolor changes the color attribute of the specified Orator object and confirms the
    change through the specifed socket (telegraph). If the color is unavailable, the user
    is informed through the specified socket.

    @param telegraph The user's socket.
    @param orator The Orator object tracking the user's info.
    @param color A string specifying a color. Example: "green"
    """
    new_color =font.get_color_code(color)
    if new_color != False:
        orator.color = new_color
        telegraph.send( font.highlight( "Your color has been set to " + new_color + color ) + "\n" )
    else:
        telegraph.send( font.highlight("The color specified is not available.\n" ) )

def setmoniker(telegraph, orator, moniker):
    """!@brief Changes user's moniker to specifed value.

    This function is inteded to be called by the obey function. When called, the function
    sets the moniker attribute of the specified Orator object to the moniker parameter.

    @param telegraph The user's socket.
    @param orator The Orator object tracking the user's info.
    @param moniker A string containing the new moniker.
    """
    orator.moniker = moniker
    telegraph.send( font.highlight( "Hello " + moniker + "\n" ) )

def disconnect(telegraph, orator, unsused_string):
    """!@brief Disconnects user from TerminalTalk chatroom.


    @param telegraph The user's socket.
    @param orator The Orator object tracking the user's info.
    @param unsused_string A string. Unused. Can contain any value.
    """
    telegraph.send( font.highlight("You have disconnected.\n")  )
    telegraph.close()
    orators.remove( orator )
    connections.remove( telegraph )

def obey(full_command, orator, telegraph):
    """!@brief Processes and executes user specified commands.

    The obey function parses the full_command parameter into command and argument strings. Using
    the command string is finds and calls the appropriate function (setcolor, setmoniker,
    disconnect) and passes the argument string and any other necessary parameters to it.

    @param full_command The string containting the command and argument sent by user.
    @param orator The Orator object tracking the user's info
    @param telegraph The user's socket.
    """
    parsed_command = []
    parsed_command = full_command.split(" ")
    command = parsed_command[0][1:]
    argument = full_command[ len(command)+2 : len(full_command)-1 ]
    switch = {
        'setcolor': setcolor,
        'setmoniker': setmoniker,
        'disconnect': disconnect
    }

    execute = switch.get(command, lambda x,y,z: telegraph.send("Command not found. (Note: \diconnect must be followed by a space.)\n") )
    execute(telegraph, orator, argument)
