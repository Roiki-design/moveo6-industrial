import socket
import sys
import struct
import time
import scapy
# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

from scapy.all import *



# Bind the socket to the port
server1_address = ('', 11000)
server2_address = ('', 11002)
print >>sys.stderr, 'starting up on %s port %s' % server1_address
print >>sys.stderr, 'starting up on %s port %s' % server2_address
sock1.bind(server1_address)
sock2.bind(server2_address)

sock1.listen(1)
sock2.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client1_address = sock1.accept()
    connection, client2_address = sock2.accept()

    try:
        print >>sys.stderr, 'connection from', client1_address
        print >>sys.stderr, 'connection from', client2_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'got data'
                print >>sys.stderr,"%s" % data
            else:
                print >>sys.stderr, 'no more data from', client1_address
                break
    finally:
             # Clean up the connection
              connection.close()
