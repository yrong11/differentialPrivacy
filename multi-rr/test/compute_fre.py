import sys
import csv
sys.path.append('../server/')
from ServerMRR import ServerMRR
import time
import pandas as pd


def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg


def est_kind(N, params, case_report, case_counts, est_counts, true_counts):
    server = None
    with open(params, 'rb') as f:
        csv_in = csv.reader(f)
        for i, row in enumerate(csv_in):
            if i == 1:
                server = ServerMRR(*row)
    csv_report = pd.read_csv(case_report)
    true_value_counts = pd.value_counts(csv_report['true_value'], False).sort_index()

    est_result = list()
    with open(true_counts, 'wb') as myFile:
        csv_out = csv.writer(myFile)
        csv_out.writerow(true_value_counts.values)
    with open(case_counts, 'rb') as myFile:
        csv_in = csv.reader(myFile)
        with open(est_counts, 'wb') as myFile:
            csv_out = csv.writer(myFile)
            for i, row in enumerate(csv_in):
                if i == 0:
                    for i in row:
                        est_result.append(server.estimate_freq(int(i)))
            csv_out.writerow(est_result)




def main(N, params,args):
    if params== None or args == None:
        raise RuntimeError('Usage: compute_fre.py <params file>')
    est_kind(N, params, args[0], args[1], args[2], args[3])


if __name__ == "__main__":
    N = 10000
    params = "../_tmp/params.csv"
    args = [None]*4
    args[0] = '../_tmp/case_report.csv'
    args[1] = '../_tmp/case_counts.csv'
    args[2] = '../_tmp/est_counts.csv'
    args[3] = '../_tmp/true_counts.csv'
    try:
        main(N, params, args)
    except RuntimeError, e:
        log('mrr_sim.py: FATAL: %s', e)
