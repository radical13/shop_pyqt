from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from ui_shoplist import *
from socket import *
import json

class ShoplistWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ShoplistWindow, self).__init__(parent)
        self.setupUi(self)
        shops = self.getshop()
        self.loadshop(shops)




    def getshop(self):
        host = '118.89.178.152'
        port = 60002
        s = socket(AF_INET,SOCK_DGRAM)
        if s.connect((host, port)) == 0:
            return
        while True:
            s.sendall(b"hello")
            try:
                data = s.recv(1024)
            except IOError:
                break
            shops = json.loads(data)
            if data:
                return shops
                break
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

    def loadshop(self,data):
        #load the first five shops
        
        for i in range(1,6):
            method = "modify_shoplist"+str(i)
            key = list(data.keys())[i-1]
            getattr(self,method)(key,data[key]["name"],data[key]["owner"])

