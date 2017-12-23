# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_inputwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_input(object):
    def setupUi(self, input):
        input.setObjectName("input")
        input.resize(280, 325)
        input.setStyleSheet("background:white")
        self.label_2 = QtWidgets.QLabel(input)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 60, 30))
        self.label_2.setStyleSheet("font: 75 14pt \"Heiti SC\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.id = QtWidgets.QLineEdit(input)
        self.id.setGeometry(QtCore.QRect(130, 80, 113, 30))
        self.id.setObjectName("id")
        self.price = QtWidgets.QLineEdit(input)
        self.price.setGeometry(QtCore.QRect(130, 180, 113, 30))
        self.price.setObjectName("price")
        self.label = QtWidgets.QLabel(input)
        self.label.setGeometry(QtCore.QRect(30, 80, 60, 30))
        self.label.setStyleSheet("font: 75 14pt \"Heiti SC\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(input)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 60, 30))
        self.label_3.setStyleSheet("font: 75 14pt \"Heiti SC\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(input)
        self.name.setGeometry(QtCore.QRect(130, 130, 113, 30))
        self.name.setObjectName("name")
        self.submit = QtWidgets.QPushButton(input)
        self.submit.setGeometry(QtCore.QRect(80, 250, 113, 32))
        self.submit.setObjectName("submit")

        self.retranslateUi(input)
        QtCore.QMetaObject.connectSlotsByName(input)

    def retranslateUi(self, input):
        _translate = QtCore.QCoreApplication.translate
        input.setWindowTitle(_translate("input", "Form"))
        self.label_2.setText(_translate("input", "商品单价"))
        self.label.setText(_translate("input", "商品ID"))
        self.label_3.setText(_translate("input", "商品名称"))
        self.submit.setText(_translate("input", "提交"))

