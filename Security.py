#!/usr/bin/python

import argparse
import sys
import RPi.GPIO as GPIO
import time
import socket
import urllib
import Emailer

STATE_OPEN = True
STATE_CLOSED = not STATE_OPEN

cameraIP = ""
email = ""

def getFileName(path):
    # Path is "/images/DateTime.png"
    return path.split("/")[2]

def handleOpening(pinNumber) :
    print "OPEN " + str(pinNumber)

    # Request the camera server to take a picture
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto("Take picture", (cameraIP, 5055))

    # Wait for the camera server to reply
    reply, addr = sock.recvfrom(1024);
    print reply

    if reply == "False alarm":
        return

    # Reply from camera is the name of a file.  Use urllib to fetch it.
    # Get image and save locally
    url = "http://" + cameraIP + reply
    fileName = getFileName(reply)
    f = open(fileName, "wb")
    f.write(urllib.urlopen(url).read())
    f.close()

    # Email the image
    print Emailer.sendMail(
            "Intruder alert at " + str(pinNumber),
            email,
            fileName)

def handleClosing(pinNumber) :
    print "CLOSE " + str(pinNumber)

def updatePinState(pinNumber, oldPinState) :
    #Check if Pin is currently open.
    if (GPIO.input(pinNumber) == STATE_OPEN):
        # Pin is currently open.
        # Check if Pin was previously in closed state
        if (oldPinState == STATE_CLOSED):
            # Pin just transitioned from closed to open.
            handleOpening(pinNumber)

        return STATE_OPEN

    #Pin is currently closed.
    #Check if Pin was previously in open state
    if (oldPinState == STATE_OPEN):
        # Pin just transitioned from closed to open.
        handleClosing(pinNumber)

    return STATE_CLOSED

# Main accepts arguments 'argv'
def main(argv):

    parser = argparse.ArgumentParser(description =
            "Security system")
    parser.add_argument("--cameraIP", required=True, help="IP of camera server.")
    parser.add_argument("--email", required=True, help="Email for notifications.")
    args = parser.parse_args()
    global cameraIP
    global email 
    cameraIP = args.cameraIP
    email = args.email

    print "Connecting to camera server " + cameraIP

    pinA = 5
    pinB = 6
    
    # Set up the pins to read from GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinA, GPIO.IN)
    GPIO.setup(pinB, GPIO.IN)
    
    # Assume both pins are closed to begin
    stateA = STATE_CLOSED 
    stateB = STATE_CLOSED

    # Run forever
    while True:
        stateA = updatePinState(pinA, stateA)
        stateB = updatePinState(pinB, stateB)
        time.sleep(2)

# Entry point for the program.
if __name__ == "__main__":

    # Call main above and pass it an array of arguments from sys.argv
    # Give main all the args, but not the first one.  Skip, argv[0]
    main(sys.argv[1:])
