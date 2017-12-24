from socket import *
import json
from ui_inputwindow import Ui_input
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class InputWindow(QtWidgets.QWidget,Ui_input):
    def __init__(self,id,parent=None):
        super(InputWindow, self).__init__(parent)
        self.setupUi(self)
        self.submit.clicked.connect(lambda :self.add_goods(id))


    def add_goods(self,shop_id):
        if self.id.text() == "":
            self.id.setText("请输入新商品id")
            return
        else:
            goods_id = self.id.text()

        if self.name.text() =="":
            self.name.setText("请输入新商品名称")
            return
        else:
            goods_name = self.name.text()

        if self.price.text() =="":
            self.name.setText("请输入新商品单价")
            return
        else:
            goods_price = self.price.text()

        host = '127.0.0.1'
        port = 62000
        s = socket(AF_INET, SOCK_DGRAM)
        info = {"method":"add_goods",
                "id":shop_id,
                "goods_id":goods_id,
                "goods_name":goods_name,
                "goods_price":goods_price}
        message = json.dumps(info)

        if s.connect((host, port)) == 0:
            return
        while True:
            s.sendall(message.encode(encoding='utf-8'))
            try:
                data = s.recv(1024)
            except IOError:
                break
            data = json.loads(data)
            break
        if data['result'] == "success":
            self.msgwindow = MsgWindow("","商品"+goods_name+"添加成功！")
            self.close()
        elif data['result'] == "id_fail":
            self.msgwindow = MsgWindow("", "商品" + goods_name + "添加失败！(ID重复)")
            self.close()
        else:
            self.msgwindow = MsgWindow("", "商品" + goods_name + "添加失败！")
            self.close()

class MsgWindow(QtWidgets.QWidget):
    def __init__(self, m1, m2):
        super().__init__()
        self.setWindowTitle(m1)
        QMessageBox.information(self, m1, m2, QMessageBox.Yes)
