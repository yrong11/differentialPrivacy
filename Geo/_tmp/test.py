import numpy as np
from scipy.linalg import solve
p_matrix = np.loadtxt(open('p_matrix.csv', "rb"), delimiter=",", skiprows=0)
# print p_matrix.T
counts = np.loadtxt(open('case_counts.csv', "rb"), delimiter=",", skiprows=0)
true_counts =np.loadtxt(open('true_counts.csv', "rb"), delimiter=",", skiprows=0)
# x = solve(p_matrix,counts)
n = 0
for i in range(1000):
    a =np.random.choice(a=20,size=int(true_counts[1]),replace=True,p = p_matrix[1])
    # print a
    sum = 0
    # print true_counts[1]
    # print p_matrix[1]
    for i,val in enumerate(a):
        if val ==1:
           sum += 1
    n += sum
print n/1000
print true_counts
c=np.dot(true_counts,p_matrix)
print c
print np.dot(c,np.matrix(p_matrix).I)# print sum