import socket
ip = '192.168.1.232'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((((ip)), 1234))
msg = s.recv(1024)
print(msg.decode("utf-8"))