#!/usr/bin/python

import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

from email import encoders

def sendMail(subject, toAddr, fileName):

    fromAddr = "eca.stemscouts@gmail.com"

    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg.attach(MIMEImage(file(fileName).read()))

    result = ""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromAddr, "stemscouts")
    server.sendmail(fromAddr, toAddr, msg.as_string())
    server.quit()

    return result
