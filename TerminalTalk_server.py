#!/usr/bin/python
import socket, select, font, orator

def server_pontificate( verbiage, connections, server ):
    for socket_i in connections:
        if socket_i != server:
            socket_i.send( font.highlight(verbiage) )

def pontificate( orator, verbiage, connections, server ):
    missive = font.bold( orator.color + orator.username ) + verbiage
    for socket_i in connections:
        if socket_i != server:
            socket_i.send( missive )


# Main
if __name__ == "__main__":
    #Setup
    port = 7777
    buffer_size = 2 ** 12
    server_address = ( socket.gethostname(), port )

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

                # Add an Orator object to orators to keep track of user data
                orators.append( Orator(socket_i) )
                socket_i.send("username")                   # Request username
                username = socket_i.recv(buffer_size)       # Wait to get a response
                orators[len(orators)-1].username = username # Assign user to Orator

                # State that a new user has entered.
                entrance_message = username + " has entered."
                server_pontificate( entrance_message, connections, server )

            # An orator is attemptings to speak
            else:
                # Determine which orator is speaking. Identify with position in orators array.
                orator_index = 0
                for orator in orators:
                    if orator.socket == socket_i:
                        break
                    else:
                        orator_index += 1

                # Now let the orator speak
                try:
                    verbiage = socket_i.recv(buffer_size)
                    if verbiage:
                        pontificate( orators[orator_index], verbiage, connections, server )
                except:
                    # This indicates that the connection has been broken.
                    missive = orators[orator_index].username + " has exited."
                    pontificate( orators[orator_index], missive, connections, server )

                    # Remove from connections and orators list
                    socket_i.close()
                    orators.remove( orators[orator_index] )
                    connectiosn.remove( socket_i )
                    continue

# If for any reason while loop is exited (this should never happen)
# then close server.
server.close()
