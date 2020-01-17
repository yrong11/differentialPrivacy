import numpy as np
import math

class ClientMRR:
    def __init__(self, epsilon, k):
        self.epsilon = epsilon
        self.k = k
        self.denominator = math.exp(epsilon)+k-1
        self.p = math.exp(epsilon)/self.denominator
        self.q = 1/self.denominator
        self.matrix = np.ones([k,k])/self.denominator
        for i in range(k):
            self.matrix[i][i] = self.p



    def __privatise(self, data):
        pri_value = np.random.choice(a=self.k, size=1, replace=False,p=self.matrix[data])+1
        return pri_value

    def client_mrr(self, data):
        mrr_value = self.__privatise(data)
        return int(mrr_value)



