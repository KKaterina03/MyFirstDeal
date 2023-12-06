import sys
import csv
import numpy as np
from PyQt5 import QtWidgets, QtCore
from myform import Ui_MainWindow
from core import calcCore
import pyqtgraph as pg
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_table()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.ui.widget.setBackground('w')
        self.ui.widget.showGrid(x=True, y=True)
        self.ui.widget_2.setBackground('w')
        self.ui.widget_2.showGrid(x=True, y=True)
        self.ui.AddButton.clicked.connect(self.add_line)
        self.ui.CalcButton.clicked.connect(self.read_data)
        self.ui.ExitButton.clicked.connect(self.close)
    def load_table(self):
        data = np.genfromtxt('data1.csv', delimiter=';')
        l = 0
        for line in data:
            current_row_count = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(current_row_count)
            for i in range(len(line)):
                if (i == 0) or (i == 1):
                    var = round(data[l,i])
                    item = QtWidgets.QTableWidgetItem(str(var))
                else:
                    item = QtWidgets.QTableWidgetItem(str(data[l, i]))
                self.ui.tableWidget_2.setItem(l,i, item)
            l+=1

        data = np.genfromtxt('data2.csv', delimiter=';')
        l = 0
        for line in data:
            current_row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(current_row_count)
            for i in range(len(line)):
                if i == 0:
                    var = round(data[l, i])
                    item = QtWidgets.QTableWidgetItem(str(var))
                else:
                    item = QtWidgets.QTableWidgetItem(str(data[l, i]))
                self.ui.tableWidget.setItem(l, i, item)
            l += 1


    def add_line(self):
        current_row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(current_row_count)
    def read_data(self):
        demand = float(self.ui.lineEdit.text())
        states = self.ui.tableWidget.rowCount()
        t_count =   self.ui.tableWidget_2.rowCount()
        rang_matrix = np.zeros((states, states))
        transition_matrix = np.zeros((states, states))
        for i in range(states):
            rang_matrix[i,i] =  (demand - float(self.ui.tableWidget.item(i, 1).text())) > 0

        for n in range(t_count):
            i = int(self.ui.tableWidget_2.item(n, 0).text())
            j = int(self.ui.tableWidget_2.item(n, 1).text())
            lam = float(self.ui.tableWidget_2.item(n, 2).text())
            mu = float(self.ui.tableWidget_2.item(n, 3).text())

            transition_matrix[i,j] = lam
            transition_matrix[j, i] = mu


        core = calcCore(rang_matrix, transition_matrix)
        
        t, res, res2 = core.solve()
        pen = pg.mkPen(color=(0, 0, 0), width=2)
        self.ui.widget.plotItem.plot(t, res, pen=pen)
        self.ui.widget_2.plotItem.plot(t, res2, pen=pen)

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())