import socket

sock = socket.socket()
sock.connect(("localhost", 6070))
sock.send("ECHO gg".encode())

data = sock.recv(1024).decode()
sock.close()

print(data)
