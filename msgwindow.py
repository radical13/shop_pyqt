from PyQt5.QtGui import QPixmap
from ui_msgbox import *
from socket import *

class MsgBoxWindow(QtWidgets.QWidget,Ui_msgbox):
    message =[]
    def __init__(self,msg,parent=None):
        super(MsgBoxWindow, self).__init__(parent)
        self.setupUi(self)
        for i in range(len(msg)):
            self.message.append(msg[i])
        self.loadmsg(msg)
        self.next_page.clicked.connect(self.to_next_page)
        self.last_page.clicked.connect(self.to_last_page)
        
    def loadmsg_range(self,r,data):
        if len(self.message) < r * 5:
            s_i = len(self.message) - 5 *(r - 1) + 1
        else:
            s_i = 6
        for i in range(1, s_i):
            method = "modify_msglist" + str(i)
            getattr(self, method)(data[(r-1) * 5 + i-1]['time'],
                                  data[(r-1) * 5 + i-1]['send'],
                                  "[" + data[(r-1) * 5 + i-1]["content"]['title'] + "]\n" + data[(r-1) * 5 + i-1]["content"]['text'])
        for i in range(s_i,6):
            method = "modify_msglist" + str(i)
            getattr(self, method)("","","")
    def to_next_page(self):
        current = int(self.page.text())

        if (current+1)*5<=(int)(self.msg_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(False)
            self.page.setText(str(current+1))
            self.loadmsg_range(current+1,self.message)

        elif (current+1)*5 > (int)(self.msg_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current + 1))
            self.loadmsg_range(current+1,self.message)

    def to_last_page(self):

        current = int(self.page.text())

        if (current-1)==1:
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.page.setText(str(current - 1))
            self.loadmsg_range(current-1,self.message)
        else:
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current - 1))
            self.loadmsg_range(current - 1, self.message)

    def modify_msglist1(self,id,name,owner):
        self.time_1.setText(id)
        self.send_1.setText(name)
        self.content_1.setText(owner)
    def modify_msglist2(self,id,name,owner):
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
    def loadmsg(self,data):

        msgnum = data.__len__()

        if msgnum <=5:
            for i in range(1, msgnum+1):
                method = "modify_msglist" + str(i)
                getattr(self, method)(data[i - 1]['time'],
                                      data[i - 1]['send'],
                                     "[" +data[i - 1]["content"]['title']+"]\n"+data[i - 1]["content"]['text'])
            self.last_page.setHidden(True)
            self.next_page.setHidden(True)
            self.msg_num.setText(str(msgnum))

        else:
            for i in range(1, 6):
                method = "modify_msglist" + str(i)
                getattr(self, method)(data[i - 1]['time'],
                                      data[i - 1]['send'],
                                      "[" + data[i - 1]["content"]['title'] + "]\n" + data[i-1]["content"]['text'])
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.msg_num.setText(str(msgnum))
        self.page.setText("1")