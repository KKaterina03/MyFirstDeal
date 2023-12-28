# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myform.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1492, 800)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(50,50,50);")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(580, 120, 281, 331))
        self.tableWidget.setStyleSheet("QTableCornerButton::section {\n"
"    background-color: #30d5c8;\n"
"}\n"
"\n"
"QHeaderView::section \n"
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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(910, 40, 551, 281))
        self.widget.setStyleSheet("border: 1px solid;\n"
"border-color:  white;\n"
"color: white;\n"
"background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = PlotWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(910, 390, 551, 281))
        self.widget_2.setStyleSheet("border: 1px solid;\n"
"border-color:  white;\n"
"color: white;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.CalcButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalcButton.setGeometry(QtCore.QRect(570, 620, 321, 41))
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
        self.AddButton.setGeometry(QtCore.QRect(570, 570, 321, 41))
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
        self.label_2.setGeometry(QtCore.QRect(0, 0, 531, 801))
        self.label_2.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(570, 670, 321, 41))
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
        self.label_3.setGeometry(QtCore.QRect(370, -10, 1131, 811))
        self.label_3.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(700, 80, 77, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 74, 111, 31))
        self.label.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 460, 291, 31))
        self.label_4.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 490, 321, 31))
        self.label_5.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 520, 301, 31))
        self.label_6.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_6.setObjectName("label_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 541, 671))
        self.tableWidget_2.setStyleSheet("QTableCornerButton::section {\n"
"    background-color: #30d5c8;\n"
"}\n"
"\n"
"QHeaderView::section \n"
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
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(920, 330, 121, 16))
        self.label_7.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(920, 680, 121, 16))
        self.label_8.setStyleSheet("background-color:  rgb(253,244,227);")
        self.label_8.setObjectName("label_8")
        self.label_3.raise_()
        self.label_2.raise_()
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
        self.tableWidget_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Состояние"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "g"))
        self.CalcButton.setText(_translate("MainWindow", "Рассчёт"))
        self.AddButton.setText(_translate("MainWindow", "Добавить состояние"))
        self.ExitButton.setText(_translate("MainWindow", "Выход"))
        self.lineEdit.setText(_translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "Допустимое время"))
        self.label_4.setText(_translate("MainWindow", "λ - интенсивность возникновения риска"))
        self.label_5.setText(_translate("MainWindow", "μ - доля времени, необходимая на устранение риска"))
        self.label_6.setText(_translate("MainWindow", "g - время с учетом совершения риска"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Исх состояние"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новое состояние"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "λ"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "μ"))
        self.label_7.setText(_translate("MainWindow", "График 1"))
        self.label_8.setText(_translate("MainWindow", "График 2"))
from pyqtgraph import PlotWidget
