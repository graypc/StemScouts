#!/usr/bin/python

import sys
import argparse
import getpass
import Mailer

def printHelp():
    print 'SendTestMessage.py -s <true | false>'

def main(argv):
    parser = argparse.ArgumentParser(description = "Send a SMTP text message.")

    parser.add_argument("--recipient", required=True, help = "Recipient's phone number.")
    parser.add_argument("--provider", required=True, help = "Recipient's service provider.",
            choices=["att", "boost", "cricket", "sprint", "tmobile", "verizon"])

    args = parser.parse_args()
    recipient = args.recipient
    provider = args.provider

    if (recipient is None or provider is None):
        print "ERROR.  Incorrect arguments."
        parser.print_help()
        return

    # https://www.lifewire.com/sms-gateway-from-email-to-sms-text-message-2495456
    providers = {
            "att"       : "@txt.att.net",
            "boost"     : "@myboostmobile.com",
            "cricket"   : "@txt.att.net",
            "sprint"    : "@messaging.sprintpcs.com",
            "tmobile"   : "@tmomail.net",
            "verizon"   : "@vtext.com"}

    recipient = recipient + providers[provider]
    print "Sending message To[" + recipient + "]"

    msg = raw_input("Enter message\n-->")
    print msg
    print "Enter password for eca.stemscouts@gmail.com"
    password = getpass.getpass()

    result = Mailer.sendMail("From python", msg, password, recipient)
    print result

if __name__ == "__main__":
   main(sys.argv[1:])
