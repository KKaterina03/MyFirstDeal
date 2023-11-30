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
        self.transistionMatrix = np.zeros((states_count, states_count))
    def draw_plot(self):


    def solve(self):
