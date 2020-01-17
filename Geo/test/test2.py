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
b = np.array([5120,158,321,153,26,15,75,64])
after = np.dot(b,m)
sum = 0
for i in range(5120):
    num = int(np.random.choice(a=8,size=1,replace=True,p=m[0]))
    if num == 0:
       sum += 1
print sum
print after
print np.dot(after,mi)
