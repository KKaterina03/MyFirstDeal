import numpy as np

class calcCore():

    def __init__(self, RM, TM):
        self.rang_matrix = RM
        self.transition_matrix = TM
        self.N = len(RM)
        self.rang_matrix_inv = np.zeros((self.N,self.N))
        for i in range(len(self.transition_matrix)):
            self.transition_matrix[i,i] = -sum(self.transition_matrix[i])

        for i  in range(len(self.rang_matrix_inv)):
            self.rang_matrix_inv[i,i] = 1 - self.rang_matrix[i,i]


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

    def equals2(self,  arg):
        r = self.rang_matrix_inv
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




    def solve(self):

        V = np.zeros(self.N)
        time = 0
        h = 0.001;

        res = list()
        res2 = list()
        timeL = list()

        while time < 5:
            k1 = self.equals(V)
            k2 = self.equals(V + k1 * h / 2)
            k3 = self.equals(V + k2 * h / 2)
            k4 = self.equals(V + k3 * h)

            V += (k1 + 2*k2 + 2*k3 + k4) * h / 6
            time += h
            res.append(V.mean())
            timeL.append(time)

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
            res2.append(V.mean())
            timeL.append(time)

        return timeL, res, res2
