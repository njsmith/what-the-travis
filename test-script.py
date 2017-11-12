import socket

s = socket.socket()
# Attempt to bind an ephemeral port
s.bind(("127.0.0.1", 0))
