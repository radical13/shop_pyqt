from ui_inputwindow import Ui_input
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from server import *

class Server_InputWindow(QtWidgets.QWidget,Ui_input):
    def __init__(self,type,parent=None):
        super(Server_InputWindow, self).__init__(parent)
        self.setupUi(self)
        init_f = {"add_user": self.init_add_user,
                  "add_shop": self.init_add_shop,
                  "close_shop": self.init_close_shop,
                  'send_all': self.init_send_all,
                  'send': self.init_send}
        init_f[type]()

    def init_add_user(self):
        self.setWindowTitle("添加用户")
        self.label.setText("UserID")
        self.label_2.setText("用户名")
        self.label_3.setText("密码")
        self.submit.clicked.connect(self.add_user)

    def init_add_shop(self):
        self.setWindowTitle("添加商店")
        self.label.setText("ShopID")
        self.label_2.setText("商店名")
        self.label_3.setHidden(True)
        self.price.setHidden(True)
        self.submit.clicked.connect(self.add_shop)

    def init_close_shop(self):
        self.setWindowTitle("关闭店铺")
        self.label.setText("店铺ID")
        self.label_2.setHidden(True)
        self.label_3.setHidden(True)
        self.name.setHidden(True)
        self.price.setHidden(True)

        self.submit.clicked.connect(self.close_shop)
    def init_send_all(self):
        self.setWindowTitle("群发消息")
        self.label.setText("消息标题")
        self.label_2.setText("消息内容")
        self.label_3.setHidden(True)
        self.price.setHidden(True)
        self.submit.clicked.connect(self.send_all)
    def init_send(self):
        self.setWindowTitle("群发消息")
        self.label.setText("消息标题")
        self.label_2.setText("消息内容")
        self.label_3.setText("接收人")
        self.submit.clicked.connect(self.send)

    def add_user(self):
        if self.id.text() == "":
            self.id.setText("请输入用户id")
            return
        else:
            id = self.id.text()

        if self.name.text() =="":
            self.name.setText("请输入用户密码")
            return
        else:
            pw = self.name.text()

        if self.price.text() =="":
            self.price.setText("请输入用户名称")
            return
        else:
            name = self.price.text()
        for key in user_infomation:
            if str(user_infomation[key]['user_id']) == id:
                self.msgwindow = MsgWindow("", "用户" + name + "添加失败！(ID重复)")
                self.close()
                return
        user_infomation[name] = {}
        user_infomation[name]['user_id'] = int(id)
        user_infomation[name]['pw'] = pw
        user_infomation[name]['shop'] = 0
        self.close()
    def add_shop(self):
        if self.id.text() == "":
            self.id.setText("请输入店铺id")
            return
        else:
            id = self.id.text()

        if self.name.text() == "":
            self.name.setText("请输入店铺名称")
            return
        else:
            name = self.name.text()

        flag = 0
        owner = ""

        for key in user_infomation:
            if user_infomation[key]['user_id'] == int(id):
                owner = key
                flag = 1
                break

        if flag == 0:
            self.msgwindow = MsgWindow("", "店铺" + name + "添加失败！(ID不存在)")
            self.close()
            return

        shop_list[id] = {}
        shop_list[id]['name'] = name
        shop_list[id]['owner'] = owner
        shop_list[id]['goods'] = []
        shop_list[id]['state'] = "open"
        user_infomation[owner]['shop'] = int(id)

        self.msgwindow = MsgWindow("", "店铺" + name + "添加成功")
        self.close()

        recv = [owner]
        send = ["商城管理员：小森"]
        content = [{"title":"店铺开通","text":"已为您开通新的店铺："+name}]

        send_message_manage(content,recv,send)
    def close_shop(self):
        if self.id.text() == "":
            self.id.setText("请输入店铺id")
            return
        else:
            id = self.id.text()
        if shop_list.__contains__(id):
            shop_list[id]['state'] = 'close'
            self.msgwindow = MsgWindow("", "关闭成功")
            self.close()
            recv = shop_visit[id]
            send = []
            content = []
            for i in range(len(recv)):
                send.append("商城管理员：小森")
                content.append({"title":"店铺关闭","text":"您所逛的店铺已被关闭"})
            recv.append(shop_list[id]['owner'])
            send.append("商城管理员：小森")
            content.append({"title": "店铺关闭", "text": "您的店铺已被关闭"})
            send_message_manage(content,recv,send)
            return
        else:
            self.msgwindow = MsgWindow("", "店铺" + str(id) + "关闭失败！(ID不存在)")
            self.close()
            return

    def send_all(self):
        title = self.id.text()

        if self.name.text() == "":
            self.name.setText("消息内容不能为空")
            return
        else:
            content1 = self.name.text()

        recv = []
        send = []
        content = []
        for key in user_infomation:
            recv.append(key)
            send.append("商城管理员：小森")
            content.append({'title':title,'text':content1})
        result = send_message_manage(content,recv,send)

        flag = 0
        for i in range(len(result)):
            if result[i] == 1:
                flag = 1
                break
        if flag == 1:
            self.msgwindow = MsgWindow("部分消息或全部消息发送失败")
            self.close()
        else:
            self.msgwindow = MsgWindow("","发送成功")
            self.close()
    def send(self):
        title = self.id.text()

        if self.name.text() == "":
            self.name.setText("消息内容不能为空")
            return
        else:
            content1 = self.name.text()

        if self.price.text()=="":
            self.price.setText("接收人不能为空")
            return
        else:
            recv1 = self.price.text()

        if user_infomation.__contains__(recv1) == False:
            self.msgwindow = MsgWindow("接收人不存在")
            self.close()
        recv = [recv1]
        send = ["商城管理员：小森"]
        content = [{'title':title,'text':content1}]

        result = send_message_manage(content,recv,send)
        flag = 0
        for i in range(len(result)):
            if result[i] == 1:
                flag = 1
                break
        if flag == 1:
            self.msgwindow = MsgWindow("","发送失败")
            self.close()
        else:
            self.msgwindow = MsgWindow("","发送成功")
            self.close()

class MsgWindow(QtWidgets.QWidget):
    def __init__(self, m1, m2):
        super().__init__()
        self.setWindowTitle(m1)
        QMessageBox.information(self, m1, m2, QMessageBox.Yes)