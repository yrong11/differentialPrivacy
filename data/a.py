# coding=utf-8
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

from matplotlib import ticker
from matplotlib.ticker import MultipleLocator

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取csv
csv_data = pd.read_csv('foo.csv',usecols=[2])  # 读取训练数据

result = pd.value_counts(csv_data['value'],False)
result = result.sort_index()
print result


