#!/usr/bin/python

import socket
import argparse
import sys

PORT = 5055

def main(argv):
    parser = argparse.ArgumentParser(description = 
            "Requests a camera server take a picture")
    parser.add_argument("--ip", required=True, help = "The camera server ip")
    args = parser.parse_args()
    
    print "Connecting to " + args.ip

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto("Take picture", (args.ip, PORT))

    data, addr = sock.recvfrom(1024)
    print "Image name [" + str(data) + "]"

# Entry point for the program.
if __name__ == "__main__":
    main(sys.argv[1:])
