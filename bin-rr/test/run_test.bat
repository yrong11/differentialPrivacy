python2 brr_sim.py 3 100 40000 ../_tmp/params.csv < ../../data/foo.csv > ../_tmp/case_report.csv
python2 sum_bits.py ../_tmp/params.csv < ../_tmp/case_report.csv > ../_tmp/case_counts.csv
python2 compute_fre.py
python2 compare_dist.py