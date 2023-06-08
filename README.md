# DBCscan：DNA Barcode based contamination scanner

Test script for protistan contamination screening: python DBCscan.py -i ./test_data/tpa_wgs.DWKX.1.fsa_nt.gz -o ./results

For testing purposes, all databases have just a few records. If you want to analyze real data, you should first download the full database from BOLD and nt&taxonomy database from NCBI. And split BOLD database into inclusion/exclusion sets, then change the path in config file.
