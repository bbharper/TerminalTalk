"""!@file

Main code for TerminalTalk server. Run this file to start server.
"""
import socket, select, font
from server import *


# Main
if __name__ == "__main__":
    #Setup
    port = 7777
    buffer_size = 2 ** 12
    server_address = ( "", port )

    connections = [] # A list that keeps track of active sockets
    orators = [] # A list of active Orators

    # Create the server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( server_address )
    server.listen(5)

    # Add server to connections. This will be used to listen for new connections.
    connections.append(server)

    print("Server running...")

    while True:
        # Use select function to check which sockets are ready to be read.
        readables, writables, errors = select.select(connections, [], [])

        # Loop through readables. Address each.
        for socket_i in readables:
            # A new connection has been requested
            if socket_i == server:
                # Accept connection
                file_descriptor, address = socket_i.accept()
                connections.append(file_descriptor)

                # Add an Orator object to orators to keep track of user data
                orators.append( Orator(file_descriptor) )
                file_descriptor.send("username")                   # Request username
                username = file_descriptor.recv(buffer_size)       # Wait to get a response
                orators[len(orators)-1].username = username # Assign username to Orator


                # State that a new user has entered.
                entrance_message = username + " has entered."
                server_pontificate( entrance_message, connections, server, orators )
                print(entrance_message)
            else:
                # Determine which orator is speaking. Identify with position in orators array.
                orator_index = 0
                for i, orator in enumerate(orators):
                    if orator.socket == socket_i:
                        orator_index = i
                        break

                # Now let the orator speak
                try:
                    verbiage = socket_i.recv(buffer_size)
                    if verbiage:
                        pontificate( orators[orator_index], verbiage, connections, server, socket_i, orators )
                        print( font.bold( orators[orator_index].color + orators[orator_index].username + ": " + font.Styles.RESET ) + verbiage)
                except:
                    # This indicates that the connection has been broken.
                    missive = orators[orator_index].username + " has exited."
                    pontificate( orators[orator_index], missive, connections, server, socket_i, orators )
                    print(missive)

                    # Remove from connections and orators list
                    socket_i.close()
                    orators.remove( orators[orator_index] )
                    connections.remove( socket_i )
                    continue


# If for any reason while loop is exited (this should never happen)
# then close server.
server.close()
