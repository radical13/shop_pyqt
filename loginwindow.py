from socket import *

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from ui_mainwindow import *
import json
import hashlib


class Loginwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Loginwindow, self).__init__(parent)
        self.setupUi(self)

        self.loginbutton.clicked.connect(self.send_login_info)


    def send_login_info(self):
        _translate = QtCore.QCoreApplication.translate
        user_id = self.id_text.text()
        user_pw = self.pw_text.text()
        if user_id == "":
            self.id_text.setPlaceholderText(_translate("MainWindow", "请输入正确的账户名/手机号"))
            return
        if user_pw == "":
            self.pw_text.setPlaceholderText(_translate("MainWindow", "请输入密码"))
            return
        pw_m = hashlib.md5()
        pw_m.update(user_pw.encode("utf-8"))
        user_pw_md5 = pw_m.hexdigest()
        host = '118.89.178.152'
        port = 60000
        info_socket = socket(AF_INET, SOCK_DGRAM)
        info = [{'id': user_id, 'pw': user_pw_md5}]
        message = json.dumps(info)
        if info_socket.connect((host, port)) == 0:
            self.login_state_2.setText("网络错误，请重试！")
            return
        while True:
            info_socket.sendall(message.encode(encoding='utf-8'))
            data = info_socket.recv(1024)
            if data != "":
                print(data)
                break
        info_socket.close()
