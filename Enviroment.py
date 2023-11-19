import numpy as np



class Enviroment():
    def reset(self):
        #Q_table for 4 states and 4 actions
        self.Q_table = np.random.uniform((4,4))
        #Transition marix(4 * 4)
        self.threshold = 300
        self.Time = 0
        self.state = 3

    def step(self, action):
        if action == 2:
            print("selected action 2")
        elif action == 1:
            print("selected action 1")
        elif action >= 0:
            print("You are allowed to party")
