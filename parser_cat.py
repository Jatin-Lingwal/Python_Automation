#!/usr/bin/env python3.6
""" This script is all about how argparse module helps us to write a user friendly scripts where user is able to use command line argument"""
import argparse
import sys
vector = argparse.ArgumentParser(description="Read the file output", prog="FILE-READER")
vector.add_argument("filename", help="the name of the file to read")
vector.add_argument("--limit", "-l", type=int, help="the number of lines to read just with tail command" )
read = vector.parse_args()

try:
    g = open(read.filename)
    limit = read.limit
except FileNotFoundError:
    print("Error! file not found.")
else:
    with g:
        lines = g.readlines()
        if limit:
            lines = lines[0:limit]

        for l in lines:
            print(l.strip())

#As this scripts is just to imitate "cat" command in linux. make sure to give +x and copy it in /usr/bin dir to use it regardless of pwd and make sure to use -h flag!

