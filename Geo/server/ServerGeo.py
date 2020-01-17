import numpy as np
class ServerGeo:
    def __init__(self, N, k, epsilon, p_matrix=None):
        self.k = int(k)
        self.N = int(N)
        self.epsilon = float(epsilon)
        self.p_matrix = p_matrix
        self.p_matrix_I = None

    def update_p_matrix(self, p_matrix):
        self.p_matrix = p_matrix
        self.p_matrix_I = np.linalg.pinv(self.p_matrix)

    def estimate_freq(self, data):
        est_value = np.random.choice(a=self.k, size=1, replace=False, p=self.p_matrix[data]) + 1
        return int(est_value)

# my_matrix = np.loadtxt(open("../_tmp/p_matrix.csv", "rb"), delimiter = ",", skiprows = 0)
# server = ServerGeo(40000, 30, 3)
# server.update_p_matrix(my_matrix)
# a = 100*server.p_matrix_I[0:1].tolist()
# est = [0 for i in range(server.k)]
#
# print a
