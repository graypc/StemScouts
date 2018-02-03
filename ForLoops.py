#!/usr/bin/python

def main():
    print "This program adds the numbers 1 through 5 and displays the output."

    # Create an array of values [1, 2, 3, 4, 5].
    # Store them in the variable 'values'
    values = [1, 2, 3, 4, 5]

    # A variable to store the running total.
    total = 0

    # For each values in the array.
    for v in values :

        # Update the total.
        total = total + v

        # Print a message.  Use 'str' to convert numerics to strings.
        print "Value[" + str(v) + "] Total[" + str(total) + "]"

    print "Final Value = " + str(total)

if __name__ == "__main__":
    main()
