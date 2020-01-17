import csv
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg

true = list()
est = list()
with open("../_tmp/true_counts.csv", 'rb') as myFile:
    csv_out = csv.reader(myFile)

    for row in csv_out:
        for i in row:
            true.append(int(i))

with open("../_tmp/est_counts.csv", 'rb') as f:
    csv_out1 = csv.reader(f)
    for row in csv_out1:
        for i in row:
            est.append(float(i))

# -------------------- Calculating Error --------------------
a_true = np.array(true)
a_est = np.array(est)
relative_error = np.average(np.abs(a_true - a_est) / a_true, axis=0)
average_error = np.average(np.abs(a_true-a_est),axis=0)
log("relative error is: %s" %relative_error)
log("average_error is: %s"  %average_error)

plt.bar(range(1,true.__len__()+1),true, color ="#56B4E9")
plt.bar(range(1,est.__len__()+1), est, color = "#E69F00")
plt.savefig("test.png")
plt.show()
