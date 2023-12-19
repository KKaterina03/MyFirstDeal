#системные пакеты
import sys
#Библтотека линейной алгебры и прочей математики
import numpy as np
#Модули для Qt (интерфейс и так далее)
from PyQt5 import QtWidgets, QtCore, QtGui
#интерфейс который конвертируется из XML в PY
from myform import Ui_MainWindow
#Ядро вычисленнй где прописаны все формулы
from core import calcCore
#Библиотека для графиков
import pyqtgraph as pg

#Объявление и определение Класса приложения (ООП-короче)
class MyWindow(QtWidgets.QMainWindow):

    #Контруктор класса
    def __init__(self):
        # Фича с наследованием из парадигмы ООП
        super(MyWindow,self).__init__()
        #ui - user inteface
        self.ui = Ui_MainWindow()
        #Загрузка ui
        self.ui.setupUi(self)
        #Загрузка таблицы (функция описана ниже)
        self.load_table()
        #Убирание рамок
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        #Белый фон графика 1
        self.ui.widget.setBackground('w')
        #Сетка на графике 1
        self.ui.widget.showGrid(x=True, y=True)
        #Аналогично для второго графика
        self.ui.widget_2.setBackground('w')
        self.ui.widget_2.showGrid(x=True, y=True)

        #Вот это всё настройки каддой колонки в кажодй таблице
        header = self.ui.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        header2 = self.ui.tableWidget.horizontalHeader()
        header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header2.setStretchLastSection(True)

        #Обработка 3 событии: 3 кнопки
        self.ui.AddButton.clicked.connect(self.add_line) #добавить состояние
        self.ui.CalcButton.clicked.connect(self.read_data) #Это препроцессинг о нём ниже
        self.ui.ExitButton.clicked.connect(self.close) #Нуу "Exit" looks Exciting

     #Тот самый load table который дёргался выше. Он грузит данные из csv файлов в ui
    def load_table(self):
        #Загнали эту таблицу как набор чисеел прямо из файла
        data = np.genfromtxt('data1.csv', delimiter=';')
        #Порядковый номер строки
        l = 0
        #В каждой строчке загнанной таблицы
        for line in data:
            #Количество строк в ui-таблице
            current_row_count = self.ui.tableWidget_2.rowCount()
            #current_row_count - порядковый номер последнй строки
            #И под неё нужно вставить новую
            self.ui.tableWidget_2.insertRow(current_row_count)

            #Тут i-порядковый номер столбца
            for i in range(len(line)):
                #Если это первый или второй столбец
                if (i == 0) or (i == 1):
                    #Округляем Float в Int (Состояние это целочисленная величина)
                    var = round(data[l,i])
                    #Конфвертируем в QT формат Item
                    item = QtWidgets.QTableWidgetItem(str(var))
                else:
                    #Ну или просто не огругляем
                    item = QtWidgets.QTableWidgetItem(str(data[l, i]))
                #Вставляем этлемент
                self.ui.tableWidget_2.setItem(l,i, item)
            #Переход на порядковый номер следующей строчки
            l+=1

        #аналогично для другой таблицы
        #Импортировали
        data = np.genfromtxt('data2.csv', delimiter=';')
        #Обнулили счётчик так как таблица новая
        l = 0
        #Всё останое по той же логике
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

    #Добавление строки по кнопке
    #Алгортим тот же
    def add_line(self):
        current_row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(current_row_count)

    #Препроцессинг
    def read_data(self):
        # это спрос и мы его из текста переводим во float
        demand = float(self.ui.lineEdit.text())
        #Количество сотоянии = количествустрок во 2 Таблице
        states = self.ui.tableWidget.rowCount()
        #Количество переходов
        t_count =   self.ui.tableWidget_2.rowCount()
        #Матрица вознаграждении (пока из нулей) размером states*states
        rang_matrix = np.zeros((states, states))
        #аьрица переходов аналогично
        transition_matrix = np.zeros((states, states))
        #Вторая матрица вознагражении для второго расчёта
        rang_matrix_inv = np.zeros((states, states))

        #Таак тут пробегаемся по таблице и смотрим овзнаграждение за будущие переходы
        for i in range(states):
            for j in range(states):
                # cj,bhftv gfhs gtht[jljd
                i = int(self.ui.tableWidget.item(i, 0).text())
                j = int(self.ui.tableWidget.item(j, 0).text())
                #Оцениваем наградуд ля кажого перехода
                value_1 = demand - float(self.ui.tableWidget.item(i, 1).text())
                value_2 = demand - float(self.ui.tableWidget.item(j, 1).text())

                #По условию загоняем в матрицу возганражении
                if (value_1 > 0) and (value_2 <= 0):
                    rang_matrix_inv[i,j] = 1


        #Ну тут просто по главной диагоняли проходим и пишем больше или меньше
        for i in range(states):
            #Функция Хевисайда
            rang_matrix[i,i] = (demand - float(self.ui.tableWidget.item(i, 1).text())) > 0


        #Собираем переходы из таблицы перехожлв
        for n in range(t_count):
            i = int(self.ui.tableWidget_2.item(n, 0).text())
            j = int(self.ui.tableWidget_2.item(n, 1).text())
            lam = float(self.ui.tableWidget_2.item(n, 2).text())
            mu = float(self.ui.tableWidget_2.item(n, 3).text())

            #Далее  вот таким хитрым образом раскидываем мю и лямбду
            transition_matrix[i,j] = lam
            transition_matrix[j, i] = mu

        #Инициализируем решатель и кидаем ему наши матрицы
        core = calcCore(rang_matrix, rang_matrix_inv, transition_matrix)

        #Достаём массивы значении при расчёте
        t, res, res2 = core.solve()
        #Тут настройка пера для графика
        pen = pg.mkPen(color=(0, 0, 0), width=2)

        #Рисуем графики
        self.ui.widget.plotItem.plot(t, res, pen=pen)
        self.ui.widget_2.plotItem.plot(t, res2, pen=pen)

#А тут точка входа в программу
app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
#ну и выход из неё
sys.exit(app.exec())