import numpy as np
import pandas as pd
from scipy.linalg import solve
p_matrix = np.loadtxt(open('p_matrix.csv', "rb"), delimiter=",", skiprows=0)
# print p_matrix.T
counts = np.loadtxt(open('case_counts.csv', "rb"), delimiter=",", skiprows=0)
true_counts =np.loadtxt(open('true_counts.csv', "rb"), delimiter=",", skiprows=0)
# x = solve(p_matrix,counts)
n = 0
print true_counts
# for i in range(1000):
#     a =np.random.choice(a=10,size=int(true_counts[1]),replace=True,p = p_matrix[1])
#     # print a
#     sum = 0
#     # print true_counts[1]
#     # print p_matrix[1]
#     for i,val in enumerate(a):
#         if val ==1:
#            sum += 1
#     n += sum
# print n/1000

a0 =np.random.choice(a=10,size=int(true_counts[0]),replace=True,p = p_matrix[0])
a1 =np.random.choice(a=10,size=int(true_counts[1]),replace=True,p = p_matrix[1])
aa =pd.value_counts(a0,False).sort_index()
print p_matrix[1]
print aa
print true_counts[0]*p_matrix[0]
print true_counts[1]*p_matrix[1]
aaa =np.dot(true_counts,p_matrix)
print '---------------------'
print aaa
print true_counts
print np.dot(aaa, np.matrix(p_matrix).I)
h = np.array([2522,2944,4017,9761,9297,9807,3874,3027,2468,2282])
print np.dot(h, np.matrix(p_matrix).I)

print '===================='
print np.matrix(p_matrix).I