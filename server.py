import usocket as socket

addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print ("client connected!")
    clientsocket.send(bytes("welcome to server", "utf-8="))
