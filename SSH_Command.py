
# Need to install paramiko module and imported specific function from it.
from paramiko import SSHClient
# AutoAddPolicy helps us to add a machine in our known host(if we are connecting with a machine for the first time.)
from paramiko import AutoAddPolicy
# To hide password entered by the user
import getpass
from paramiko import ssh_exception

Host_name = input("Enter machine's IP to which you wanna connect to: ")
User_name = input("Enter username: ")
Password = getpass.getpass("Enter your password: ")
Command = input("Enter any command to execute: ")
def Connection():
    with SSHClient() as slave:
# Set policy to use when connecting to servers without a known host key or as first time access.
        slave.set_missing_host_key_policy(AutoAddPolicy)
# If  your using key base authentication key_file=</root/.ssh/id_rsa>
        slave.connect(hostname=Host_name, username=User_name, password=Password)
# While using paramiko the output comes in tuple format, it contains 3 values(input,output & error)
        stdin, stdout, stderr = slave.exec_command(Command)
        output = stdout.read()
        print(output.decode())# decode function return a string decoded from the given bytes

Connection()
