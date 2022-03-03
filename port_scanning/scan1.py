"""Port scanning for machine via importing to files(classes)"""

from scan import Scanner
from grappler import Grappler
def main():
    ip = input("Please enter IP to initiate port scan: ")
    scanner = Scanner(ip)
    scanner.scan(1, 10000)
    for port in scanner.open_ports:
        try:
            grappler = Grappler(ip,port)
            print(f"{port} ==> {grappler.read()}")
            grappler.close()
        except:
            print(f"{port} is not responding")



main()
