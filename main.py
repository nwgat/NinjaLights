import usocket as socket
import hue
addr = socket.getaddrinfo('0.0.0.0', 1234)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr))
s.listen(1)
h = hue.Bridge()
while True:
    clientsocket, address = s.accept()
    print ("client connected!")
    clientsocket.send(bytes("welcome to server", "utf-8="))
    h.setGroup(1,on=False)
    h.setGroup(2,on=False)
