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
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.ui.widget.setBackground('w')
        self.ui.widget.showGrid(x=True, y=True)
        self.ui.widget_2.setBackground('w')
        self.ui.widget_2.showGrid(x=True, y=True)
        self.ui.AddButton.clicked.connect(self.add_line)
        self.ui.ExitButton.clicked.connect(self.close)
    def add_line(self):
        current_row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(current_row_count)

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())