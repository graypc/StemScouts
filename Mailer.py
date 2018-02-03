#!/usr/bin/python

import smtplib

def sendMail(subject, msg, password, recipient):

	username = "eca.stemscouts@gmail.com"
	message = 'Subject: %s\n\n%s' % (subject, msg)
	result = ""

	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(username, password)
		server.sendmail(username, recipient, message)

	except Exception, e:
		result = str(e)

	server.quit()
	return result
