"""!@file

"""

import font
from server import Orator

def megaphone( verbiage, connections, ear_trumpet, orators ):
    """!@brief Make announcements from server to everyone connected.

    The message will be formatted (see font.highlight ) so as to stick out
    from all other text. Every connected user will see the message.

    @param verbiage The message displayed.
    @param connections A list of all current connections (sockets).
    @param ear_trumpet The server's socket. Used to ensure message isn't sent to server itself (this
    would break pipe).
    @param orators A list of Orator objects for currently connected clients. If a disconnection
    is discovered while function is being run, it is necessary to remove the object from the
    list.
    """
    for telegraph_i in connections:
        if telegraph_i != ear_trumpet:
            try:
                telegraph_i.send( "\n" + font.highlight(verbiage) + "\n")
            except:
                orator_index = 0
                for i, orator in enumerate(orators):
                    if orator.telegraph == telegraph_i:
                        orator_index = i
                        break

                telegraph_i.close()
                connections.remove(telegraph_i)
                orators.remove(orator_index)

def pontificate( orator, verbiage, connections, ear_trumpet, orators):
    """!@brief Transmit a clients message to all other connected users.

    @param orator The sending client's Orator object.
    @param verbiage The message displayed.
    @param connections A list of all current connections (sockets).
    @param ear_trumpet The server's socket. Used to ensure message isn't sent to server itself (this
    would break pipe).
    @param orators A list of Orator objects for currently connected clients. If a disconnection
    is discovered while function is being run, it is necessary to remove the object from the
    list.
    """
    missive = font.bold( orator.color + orator.moniker + ": " + font.Styles.RESET ) + verbiage
    for telegraph_i in connections:
        if telegraph_i != ear_trumpet and telegraph_i != orator.telegraph:
            try:
                telegraph_i.send( "\n" + missive )
            except:
                orator_index = 0
                for i, orator in enumerate(orators):
                    if orator.telegraph == telegraph_i:
                        orator_index = i
                        break

                telegraph_i.close()
                connections.remove(telegraph_i)
                orators.remove(orator_index)
