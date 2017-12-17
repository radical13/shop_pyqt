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
        MainWindow.resize(400, 500)
        MainWindow.setMaximumSize(QtCore.QSize(980, 16777215))
        MainWindow.setStyleSheet("background-color:white;")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.loginbutton = QtWidgets.QPushButton(self.centralWidget)
        self.loginbutton.setGeometry(QtCore.QRect(340, 230, 51, 51))
        self.loginbutton.setStyleSheet("\n"
"QPushButton#loginbutton\n"
"{\n"
"    font:48pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#loginbutton:hover\n"
"{\n"
"   font:48pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#loginbutton:pressed\n"
"{\n"
"   font:48pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.loginbutton.setObjectName("loginbutton")
        self.logo_title = QtWidgets.QLabel(self.centralWidget)
        self.logo_title.setGeometry(QtCore.QRect(90, 90, 220, 41))
        self.logo_title.setStyleSheet("font: 75 36pt \"Heiti SC\";")
        self.logo_title.setObjectName("logo_title")
        self.pw_text = QtWidgets.QLineEdit(self.centralWidget)
        self.pw_text.setGeometry(QtCore.QRect(75, 230, 250, 51))
        self.pw_text.setStyleSheet("background:transparent;border-width:0;border-style:outset;\n"
"font: 18pt \"Heiti SC\";\n"
"\n"
"")
        self.pw_text.setMaxLength(16)
        self.pw_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_text.setObjectName("pw_text")
        self.id_text = QtWidgets.QLineEdit(self.centralWidget)
        self.id_text.setGeometry(QtCore.QRect(75, 160, 250, 51))
        self.id_text.setStyleSheet("background:transparent;border-width:0;border-style:outset;\n"
"font: 18pt \"Heiti SC\";\n"
"QTreeView::foucus{border:1px solid white;}")
        self.id_text.setMaxLength(16)
        self.id_text.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.id_text.setObjectName("id_text")
        self.see_pw = QtWidgets.QPushButton(self.centralWidget)
        self.see_pw.setGeometry(QtCore.QRect(630, 360, 51, 51))
        self.see_pw.setStyleSheet("QPushButton#see_pw\n"
"{\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#see_pw:hover\n"
"{\n"
"  \n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#see_pw:pressed\n"
"{\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.see_pw.setText("")
        self.see_pw.setObjectName("see_pw")
        self.net_error = QtWidgets.QLabel(self.centralWidget)
        self.net_error.setGeometry(QtCore.QRect(30, 330, 350, 150))
        self.net_error.setText("")
        self.net_error.setObjectName("net_error")
        self.sline1 = QtWidgets.QLabel(self.centralWidget)
        self.sline1.setGeometry(QtCore.QRect(75, 285, 250, 1))
        self.sline1.setStyleSheet("background:black\n"
"")
        self.sline1.setText("")
        self.sline1.setObjectName("sline1")
        self.sline2 = QtWidgets.QLabel(self.centralWidget)
        self.sline2.setGeometry(QtCore.QRect(75, 206, 250, 1))
        self.sline2.setStyleSheet("background:black\n"
"")
        self.sline2.setText("")
        self.sline2.setObjectName("sline2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginbutton.setText(_translate("MainWindow", "→"))
        self.logo_title.setText(_translate("MainWindow", "森普网上商城"))
        self.pw_text.setPlaceholderText(_translate("MainWindow", "密码"))
        self.id_text.setPlaceholderText(_translate("MainWindow", "账户名/手机号"))

