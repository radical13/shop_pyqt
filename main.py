# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from loginwindow import Loginwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Loginwindow()
    login_window.show()
    sys.exit(app.exec_())