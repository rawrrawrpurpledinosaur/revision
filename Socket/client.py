import socket 

sock = socket.socket()

sock.connect(('localhost', 5000))

end = False

while not end: 
    message = input("Enter a message: ")
    sock.send(message.encode())
    if message == "exit":
        end = True
    else:
        response = sock.recv(1024)
        print(response.decode())

sock.close()

