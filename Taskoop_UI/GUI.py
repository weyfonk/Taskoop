from tkinter import *
from tkinter.ttk import *
from PyQt4 import QtGui, QtCore
from Taskoop_Bll import Schedule
    
class GUI(QtGui.QMainWindow):
    
    def __init__(self, master=None):
        
        app = QtGui.QApplication(sys.argv)
        super(GUI, self).__init__()
        
        self.schedule = Schedule.Schedule()
        
        # Main window definition
        self.resize(450, 250)
        #self.move(300, 300)
        
        #Center window on screen
        windowFrame = self.frameGeometry()
        screenCenter = QtGui.QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(screenCenter)
        self.move(windowFrame.topLeft())
        
        self.setWindowTitle('Taskoop')
        
        
        # HTML generation button
        btnHtml = QtGui.QPushButton('Generate HTML', self)
        btnHtml.resize(btnHtml.sizeHint())
        btnHtml.move(150, 200)
        btnHtml.setEnabled(False)
        btnHtml.clicked.connect(self.schedule.GenerateHTML)
        
        # Quit button
        btnQuit = QtGui.QPushButton('Quit', self)
        btnQuit.setToolTip('Quit the application')
        btnQuit.resize(btnQuit.sizeHint())
        btnQuit.move(350, 200)
        btnQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        self.show()
        
        sys.exit(app.exec_())
#         Frame.__init__(self, 
#                        master, 
#                        width = 500, 
#                        height = 800)
#         self.pack(fill = BOTH)
#         
#         # label
#         self.testLabel = Label(self, text = "Taskoop Window hell yeah!")
#         self.testLabel.pack()
#         
#         # generate HTML button
#         self.btnHTML = Button(self, 
#                               text = "Generate HTML",
#                               command = self.schedule.GenerateHTML,
#                               state = DISABLED)
#         self.btnHTML.pack()
#         
#         # quit button
#         self.btnQuit = Button(self, text = "Quit", command = self.quit)
#         self.btnQuit.pack()
#         
#         # orientation
#         self.cbxArePeopleInHeader = Checkbutton(self, 
#                                            text = "Display people names in header", 
#                                            variable = self.schedule.arePeopleInHeader,
#                                            command = self.SetOrientation)
#         #TODO bind to object
#         
#         # Nb people
#         self.lblNbPeople = Label(self, text="Number of people: ")
#         self.lblNbPeople.pack()
#         
#         self.sbNbPeople = Spinbox(self, 
#                              from_ = 2, 
#                              to = 10, 
#                              increment = 1, 
#                              textvariable = self.schedule.peopleNb,
#                              command = self.UpdatePeopleNb,
#                              width = 5)
#         self.sbNbPeople.pack()
#         
#         self.cbxArePeopleInHeader.pack()
#         
#         # launch loop that will be stopped when the window is closed
#         self.master.title("Taskoop")
#         self.mainloop()
#         #self.destroy()
#         
        
    def UpdatePeopleNb(self):
        self.schedule.peopleNb = self.sbNbPeople.get()
        self.btnHTML["state"] = "normal" if self.ValidateInput() else "disabled"
        print("Value: {0}".format(self.schedule.peopleNb))
        
    
    def SetOrientation(self):
        self.schedule.arePeopleInHeader = not self.schedule.arePeopleInHeader
        
    def ValidateInput(self):
        # TODO return true if all conditions are met for HTML to be generated
        return True
    
    #events
    
    # Overriden
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 
                                           'Taskoop', 
                                           'Do you really want to quit Taskoop ?', 
                                           buttons= QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, 
                                           defaultButton=QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()