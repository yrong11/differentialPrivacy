# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取csv
csv_data = pd.read_csv('est_report.csv')  # 读取训练数据

#创建子图
fig, axs = plt.subplots(2)
# result.plot.bar()
# axs.xaxis.set_major_locator(MultipleLocator(10))
# plt.show()

# print result

result_keep1 = pd.value_counts(csv_data['est_value'],False)
result1 = result_keep1.sort_index()


result1.plot.bar()
plt.show()

