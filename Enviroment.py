import numpy as np


class Enviroment():
    def reset(self):
        #Q_table for 4 states and 4 actions
        self.Q_table = np.random.uniform((4,4))
        #Transition marix(4 * 4)
        self.transotion_matrix = np.zeros((4,4))
        self.transotion_matrix[0,0] = -446.9
        self.transotion_matrix[1,1] = -742.8
        self.transotion_matrix[2,2] = -2091.0
        self.transotion_matrix[3,3] = -(7.01+2.63+13.14)
        print(self.transotion_matrix)
        #reward_matrix(also 4*4)
        self.reward_matrix = np.zeros((4,4))
