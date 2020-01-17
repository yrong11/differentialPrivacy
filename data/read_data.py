# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from collections import Counter

from matplotlib import ticker
from matplotlib.ticker import MultipleLocator

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取csv
csv_data = pd.read_csv('foo.csv')  # 读取训练数据
result_keep = pd.value_counts(csv_data['value'],False)
result = result_keep.sort_index()

#创建子图
fig, axs = plt.subplots(2)
result.plot.bar()
# axs.xaxis.set_major_locator(MultipleLocator(10))
# plt.show()

# print result

data = csv_data['value'].get_values()
bins = np.arange(start=min(data), stop = max(data) + 1)
# fig, axs = plt.subplots(1)
sns.distplot(data, bins=bins, ax=axs[0],hist_kws={'ec': "black"})
axs[0].set_title("Count Mean Sketch ")
plt.show()

