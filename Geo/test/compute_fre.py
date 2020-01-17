import sys
import csv
sys.path.append('../server/')
from ServerGeo import ServerGeo
import time
import pandas as pd
import numpy as np


def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg


def est_kind(params, p_matrix_filename, case_counts_filename, est_counts_f):
    #initialization serverGeo
    server = None
    with open(params, 'rb') as f:
        csv_in = csv.reader(f)
        for i, row in enumerate(csv_in):
            if i == 1:
                server = ServerGeo(*row)
    p_matrix = np.loadtxt(open(p_matrix_filename, "rb"), delimiter=",", skiprows=0)
    server.update_p_matrix(p_matrix)
    np.savetxt('../_tmp/p_matrix_I.csv', server.p_matrix_I, delimiter=',')
    case_counts = np.loadtxt(open(case_counts_filename, "rb"), delimiter=",", skiprows=0)
    est = np.dot(case_counts, server.p_matrix_I)
    log(est)
    np.savetxt(est_counts_f, est, delimiter=',')






def main(argv):
    est_kind(argv[1], argv[2], argv[3], argv[4])


if __name__ == "__main__":
    try:
        main(sys.argv)
    except RuntimeError, e:
        log('compute_fre.py: FATAL: %s', e)
