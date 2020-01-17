import numpy as np
import math
import sys
import csv

def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg

class Error(Exception):
  pass

class Params:
    def __init__(self):
        self.N = 10000
        self.k = 100
        self.p = 0.6
        self.q = 0.4
        self.epsilon = 3

    @staticmethod
    def from_csv(f):
        """Read the RAPPOR parameters from a CSV file.

        Args:
          f: file handle

        Returns:
          Params instance.

        Raises:
          rappor.Error: when the file is malformed.
        """
        c = csv.reader(f)
        ok = False
        p = Params()
        for i, row in enumerate(c):

            if i == 0:
                if row != ['N', 'k', 'epsilon', 'p', 'q']:
                    raise Error('Header %s is malformed; expected N,k,epsilon,p,q' % row)

            elif i == 1:
                try:
                    # NOTE: May raise exceptions
                    p.N = int(row[0])
                    p.k = int(row[1])
                    p.epsilon = int(row[2])
                    p.p = float(row[3])
                    p.q = float(row[4])
                except (ValueError, IndexError) as e:
                    raise Error('Row is malformed: %s' % e)
                ok = True

            else:
                raise Error('Params file should only have two rows')

        if not ok:
            raise Error("Expected second row with params")

        return p

class ClientBRR:
    def __init__(self, epsilon, k):
        self.epsilon = epsilon
        self.k = k
        self.denominator = math.exp(epsilon)+1
        self.p = math.exp(epsilon)/self.denominator
        self.q = 1/self.denominator

    def privatise(self, p, q):
        bit = (np.random.choice(a=[0, 1], size=1, replace=False, p=[p, q]))
        if bit == 0:
            return "0"
        else:
            return "1"


    def client_brr(self, data):
        bits = []
        for i in range(self.k):
            if data == i+1:
                bits.append(self.privatise(self.q,self.p))
            else:
                bits.append(self.privatise(self.p,self.q))
        return ''.join(bits)

    def client_brr1(self, data):
        bit =np.random.choice(a=['0', '1'], size=self.k, replace=True, p=[self.p, self.q])

        bits = bit.tolist()
        if bits[data-1] == '0':
            bits[data-1] = '1'
        return ''.join(bits)



# client = ClientBRR(2,10)
# print client.p
# print client.q
#
# a = client.client_brr1(3)
# print a
