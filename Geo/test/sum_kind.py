
import csv
import sys
import pandas as pd
sys.path.append('../client/')
sys.path.append('../_tmp/')
from ClientGeo import ClientGeo


def SumKind(true_counts_filename, stdin, stdout):
    csv_report = pd.read_csv(stdin)
    true_value_counts = pd.value_counts(csv_report['true_value'], False).sort_index()
    geo_value_counts = pd.value_counts(csv_report['geo_value'], False).sort_index()
    csv_out = csv.writer(stdout)
    csv_out.writerow(geo_value_counts.values)

    with open(true_counts_filename, 'wb') as myFile:
        csv_out_true = csv.writer(myFile)
        csv_out_true.writerow(true_value_counts.values)

def main(argv):
  try:
    filename = argv[1]
  except IndexError:
    raise RuntimeError('Usage: sum_bits.py <params file>')
  SumKind(filename, sys.stdin, sys.stdout)


if __name__ == '__main__':
  try:
    main(sys.argv)
  except RuntimeError, e:
    print >>sys.stderr, e.args[0]
    sys.exit(1)

