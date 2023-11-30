import sys
from PyQt5 import QtWidgets, QtCore
from myform import Ui_MainWindow
from core import calcCore

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
        self.ui.CalcButton.clicked.connect(self.read_data)
        self.ui.ExitButton.clicked.connect(self.close)

    def add_line(self):
        current_row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(current_row_count)
    def read_data(self):
        demand = float(self.ui.lineEdit.text())
        current_row_count = self.ui.tableWidget.rowCount()
        mode = 1
        if self.ui.radioButton_2.isChecked() == True:
            mode = 2
        if self.ui.radioButton_3.isChecked() ==True:
            mode =3
        lam_list = list()
        mu_list = list()
        g_list = list()
        for i in range(current_row_count):
            g = self.ui.tableWidget.item(i, 3).text()
            g_list.append(float(g))
            mu = self.ui.tableWidget.item(i, 2).text()
            mu_list.append(float(mu))
            lam = self.ui.tableWidget.item(i, 1).text()
            lam_list.append(float(lam))

        core = calcCore(lam_list, mu_list, g_list, demand, mode)

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())