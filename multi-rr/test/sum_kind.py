
import csv
import sys
import pandas as pd
sys.path.append('../client/')
sys.path.append('../_tmp/')
from ClientMRR import ClientMRR


def SumKind(stdin, stdout):
    csv_data = pd.read_csv(stdin)
    mrr_value_counts = pd.value_counts(csv_data['mrr_value'], False).sort_index()

    with open(stdout, 'wb') as myFile:
        csv_out = csv.writer(myFile)
        csv_out.writerow(mrr_value_counts.values)

def main(argv):
  if sys.stdin == None or sys.stdout == None:
      raise RuntimeError('Usage: sum_bits.py <params file>')
  SumKind(sys.stdin, sys.stdout)


if __name__ == '__main__':
  sys.stdin = "../_tmp/case_report.csv"
  sys.stdout = "../_tmp/case_counts.csv"
  try:
    main(sys)
  except RuntimeError, e:
    print >>sys.stderr, e.args[0]
    sys.exit(1)
