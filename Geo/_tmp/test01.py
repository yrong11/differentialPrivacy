import numpy as np
import pandas as pd
csv_data = pd.read_csv('case_report.csv')
p_matrix = np.loadtxt(open('p_matrix.csv', "rb"), delimiter=",", skiprows=0)
true_counts =np.loadtxt(open('true_counts.csv', "rb"), delimiter=",", skiprows=0)

est = list()
for i, row in csv_data.iterrows():
    if i ==0:
        continue
    true_value = row['true_value']
    geo_value = int(np.random.choice(a=10,size=1,replace=True,p=p_matrix[true_value-1]))+1
    est.append(geo_value)
aa =pd.value_counts(est,False).sort_index()
print aa
print np.dot(np.array(aa), np.matrix(p_matrix).I)

