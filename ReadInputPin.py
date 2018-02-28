#!/usr/bin/python

import argparse
import sys
import RPi.GPIO as GPIO

# Main accepts arguments 'argv'
def main(argv):

    # Create an argument parser to get info from the command line.
    parser = argparse.ArgumentParser(description = "Reads a single GPIO pin.")
    parser.add_argument("--pin", required=True, help="Pin number to read.")
    
    args = parser.parse_args()
    pin = 0
    try :
        pin = int(args.pin)
    except ValueError :
        print "Arg must be an integer."
        return
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    
    state = GPIO.input(pin)
    print "Pin state[" + str(state) + "]"

# Entry point for the program.
if __name__ == "__main__":

    # Call main above and pass it an array of arguments from sys.argv
    # Give main all the args, but not the first one.  Skip, argv[0]
    main(sys.argv[1:])
