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
    server_ip = "192.168.1.77" # Change to public or local IP depending on intended use.
    server_address = ( server_ip, port )


    # Create the server socket
    ear_trumpet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ear_trumpet.bind( server_address )
    ear_trumpet.listen(5)

    connections = [ear_trumpet] # A list that keeps track of active sockets
    orators = [] # A list of active Orators

    print("Server running...")

    while True:
        # Use select function to check which sockets are ready to be read.
        readables, writables, errors = select.select(connections, [], [])

        # Loop through readables. Address each.
        for telegraph_i in readables:
            # A new connection has been requested
            if telegraph_i == ear_trumpet:
                # Accept connection
                file_descriptor, address = telegraph_i.accept()
                connections.append(file_descriptor)

                # Add an Orator object to orators to keep track of user data
                orators.append( Orator(file_descriptor) )
                file_descriptor.send("moniker")                   # Request moniker
                moniker = file_descriptor.recv(buffer_size)       # Wait to get a response
                orators[len(orators)-1].moniker = moniker # Assign moniker to Orator


                # State that a new user has entered.
                entrance_message = moniker + " has entered."
                megaphone( entrance_message, connections, ear_trumpet, orators )
                print(entrance_message)
            else:
                # Determine which orator is speaking. Identify with position in orators array.
                orator_index = 0
                for i, orator in enumerate(orators):
                    if orator.telegraph == telegraph_i:
                        orator_index = i
                        break

                # Now read the orator socket
                try:
                    verbiage = telegraph_i.recv(buffer_size)
                    if verbiage:
                        # Check whether the recieved missive is a command
                        if verbiage[0] == "\\":
                            # Decode and action command
                            obey(verbiage, orators[orator_index], telegraph_i)
                        else:
                            pontificate( orators[orator_index], verbiage, connections, ear_trumpet, orators )
                            print( font.bold( orators[orator_index].color + orators[orator_index].moniker + ": " + font.Styles.RESET ) + verbiage)
                except:
                    # This indicates that the connection has been broken.
                    missive = orators[orator_index].moniker + " has exited."
                    pontificate( orators[orator_index], missive, connections, ear_trumpet, orators )
                    print(missive)

                    # Remove from connections and orators list
                    telegraph_i.close()
                    orators.remove( orators[orator_index] )
                    connections.remove( telegraph_i )
                    continue


# If for any reason while loop is exited (this should never happen)
# then close server.
ear_trumpet.close()
