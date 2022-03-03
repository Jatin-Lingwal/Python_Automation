import socket

class Grappler:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.socket.settimeout(2)
        self.socket.connect((self.ip, self.port))

    def read(self, len=1024): #receiving the data from the socket
        return self.socket.recv(len)

    def close(self):
        self.socket.close()

