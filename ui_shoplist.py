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
        self.username.setGeometry(QtCore.QRect(620, 20, 100, 21))
        self.username.setStyleSheet("background:transparent;")
        self.username.setText("")
        self.username.setObjectName("username")
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
        self.shop_name_4 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_4.setStyleSheet("font: 14pt \"Heiti SC\";\n"
"")
        self.shop_name_4.setText("")
        self.shop_name_4.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_4.setObjectName("shop_name_4")
        self.verticalLayout_2.addWidget(self.shop_name_4)
        self.shop_name_5 = QtWidgets.QLabel(self.layoutWidget)
        self.shop_name_5.setText("")
        self.shop_name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_5.setObjectName("shop_name_5")
        self.verticalLayout_2.addWidget(self.shop_name_5)
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
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(740, 20, 30, 21))
        self.exit.setStyleSheet("\n"
"QPushButton#exit\n"
"{\n"
"    font:14pt,rgb(255, 255, 255);\n"
"    background-color:transparent;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#exit:hover\n"
"{\n"
"   font:14pt,rgb(255, 255, 255);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton#exit:pressed\n"
"{\n"
"   font:14pt,rgb(255, 255, 255);\n"
"    background-color:transparent;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
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
        self.good_sinfo.setGeometry(QtCore.QRect(10, 120, 60, 16))
        self.good_sinfo.setStyleSheet("background:rgb(242, 242, 243);\n"
"font: 15pt, \"Heiti SC\" ;\n"
"color:rgb(102, 104, 104);\n"
"")
        self.good_sinfo.setObjectName("good_sinfo")
        self.bought = QtWidgets.QPushButton(Form)
        self.bought.setGeometry(QtCore.QRect(0, 180, 192, 32))
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
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(15, 260, 60, 16))
        self.label_5.setStyleSheet("background:rgb(242, 242, 243);\n"
"font: 15pt, \"Heiti SC\" ;\n"
"color:rgb(102, 104, 104);\n"
"")
        self.label_5.setObjectName("label_5")
        self.enter_my_shop = QtWidgets.QPushButton(Form)
        self.enter_my_shop.setGeometry(QtCore.QRect(0, 310, 192, 32))
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
        self.shop_custom = QtWidgets.QPushButton(Form)
        self.shop_custom.setGeometry(QtCore.QRect(0, 370, 192, 32))
        self.shop_custom.setStyleSheet("\n"
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
        self.shop_custom.setObjectName("shop_custom")
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
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(15, 550, 60, 16))
        self.label_7.setStyleSheet("background:rgb(242, 242, 243);\n"
"font: 15pt, \"Heiti SC\" ;\n"
"color:rgb(102, 104, 104);\n"
"")
        self.label_7.setObjectName("label_7")
        self.login_info = QtWidgets.QPushButton(Form)
        self.login_info.setGeometry(QtCore.QRect(0, 580, 192, 32))
        self.login_info.setStyleSheet("\n"
"QPushButton#login_info\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#login_info:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#login_info:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.login_info.setObjectName("login_info")
        self.next_page = QtWidgets.QPushButton(Form)
        self.next_page.setGeometry(QtCore.QRect(670, 610, 75, 40))
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
        self.last_page = QtWidgets.QPushButton(Form)
        self.last_page.setGeometry(QtCore.QRect(270, 610, 75, 40))
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
        self.page3 = QtWidgets.QLabel(Form)
        self.page3.setGeometry(QtCore.QRect(340, 610, 41, 40))
        self.page3.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page3.setAlignment(QtCore.Qt.AlignCenter)
        self.page3.setObjectName("page3")
        self.page_2 = QtWidgets.QLabel(Form)
        self.page_2.setGeometry(QtCore.QRect(440, 610, 121, 40))
        self.page_2.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page_2.setAlignment(QtCore.Qt.AlignCenter)
        self.page_2.setObjectName("page_2")
        self.shop_num = QtWidgets.QLabel(Form)
        self.shop_num.setGeometry(QtCore.QRect(380, 610, 61, 40))
        self.shop_num.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.shop_num.setText("")
        self.shop_num.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_num.setObjectName("shop_num")
        self.page = QtWidgets.QLabel(Form)
        self.page.setGeometry(QtCore.QRect(570, 610, 61, 40))
        self.page.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page.setText("")
        self.page.setAlignment(QtCore.Qt.AlignCenter)
        self.page.setObjectName("page")
        self.page_5 = QtWidgets.QLabel(Form)
        self.page_5.setGeometry(QtCore.QRect(630, 610, 51, 40))
        self.page_5.setStyleSheet("font: 75 16pt \"Heiti SC\";")
        self.page_5.setAlignment(QtCore.Qt.AlignCenter)
        self.page_5.setObjectName("page_5")
        self.see_msg = QtWidgets.QPushButton(Form)
        self.see_msg.setGeometry(QtCore.QRect(800, 20, 41, 21))
        self.see_msg.setStyleSheet("\n"
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
        self.see_msg.setObjectName("see_msg")
        self.input_shop_id = QtWidgets.QLineEdit(Form)
        self.input_shop_id.setGeometry(QtCore.QRect(250, 15, 221, 31))
        self.input_shop_id.setText("")
        self.input_shop_id.setMaxLength(5)
        self.input_shop_id.setAlignment(QtCore.Qt.AlignCenter)
        self.input_shop_id.setObjectName("input_shop_id")
        self.now_shop = QtWidgets.QLabel(Form)
        self.now_shop.setGeometry(QtCore.QRect(280, 70, 101, 31))
        self.now_shop.setText("")
        self.now_shop.setObjectName("now_shop")
        self.now_shop_head = QtWidgets.QLabel(Form)
        self.now_shop_head.setGeometry(QtCore.QRect(220, 80, 61, 21))
        self.now_shop_head.setObjectName("now_shop_head")
        self.now_shop_name = QtWidgets.QLabel(Form)
        self.now_shop_name.setGeometry(QtCore.QRect(400, 70, 151, 31))
        self.now_shop_name.setText("")
        self.now_shop_name.setObjectName("now_shop_name")
        self.back_shoplist = QtWidgets.QPushButton(Form)
        self.back_shoplist.setGeometry(QtCore.QRect(570, 70, 61, 31))
        self.back_shoplist.setStyleSheet("\n"
"QPushButton#back_shoplist\n"
"{\n"
"    font:36pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#back_shoplist:hover\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#back_shoplist:pressed\n"
"{\n"
"   font:36pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.back_shoplist.setObjectName("back_shoplist")
        self.msg_num = QtWidgets.QLabel(Form)
        self.msg_num.setGeometry(QtCore.QRect(840, 20, 71, 21))
        self.msg_num.setStyleSheet("background:transparent;\n"
"color:white")
        self.msg_num.setText("")
        self.msg_num.setObjectName("msg_num")
        self.num_1 = QtWidgets.QLineEdit(Form)
        self.num_1.setGeometry(QtCore.QRect(730, 190, 90, 23))
        self.num_1.setStyleSheet("font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;")
        self.num_1.setAlignment(QtCore.Qt.AlignCenter)
        self.num_1.setObjectName("num_1")
        self.num_2 = QtWidgets.QLineEdit(Form)
        self.num_2.setGeometry(QtCore.QRect(730, 270, 90, 23))
        self.num_2.setStyleSheet("font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;")
        self.num_2.setAlignment(QtCore.Qt.AlignCenter)
        self.num_2.setObjectName("num_2")
        self.num_3 = QtWidgets.QLineEdit(Form)
        self.num_3.setGeometry(QtCore.QRect(730, 360, 90, 23))
        self.num_3.setStyleSheet("font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;")
        self.num_3.setAlignment(QtCore.Qt.AlignCenter)
        self.num_3.setObjectName("num_3")
        self.num_4 = QtWidgets.QLineEdit(Form)
        self.num_4.setGeometry(QtCore.QRect(730, 440, 90, 23))
        self.num_4.setStyleSheet("font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;")
        self.num_4.setAlignment(QtCore.Qt.AlignCenter)
        self.num_4.setObjectName("num_4")
        self.num_5 = QtWidgets.QLineEdit(Form)
        self.num_5.setGeometry(QtCore.QRect(730, 520, 90, 23))
        self.num_5.setStyleSheet("font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;")
        self.num_5.setMaxLength(3)
        self.num_5.setAlignment(QtCore.Qt.AlignCenter)
        self.num_5.setObjectName("num_5")
        self.num_head = QtWidgets.QLabel(Form)
        self.num_head.setGeometry(QtCore.QRect(720, 120, 91, 20))
        self.num_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.num_head.setAlignment(QtCore.Qt.AlignCenter)
        self.num_head.setObjectName("num_head")
        self.enter_sold_recording = QtWidgets.QPushButton(Form)
        self.enter_sold_recording.setGeometry(QtCore.QRect(0, 430, 192, 32))
        self.enter_sold_recording.setStyleSheet("\n"
"QPushButton#enter_sold_recording\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#enter_sold_recording:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#enter_sold_recording:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.enter_sold_recording.setObjectName("enter_sold_recording")
        self.add_goods = QtWidgets.QPushButton(Form)
        self.add_goods.setGeometry(QtCore.QRect(0, 490, 192, 32))
        self.add_goods.setStyleSheet("\n"
"QPushButton#add_goods\n"
"{\n"
"    font:12pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#add_goods:hover\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#add_goods:pressed\n"
"{\n"
"   font:12pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.add_goods.setObjectName("add_goods")
        self.shop_name_head = QtWidgets.QLabel(Form)
        self.shop_name_head.setGeometry(QtCore.QRect(250, 120, 129, 20))
        self.shop_name_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_name_head.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_head.setObjectName("shop_name_head")
        self.shop_id_head = QtWidgets.QLabel(Form)
        self.shop_id_head.setGeometry(QtCore.QRect(390, 120, 129, 20))
        self.shop_id_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_id_head.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_id_head.setObjectName("shop_id_head")
        self.shop_owner_head = QtWidgets.QLabel(Form)
        self.shop_owner_head.setGeometry(QtCore.QRect(550, 120, 99, 20))
        self.shop_owner_head.setStyleSheet("font: 75 20pt \"Heiti SC\";")
        self.shop_owner_head.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_owner_head.setObjectName("shop_owner_head")
        self.buy_good_1 = QtWidgets.QPushButton(Form)
        self.buy_good_1.setGeometry(QtCore.QRect(851, 190, 36, 26))
        self.buy_good_1.setStyleSheet("\n"
"QPushButton#buy_good_1\n"
"{\n"
"    font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#buy_good_1:hover\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#buy_good_1:pressed\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.buy_good_1.setObjectName("buy_good_1")
        self.buy_good_3 = QtWidgets.QPushButton(Form)
        self.buy_good_3.setGeometry(QtCore.QRect(851, 360, 36, 26))
        self.buy_good_3.setStyleSheet("\n"
"QPushButton#buy_good_3\n"
"{\n"
"    font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#buy_good_3:hover\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#buy_good_3:pressed\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.buy_good_3.setObjectName("buy_good_3")
        self.buy_good_4 = QtWidgets.QPushButton(Form)
        self.buy_good_4.setGeometry(QtCore.QRect(851, 440, 36, 26))
        self.buy_good_4.setStyleSheet("\n"
"QPushButton#buy_good_4\n"
"{\n"
"    font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#buy_good_4:hover\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#buy_good_4:pressed\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.buy_good_4.setObjectName("buy_good_4")
        self.buy_good_2 = QtWidgets.QPushButton(Form)
        self.buy_good_2.setGeometry(QtCore.QRect(851, 270, 36, 26))
        self.buy_good_2.setStyleSheet("\n"
"QPushButton#buy_good_2\n"
"{\n"
"    font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#buy_good_2:hover\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#buy_good_2:pressed\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.buy_good_2.setObjectName("buy_good_2")
        self.buy_good_5 = QtWidgets.QPushButton(Form)
        self.buy_good_5.setGeometry(QtCore.QRect(851, 520, 36, 26))
        self.buy_good_5.setStyleSheet("\n"
"QPushButton#buy_good_5\n"
"{\n"
"    font:18pt,black;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#buy_good_5:hover\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"}\n"
"\n"
"QPushButton#buy_good_5:pressed\n"
"{\n"
"   font:18pt,rgb(0, 172, 230);\n"
"    background-color:white;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"")
        self.buy_good_5.setObjectName("buy_good_5")
        self.enter_shop_2 = QtWidgets.QPushButton(Form)
        self.enter_shop_2.setGeometry(QtCore.QRect(680, 260, 30, 43))
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
        self.enter_shop_1 = QtWidgets.QPushButton(Form)
        self.enter_shop_1.setGeometry(QtCore.QRect(680, 180, 30, 43))
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
        self.enter_shop_5 = QtWidgets.QPushButton(Form)
        self.enter_shop_5.setGeometry(QtCore.QRect(680, 510, 30, 43))
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
        self.enter_shop_3 = QtWidgets.QPushButton(Form)
        self.enter_shop_3.setGeometry(QtCore.QRect(680, 350, 30, 43))
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
        self.enter_shop_4 = QtWidgets.QPushButton(Form)
        self.enter_shop_4.setGeometry(QtCore.QRect(680, 430, 30, 43))
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
        self.label_4.raise_()
        self.label_6.raise_()
        self.username.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.exit.raise_()
        self.head.raise_()
        self.good_sinfo.raise_()
        self.bought.raise_()
        self.label_5.raise_()
        self.enter_my_shop.raise_()
        self.shop_custom.raise_()
        self.enter_shop.raise_()
        self.sline_2.raise_()
        self.logo.raise_()
        self.label_7.raise_()
        self.login_info.raise_()
        self.next_page.raise_()
        self.last_page.raise_()
        self.page3.raise_()
        self.page_2.raise_()
        self.shop_num.raise_()
        self.page.raise_()
        self.page_5.raise_()
        self.see_msg.raise_()
        self.input_shop_id.raise_()
        self.now_shop.raise_()
        self.now_shop_head.raise_()
        self.now_shop_name.raise_()
        self.back_shoplist.raise_()
        self.msg_num.raise_()
        self.num_1.raise_()
        self.num_2.raise_()
        self.num_3.raise_()
        self.num_4.raise_()
        self.num_5.raise_()
        self.num_head.raise_()
        self.enter_sold_recording.raise_()
        self.add_goods.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exit.setText(_translate("Form", "退出"))
        self.good_sinfo.setText(_translate("Form", "购物信息"))
        self.bought.setText(_translate("Form", "已购买商品"))
        self.label_5.setText(_translate("Form", "店铺信息"))
        self.enter_my_shop.setText(_translate("Form", "我的店铺"))
        self.shop_custom.setText(_translate("Form", "顾客信息"))
        self.enter_shop.setText(_translate("Form", "→"))
        self.label_7.setText(_translate("Form", "用户信息"))
        self.login_info.setText(_translate("Form", "登录记录"))
        self.next_page.setText(_translate("Form", "→"))
        self.last_page.setText(_translate("Form", "←"))
        self.page3.setText(_translate("Form", "共"))
        self.page_2.setText(_translate("Form", "家店铺 当前是第"))
        self.page_5.setText(_translate("Form", "页"))
        self.see_msg.setText(_translate("Form", "私信"))
        self.input_shop_id.setPlaceholderText(_translate("Form", "输入店铺ID进入"))
        self.now_shop_head.setText(_translate("Form", "您当前在"))
        self.back_shoplist.setText(_translate("Form", "←"))
        self.num_1.setPlaceholderText(_translate("Form", "×1"))
        self.num_2.setPlaceholderText(_translate("Form", "×1"))
        self.num_3.setPlaceholderText(_translate("Form", "×1"))
        self.num_4.setPlaceholderText(_translate("Form", "×1"))
        self.num_5.setPlaceholderText(_translate("Form", "×1"))
        self.num_head.setText(_translate("Form", "件数"))
        self.enter_sold_recording.setText(_translate("Form", "销售信息"))
        self.add_goods.setText(_translate("Form", "发布新商品"))
        self.shop_name_head.setText(_translate("Form", "店铺名"))
        self.shop_id_head.setText(_translate("Form", "ID"))
        self.shop_owner_head.setText(_translate("Form", "店  主"))
        self.buy_good_1.setText(_translate("Form", "剁手"))
        self.buy_good_3.setText(_translate("Form", "剁手"))
        self.buy_good_4.setText(_translate("Form", "剁手"))
        self.buy_good_2.setText(_translate("Form", "剁手"))
        self.buy_good_5.setText(_translate("Form", "剁手"))
        self.enter_shop_2.setText(_translate("Form", "→"))
        self.enter_shop_1.setText(_translate("Form", "→"))
        self.enter_shop_5.setText(_translate("Form", "→"))
        self.enter_shop_3.setText(_translate("Form", "→"))
        self.enter_shop_4.setText(_translate("Form", "→"))

