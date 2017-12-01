# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(248, 294)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.loginbutton = QtWidgets.QPushButton(self.centralWidget)
        self.loginbutton.setGeometry(QtCore.QRect(100, 250, 51, 31))
        self.loginbutton.setStyleSheet("QPushButton#loginbutton\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#loginbutton:hover\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"QPushButton#loginbutton:pressed\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.loginbutton.setObjectName("loginbutton")
        self.logo_title = QtWidgets.QLabel(self.centralWidget)
        self.logo_title.setGeometry(QtCore.QRect(80, 10, 81, 41))
        self.logo_title.setObjectName("logo_title")
        self.head = QtWidgets.QLabel(self.centralWidget)
        self.head.setGeometry(QtCore.QRect(80, 50, 81, 71))
        self.head.setText("")
        self.head.setObjectName("head")
        self.pw_text = QtWidgets.QLineEdit(self.centralWidget)
        self.pw_text.setGeometry(QtCore.QRect(40, 180, 181, 31))
        self.pw_text.setMaxLength(16)
        self.pw_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_text.setObjectName("pw_text")
        self.id_text = QtWidgets.QLineEdit(self.centralWidget)
        self.id_text.setGeometry(QtCore.QRect(40, 140, 181, 31))
        self.id_text.setMaxLength(16)
        self.id_text.setObjectName("id_text")
        self.login_state_2 = QtWidgets.QLabel(self.centralWidget)
        self.login_state_2.setGeometry(QtCore.QRect(40, 220, 181, 20))
        self.login_state_2.setStyleSheet("text-align:center\n"
"")
        self.login_state_2.setText("")
        self.login_state_2.setObjectName("login_state_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginbutton.setText(_translate("MainWindow", "登陆"))
        self.logo_title.setText(_translate("MainWindow", "森普网上商城"))
        self.pw_text.setPlaceholderText(_translate("MainWindow", "密码"))
        self.id_text.setPlaceholderText(_translate("MainWindow", "账户名/手机号"))

