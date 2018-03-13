#!/usr/bin/python

import argparse
import sys
import RPi.GPIO as GPIO
import time

STATE_OPEN = True
STATE_CLOSED = not STATE_OPEN

def handleOpening(pinNumber) :
    print "OPEN " + str(pinNumber)

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
