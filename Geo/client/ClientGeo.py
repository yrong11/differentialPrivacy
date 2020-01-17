import numpy as np
import pandas as pd
class ClientGeo:
    def __init__(self, epsilon, k):
        self.epsilon = epsilon
        self.k = k  #Number of points
        self.p_matrix = 0   #probability_matrix
        self.x = 0  #Original x coordinate
        self.y = 0  #Original y coordinate
        self.d_matrix = 0   #distance_matrix

    def create_matrix_from_point(self):
        """
        Generate probability matrix based on position coordinates
        :return:
        """

        #generate points
        samples_num = self.k
        t = np.random.random(size=samples_num) * 2 * np.pi
        x = np.cos(t)
        y = np.sin(t)
        i_set = np.arange(0, samples_num, 1)
        for i in i_set:
            len = np.sqrt(np.random.random())/2
            x[i] = x[i] * len
            y[i] = y[i] * len
        self.x = x
        self.y = y

        # generate the distance matrix
        dist = np.array(zip(x,y))
        dist = ((dist[:, np.newaxis, :] - dist[np.newaxis, :, :]) ** 2).T
        self.d_matrix = np.sqrt(dist[0:1]+dist[1:2]).reshape(self.k, self.k)

        #generate the probability matrix
        self.p_matrix = np.exp(-self.epsilon*self.d_matrix)
        p_sum = np.sum(self.p_matrix, axis=1)
        for i in range(self.k):
            self.p_matrix[i:i+1] = self.p_matrix[i:i+1]/p_sum[i]



    def create_matrix_from_distribution(self, dist):
        """
        Generate a probability matrix from a distribution
        :param dist:
        :return:
        """
        dist = np.array(dist)
        p = np.zeros([self.k, self.k])
        for i in range(self.k):
            p[i:i+1] = np.abs(dist - dist[i])
        p_normed = p/(p.max(axis=0)-p.min(axis=0))
        self.d_matrix = p_normed

        self.p_matrix = np.exp(-self.epsilon * self.d_matrix)
        p_sum = np.sum(self.p_matrix, axis=1)
        for i in range(self.k):
            self.p_matrix[i:i + 1] = self.p_matrix[i:i + 1] / p_sum[i]

    def create_matrix(self, use_point=True, dist=None):
        """
        If use_point = True, a probability matrix is generated based on the location points,
        otherwise it is generated based on the distribution.
        :param use_point:
        :param dist:
        :return:
        """
        if use_point:
            self.create_matrix_from_point()
        else:
            self.create_matrix_from_distribution(dist)


    def client_geo(self, data):
        geo_value = np.random.choice(a=self.k, size=1, replace=False, p=self.p_matrix[data])+1
        return int(geo_value)


# client = ClientGeo(3,20)
# client.create_matrix_from_point()
# # print client.p_matrix
# sum = 0
# for i in range(40000):
#     if client.client_mrr(1)==1:
#         sum+=1
# print sum

# client = ClientGeo(3, 10)
# csv_data = pd.read_csv('../../data/foo.csv')
# result = pd.value_counts(csv_data['value'], False).sort_index()
# client.create_matrix(use_point=False,dist=result.values)
# print client.d_matrix
# print client.p_matrix
