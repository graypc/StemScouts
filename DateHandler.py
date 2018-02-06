#!/usr/bin/python

import argparse
import sys
import datetime

# Main accepts arguments 'argv'
def main(argv):

    # Create an argument parser to get info from the command line.
    parser = argparse.ArgumentParser(description = 
            "Prints the day of the week for a given date.")
    parser.add_argument("--y", required=True, help = "The year")
    parser.add_argument("--m", required=True, help = "The month")
    parser.add_argument("--d", required=True, help = "The day")

    args = parser.parse_args()

    year = 0
    month = 0
    day = 0
    try :
        year = int(args.y)
        month = int(args.m)
        day = int (args.d)

    except ValueError:
        "Bad values entered."
        parser.print_help()

    userDate = datetime.date(year, month, day)
    print "Date entered...\n" + userDate.strftime("%Y%h%d")

    dayOfWeek = userDate.weekday()

    if dayOfWeek == 0 :
        print "Sunday"

    elif dayOfWeek == 1 :
        print "Monday"

    elif dayOfWeek == 2 :
        print "Tuesday"

    elif dayOfWeek == 3 :
        print "Wednesday"

    elif dayOfWeek == 4 :
        print "Thursday"

    elif dayOfWeek == 5 :
        print "Friday"

    elif dayOfWeek == 6 :
        print "Saturday"

    today = datetime.date.today()
    delta = today - userDate
    print "Number of days elapsed: " + str(delta)

# Entry point for the program.
if __name__ == "__main__":

    # Call main above and pass it an array of arguments from sys.argv
    # Give main all the args, but not the first one.  Skip, argv[0]
    main(sys.argv[1:])
