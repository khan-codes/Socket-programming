from socket import *

host = "192.168.10.8"
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

msg = 'This is from the client'

s.send(msg.encode('ascii'))
r_msg = s.recv(1024)

print(r_msg.decode('ascii'))

s.close()
