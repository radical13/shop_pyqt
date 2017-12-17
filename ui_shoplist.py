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
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(710, 20, 100, 21))
        self.username.setText("")
        self.username.setObjectName("username")
        self.shopcar = QtWidgets.QPushButton(Form)
        self.shopcar.setGeometry(QtCore.QRect(0, 130, 192, 32))
        self.shopcar.setStyleSheet("\n"
"QPushButton#shopcar\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#shopcar:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#shopcar:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.shopcar.setObjectName("shopcar")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 160, 131, 421))
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
        self.layoutWidget1.setGeometry(QtCore.QRect(390, 160, 121, 421))
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
        self.layoutWidget2.setGeometry(QtCore.QRect(550, 160, 101, 421))
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
        self.layoutWidget3.setGeometry(QtCore.QRect(680, 160, 75, 421))
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
        self.layoutWidget4.setGeometry(QtCore.QRect(260, 120, 451, 31))
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
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(820, 20, 30, 21))
        self.exit.setStyleSheet("\n"
"QPushButton#exit\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#exit:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#exit:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 192, 681))
        self.label_4.setStyleSheet("background:rgb(244, 244, 244)")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.head = QtWidgets.QLabel(Form)
        self.head.setGeometry(QtCore.QRect(925, 10, 40, 40))
        self.head.setText("")
        self.head.setObjectName("head")
        self.good_sinfo = QtWidgets.QLabel(Form)
        self.good_sinfo.setGeometry(QtCore.QRect(10, 100, 60, 16))
        self.good_sinfo.setStyleSheet("background:rgb(242, 242, 243);\n"
"font: 15pt, \"Heiti SC\" ;\n"
"color:rgb(102, 104, 104);\n"
"")
        self.good_sinfo.setObjectName("good_sinfo")
        self.bought = QtWidgets.QPushButton(Form)
        self.bought.setGeometry(QtCore.QRect(0, 190, 192, 32))
        self.bought.setStyleSheet("\n"
"QPushButton#bought\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#bought:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#bought:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.bought.setObjectName("bought")
        self.orders = QtWidgets.QPushButton(Form)
        self.orders.setGeometry(QtCore.QRect(0, 250, 192, 32))
        self.orders.setStyleSheet("QPushButton#orders\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#orders:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#orders:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.orders.setObjectName("orders")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(15, 350, 60, 16))
        self.label_5.setStyleSheet("background:rgb(242, 242, 243);\n"
"font: 15pt, \"Heiti SC\" ;\n"
"color:rgb(102, 104, 104);\n"
"")
        self.label_5.setObjectName("label_5")
        self.enter_my_shop = QtWidgets.QPushButton(Form)
        self.enter_my_shop.setGeometry(QtCore.QRect(0, 380, 192, 32))
        self.enter_my_shop.setStyleSheet("\n"
"QPushButton#enter_my_shop\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_my_shop:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_my_shop:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.enter_my_shop.setObjectName("enter_my_shop")
        self.enter_my_shop_2 = QtWidgets.QPushButton(Form)
        self.enter_my_shop_2.setGeometry(QtCore.QRect(0, 440, 192, 32))
        self.enter_my_shop_2.setStyleSheet("\n"
"QPushButton#enter_my_shop_2\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_my_shop_2:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_my_shop_2:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.enter_my_shop_2.setObjectName("enter_my_shop_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(270, 15, 200, 31))
        self.textEdit.setStyleSheet("background:transparent;border-width:0;border-style:outset;\n"
"font: 18pt \"Heiti SC\";")
        self.textEdit.setObjectName("textEdit")
        self.enter_shop = QtWidgets.QPushButton(Form)
        self.enter_shop.setGeometry(QtCore.QRect(480, 15, 51, 31))
        self.enter_shop.setStyleSheet("\n"
"QPushButton#enter_shop\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_shop:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_shop:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.enter_shop.setObjectName("enter_shop")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 981, 60))
        self.label_6.setStyleSheet("background:rgb(169, 19, 3)")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.sline_2 = QtWidgets.QLabel(Form)
        self.sline_2.setGeometry(QtCore.QRect(910, 0, 1, 60))
        self.sline_2.setStyleSheet("background:rgb(143, 12, 4)")
        self.sline_2.setText("")
        self.sline_2.setObjectName("sline_2")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.logo.setStyleSheet("background-color: transparent;")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.label_4.raise_()
        self.label_6.raise_()
        self.username.raise_()
        self.shopcar.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.exit.raise_()
        self.head.raise_()
        self.good_sinfo.raise_()
        self.bought.raise_()
        self.orders.raise_()
        self.label_5.raise_()
        self.enter_my_shop.raise_()
        self.enter_my_shop_2.raise_()
        self.textEdit.raise_()
        self.enter_shop.raise_()
        self.sline_2.raise_()
        self.logo.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.shopcar.setText(_translate("Form", "购物车"))
        self.enter_shop_1.setText(_translate("Form", "→"))
        self.enter_shop_2.setText(_translate("Form", "→"))
        self.enter_shop_3.setText(_translate("Form", "→"))
        self.enter_shop_4.setText(_translate("Form", "→"))
        self.enter_shop_5.setText(_translate("Form", "→"))
        self.shop_name_head.setText(_translate("Form", "店铺名"))
        self.shop_id_head.setText(_translate("Form", "     ID"))
        self.shop_owner_head.setText(_translate("Form", "店  主"))
        self.good_sinfo.setText(_translate("Form", "购物信息"))
        self.bought.setText(_translate("Form", "已购买商品"))
        self.orders.setText(_translate("Form", "所有订单"))
        self.label_5.setText(_translate("Form", "店铺信息"))
        self.enter_my_shop.setText(_translate("Form", "我的店铺"))
        self.enter_my_shop_2.setText(_translate("Form", "谁在逛我的店铺"))
        self.textEdit.setPlaceholderText(_translate("Form", "输入店铺名或ID进入"))
        self.enter_shop.setText(_translate("Form", "→"))

