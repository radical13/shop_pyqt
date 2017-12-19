# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from loginwindow import Loginwindow
from shoplistwindow import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #login_window = Loginwindow()
    #login_window.show()
   # login_window.setFixedSize(login_window.width(),login_window.height())
    window = ShoplistWindow("hushiyang")
    window.show()

    sys.exit(app.exec_())

