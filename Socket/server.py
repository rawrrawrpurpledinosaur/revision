import socket 

sock = socket.socket()

sock.bind(('localhost', 500))

sock.listen()

conn, addr = sock.accept()

end = False

while not end: 
    data = conn.recv(1024)
    if not data:
        end = True
    else:
        print(data.decode())
        conn.send(data)

conn.close()
sock.close()
