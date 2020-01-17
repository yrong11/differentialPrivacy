import sys
import csv
sys.path.append('../client/')
from ClientMRR import ClientMRR
import time

def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg


def MrrClientSim(client):
    with open('../../data/foo.csv', 'rb') as myFile:
        csv_in = csv.reader(myFile)
        with open('../_tmp/case_report.csv', 'wb') as myFile:
            csv_out = csv.writer(myFile)
            header = ('client', 'true_value', 'mrr_value')
            csv_out.writerow(header)


            start_time = time.time()

            for i, (client_str, cohort_str, true_value) in enumerate(csv_in):
                if i == 0:
                    if client_str != 'client':
                        raise RuntimeError('Expected client header, got %s' % client_str)
                    if cohort_str != 'cohort':
                        raise RuntimeError('Expected cohort header, got %s' % cohort_str)
                    if true_value != 'value':
                        raise RuntimeError('Expected value header, got %s' % true_value)
                    continue

                if i % 10000 == 0:
                    elapsed = time.time() - start_time
                    log('Processed %d inputs in %.2f seconds', i, elapsed)

                mrr_value = client.client_mrr(int(true_value)-1)

                out_row = (client_str, true_value, mrr_value)
                csv_out.writerow(out_row)

def main(epsilon, k):
    if k == None:
        raise AssertionError
    if epsilon == None:
        epsilon = 3
    client = ClientMRR(epsilon, k)
    with open("../_tmp/params.csv", "wb") as myFile:
        csv_out = csv.writer(myFile)
        header = ('N', 'k', 'epsilon','p','q')
        csv_out.writerow(header)
        params = (40000, client.k, client.epsilon, client.p,client.q)
        csv_out.writerow(params)
    # with open('../../data/foo.csv', 'rb') as myFile:
    #     csv_in = csv.reader(myFile)
    # with open('../_tmp/case_report.csv', 'wb') as myFile:
    #     csv_out = csv.writer(myFile)
    MrrClientSim(client)


if __name__ == "__main__":
    epsilon = eval(sys.argv[1])
    k = eval(sys.argv[2])
    try:
        main(epsilon, k)
    except RuntimeError, e:
        log('mrr_sim.py: FATAL: %s', e)
