# -*- coding: utf-8 -*-
import string
import os.path
from Taskoop_Bll import StringUtils, MailUtils
from Taskoop_UI import ConsoleUI, GUI
import sys
from PyQt4 import QtGui


# Main method, to be coded :þ
def main(argv):
    if len(argv) >= 1 and argv[0].upper() == '-X':
        GUI.GUI()
    else:
        ConsoleUI.Start()    
    

def doStuff():
        
    # Generate the HTML code
    loopCount = 3  # how many times each participant has to perform each task
    htmlFile = GenerateHTML(tasks, people, loopCount, arePeopleShownInHeader,
        startingPoint, frequency)

    # Decide whether to send the generated table by email
    #userInput = string.whitespace
    #while not StringUtils.IsYesNoInputValid(userInput):
        #userInput = input("Send the generated table by email ? [Y/N]")
    #if userInput.upper() == StringUtils.YES_KEY:
        #SendMail(htmlFile)

    print("OK")


# Send a file by email
def SendMail(fileToSend):
    userInput = string.whitespace
    while not StringUtils.IsEmailInputValid(userInput):
        userInput = input("Please type a valid email address: ")
    #TODO enable the generated table to be sent by mail
    MailUtils.SendMail(fileToSend, userInput)
    print('OK')

main(sys.argv[1:])