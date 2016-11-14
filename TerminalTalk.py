"""!@file

Main code for TerminalTalk client. Run this file to use as client.
"""
import socket, select, sys
from client import *


# Main
if __name__ == "__main__":

    if( len(sys.argv) < 2 ):
        moniker = "Anonymous"
    else:
        moniker = sys.argv[1]

    # Connection Setup
    buffer_size = 2 ** 12
    server_port = 7777
    server_ip = "108.74.132.217" # Change to public or local IP depending on intended use.
    server_address = ( server_ip, server_port )

    # Create socket
    megaphone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Three-way Handshake
    try:
        megaphone.connect(server_address)

        # Wait for server to request moniker
        request = megaphone.recv(buffer_size)
        if request == "moniker":
            megaphone.send(moniker)

    except:
        print('Could not connect to TerminalTalk servers. Please try again later.')
        sys.exit()

    # From here on out, we only want to briefly listen to the megaphone socket
    # rather than waiting for data to be recieved. Thus, set a timeout
    megaphone.settimeout(2)

    # Create a list to keep track of connections (terminal input and megaphone)
    connections = [megaphone, sys.stdin]

    eavesdrop() # Listen for user input
    while True:
        # Get a list of readable sockets / inputs
        readables, writables, errors = select.select(connections, [], [])

        for telegraph_i in readables:
            # See if a message has been sent from server
            if telegraph_i == megaphone:
                missive = telegraph_i.recv(buffer_size)
                if missive:
                    sys.stdout.write(missive)
                    eavesdrop() # Listen for user input
                else:
                    # If misssive returns False, the connection is broken.
                    print("\n The connection has been lost... please reconnect.")
                    sys.exit()
            else:
                # See if the user has entered a message
                verbiage = sys.stdin.readline()
                megaphone.send(verbiage)
                eavesdrop() # Listen for user input
