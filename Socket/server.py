import socket 

sock = socket.socket()

sock.bind(('localhost', 500))

sock.listen()

conn, addr = sock.accept()
