import sys
sys.path.append('../client/')
sys.path.append('../data/')
from ClientMRR import ClientMRR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from collections import Counter

from matplotlib import ticker
from matplotlib.ticker import MultipleLocator

csv_data = pd.read_csv('foo.csv')  # 读取训练数据
true_value = pd.value_counts(csv_data['value'],False).sort_index()

