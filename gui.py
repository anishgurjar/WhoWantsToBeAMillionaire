from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

import bg
from questions import *
import random
from playsound import playsound
import os 
import pyttsx3

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # launching the UI initiialization
        self.setupUi()

    def setupUi(self):
        ## setting properties for main window

        # set title
        self.setWindowTitle("Who Wants To Be A Millionaire")
        # set size
        self.resize(1384, 891)
        self.setMaximumSize(QtCore.QSize(1384, 891))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: rgb(0, 0, 109);")
        
        ## defining setting properties for central widget
        self.centralwidget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        
        ## defining layout of objects in central widget
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        ## defining a frame for questions and lifelines 
        self.frame_questions = QtWidgets.QFrame(self.centralwidget)
        self.frame_questions.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame_questions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_questions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_questions.setLineWidth(0)
        
        ## defining layout of objects in frame_questions
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_questions)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        
        ## adding a splitter object so that we can split lifeline and option frames
        self.splitter = QtWidgets.QSplitter(self.frame_questions)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(False)
        
        ## defining frame for lifelines
        self.frame_lifeline = QtWidgets.QFrame(self.splitter)
        self.frame_lifeline.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_lifeline.setStyleSheet("background-color: rgb(0, 0, 109);")
        self.frame_lifeline.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lifeline.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lifeline.setLineWidth(0)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_lifeline)
        self.verticalLayout_2.setContentsMargins(60, 0, 60, 0)
        self.verticalLayout_2.setSpacing(0)
        
        ## defining splitter between objects in lifeline frame
        self.splitter_2 = QtWidgets.QSplitter(self.frame_lifeline)
        self.splitter_2.setMinimumSize(QtCore.QSize(100, 100))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(400)
        self.splitter_2.setChildrenCollapsible(False)
        
        ## defining two btn for two lifelines 5050 and flip question
        self.btn_5050 = QtWidgets.QPushButton(self.splitter_2)
        self.btn_5050.setText("")
        self.btn_5050.setIcon(QtGui.QIcon("images/Classic5050.png"))
        self.btn_5050.setIconSize(QtCore.QSize(230, 250))
        self.btn_5050.setMaximumSize(QtCore.QSize(230, 250))
        
        self.btn_flip = QtWidgets.QPushButton(self.splitter_2)
        self.btn_flip.setText("")
        self.btn_flip.setIcon(QtGui.QIcon("images/flip1.png"))
        self.btn_flip.setIconSize(QtCore.QSize(230, 250))
        self.btn_flip.setMaximumSize(QtCore.QSize(230, 250))
        self.verticalLayout_2.addWidget(self.splitter_2)

        ## defining frame for options 
        self.frame_options = QtWidgets.QFrame(self.splitter)
        self.frame_options.setStyleSheet("QFrame#frame_options{border-image: url(:/back/bg.jpg);}border:0px;")
        self.frame_options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_options.setLineWidth(0)
        self.frame_options.setObjectName("frame_options")
        ## defining question label where question will be displayed 
        self.lbl_question = QtWidgets.QLabel(self.frame_options) 
        self.lbl_question.setGeometry(QtCore.QRect(110, 490, 781, 90))  # size (x, y, width, height)
        self.lbl_question.setAlignment(QtCore.Qt.AlignCenter) # centre aligned text
        self.lbl_question.setStyleSheet("color: rgb(255, 255, 255);border: 0px;font: 12pt \"MS Shell Dlg 2\";") # font 

        # font for all the options
        answer_stylesheet = "border: 0px;font: 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);"
        
        ## defining labels for all the 4 options 
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_options)
        self.pushButton_1.setGeometry(QtCore.QRect(128, 595, 341, 40)) 
        self.pushButton_1.setStyleSheet(answer_stylesheet)
   
        self.pushButton_2 = QtWidgets.QPushButton( self.frame_options)
        self.pushButton_2.setGeometry(QtCore.QRect(545, 595, 341, 40))
        self.pushButton_2.setStyleSheet(answer_stylesheet)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_options)
        self.pushButton_3.setGeometry(QtCore.QRect(128, 650, 341, 40))
        self.pushButton_3.setStyleSheet(answer_stylesheet)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_options)
        self.pushButton_4.setGeometry(QtCore.QRect(545, 650, 341, 40))
        self.pushButton_4.setStyleSheet(answer_stylesheet)
        
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout.addWidget(self.frame_questions)

        ## defining frame to hold the list of prizes 
        self.frame_cash = QtWidgets.QFrame(self.centralwidget)
        self.frame_cash.setStyleSheet("background-color: rgb(0, 0, 109);border:0px;")
        self.frame_cash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cash.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_cash)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        ## defining a list widget which will hold the prizes
        self.listView = QtWidgets.QListWidget(self.frame_cash)
        self.listView.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);") # font
        self.listView.setSpacing(28) # spacing between lines
        
        ## defining prizes in list
        cashes = ["7 crore", "3 Crore", "1 Crore", "50 Lakhs", "25 Lakhs", "10 Lakhs", "7 Lakh","1 Lakh", "Rs. 50,000","Rs. 10,000"]
        
        # creating a list item for each prize in cashes and adding them to list widget
        for prize in cashes:
            item = QtWidgets.QListWidgetItem(prize)
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.listView.addItem(item)
        
        ## making the list uneditable
        self.listView.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        
        ## initializing with the last entry. 
        self.curr_row = 9
        self.listView.setCurrentRow(self.curr_row)

        self.verticalLayout_3.addWidget(self.listView)
        self.horizontalLayout.addWidget(self.frame_cash)
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)


        ####### Functionalities ########

        # function when 50-50 lifeline is used
        def fifty_fifty():
            ## disabling the 50-50 lifeline
            self.btn_5050.setEnabled(False)

            ## if answer is either A or D, remove B and C and vice versa
            if self.pushButton_1.text() == self.answer or self.pushButton_4.text() == self.answer:    
                self.pushButton_2.setEnabled(False)
                self.pushButton_2.setText("")
                self.pushButton_3.setEnabled(False)
                self.pushButton_3.setText("")
            else:
                self.pushButton_1.setEnabled(False)
                self.pushButton_1.setText("")
                self.pushButton_4.setEnabled(False)
                self.pushButton_4.setText("")

        ## func when flip question lifeline is used
        def flip_question():
            # disable the flip lifeline button
            self.btn_flip.setEnabled(False)

            ## call launch function again, as it will choose a random question anytime its called
            self.flag= False
            self.launch()
            
        ## connecting functions to the clicked signal of the buttons
        self.btn_5050.clicked.connect(fifty_fifty)
        self.btn_flip.clicked.connect(flip_question)

        self.currentIndex = 0

    def launch(self):
        
        ## recoloring the options back to normal as this is a new round.
        answer_stylesheet = "border: 0px;font: 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);"
        self.pushButton_1.setStyleSheet(answer_stylesheet)
        self.pushButton_2.setStyleSheet(answer_stylesheet)
        self.pushButton_3.setStyleSheet(answer_stylesheet)
        self.pushButton_4.setStyleSheet(answer_stylesheet)

        # taking current index into i 
        i = self.currentIndex
        questionnumber = random.randint(0,9)

        self.question = questionlist[i][questionnumber]["question"]
        
        ## Adds the question to the GUI label
        self.lbl_question.setText(self.question)

        self.a = questionlist[i][questionnumber]["options"][0]
        self.b = questionlist[i][questionnumber]["options"][1]
        self.c = questionlist[i][questionnumber]["options"][2]
        self.d = questionlist[i][questionnumber]["options"][3]

        ## add options of the question to the GUI labels
        self.pushButton_1.setText(self.a)
        self.pushButton_2.setText(self.b)
        self.pushButton_3.setText(self.c)
        self.pushButton_4.setText(self.d)

        QtWidgets.QApplication.processEvents()
        self.speak()

        answerindex = questionlist[i][questionnumber]["answer"]
        self.answer = questionlist[i][questionnumber]["options"][answerindex]

        self.flag=True        
    
    def process(self):
        self.flag =False
        if(self.choice == "correct"):

            signal = "correct"
            engine.say("Congrats on winning")

            #moving a row up in listwidget
            self.curr_row -= 1
            # moving to the next level
            self.currentIndex += 1
            # highlighting the new row in list widget
            self.listView.setCurrentRow(self.curr_row)
            # calling launch again with the updated values
            self.launch()      
        else:
            signal = "loss"
            engine.say("Better Luck Next Time")
            # getting the current prize from the list widget
            prize_won = self.listView.currentItem().text()

            ## showing a pop up window with the prize won 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(f"Your final amount is {prize_won} !!")
            msg.setWindowTitle("Congratulations!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            ret = msg.exec_()
            # on closing the pop up window the program exits
            if ret:
                sys.exit()    
        engine.runAndWait()

    def speak(self):
        # speak the questions and options
        engine.say(self.question)
        engine.say(self.a)
        engine.say(self.b)
        engine.say(self.c)
        engine.say(self.d)
        engine.runAndWait()

    def keyPressEvent(self, event):
        if self.flag == True:
            
            if event.key() == QtCore.Qt.Key_A:
                # changing background to yellow
                self.pushButton_1.setStyleSheet(base_stylesheet+add_yellow)
                QtWidgets.QApplication.processEvents()
                playsound("optionlock.mp3")

                if(self.answer == self.a):
                    # changing background to green
                    self.pushButton_1.setStyleSheet(base_stylesheet+add_green)
                    QtWidgets.QApplication.processEvents()
                    engine.say("Correct Answer!")
                    engine.say("Moving onto the next question")
                    status = "correct"
                    playsound("kbcright.mp3")
                    self.choice = status 
                else:
                    # changing background to red
                    self.pushButton_1.setStyleSheet(base_stylesheet+add_red)
                    QtWidgets.QApplication.processEvents()
                    engine.say("Incorrect!")
                    status = "incorrect"
                    self.choice = status

            if event.key() == QtCore.Qt.Key_B:

                self.pushButton_2.setStyleSheet(base_stylesheet+add_yellow)
                QtWidgets.QApplication.processEvents()
                
                playsound("optionlock.mp3")
                if(self.answer == self.b):
                    self.pushButton_2.setStyleSheet(base_stylesheet+add_green)
                    QtWidgets.QApplication.processEvents()
                    
                    engine.say("Correct Answer!")
                    engine.say("Moving onto the next question")
                    status = "correct"
                    playsound("kbcright.mp3")
                    self.choice = status 
                else:
                    self.pushButton_2.setStyleSheet(base_stylesheet+add_red)
                    QtWidgets.QApplication.processEvents()
                    
                    engine.say("Incorrect!")
                    status = "incorrect"
                    self.choice = status
            
            if event.key() == QtCore.Qt.Key_C:
                self.pushButton_3.setStyleSheet(base_stylesheet+add_yellow)
                QtWidgets.QApplication.processEvents()
                playsound("optionlock.mp3")
                if(self.answer == self.c):
                    self.pushButton_3.setStyleSheet(base_stylesheet+add_green)
                    QtWidgets.QApplication.processEvents()
                    
                    engine.say("Correct Answer!")
                    engine.say("Moving onto the next question")
                    status = "correct"
                    playsound("kbcright.mp3")
                    self.choice = status 
                else:
                    self.pushButton_3.setStyleSheet(base_stylesheet+add_red)
                    QtWidgets.QApplication.processEvents()
                    engine.say("Incorrect!")
                    status = "incorrect"
                    self.choice = status
            
            if event.key() == QtCore.Qt.Key_D:
                self.pushButton_4.setStyleSheet(base_stylesheet+add_yellow)
                QtWidgets.QApplication.processEvents()
                playsound("optionlock.mp3")
                if(self.answer == self.d):
                    self.pushButton_4.setStyleSheet(base_stylesheet+add_green)
                    QtWidgets.QApplication.processEvents()
                
                    engine.say("Correct Answer!")
                    engine.say("Moving onto the next question")
                    status = "correct"
                    playsound("kbcright.mp3")
                    self.choice = status 
                else:
                    self.pushButton_4.setStyleSheet(base_stylesheet+add_red)
                    QtWidgets.QApplication.processEvents()
                    engine.say("Incorrect!")
                    status = "incorrect"
                    self.choice = status
            engine.runAndWait()
            self.process()

if __name__ == "__main__":
    import sys
    # initializing text to speech engine 
    engine = pyttsx3.init()

    # storing different color background for correct/incorrect answers
    base_stylesheet = "border: 0px;font: 12pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);"
    add_yellow = "background-color: rgb(218, 218, 0);" # yellow
    add_green = "background-color: rgb(68, 206, 0);" #green
    add_red = "background-color: rgb(184, 0, 0);" #red
    
    # loading the app
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    ui.launch()
    sys.exit(app.exec_())
