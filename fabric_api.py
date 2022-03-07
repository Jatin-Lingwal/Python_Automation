"""Executing commands for a remote server, similar to ansible """

# When erver using fabric.api--> file name should be "fabfile.py" and there are some special variable which are used by fabric
# Need fabric and fabric3 modules

from fabric.api import *

env.hosts = ["192.168.1.100"]  # fixed var

env.user = 'root'  # fixed var


def create_():
    """"
            create file and folder
    """
    run('lsblk')
    run('df -Th')


def recreate():
    """
        update server
    :return:
    """
    run("yum update")


def both():
    create_()
    recreate()

# To initialize script "fab <fun>", if we call both then it it will execute both fuctions
# How to execute ---> fab <function_name>
# Executing the file from some another path <fab -f /<DIR>/fabfile.py create_>
