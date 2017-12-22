from socket import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_mainwindow import *
from shoplistwindow import ShoplistWindow
import json
import hashlib


class Loginwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Loginwindow, self).__init__(parent)
        self.setupUi(self)

        self.id_text.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.pw_text.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.loginbutton.clicked.connect(self.send_login_info)
        icon_see = QIcon("img/see.png")
        self.see_pw.setIcon(icon_see)
        self.see_pw.setIconSize(QSize(20,20))
        self.see_pw.show()
        self.see_pw.clicked.connect(self.seepw)

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
        host = '127.0.0.1'
        port = 62000
        info_socket = socket(AF_INET, SOCK_DGRAM)

        info = {"method":"login_check","id": user_id, "pw": user_pw_md5}
        message = json.dumps(info)
        if info_socket.connect((host, port)) == 0:
            pixmap = QPixmap("img/neterror.png")
            self.net_error.setPixmap(pixmap)
            return
        while True:
            info_socket.sendall(message.encode(encoding='utf-8'))
            try:
                data = info_socket.recv(1024)
            except IOError:
                pixmap = QPixmap("img/neterror.png")
                self.net_error.setPixmap(pixmap)
                break

            if data == b"SUCCESS":
                address = info_socket.getsockname()
                info_socket.close()
                self.shoplist_window = ShoplistWindow(user_id,address)
                self.close()
                self.shoplist_window.show()

                break

            if data == b"FAIL":
                pixmap = QPixmap("img/wrong_pw.png")
                self.net_error.setPixmap(pixmap)
                break

            if data == b"NO_USER":
                pixmap = QPixmap("img/wrong_id.png")
                self.net_error.setPixmap(pixmap)
                break

        info_socket.close()

    def seepw(self):
        self.pw_text.setEchoMode(0)
