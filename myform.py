

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 717)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(50,50,50);")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 421, 81))
        self.groupBox.setStyleSheet("border: 1px solid;\n"
"border-color:  black;\n"
"color: black;;\n"
"background-color:  rgb(253,244,227);\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 30, 99, 16))
        self.radioButton_2.setStyleSheet("border: 0px solid;\n"
"border-color:  rgb(242, 141, 24);\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(210, 30, 101, 16))
        self.radioButton_3.setStyleSheet("border: 0px solid;\n"
"border-color:  rgb(242, 141, 24);\n"
"")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 291, 16))
        self.radioButton.setStyleSheet("border: none;\n"
"border-color:  rgb(242, 141, 24);\n"
"")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 140, 321, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 290, 441, 171))
        self.tableWidget.setStyleSheet("QHeaderView::section \n"
"{\n"
"    background-color:#30d5c8;\n"
"    color: black;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"background-color:   rgb(253,244,227);\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(530, 30, 551, 281))
        self.widget.setStyleSheet("border: 1px solid;\n"
"border-color:  white;\n"
"color: white;\n"
"background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = PlotWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(530, 380, 551, 281))
        self.widget_2.setStyleSheet("border: 1px solid;\n"
"border-color:  white;\n"
"color: white;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.CalcButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalcButton.setGeometry(QtCore.QRect(10, 520, 211, 41))
        self.CalcButton.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    color: white; \n"
"    background:  #30d5c8;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 15px;\n"
"    color: black; \n"
"    background: white;\n"
"    \n"
"}\n"
"")
        self.CalcButton.setObjectName("CalcButton")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(10, 470, 441, 41))
        self.AddButton.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    color: white; \n"
"    background:  #30d5c8;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 15px;\n"
"    color: black; \n"
"    background: white;\n"
"    \n"
"}\n"
"\n"
"")
        self.AddButton.setObjectName("AddButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 531, 721))
        self.label_2.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(230, 520, 221, 41))
        self.ExitButton.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    color: white; \n"
"    background:  #30d5c8;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 15px;\n"
"    color: black; \n"
"    background: white;\n"
"    \n"
"}\n"
"\n"
"")
        self.ExitButton.setObjectName("ExitButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, -10, 751, 811))
        self.label_3.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 136, 77, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 111, 31))
        self.label.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 181, 31))
        self.label_4.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 181, 31))
        self.label_5.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 181, 31))
        self.label_6.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_6.setObjectName("label_6")
        self.label_3.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.tableWidget.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.CalcButton.raise_()
        self.AddButton.raise_()
        self.ExitButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Сложность детали"))
        self.radioButton_2.setText(_translate("MainWindow", "Средняя"))
        self.radioButton_3.setText(_translate("MainWindow", "Сложная"))
        self.radioButton.setText(_translate("MainWindow", "Простая"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Состояние"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "λ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "μ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "g"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "идеальное"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "корректировка настроек инструмента"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "корректировка настроек оборудования"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "2"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.CalcButton.setText(_translate("MainWindow", "Рассчёт"))
        self.AddButton.setText(_translate("MainWindow", "Добавить состояние"))
        self.ExitButton.setText(_translate("MainWindow", "Выход"))
        self.lineEdit.setText(_translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "Постоянный спрос"))
        self.label_4.setText(_translate("MainWindow", "λ - "))
        self.label_5.setText(_translate("MainWindow", "μ - "))
        self.label_6.setText(_translate("MainWindow", "g - "))
from pyqtgraph import PlotWidget
