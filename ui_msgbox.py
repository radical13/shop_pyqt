# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_msgbox.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_msgbox(object):
    def setupUi(self, msgbox):
        msgbox.setObjectName("msgbox")
        msgbox.resize(982, 678)
        msgbox.setStyleSheet("background:white;\n"
"")
        self.page = QtWidgets.QLabel(msgbox)
        self.page.setGeometry(QtCore.QRect(570, 590, 61, 40))
        self.page.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page.setText("")
        self.page.setAlignment(QtCore.Qt.AlignCenter)
        self.page.setObjectName("page")
        self.page_2 = QtWidgets.QLabel(msgbox)
        self.page_2.setGeometry(QtCore.QRect(420, 590, 121, 40))
        self.page_2.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page_2.setAlignment(QtCore.Qt.AlignCenter)
        self.page_2.setObjectName("page_2")
        self.page3 = QtWidgets.QLabel(msgbox)
        self.page3.setGeometry(QtCore.QRect(300, 590, 41, 40))
        self.page3.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page3.setAlignment(QtCore.Qt.AlignCenter)
        self.page3.setObjectName("page3")
        self.page_5 = QtWidgets.QLabel(msgbox)
        self.page_5.setGeometry(QtCore.QRect(650, 590, 51, 40))
        self.page_5.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page_5.setAlignment(QtCore.Qt.AlignCenter)
        self.page_5.setObjectName("page_5")
        self.last_page = QtWidgets.QPushButton(msgbox)
        self.last_page.setGeometry(QtCore.QRect(200, 590, 75, 40))
        self.last_page.setStyleSheet("\n"
"QPushButton#last_page\n"
"{\n"
"    font:24pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#last_page:hover\n"
"{\n"
"   font:24pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#last_page:pressed\n"
"{\n"
"   font:24pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.last_page.setObjectName("last_page")
        self.next_page = QtWidgets.QPushButton(msgbox)
        self.next_page.setGeometry(QtCore.QRect(720, 590, 75, 40))
        self.next_page.setStyleSheet("\n"
"QPushButton#next_page\n"
"{\n"
"    font:24pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#next_page:hover\n"
"{\n"
"   font:24pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#next_page:pressed\n"
"{\n"
"   font:24pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.next_page.setObjectName("next_page")
        self.msg_num = QtWidgets.QLabel(msgbox)
        self.msg_num.setGeometry(QtCore.QRect(360, 590, 61, 40))
        self.msg_num.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.msg_num.setText("")
        self.msg_num.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_num.setObjectName("msg_num")
        self.time_head = QtWidgets.QLabel(msgbox)
        self.time_head.setGeometry(QtCore.QRect(260, 50, 200, 20))
        self.time_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.time_head.setAlignment(QtCore.Qt.AlignCenter)
        self.time_head.setObjectName("time_head")
        self.send_head = QtWidgets.QLabel(msgbox)
        self.send_head.setGeometry(QtCore.QRect(90, 50, 130, 20))
        self.send_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.send_head.setAlignment(QtCore.Qt.AlignCenter)
        self.send_head.setObjectName("send_head")
        self.shop_owner_head = QtWidgets.QLabel(msgbox)
        self.shop_owner_head.setGeometry(QtCore.QRect(500, 50, 450, 20))
        self.shop_owner_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_owner_head.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_head.setObjectName("shop_owner_head")
        self.send_1 = QtWidgets.QLabel(msgbox)
        self.send_1.setGeometry(QtCore.QRect(90, 90, 130, 51))
        self.send_1.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.send_1.setText("")
        self.send_1.setAlignment(QtCore.Qt.AlignCenter)
        self.send_1.setObjectName("send_1")
        self.time_1 = QtWidgets.QLabel(msgbox)
        self.time_1.setGeometry(QtCore.QRect(260, 90, 200, 51))
        self.time_1.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.time_1.setText("")
        self.time_1.setAlignment(QtCore.Qt.AlignCenter)
        self.time_1.setObjectName("time_1")
        self.content_1 = QtWidgets.QLabel(msgbox)
        self.content_1.setGeometry(QtCore.QRect(500, 90, 450, 51))
        self.content_1.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.content_1.setText("")
        self.content_1.setAlignment(QtCore.Qt.AlignCenter)
        self.content_1.setWordWrap(True)
        self.content_1.setObjectName("content_1")
        self.time_2 = QtWidgets.QLabel(msgbox)
        self.time_2.setGeometry(QtCore.QRect(260, 200, 200, 51))
        self.time_2.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.time_2.setText("")
        self.time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_2.setObjectName("time_2")
        self.content_2 = QtWidgets.QLabel(msgbox)
        self.content_2.setGeometry(QtCore.QRect(500, 200, 450, 51))
        self.content_2.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.content_2.setText("")
        self.content_2.setAlignment(QtCore.Qt.AlignCenter)
        self.content_2.setWordWrap(True)
        self.content_2.setObjectName("content_2")
        self.send_2 = QtWidgets.QLabel(msgbox)
        self.send_2.setGeometry(QtCore.QRect(90, 200, 130, 51))
        self.send_2.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.send_2.setText("")
        self.send_2.setAlignment(QtCore.Qt.AlignCenter)
        self.send_2.setObjectName("send_2")
        self.time_3 = QtWidgets.QLabel(msgbox)
        self.time_3.setGeometry(QtCore.QRect(260, 310, 200, 51))
        self.time_3.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.time_3.setText("")
        self.time_3.setAlignment(QtCore.Qt.AlignCenter)
        self.time_3.setObjectName("time_3")
        self.content_3 = QtWidgets.QLabel(msgbox)
        self.content_3.setGeometry(QtCore.QRect(500, 310, 450, 51))
        self.content_3.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.content_3.setText("")
        self.content_3.setAlignment(QtCore.Qt.AlignCenter)
        self.content_3.setWordWrap(True)
        self.content_3.setObjectName("content_3")
        self.send_3 = QtWidgets.QLabel(msgbox)
        self.send_3.setGeometry(QtCore.QRect(90, 310, 130, 51))
        self.send_3.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.send_3.setText("")
        self.send_3.setAlignment(QtCore.Qt.AlignCenter)
        self.send_3.setObjectName("send_3")
        self.content_5 = QtWidgets.QLabel(msgbox)
        self.content_5.setGeometry(QtCore.QRect(510, 510, 450, 51))
        self.content_5.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.content_5.setText("")
        self.content_5.setAlignment(QtCore.Qt.AlignCenter)
        self.content_5.setWordWrap(True)
        self.content_5.setObjectName("content_5")
        self.time_5 = QtWidgets.QLabel(msgbox)
        self.time_5.setGeometry(QtCore.QRect(270, 510, 200, 51))
        self.time_5.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.time_5.setText("")
        self.time_5.setAlignment(QtCore.Qt.AlignCenter)
        self.time_5.setObjectName("time_5")
        self.send_5 = QtWidgets.QLabel(msgbox)
        self.send_5.setGeometry(QtCore.QRect(90, 510, 130, 51))
        self.send_5.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.send_5.setText("")
        self.send_5.setAlignment(QtCore.Qt.AlignCenter)
        self.send_5.setObjectName("send_5")
        self.content_4 = QtWidgets.QLabel(msgbox)
        self.content_4.setGeometry(QtCore.QRect(500, 420, 450, 51))
        self.content_4.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.content_4.setText("")
        self.content_4.setAlignment(QtCore.Qt.AlignCenter)
        self.content_4.setWordWrap(True)
        self.content_4.setObjectName("content_4")
        self.time_4 = QtWidgets.QLabel(msgbox)
        self.time_4.setGeometry(QtCore.QRect(260, 420, 200, 51))
        self.time_4.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.time_4.setText("")
        self.time_4.setAlignment(QtCore.Qt.AlignCenter)
        self.time_4.setObjectName("time_4")
        self.send_4 = QtWidgets.QLabel(msgbox)
        self.send_4.setGeometry(QtCore.QRect(90, 420, 130, 51))
        self.send_4.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.send_4.setText("")
        self.send_4.setAlignment(QtCore.Qt.AlignCenter)
        self.send_4.setObjectName("send_4")

        self.retranslateUi(msgbox)
        QtCore.QMetaObject.connectSlotsByName(msgbox)

    def retranslateUi(self, msgbox):
        _translate = QtCore.QCoreApplication.translate
        msgbox.setWindowTitle(_translate("msgbox", "消息信箱"))
        self.page_2.setText(_translate("msgbox", "条消息 当前是第"))
        self.page3.setText(_translate("msgbox", "共"))
        self.page_5.setText(_translate("msgbox", "页"))
        self.last_page.setText(_translate("msgbox", "←"))
        self.next_page.setText(_translate("msgbox", "→"))
        self.time_head.setText(_translate("msgbox", "时间"))
        self.send_head.setText(_translate("msgbox", "发送人"))
        self.shop_owner_head.setText(_translate("msgbox", "内容"))

