# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from serverwindow import ServerWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    server_window = ServerWindow()
    server_window.show()
    server_window.setFixedSize(server_window.width(),server_window.height())

    sys.exit(app.exec_())

