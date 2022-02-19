""" Argparser """
import argparse

vector = argparse.ArgumentParser(description="Read the file output")
vector.add_argument("filename", help="the name of the file to read")
vector.add_argument("--limit", "-l", type=int, help="the number of lines to read just with tail command" )
example = vector.parse_args()

                                  