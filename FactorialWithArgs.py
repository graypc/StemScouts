#!/usr/bin/python

import argparse
import sys

def calculateFactorial(val):
    total = 1
    for v in range(1, val + 1):
        total = total * v

    return total

# Main accepts arguments 'argv'
def main(argv):

    # Create an argument parser to get info from the command line.
    parser = argparse.ArgumentParser(description = 
    "Calculate the factorial of a number.")
    parser.add_argument("--value", required=True, help = "An integer for calculate.")

    args = parser.parse_args()
    userInput = args.value

    # Make sure the user supplied an integer
    val = 0
    try :
        val = int(userInput)

    except ValueError:
        # User supplied a non-integer value so exit.
        print "Only integer arguments allowed."
        parser.print_help()
        return

    print str(val) + "! = " + str(calculateFactorial(val))

# Entry point for the program.
if __name__ == "__main__":

    # Call main above and pass it an array of arguments from sys.argv
    # Give main all the args, but not the first one.  Skip, argv[0]
    main(sys.argv[1:])
