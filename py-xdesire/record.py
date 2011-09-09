import socket

HOST = "localhost"
PORT = 1984
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "Connect"
body = ''
while True:
    data = conn.recv(1024)
    if not data:
        break
    body += data

conn.close()
f = open("request.txt", "w")
f.write(body)

