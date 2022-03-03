import socket

class Scanner:
    def __init__(self,ip):
        self.ip = ip
        self.open_ports = []

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lp, up):
        for port in range(lp, up+1):
            if self.is_open(port):
               self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #for establishing connection, the values may vary, socket.socket()=>sets to default values
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0
