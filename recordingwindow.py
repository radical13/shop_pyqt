from PyQt5.QtGui import QPixmap
from ui_msgbox import *
from socket import *


class RecordingBoxWindow(QtWidgets.QWidget, Ui_msgbox):
    message = []


    def __init__(self, type, msg,parent=None):
        super(RecordingBoxWindow, self).__init__(parent)
        self.setupUi(self)
        init_f={"buy":self.init_buy,
               "sold":self.init_sold,
               "login":self.init_login}

        init_f[type](msg)
        self.loadmsg(self.message)
        self.next_page.clicked.connect(self.to_next_page)
        self.last_page.clicked.connect(self.to_last_page)

    def init_buy(self,data):
        self.setWindowTitle("购买记录")
        self.send_head.setText("订单号")
        self.shop_owner_head.setText("购买信息")
        msg=[]

        for i in range(len(data)):
            m = {}
            m['time'] = data[i]['time']
            m['send'] = data[i]['shopping_num']
            m['content'] = data[i]['goods_name'] + " × " +data[i]['num']
            msg.append(m)
        self.message = msg

    def init_sold(self,data):
        self.setWindowTitle("销售记录")
        self.send_head.setText("订单号")
        self.shop_owner_head.setText("销售信息")
        msg = []

        for i in range(len(data)):
            m = {}
            m['time'] = data[i]['time']
            m['send'] = data[i]['shopping_num']
            m['content'] = "向" + data[i]['user'] + "卖出" + data[i]['id'] + " × " + data[i]['num']
            msg.append(m)
        self.message = msg
    def init_login(self,data):
        self.setWindowTitle("登陆记录")
        self.send_head.setText("编号")
        self.shop_owner_head.setText("登陆位置")
        msg = []

        for i in range(len(data)):
            m = {}
            m['time'] = data[i]['time']
            m['send'] = str(i+1)
            m['content'] = str(data[i]['add'])
            msg.append(m)
        self.message = msg
    def loadmsg_range(self, r, data):
        if len(self.message) < r * 5:
            s_i = len(self.message) - 5 * (r - 1) + 1
        else:
            s_i = 6
        for i in range(1, s_i):
            method = "modify_msglist" + str(i)
            getattr(self, method)(data[(r - 1) * 5 + i - 1]['time'],
                                  data[(r - 1) * 5 + i - 1]['send'],
                                  data[(r - 1) * 5 + i - 1]["content"])
        for i in range(s_i, 6):
            method = "modify_msglist" + str(i)
            getattr(self, method)("", "", "")

    def to_next_page(self):
        current = int(self.page.text())

        if (current + 1) * 5 <= (int)(self.msg_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(False)
            self.page.setText(str(current + 1))
            self.loadmsg_range(current + 1, self.message)

        elif (current + 1) * 5 > (int)(self.msg_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current + 1))
            self.loadmsg_range(current + 1, self.message)

    def to_last_page(self):

        current = int(self.page.text())

        if (current - 1) == 1:
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.page.setText(str(current - 1))
            self.loadmsg_range(current - 1, self.message)
        else:
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current - 1))
            self.loadmsg_range(current - 1, self.message)

    def modify_msglist1(self, id, name, owner):
        self.time_1.setText(id)
        self.send_1.setText(name)
        self.content_1.setText(owner)

    def modify_msglist2(self, id, name, owner):
        self.time_2.setText(id)
        self.send_2.setText(name)
        self.content_2.setText(owner)

    def modify_msglist3(self, id, name, owner):
        self.time_3.setText(id)
        self.send_3.setText(name)
        self.content_3.setText(owner)

    def modify_msglist4(self, id, name, owner):
        self.time_4.setText(id)
        self.send_4.setText(name)
        self.content_4.setText(owner)

    def modify_msglist5(self, id, name, owner):
        self.time_5.setText(id)
        self.send_5.setText(name)
        self.content_5.setText(owner)

    def loadmsg(self, data):

        msgnum = data.__len__()

        if msgnum <= 5:
            for i in range(1, msgnum + 1):
                method = "modify_msglist" + str(i)
                getattr(self, method)(data[i - 1]['time'],
                                      data[i - 1]['send'],
                                      data[i - 1]["content"])
            self.last_page.setHidden(True)
            self.next_page.setHidden(True)
            self.msg_num.setText(str(msgnum))

        else:
            for i in range(1, 6):
                method = "modify_msglist" + str(i)
                getattr(self, method)(data[i - 1]['time'],
                                      data[i - 1]['send'],
                                      data[i - 1]["content"])
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.msg_num.setText(str(msgnum))
        self.page.setText("1")


