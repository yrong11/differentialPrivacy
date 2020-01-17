import csv
import sys
sys.path.append('../client/')
from ClientBRR import Params

def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg

def SumBits(params, stdin, stdout):
    csv_in = csv.reader(stdin)
    csv_out = csv.writer(stdout)

    sums = [0 for i in range(params.k)]
    log(sums.__len__())
    for i, row in enumerate(csv_in):
        try:
            (client, true_value, brr_value) = row
        except ValueError:
            raise RuntimeError('Error parsing row %r' % row)

        if i == 0:
            continue  # skip header

        if not len(brr_value) == params.k:
            raise RuntimeError(
                "Expected %d bits, got %r" % (params.k, len(brr_value)))
        for i, c in enumerate(brr_value):
            if c == '1':
                sums[i] += 1
            else:
                if c != '0':
                    raise RuntimeError('Invalid IRR -- digits should be 0 or 1')


    csv_out.writerow(sums)


def main(argv):
  try:
    filename = argv[1]
  except IndexError:
    raise RuntimeError('Usage: sum_bits.py <params file>')
  with open(filename) as f:
    try:
      params = Params.from_csv(f)
    except RuntimeError, e:
        raise RuntimeError('Usage: sum_bits.py <params file>')
  SumBits(params, sys.stdin, sys.stdout)


if __name__ == '__main__':
  try:
    main(sys.argv)
  except RuntimeError, e:
    print >>sys.stderr, e.args[0]
    sys.exit(1)
