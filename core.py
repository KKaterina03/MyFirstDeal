import numpy as np

class calcCore():

    def __init__(self, l1, l2, l3, var, mode):
        print(l1)
        print(l2)
        print(l3)
        print(var)
        print(mode)
        states_count = len(l1)
        print(states_count)

    def gen_transition_matrix(self, l1, l2):
        Matrix = np.zeros((9, 9))


    def solve(self):
        x = np.linspace(0,100,1000)
        y = 0.1*x+np.sin(x)
        y1 = 10*np.exp(-0.05*x)*(np.exp(0.05*x)-1)

        return x, y, y1
