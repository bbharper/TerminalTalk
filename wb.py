import font, sys, socket, random
from orator import Orator

port = 7777
buffer_size = 2 ** 12
server_address = ( socket.gethostname(), port )
# Create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind( server_address )
server.listen(5)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

bob = Orator(server)
bob.username= "Pegasus"
print(bob.username)
