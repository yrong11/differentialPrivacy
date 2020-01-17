import numpy as np
a = np.array([101, 88, 69, 50,12,9, 5, 2])
epsilon = 3
k = a.__len__()
dist = np.array(a)
p = np.zeros([k, k])
for i in range(k):
    p[i:i+1] = np.abs(dist - dist[i])
p_normed = p/(p.max(axis=0)-p.min(axis=0))
d_matrix = p_normed

p_matrix = np.exp(-epsilon * d_matrix)
p_sum = np.sum(p_matrix, axis=1)
for i in range(k):
    p_matrix[i:i + 1] = p_matrix[i:i + 1] / p_sum[i]
MI = np.matrix(p_matrix).I


m =p_matrix
mi = MI
pp = np.dot(p,m)
p = a*1.0/a.sum()
print m
client = np.random.choice(a=k, size=100, replace=True, p=p).tolist()
print client
krr = list()
for val in client:
    krr_value = int(np.random.choice(a=k, size=1, replace=False, p=m[val]))
    krr.append(krr_value)
print krr
# val_0 = 0
# val_1 = 0
# val_2 = 0
# for val in krr:
#     if(val == 0):
#         val_0 += 1
#     if (val == 1):
#         val_1 += 1
#     if (val == 2):
#         val_2 += 1
# krr_num = np.array([val_0, val_1, val_2])
# print np.dot(krr_num, mi)