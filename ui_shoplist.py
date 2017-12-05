# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_shoplist.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(981, 678)
        Form.setStyleSheet("background:white;\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 20, 131, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 10, 81, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 30, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 140, 101, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shop_name_1 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_1.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"\n"
"\n"
"")
        self.shop_name_1.setText("")
        self.shop_name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_1.setObjectName("shop_name_1")
        self.verticalLayout_2.addWidget(self.shop_name_1)
        self.shop_name_2 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_2.setText("")
        self.shop_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_2.setObjectName("shop_name_2")
        self.verticalLayout_2.addWidget(self.shop_name_2)
        self.shop_name_3 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_3.setText("")
        self.shop_name_3.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_3.setObjectName("shop_name_3")
        self.verticalLayout_2.addWidget(self.shop_name_3)
        self.shop_name_5 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_5.setText("")
        self.shop_name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_5.setObjectName("shop_name_5")
        self.verticalLayout_2.addWidget(self.shop_name_5)
        self.shop_name_4 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_4.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"")
        self.shop_name_4.setText("")
        self.shop_name_4.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_4.setObjectName("shop_name_4")
        self.verticalLayout_2.addWidget(self.shop_name_4)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(310, 140, 91, 421))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.shop_id_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.shop_id_1.setStyleSheet("font: 14pt \"Heiti SC\";")
        self.shop_id_1.setText("")
        self.shop_id_1.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_id_1.setObjectName("shop_id_1")
        self.verticalLayout_3.addWidget(self.shop_id_1)
        self.shop_id_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.shop_id_2.setText("")
        self.shop_id_2.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_id_2.setObjectName("shop_id_2")
        self.verticalLayout_3.addWidget(self.shop_id_2)
        self.shop_id_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.shop_id_3.setText("")
        self.shop_id_3.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_id_3.setObjectName("shop_id_3")
        self.verticalLayout_3.addWidget(self.shop_id_3)
        self.shop_id_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.shop_id_4.setText("")
        self.shop_id_4.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_id_4.setObjectName("shop_id_4")
        self.verticalLayout_3.addWidget(self.shop_id_4)
        self.shop_id_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.shop_id_5.setText("")
        self.shop_id_5.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_id_5.setObjectName("shop_id_5")
        self.verticalLayout_3.addWidget(self.shop_id_5)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(420, 140, 101, 421))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.shop_owner_1 = QtWidgets.QLabel(self.layoutWidget2)
        self.shop_owner_1.setText("")
        self.shop_owner_1.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_1.setObjectName("shop_owner_1")
        self.verticalLayout_4.addWidget(self.shop_owner_1)
        self.shop_owner_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.shop_owner_2.setText("")
        self.shop_owner_2.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_2.setObjectName("shop_owner_2")
        self.verticalLayout_4.addWidget(self.shop_owner_2)
        self.shop_owner_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.shop_owner_3.setText("")
        self.shop_owner_3.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_3.setObjectName("shop_owner_3")
        self.verticalLayout_4.addWidget(self.shop_owner_3)
        self.shop_owner_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.shop_owner_4.setText("")
        self.shop_owner_4.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_4.setObjectName("shop_owner_4")
        self.verticalLayout_4.addWidget(self.shop_owner_4)
        self.shop_owner_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.shop_owner_5.setStyleSheet("font: 14pt \"Heiti SC\";")
        self.shop_owner_5.setText("")
        self.shop_owner_5.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_5.setObjectName("shop_owner_5")
        self.verticalLayout_4.addWidget(self.shop_owner_5)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(580, 140, 75, 421))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enter_shop_1 = QtWidgets.QPushButton(self.layoutWidget3)
        self.enter_shop_1.setStyleSheet("\n"
"QPushButton#enter_shop_1\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_shop_1:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_shop_1:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.enter_shop_1.setObjectName("enter_shop_1")
        self.verticalLayout.addWidget(self.enter_shop_1)
        self.enter_shop_2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.enter_shop_2.setStyleSheet("\n"
"QPushButton#enter_shop_2\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_shop_2:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_shop_2:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.enter_shop_2.setObjectName("enter_shop_2")
        self.verticalLayout.addWidget(self.enter_shop_2)
        self.enter_shop_3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.enter_shop_3.setStyleSheet("\n"
"QPushButton#enter_shop_3\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_shop_3:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_shop_3:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.enter_shop_3.setObjectName("enter_shop_3")
        self.verticalLayout.addWidget(self.enter_shop_3)
        self.enter_shop_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.enter_shop_4.setStyleSheet("\n"
"QPushButton#enter_shop_4\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_shop_4:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_shop_4:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.enter_shop_4.setObjectName("enter_shop_4")
        self.verticalLayout.addWidget(self.enter_shop_4)
        self.enter_shop_5 = QtWidgets.QPushButton(self.layoutWidget3)
        self.enter_shop_5.setStyleSheet("\n"
"QPushButton#enter_shop_5\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_shop_5:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_shop_5:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.enter_shop_5.setObjectName("enter_shop_5")
        self.verticalLayout.addWidget(self.enter_shop_5)
        self.layoutWidget4 = QtWidgets.QWidget(Form)
        self.layoutWidget4.setGeometry(QtCore.QRect(190, 100, 371, 31))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shop_name_head = QtWidgets.QLabel(self.layoutWidget4)
        self.shop_name_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_name_head.setObjectName("shop_name_head")
        self.horizontalLayout.addWidget(self.shop_name_head)
        self.shop_id_head = QtWidgets.QLabel(self.layoutWidget4)
        self.shop_id_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_id_head.setObjectName("shop_id_head")
        self.horizontalLayout.addWidget(self.shop_id_head)
        self.shop_owner_head = QtWidgets.QLabel(self.layoutWidget4)
        self.shop_owner_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_owner_head.setObjectName("shop_owner_head")
        self.horizontalLayout.addWidget(self.shop_owner_head)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "选个心仪的店铺逛逛吧"))
        self.label_2.setText(_translate("Form", "user name"))
        self.label_3.setText(_translate("Form", "欢迎语"))
        self.pushButton_9.setText(_translate("Form", "谁在逛我的店铺"))
        self.enter_shop_1.setText(_translate("Form", "→"))
        self.enter_shop_2.setText(_translate("Form", "→"))
        self.enter_shop_3.setText(_translate("Form", "→"))
        self.enter_shop_4.setText(_translate("Form", "→"))
        self.enter_shop_5.setText(_translate("Form", "→"))
        self.shop_name_head.setText(_translate("Form", "店铺名"))
        self.shop_id_head.setText(_translate("Form", "     ID"))
        self.shop_owner_head.setText(_translate("Form", "店  主"))

