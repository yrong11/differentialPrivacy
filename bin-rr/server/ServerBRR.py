class ServerBRR:
    def __init__(self, N, k, epsilon, p,q):
        self.p = float(p)
        self.q = float(q)
        self.k = int(k)
        self.N = int(N)
        self.epsilon = float(epsilon)

    def estimate_freq(self, data_counts):
        est_fre = (data_counts-self.N*self.q)/(self.p-self.q)
        return est_fre