import socket
request = "GET http://www.baidu.com/ HTTP/1.1\n\rHost: www.baidu.com\n\r\n\r"

HOST = "http://xdesire-args.dotcloud.com"
PORT = 8080
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(request)
body = ''
while True:
    data = s.recv(1024)
    print data
    if not data:
        break
    body += data

s.close()
print body
