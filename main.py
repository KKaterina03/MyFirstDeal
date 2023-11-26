import sys
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from myform import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.prog)
    def prog(self):
        text = self.ui.lineEdit.text()
        self.ui.label.setText("Ага, " + text)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())