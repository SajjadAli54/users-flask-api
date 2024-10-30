# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(33, 33, 33);\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    background-color: rgb(46, 46, 46);    \n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(46, 46, 46);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(120, 120, 120);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditRec = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRec.setObjectName("lineEditRec")
        self.gridLayout.addWidget(self.lineEditRec, 0, 1, 1, 1)
        self.textEditEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEmail.setObjectName("textEditEmail")
        self.gridLayout.addWidget(self.textEditEmail, 2, 1, 1, 1)
        self.pushButtonSend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.gridLayout.addWidget(self.pushButtonSend, 3, 1, 1, 1)
        self.labelRecipient = QtWidgets.QLabel(self.centralwidget)
        self.labelRecipient.setObjectName("labelRecipient")
        self.gridLayout.addWidget(self.labelRecipient, 0, 0, 1, 1)
        self.labelEmail = QtWidgets.QLabel(self.centralwidget)
        self.labelEmail.setObjectName("labelEmail")
        self.gridLayout.addWidget(self.labelEmail, 2, 0, 1, 1)
        self.labelSub = QtWidgets.QLabel(self.centralwidget)
        self.labelSub.setObjectName("labelSub")
        self.gridLayout.addWidget(self.labelSub, 1, 0, 1, 1)
        self.lineEditSub = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSub.setObjectName("lineEditSub")
        self.gridLayout.addWidget(self.lineEditSub, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSend.setText(_translate("MainWindow", "Send"))
        self.labelRecipient.setText(_translate("MainWindow", "Receipient"))
        self.labelEmail.setText(_translate("MainWindow", "Email"))
        self.labelSub.setText(_translate("MainWindow", "Subject"))