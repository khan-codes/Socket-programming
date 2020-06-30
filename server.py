from socket import *

host = "192.168.10.8"
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))

s.listen(5)  #the number of connections that you want to hear to at a time

while True:
    c, addr = s.accept()
    print("[+] got connection form: ", addr)
    r_msg = c.recv(1024)
    print(r_msg.decode("ascii"))
    msg = "This is from the server"
    c.send(msg.encode("ascii"))
    c.close()
