from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from ui_server import *
from server import *
import threading
from recordingwindow import RecordingBoxWindow
from server_inputwindow import Server_InputWindow

class ServerWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ServerWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("欢迎使用森普商城服务端...服务端正在运行")
        self.input_shop_id.setAttribute(Qt.WA_MacShowFocusRect, False)


        # listen the client request
        t = threading.Thread(target=listen_request, args=())
        t.setDaemon(True)
        t.start()

        # init some infomation
        shops = self.getshop()
        self.loadshop(shops)

        pixmap = QPixmap("img/logo.png")
        self.logo.setPixmap(pixmap)

        icon_update = QIcon("img/update.png")
        self.update_button.setIcon(icon_update)

        # connect function
        self.next_page.clicked.connect(self.to_next_page)
        self.last_page.clicked.connect(self.to_last_page)
        self.enter_shop_1.clicked.connect(lambda: self.enter_shop_request("1"))
        self.enter_shop_2.clicked.connect(lambda: self.enter_shop_request("2"))
        self.enter_shop_3.clicked.connect(lambda: self.enter_shop_request("3"))
        self.enter_shop_4.clicked.connect(lambda: self.enter_shop_request("4"))
        self.enter_shop_5.clicked.connect(lambda: self.enter_shop_request("5"))
        self.enter_shop.clicked.connect(lambda: self.enter_shop_request("0"))
        self.back_shoplist.clicked.connect(self.back_list)
        self.custom_button.clicked.connect(self.get_custom)
        self.see_user_info_button.clicked.connect(self.get_user_all)
        self.add_user_button.clicked.connect(self.add_user)
        self.add_shop_button.clicked.connect(self.add_shop)
        self.close_shop_button.clicked.connect(self.close_shop)
        self.send_msg_button.clicked.connect(self.send)
        self.send_msg_all_button.clicked.connect(self.send_all)
        self.update_button.clicked.connect(self.update)

    # modify the shop list

    def modify_shoplist1(self, id, name, owner):
        self.shop_id_1.setText(id)
        self.shop_name_1.setText(name)
        self.shop_owner_1.setText(owner)

    def modify_shoplist2(self, id, name, owner):
        self.shop_id_2.setText(id)
        self.shop_name_2.setText(name)
        self.shop_owner_2.setText(owner)

    def modify_shoplist3(self, id, name, owner):
        self.shop_id_3.setText(id)
        self.shop_name_3.setText(name)
        self.shop_owner_3.setText(owner)

    def modify_shoplist4(self, id, name, owner):
        self.shop_id_4.setText(id)
        self.shop_name_4.setText(name)
        self.shop_owner_4.setText(owner)

    def modify_shoplist5(self, id, name, owner):
        self.shop_id_5.setText(id)
        self.shop_name_5.setText(name)
        self.shop_owner_5.setText(owner)

        # show function

    def getshop(self):
        msg = {}
        for key in shop_list:
            if shop_list[key]["state"] == "open":
                msg[key] = {"name": "", "owner": ""}
                msg[key]["name"] = shop_list[key]["name"]
                msg[key]["owner"] = shop_list[key]["owner"]
        return msg

    def loadshop_range(self, r, data):
        if 5 * r >= len(data):
            for i in range(1,len(data) - 5 *(r - 1) + 1):
                method = "modify_shoplist" + str(i)
                key = list(data.keys())[5 * (r - 1) + i - 1]
                getattr(self, method)(key, data[key]["name"], data[key]["owner"])
            for i in range(len(data) - 5 * (r - 1) + 1, 6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)("", "", "")
        else:
            for i in range(1,6):
                method = "modify_shoplist" + str(i)
                key = list(data.keys())[5 * (r - 1) + i - 1]
                getattr(self, method)(key, data[key]["name"], data[key]["owner"])

    def loadgood_range(self, r, data):
        if 5 * r >= len(data):
            for i in range(1, len(data) - 5 * (r - 1) + 1):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(data[5 * (r - 1) + i - 1]["id"], data[5 * (r - 1) + i - 1]["name"],
                                      data[5 * (r - 1) + i - 1]["price"])
            for i in range(len(data) - 5 * (r - 1) + 1, 6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)("", "", "")
        else:
            for i in range(1, 6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(data[5 * (r - 1) + i - 1]["id"], data[5 * (r - 1) + i - 1]["name"],
                                      data[5 * (r - 1) + i - 1]["price"])

    def to_next_page(self):
        state = self.shop_name_head.text()
        hidden_operation = {
            "1shop": self.enter_shop_1.setHidden,
            "2shop": self.enter_shop_2.setHidden,
            "3shop": self.enter_shop_3.setHidden,
            "4shop": self.enter_shop_4.setHidden,
            "5shop": self.enter_shop_5.setHidden
        }
        current = int(self.page.text())
        if state == "店铺名":
            shops = self.getshop()
        else:
            goods = self.enter_shop_request("6")

        if (current + 1) * 5 < (int)(self.shop_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(False)
            self.page.setText(str(current + 1))

            if state == "店铺名":
                self.loadshop_range(current + 1, shops)
            else:
                self.loadgood_range(current + 1, goods)

        elif (current + 1) * 5 >= (int)(self.shop_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current + 1))

            if state == "店铺名":
                self.loadshop_range(current + 1, shops)
                for i in range(6 - (current + 1) * 5 + (int)(self.shop_num.text()), 6):
                    hidden_operation[str(i) + "shop"](True)
            else:
                self.loadgood_range(current + 1, goods)

    def to_last_page(self):
        state = self.shop_name_head.text()
        current = int(self.page.text())
        if state == "店铺名":
            shops = self.getshop()
        else:
            goods = self.enter_shop_request("6")
        if (current - 1) == 1:
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.page.setText(str(current - 1))
            if state == "店铺名":
                self.loadshop_range(current - 1, shops)
            else:
                self.loadgood_range(current - 1, goods)
        else:
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current - 1))
            if state == "店铺名":
                self.loadshop_range(current - 1, shops)
            else:
                self.loadgood_range(current - 1, goods)
                # request function

    def loadshop(self, data):
        self.shop_name_head.setText("店铺名")
        self.shop_owner_head.setText("拥有者")
        self.page_2.setText("个店铺 当前是第")

        self.now_shop_head.setHidden(True)
        self.now_shop.setHidden(True)
        self.back_shoplist.setHidden(True)
        self.now_shop_name.setHidden(True)
        self.custom_button.setHidden(True)
        hidden_operation = {
            "1shop": self.enter_shop_1.setHidden,
            "2shop": self.enter_shop_2.setHidden,
            "3shop": self.enter_shop_3.setHidden,
            "4shop": self.enter_shop_4.setHidden,
            "5shop": self.enter_shop_5.setHidden
        }


        for i in range(1, 6):
            hidden_operation[str(i) + "shop"](False)

            # load the first five shops
            shopnum = data.__len__()

        if shopnum <= 5:
            for i in range(1, shopnum + 1):
                method = "modify_shoplist" + str(i)
                key = list(data.keys())[i - 1]
                getattr(self, method)(key, data[key]["name"], data[key]["owner"])
            for i in range(shopnum + 1, 6):
                hidden_operation[str(i) + "shop"](True)
            self.last_page.setHidden(True)
            self.next_page.setHidden(True)
            self.shop_num.setText(str(shopnum))

        else:
            for i in range(1, 6):
                method = "modify_shoplist" + str(i)
                key = list(data.keys())[i - 1]
                getattr(self, method)(key, data[key]["name"], data[key]["owner"])
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.shop_num.setText(str(shopnum))
        self.page.setText("1")

    def load_goods(self, goods, sname):
        hidden_operation = {
            "1shop": self.enter_shop_1.setHidden,
            "2shop": self.enter_shop_2.setHidden,
            "3shop": self.enter_shop_3.setHidden,
            "4shop": self.enter_shop_4.setHidden,
            "5shop": self.enter_shop_5.setHidden
        }

        self.shop_name_head.setText("商品名")
        self.shop_owner_head.setText("价格")
        self.page_2.setText("个商品 当前是第")
        self.custom_button.setHidden(False)
        for i in range(1, 6):
            hidden_operation[str(i) + "shop"](True)

        self.now_shop_head.setHidden(False)
        self.now_shop.setHidden(False)
        self.back_shoplist.setHidden(False)
        goodsnum = len(goods)
        self.now_shop_name.setHidden(False)
        self.now_shop_name.setText(sname)

        if goodsnum < 5:
            for i in range(1, goodsnum + 1):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(goods[i - 1]["id"], goods[i - 1]["name"], goods[i - 1]["price"])
            for i in range(goodsnum + 1, 6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)("", "", "")
            self.last_page.setHidden(True)
            self.next_page.setHidden(True)
            self.shop_num.setText(str(goodsnum))
            self.page.setText("1")

        else:
            for i in range(1, 6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(goods[i - 1]["id"], goods[i - 1]["name"], goods[i - 1]["price"])

            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.shop_num.setText(str(goodsnum))
            self.page.setText("1")

    def enter_shop_request(self, num):
        id_dic = {"1": self.shop_id_1.text(),
                  "2": self.shop_id_2.text(),
                  "3": self.shop_id_3.text(),
                  "4": self.shop_id_4.text(),
                  "5": self.shop_id_5.text(),
                  "0": self.input_shop_id.text(),
                  "6": self.now_shop.text()
                  }
        shop_id = id_dic[num]
        msg = {"state": "open", "goods": []}
        if shop_list.__contains__(shop_id):
            msg["goods"] = shop_list[shop_id]["goods"]
            msg["id"] = shop_id
            msg["name"] = shop_list[shop_id]['name']
        else:
            msg ['state'] = 'null'
        goods = msg
        if goods["state"] == "open":
            self.now_shop.setText(str(shop_id))
            self.load_goods(goods["goods"], goods["name"])
            return goods["goods"]
        elif goods["state"] == "close":
            # shop has closed
            self.msgwindow = MsgWindow("", "此店铺已被关闭")
            self.msgwindow.show()
        elif goods["state"] == "null":
            self.msgwindow = MsgWindow("", "此店铺不存在")
            self.msgwindow.show()

    def back_list(self):
        self.now_shop_head.setHidden(True)
        self.now_shop.setHidden(True)
        self.back_shoplist.setHidden(True)
        self.enter_shop_1.setHidden(False)
        self.enter_shop_2.setHidden(False)
        self.enter_shop_3.setHidden(False)
        self.enter_shop_4.setHidden(False)
        self.enter_shop_5.setHidden(False)
        self.now_shop.setText("")
        shop = self.getshop()
        self.loadshop(shop)

    def get_custom(self):

        data1={}
        id = self.now_shop.text()
        msg = {}

        if shop_visit.__contains__(id):
            msg[id] = shop_visit[id]
        else:
            msg[id] = []
        data1['id'] = self.now_shop.text()
        data1['custom'] = msg[self.now_shop.text()]
        self.recodwindow = RecordingBoxWindow("custom", data1)
        self.recodwindow.show()

    def get_user_all(self):
        data = []
        for key in user_infomation:
            m={}
            m['id'] = str(user_infomation[key]['user_id'])
            m['name'] = key
            if login_info.__contains__(key) == False:
                m['state'] = False
            else:
                m['state'] = login_info[key]['state']
            if user_infomation[key]['shop'] == 0:
                m['shop'] = "无"
            elif shop_list[str(user_infomation[key]['shop'])]['state'] == "open":
                m['shop'] = "有"
            else:
                m['shop'] = "已被关闭"
            data.append(m)
        self.info_window = RecordingBoxWindow('user',data)
        self.info_window.show()

    def add_user(self):
        self.input1_window = Server_InputWindow('add_user')
        self.input1_window.show()

    def add_shop(self):
        self.input2_window = Server_InputWindow('add_shop')
        self.input2_window.show()

    def close_shop(self):
        self.input3_window = Server_InputWindow('close_shop')
        self.input3_window.show()

    def send_all(self):
        self.input4_window = Server_InputWindow('send_all')
        self.input4_window.show()

    def send(self):
        self.input5_window = Server_InputWindow('send')
        self.input5_window.show()

    def update(self):
        if self.shop_name_head.text() == "店铺名":
            print('1')
            shops = self.getshop()
            self.loadshop(shops)
        else:
            self.enter_shop_request("6")
class MsgWindow(QtWidgets.QWidget):
    def __init__(self,m1,m2):
        super().__init__()
        self.setWindowTitle(m1)
        QMessageBox.information(self, m1, m2, QMessageBox.Yes)
