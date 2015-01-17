# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Sends an email with an attachment
def SendMail(attachment, receiver):
    # Create a text/plain message
    msg = MIMEMultipart()

    msg['Subject'] = 'Taskoop automatic message: your tasks'
    msg['From'] = 'donotreply@taskoop.com'
    msg['To'] = receiver
    msg['Body'] = 'Test \n\n Kind regards, \n Taskoop'

    fileBuffer = open(attachment, encoding="utf-8", mode='r')
    att = MIMEText(fileBuffer.read())
    fileBuffer.close()
    msg.attach(att)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    # seems to work after issuing:
    #     python -m smtpd -n -c DebuggingServer localhost:1025
    s = smtplib.SMTP('localhost', port=1025)
    #s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()