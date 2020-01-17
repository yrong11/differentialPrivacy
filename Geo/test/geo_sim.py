import sys
import csv
sys.path.append('../client/')
from ClientGeo import ClientGeo
import numpy as np
import time

def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg


def GeoClientSim(client):
    csv_in = csv.reader(sys.stdin)

    csv_out = csv.writer(sys.stdout)
    header = ('client', 'true_value', 'geo_value')
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

        geo_value = client.client_geo(int(true_value)-1)
        out_row = (client_str, true_value, geo_value)
        csv_out.writerow(out_row)

def main(epsilon, k, N, params_file, p_matrix_file):
    if k == None:
        raise AssertionError
    if epsilon == None:
        epsilon = 3
    client = ClientGeo(epsilon, k)
    client.create_matrix()

    with open(params_file, "wb") as myFile:
        csv_out = csv.writer(myFile)
        header = ('N', 'k', 'epsilon')
        csv_out.writerow(header)
        params = (N, client.k, client.epsilon)
        csv_out.writerow(params)
        myFile.close()
    np.savetxt(p_matrix_file, client.p_matrix, delimiter=',')
    GeoClientSim(client)


if __name__ == "__main__":
    epsilon = eval(sys.argv[1])
    k = eval(sys.argv[2])
    N = eval(sys.argv[3])
    params_file = sys.argv[4]
    p_matrix_file = sys.argv[5]
    try:
        main(epsilon, k, N, params_file, p_matrix_file)
    except RuntimeError, e:
        log('brr_sim.py: FATAL: %s', e)
