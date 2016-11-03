"""!@file

"""

import font
from server import Orator

def server_pontificate( verbiage, connections, server, orators ):
    """!@brief Make announcements from server to everyone connected.

    The message will be formatted (see font.highlight ) so as to stick out
    from all other text. Every connected user will see the message.

    @param verbiage The message displayed.
    @param connections A list of all current connections (sockets).
    @param server The server's socket. Used to ensure message isn't sent to server itself (this
    would break pipe).
    @param orators A list of Orator objects for currently connected clients. If a disconnection
    is discovered while function is being run, it is necessary to remove the object from the
    list.
    """
    for socket_i in connections:
        if socket_i != server:
            try:
                socket_i.send( "\n" + font.highlight(verbiage) + "\n")
            except:
                orator_index = 0
                for i, orator in enumerate(orators):
                    if orator.socket == socket_i:
                        orator_index = i
                        break

                socket_i.close()
                connections.remove(socket_i)
                orators.remove(orator_index)

def pontificate( orator, verbiage, connections, server, client, orators):
    """!@brief Transmit a clients message to all other connected users.

    @param orator The sending client's Orator object.
    @param verbiage The message displayed.
    @param connections A list of all current connections (sockets).
    @param server The server's socket. Used to ensure message isn't sent to server itself (this
    would break pipe).
    @param client The sending client's socket. Used to avoid sending message back to client.
    @param orators A list of Orator objects for currently connected clients. If a disconnection
    is discovered while function is being run, it is necessary to remove the object from the
    list.
    """
    missive = font.bold( orator.color + orator.username + ": " + font.Styles.RESET ) + verbiage
    for socket_i in connections:
        if socket_i != server and socket_i != client:
            try:
                socket_i.send( "\n" + missive )
            except:
                orator_index = 0
                for i, orator in enumerate(orators):
                    if orator.socket == socket_i:
                        orator_index = i
                        break

                socket_i.close()
                connections.remove(socket_i)
                orators.remove(orator_index)
