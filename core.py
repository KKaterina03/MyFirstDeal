import numpy as np
#Итак, решатель всего этог

class calcCore():
    # Мы скормили ему матрицы в главном файле вот они тут выглядят как RM RMI TM
    def __init__(self, RM, RM2, RM3, RM4, TM):
        #Они будут как атрибуты объектра (хранится внутри решателя проще говоря)
        self.rang_matrix = RM
        self.transition_matrix = TM
        self.rang_matrix_2 = RM2
        self.rang_matrix_3 = RM3
        self.rang_matrix_4 = RM4
        #Размер нащих матриц а они все N*N | N = количество стостоянии
        self.N = len(RM)
        #Суммируем стрки по главной диагоняли в матрице переходов
        for i in range(len(self.transition_matrix)):
            self.transition_matrix[i,i] = -sum(self.transition_matrix[i])

    #Система диф уравнении которые прописаны точь в точь как в статье
    def equals(self,  arg):
        r = self.rang_matrix
        a = self.transition_matrix
        dV = np.zeros(self.N)
        for i in range(self.N):
            A = 0
            B = 0
            for j in range(self.N):
                if j != i:
                    A += a[i][j] * r[i][j]
                B += a[i][j] * arg[j]

            dV[i] = r[i][i] + A + B

        return dV

    # Система диф уравнении но уже для другой матрицы переходов
    def equals2(self,  arg):
        r = self.rang_matrix_2
        a = self.transition_matrix
        dV = np.zeros(self.N)
        for i in range(self.N):
            A = 0
            B = 0
            for j in range(self.N):
                if j != i:
                    A += a[i][j] * r[i][j]
                B += a[i][j] * arg[j]

            dV[i] = r[i][i] + A + B
        return dV

    def equals3(self, arg):
        r = self.rang_matrix_3
        a = self.transition_matrix
        dV = np.zeros(self.N)
        for i in range(self.N):
            A = 0
            B = 0
            for j in range(self.N):
                if j != i:
                    A += a[i][j] * r[i][j]
                B += a[i][j] * arg[j]

            dV[i] = r[i][i] + A + B
        return dV


    #Интегратор
    def solve(self):
        #Вектор значении которые интегрируются V = (0,0,0,...,0)
        V = np.zeros(self.N)
        time = 0
        #Шаг интегрирования
        h = 0.001;

        #Массивы результатов пока пустые
        res = list()
        res2 = list()
        timeL = list()

        #метод рунге кутты (о нём в википедии)
        while time < 5:
            k1 = self.equals(V)
            k2 = self.equals(V + k1 * h / 2)
            k3 = self.equals(V + k2 * h / 2)
            k4 = self.equals(V + k3 * h)

            V += (k1 + 2*k2 + 2*k3 + k4) * h / 6

            time += h
            #Каждый щаг заполняем массив данных
            res.append(V[0])
            timeL.append(time)

        #По новой для другой ситемы ДУ
        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals(V)
            k2 = self.equals2(V + k1 * h / 2)
            k3 = self.equals2(V + k2 * h / 2)
            k4 = self.equals2(V + k3 * h)

            V += (k1 + 2*k2 + 2*k3 + k4) * h / 6
            time += h
            res2.append(sum(V[2:-1]))
            timeL.append(time)
        #Выдаём результаты в main.py  дальше их в графики
        return timeL, res, res2
