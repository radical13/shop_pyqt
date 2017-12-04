from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from ui_shoplist import *


class ShoplistWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ShoplistWindow, self).__init__(parent)
        self.setupUi(self)
