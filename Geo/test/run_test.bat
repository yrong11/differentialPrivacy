python2 geo_sim_dist.py 3 100 1000 ../_tmp/params.csv ../_tmp/p_matrix.csv < ../../data/foo.csv > ../_tmp/case_report.csv
python2 sum_kind.py ../_tmp/true_counts.csv < ../_tmp/case_report.csv > ../_tmp/case_counts.csv
python2 compute_fre.py ../_tmp/params.csv ../_tmp/p_matrix.csv ../_tmp/case_counts.csv ../_tmp/est_counts.csv
python2 compare_dist.py