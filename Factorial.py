#!/usr/bin/python

def main():
    print "This program calculates 5!"

    # Want to calculate 5*4*3*2*1
    maxVal = 5

    # A variable to store the running total.
    total = 1

    # Create a 'range' to use in the for loop. The range function want to start at 0
    # and end at maxValue-1.  Force it it star at 1 and end at maxValue.
    values = range(1, maxVal + 1) 
    for v in values :

        # Update the total.
        total = total * v

        # Print a message.  Use 'str' to convert numerics to strings.
        print "Value[" + str(v) + "] Total[" + str(total) + "]"

    print "Final Value = " + str(total)

if __name__ == "__main__":
    main()
