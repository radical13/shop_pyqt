from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from ui_shoplist import *
from socket import *
import json
import threading

# a dic to store the message recived
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

class ShoplistWindow(QtWidgets.QWidget, Ui_Form):


    r_msg = []
    def __init__(self, user,address,parent=None):
        super(ShoplistWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.username.setText(user)
        shops = self.getshop()
        self.loadshop(shops)
        pixmap = QPixmap("img/logo.png")
        self.logo.setPixmap(pixmap)

        #listen msg
        thread_list=[]
        print (address)
        t = threading.Thread(target=self.listen_msg,args=(address,))
        t.setDaemon(True)
        t.start()


        #connect function
        self.exit.clicked.connect(self.exit_request)
        self.next_page.clicked.connect(self.to_next_page)
        self.last_page.clicked.connect(self.to_last_page)
        self.enter_shop_1.clicked.connect(lambda:self.enter_shop_request("1"))
        self.enter_shop_2.clicked.connect(lambda:self.enter_shop_request("2"))
        self.enter_shop_3.clicked.connect(lambda:self.enter_shop_request("3"))
        self.enter_shop_4.clicked.connect(lambda:self.enter_shop_request("4"))
        self.enter_shop_5.clicked.connect(lambda:self.enter_shop_request("5"))
        self.enter_shop.clicked.connect(lambda:self.enter_shop_request("0"))
        self.back_shoplist.clicked.connect(self.back_list)
        self.enter_my_shop.clicked.connect(self.enter_own_shop_request)
    def getshop(self):
        host = '118.89.178.152'
        port = 62000
        s = socket(AF_INET,SOCK_DGRAM)
        if s.connect((host, port)) == 0:
            return
        while True:
            info = {"method": "send_shoplist"}
            message = json.dumps(info)
            s.sendall(message.encode(encoding='utf-8'))
            try:
                data = s.recv(2048)
            except IOError:
                break
            shops = json.loads(data)
            if data:
                return shops
                break

    #modify the shop list
    def modify_shoplist1(self,id,name,owner):
        self.shop_id_1.setText(id)
        self.shop_name_1.setText(name)
        self.shop_owner_1.setText(owner)
    def modify_shoplist2(self,id,name,owner):
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

    #show function
    def loadshop(self,data):
        self.shop_name_head.setText("店铺名")
        self.shop_owner_head.setText("拥有者")
        self.page_2.setText("个店铺 当前是第")
        self.now_shop_head.setHidden(True)
        self.now_shop.setHidden(True)
        self.back_shoplist.setHidden(True)
        self.now_shop_name.setHidden(True)
        #load the first five shops

        for i in range(1,6):
            method = "modify_shoplist"+str(i)
            key = list(data.keys())[i-1]
            getattr(self,method)(key,data[key]["name"],data[key]["owner"])

        shopnum = data.__len__()
        if shopnum <=5:
            self.last_page.setHidden(True)
            self.next_page.setHidden(True)
            self.shop_num.setText(str(shopnum))
            self.page.setText("1")
        else:
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.shop_num.setText(str(shopnum))
            self.page.setText("1")
    def loadshop_range(self,r,data):
        for i in range(1, 6):
            method = "modify_shoplist" + str(i)
            key = list(data.keys())[5*(r - 1)+i - 1]
            getattr(self, method)(key, data[key]["name"], data[key]["owner"])
    def loadgood_range(self,r,data):
        if 5 * r >= len(data):
            for i in range(1, len(data) - 5*(r-1) + 1):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(data[5*(r - 1)+i - 1]["id"], data[5*(r - 1)+i - 1]["name"], data[5*(r - 1)+i - 1]["price"])
            for i in range(len(data) - 5*(r-1) + 1,6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)("","","")
        else:
            for i in range(1, 6):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(data[5*(r - 1)+i - 1]["id"], data[5*(r - 1)+i - 1]["name"], data[5*(r - 1)+i - 1]["price"])
    def exit_request(self):
        user_current = self.username.text()
        host = '118.89.178.152'
        port = 62000
        s = socket(AF_INET, SOCK_DGRAM)
        if s.connect((host, port)) == 0:
            return
        while True:
            info = {"method": "exit_request","user":user_current}
            message = json.dumps(info)
            s.sendall(message.encode(encoding='utf-8'))

            try:
                data = s.recv(1024)
            except IOError:
                break
            if data == b"0":
                self.close()
                break
            else:
                print("exit fail")
                return
    def to_next_page(self):
        state = self.shop_name_head.text()

        current = int(self.page.text())
        if state == "店铺名":
            shops = self.getshop()
        else:
            goods = self.enter_shop_request("6")

        if (current+1)*5<(int)(self.shop_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(False)
            self.page.setText(str(current+1))

            if state == "店铺名":
                self.loadshop_range(current+1,shops)
            else:
                self.loadgood_range(current+1,goods)
        elif (current+1)*5 >= (int)(self.shop_num.text()):
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current + 1))

            if state == "店铺名":
                self.loadshop_range(current+1,shops)
            else:
                self.loadgood_range(current + 1, goods)
    def to_last_page(self):
        state = self.shop_name_head.text()
        current = int(self.page.text())
        if state == "店铺名":
            shops = self.getshop()
        else:
            goods = self.enter_shop_request("6")
        if (current-1)==1:
            self.last_page.setHidden(True)
            self.next_page.setHidden(False)
            self.page.setText(str(current - 1))
            if  state =="店铺名":
                self.loadshop_range(current-1,shops)
            else:
                self.loadgood_range(current-1,goods)
        else:
            self.last_page.setHidden(False)
            self.next_page.setHidden(True)
            self.page.setText(str(current - 1))
            if  state == "店铺名":
                self.loadshop_range(current - 1, shops)
            else:
                self.loadgood_range(current - 1, goods)
    def load_goods(self,goods,sname):

        self.shop_name_head.setText("商品名")
        self.shop_owner_head.setText("价格")
        self.page_2.setText("个商品 当前是第")
        self.now_shop_head.setHidden(False)
        self.now_shop.setHidden(False)
        self.back_shoplist.setHidden(False)
        goodsnum = len(goods)
        self.now_shop_name.setHidden(False)
        self.now_shop_name.setText(sname)
        if goodsnum <5:
            for i in range(1, goodsnum + 1):
                method = "modify_shoplist" + str(i)
                getattr(self, method)(goods[i - 1]["id"], goods[i - 1]["name"], goods[i - 1]["price"])
            for i in range(goodsnum+1, 6):
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
    def enter_shop_request(self,num):

        id_dic={"1":self.shop_id_1.text(),
                "2":self.shop_id_2.text(),
                "3":self.shop_id_3.text(),
                "4": self.shop_id_4.text(),
                "5": self.shop_id_5.text(),
                "0":self.input_shop_id.text(),
                "6":self.now_shop.text()
                }
        shop_id = id_dic[num]
        info = {"method":"enter_shop","id":str(shop_id),"user":self.username.text()}
        host = '118.89.178.152'
        port = 62000
        s = socket(AF_INET, SOCK_DGRAM)
        if s.connect((host, port)) == 0:
            return
        while True:
            message = json.dumps(info)
            s.sendall(message.encode(encoding='utf-8'))
            try:
                data = s.recv(4096)
            except IOError:
                break

            if data:
                goods = json.loads(data)
                if goods["state"] == "open":
                    self.now_shop.setText(str(shop_id))
                    #self.now_shop_name.setText()
                    self.load_goods(goods["goods"],goods["name"])
                    return goods["goods"]
                    break
                elif goods["state"] == "close":
                    #shop has closed
                    break
                elif goods["state"] == "null":
                    #no this shop
                    break
            else:
                continue
    def enter_own_shop_request(self):
        info={"method":"enter_own_shop","user":self.username.text()}
        host = '118.89.178.152'
        port = 62000
        s = socket(AF_INET, SOCK_DGRAM)
        if s.connect((host, port)) == 0:
            return
        while True:
            message = json.dumps(info)
            s.sendall(message.encode(encoding='utf-8'))

            try:
                data = s.recv(1024)
            except IOError:
                break
            if data:
                goods = json.loads(data)
                if goods["state"] == "open":
                    self.now_shop.setText(goods["id"])
                    self.load_goods(goods["goods"],goods['name'])
                    return goods["goods"]
                    break
                elif goods["state"] == "close":
                    # shop has closed
                    break
                elif goods["state"] == "null":
                    # no this shop
                    break
            else:
                continue
    def back_list(self):
        self.now_shop_head.setHidden(True)
        self.now_shop.setHidden(True)
        self.back_shoplist.setHidden(True)
        host = '118.89.178.152'
        port = 62000
        s = socket(AF_INET, SOCK_DGRAM)
        info = {"method":"leave_shop","user":self.username.text(),"id":self.now_shop.text()}
        message = json.dumps(info)
        if s.connect((host, port)) == 0:
            return
        while True:
            s.sendall(message.encode(encoding='utf-8'))
            try:
                data = s.recv(4096)
            except IOError:
                break
            if data == b"0":
                shop = self.getshop()
                self.loadshop(shop)
                break
            else:
                print(data)
                break

    #recv message function
    def listen_msg(self,address):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(address)
        while True:
            data, address = s.recvfrom(1024)
            if not data:
                break
            data = json.loads(data)
            print (data)
            #data = byteify(data)
            self.r_msg.append(data)
            #some tips to tell the user