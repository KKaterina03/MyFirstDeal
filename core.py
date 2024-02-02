import numpy as np
#Итак, решатель всего этого

class calcCore():
    # Матрицы из главного файла, они выглядят как RM RMI TM
    def __init__(self, RM, RM2, RM3, RM4, TM):
        #Они будут как атрибуты объектра (храниться внутри решателя)
        self.rang_matrix = RM
        self.transition_matrix = TM
        self.rang_matrix_2 = RM2
        self.rang_matrix_3 = RM3
        self.rang_matrix_4 = RM4


        #Размер нащих матриц N*N | N = количество стостоянии
        self.N = len(RM)
        upper = np.triu(TM, 1)

        print(upper)

    #Создание матрицы с мю в виде функции
    def gen_matrix(self, time):
        lower_tri = np.tril(self.transition_matrix, -1) * (0.2*pow(time,0.2) )
        upper_tri = np.triu(self.transition_matrix, 1)
        pretransition_matrix = lower_tri + upper_tri
        # Суммируем строки по главной диагоняли в матрице переходов
        for i in range(len(self.transition_matrix)):
            pretransition_matrix[i, i] = -sum(pretransition_matrix[i])
        return pretransition_matrix

    # Создание матрицы с мю константой
    def gen_matrix_const(self):
        pretransition_matrix = self.transition_matrix
        # Суммируем строки по главной диагонали в матрице переходов
        for i in range(len(self.transition_matrix)):
            pretransition_matrix[i, i] = -sum(pretransition_matrix[i])
        return pretransition_matrix


    #Система диф уравнений
    def equals(self,  arg):
        r = self.rang_matrix
        a = self.gen_matrix_const()
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

    #Система диф уравнении для других матриц переходов
    def equals2(self,  arg):
        r = self.rang_matrix_2

        a = self.gen_matrix_const()
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
        a = self.gen_matrix_const()
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

    def equals4(self, arg):
        r = self.rang_matrix_4
        a = self.gen_matrix_const()
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

    def equals11(self, t, arg):
        r = self.rang_matrix
        a = self.gen_matrix(t)
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

    def equals12(self, t, arg):
        r = self.rang_matrix_2
        a = self.gen_matrix(t)
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

    def equals13(self, t, arg):
        r = self.rang_matrix_3
        a = self.gen_matrix(t)
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


    def equals14(self, t, arg):
        r = self.rang_matrix_4
        a = self.gen_matrix(t)
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
        res3 = list()
        res4 = list()
        res11 = list()
        res12 = list()
        res13 = list()
        res14 = list()
        timeL = list()

        #метод Рунге Кутты
        while time < 5:
            k1 = self.equals(V)
            k2 = self.equals(V + k1 * h / 2)
            k3 = self.equals(V + k2 * h / 2)
            k4 = self.equals(V + k3 * h)

            V += (k1 + 2*k2 + 2*k3 + k4) * h / 6

            time += h
            #Каждый шаг заполняем массив данных
            res.append(np.mean(V))
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
            res2.append(np.mean(V))
            timeL.append(time)

        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals3(V)
            k2 = self.equals3(V + k1 * h / 2)
            k3 = self.equals3(V + k2 * h / 2)
            k4 = self.equals3(V + k3 * h)

            V += (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            time += h
            res3.append(np.mean(V))
            timeL.append(time)

        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals4(V)
            k2 = self.equals4(V + k1 * h / 2)
            k3 = self.equals4(V + k2 * h / 2)
            k4 = self.equals4(V + k3 * h)

            V += (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            time += h
            res4.append(np.mean(V))
            timeL.append(time)

        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals11(time, V)
            k2 = self.equals11(time + h/2, V + k1 * h / 2)
            k3 = self.equals11(time + h/2, V + k2 * h / 2)
            k4 = self.equals11(time + h, V + k3 * h)

            V += (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            time += h
            res11.append(np.mean(V))
            timeL.append(time)

        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals12(time, V)
            k2 = self.equals12(time + h / 2, V + k1 * h / 2)
            k3 = self.equals12(time + h / 2, V + k2 * h / 2)
            k4 = self.equals12(time + h, V + k3 * h)

            V += (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            time += h
            res12.append(np.mean(V))
            timeL.append(time)

        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals13(time, V)
            k2 = self.equals13(time + h / 2, V + k1 * h / 2)
            k3 = self.equals13(time + h / 2, V + k2 * h / 2)
            k4 = self.equals13(time + h, V + k3 * h)

            V += (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            time += h
            res13.append(np.mean(V))
            timeL.append(time)

        V = np.zeros(self.N)
        time = 0
        timeL.clear()
        while time < 5:
            k1 = self.equals11(time, V)
            k2 = self.equals11(time + h / 2, V + k1 * h / 2)
            k3 = self.equals11(time + h / 2, V + k2 * h / 2)
            k4 = self.equals11(time + h, V + k3 * h)

            V += (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
            time += h
            res14.append(np.mean(V))
            timeL.append(time)

        #Выдаём результаты в main.py  дальше их в графики
        return timeL, res, res2, res3, res4, res11, res12, res13, res14



