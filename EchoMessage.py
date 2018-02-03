#!/usr/bin/python

import argparse
import sys

# Main accepts arguments 'argv'
def main(argv):

    # Create an argument parser to get info from the command line.
    parser = argparse.ArgumentParser(description = "Echo a message to the terminal.")
    parser.add_argument("--message", required=True, help="Message to echo.")

    args = parser.parse_args()
    message = args.message

    print message

# Entry point for the program.
if __name__ == "__main__":

    # Call main above and pass it an array of arguments from sys.argv
    # Give main all the args, but not the first one.  Skip, argv[0]
    main(sys.argv[1:])
