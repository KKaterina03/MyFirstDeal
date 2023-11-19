import matplotlib.pyplot as plt
import numpy as np



def failure_rates_func(t):
    lam_matrx = np.zeros((4, 4))
    lam_matrx[3,0] = 2.63
    lam_matrx[3,1] = 7.01+0.2189*pow(t,2)
    lam_matrx[3,2] = 13.14
    lam_matrx[0,3] = 446.9
    lam_matrx[1,3] = 742.9
    lam_matrx[2,3] = 2091.0

    lam_matrx[0,0] = -lam_matrx[0][3]
    lam_matrx[1,1] = -lam_matrx[1][3]
    lam_matrx[2,2] = -lam_matrx[2][3]
    lam_matrx[3,3] = -(lam_matrx[3][0] +  lam_matrx[3][1] + lam_matrx[3][2])
    return lam_matrx


def reward_func(t):
    reward_matrx = np.zeros((4, 4))
    reward_matrx[0,0] = 300
    reward_matrx[1,1] = 85
    return reward_matrx


V = np.zeros(4)
dV = np.zeros(4)
time = 0
h = 0.001;
res = list()
timeL = list()
while time < 5:
    res.append(np.mean(V))
    timeL.append(time)
    r = reward_func(time)
    a = failure_rates_func(time)
    for i in range(4):
        A = 0
        B = 0
        for j in range(4):
            A += a[i][j]*r[i][j]
            B += a[i][j]*V[j]
        dV[i] = r[i][i] + A + B
        print(dV)
    V += dV * h
    time += h

plt.plot(timeL,res)
plt.show()






