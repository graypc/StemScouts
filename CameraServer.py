#!/usr/bin/python

import socket
import sys
import datetime
import cv2

NUM_WARM_UP_FRAMES = 10
IMAGE_DIR = "/var/www/html/images/"
PORT = 5055
CAMERA_PORT = 0

def main(argv):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORT))

    print "Socket open"

    while True:
        data, addr = sock.recvfrom(1024)

        # Received a request to take a picture.
        # Create the file name based on date-time.
        timestamp = datetime.datetime.now().strftime("%Y%b%d_%H:%M:%S.%f")
        camera = cv2.VideoCapture(CAMERA_PORT)

        # Let the camera adjust to the lighting.
        image = None
        for i in xrange(NUM_WARM_UP_FRAMES):
            retval, image = camera.read()

        fileName = IMAGE_DIR + timestamp + ".png"
        print "Saving image.  " + fileName
        cv2.imwrite(fileName, image)
        sock.sendto(fileName, addr)

# Entry point for the program.
if __name__ == "__main__":
    main(sys.argv[1:])
